import openpyxl
import requests
import codecs
import shutil
import time
import os
import copy

from bs4 import BeautifulSoup
from json import dumps
from datetime import datetime, timedelta, timezone

from typing import Dict

jst = timezone(timedelta(hours=9), 'JST')
base_url = "https://www.city.kobe.lg.jp/"

OLD_SUMMARY_INIT = {
    'attr': '検査実施人数',
    'value': 0,
    'children': [
        {
            'attr': '陽性患者数',
            'value': 0,
            'children': [
                {
                    'attr': '入院中',
                    'value': 0,
                    'children': [
                        {
                            'attr': '軽症・中等症',
                            'value': 0
                        },
                        {
                            'attr': '重症',
                            'value': 0
                        }
                    ]
                },
                {
                    'attr': '死亡',
                    'value': 0
                },
                {
                    'attr': '治癒確認',
                    'value': 0
                }
            ]
        }
    ]
}


SUMMARY_INIT = copy.copy(OLD_SUMMARY_INIT)
SUMMARY_INIT["attr"] = "患者発生総数"


def print_log(type: str, message: str) -> None:
    print(f"[{datetime.now(jst).strftime('%Y-%m-%d %H:%M:%S+09:00')}][covid19kobe-scraping:{type}]: {message}")


def make_data(date, value):
    return {"日付": date, "小計": value}


def template_json(last_update: str) -> Dict:
    # テンプレート、これをもとにデータを追加していく
    return {
        "date": last_update,
        "data": []
    }


def excel_date(num) -> datetime:
    return datetime(1899, 12, 30) + timedelta(days=num, hours=8)


def requests_html(path: str) -> BeautifulSoup:
    print_log("requests", "Requests html...")
    response = requests.get(base_url + path)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_xlsx(path: str, number: int = 0) -> openpyxl.workbook.workbook.Workbook:
    print_log("get", "Get html file...")
    html_doc = ""
    failed_count = 0
    while not html_doc:
        try:
            html_doc = requests.get(base_url + path).text
        except Exception:
            if failed_count >= 5:
                raise Exception(f"Failed get html file from \"{base_url + path}\"!")
            print_log("get", f"Failed get html file from \"{base_url + path}\". retrying...")
            failed_count += 1
            time.sleep(5)
    soup = BeautifulSoup(html_doc, 'html.parser')

    real_page_tags = soup.find_all("a")

    file_url = ""
    count = 0
    for tag in real_page_tags:
        if tag.get("href") is None:
            continue
        if tag.get("href")[-4:] == "xlsx":
            if count == number:
                file_url = base_url + tag.get("href")
                break
            count += 1

    assert file_url, f"Can't get xlsx file!"
    return requests_xlsx(file_url)


def requests_xlsx(url: str) -> openpyxl.workbook.workbook.Workbook:
    print_log("request", "Request xlsx file...")
    filename = "./data/" + os.path.basename(url)
    failed_count = 0
    status_code = 404
    while not status_code == 200:
        try:
            res = requests.get(url, stream=True)
            status_code = res.status_code
        except Exception:
            if failed_count >= 5:
                raise Exception(f"Failed get xlsx file from \"{url}\"!")
            print_log("request", f"Failed get xlsx file from \"{url}\". retrying...")
            failed_count += 1
            time.sleep(5)
    with open(filename, 'wb') as f:
        res.raw.decode_content = True
        shutil.copyfileobj(res.raw, f)
    return openpyxl.load_workbook(filename)


def dumps_json(file_name: str, json_data: Dict) -> None:
    with codecs.open("./data/" + file_name, "w", "utf-8") as f:
        f.write(dumps(json_data, ensure_ascii=False, indent=4, separators=(',', ': ')))
