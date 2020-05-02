from util import OLD_SUMMARY_INIT, SUMMARY_INIT, dumps_json, requests_html, get_xlsx, make_data, template_json, jst
import config

from datetime import datetime, timedelta
from typing import Dict, List

summary_first_cell = 2
all_summary_first_cell = 2
contacts_first_cell = 2


class DataJson:
    def __init__(self):
        self.contacts_sheet = get_xlsx(config.main_page, 1)["相談件数"]
        self.patients_html = requests_html("/a57337/kenko/health/corona_zokusei.html")
        # self.inspections_sheet = get_xlsx(config.inspections_xlsx, "inspections.xlsx")["検査件数・陽性患者"]
        self.main_summary_html = requests_html("/a73576/kenko/health/infection/protection/covid_19.html")
        self.summary_xlsx = get_xlsx(config.main_page)
        self.main_summary_sheet = self.summary_xlsx["kobe"]
        # 神戸市のサイト形式変更に伴い、self.summary_xlsxに"all"シートが追加され、これが使えるようになるので、
        # allが取得できるようになり次第、自動で切り替えるようにする
        self.all_summary_sheet = None
        try:
            self.all_summary_sheet = self.summary_xlsx["all"]
        except Exception:
            pass
        # self.inspections_count = 4
        self.contacts_count = contacts_first_cell
        self.summary_count = summary_first_cell
        self.all_summary_count = all_summary_first_cell
        self.main_summary_values = []
        self.last_update = datetime.today().astimezone(jst).strftime("%Y/%m/%d %H:%M")
        self._data_json = {}
        # 以下内部変数
        self._contacts_summary_json = {}
        self._health_center_summary_json = {}
        self._patients_json = {}
        self._patients_summary_json = {}
        self._inspections_summary_json = {}
        self._main_summary_json = {}
        # 初期化
        # self.get_inspections()
        self.get_contacts()
        self.get_summary_count()
        self.get_all_summary_count()

    def data_json(self) -> Dict:
        # 内部変数にデータが保管されているか否かを確認し、保管されていなければ生成し、返す。
        # 以下Dictを返す関数はこれに同じ
        if not self._data_json:
            self.make_data()
        return self._data_json

    def contacts_summary_json(self) -> Dict:
        if not self._contacts_summary_json:
            self.make_contacts()
        return self._contacts_summary_json

    def health_center_summary_json(self) -> Dict:
        if not self._health_center_summary_json:
            self.make_contacts()
        return self._health_center_summary_json

    def patients_json(self) -> Dict:
        if not self._patients_json:
            self.make_patients()
        return self._patients_json

    def patients_summary_json(self) -> Dict:
        if not self._patients_summary_json:
            self.make_summaries()
        return self._patients_summary_json

    def inspections_summary_json(self) -> Dict:
        if not self._inspections_summary_json:
            self.make_summaries()
        return self._inspections_summary_json

    def main_summary_json(self) -> Dict:
        if not self._main_summary_json:
            self.make_main_summary()
        return self._main_summary_json

    def make_data(self) -> None:
        self._data_json = {
            "contacts_summary": self.contacts_summary_json(),
            "health_center_summary": self.health_center_summary_json(),
            "patients": self.patients_json(),
            "patients_summary": self.patients_summary_json(),
            "inspections_summary": self.inspections_summary_json(),
            "lastUpdate": self.last_update,
            "main_summary": self.main_summary_json()
        }

    def make_contacts(self) -> None:
        # 最終データの日の次の日を最終更新日とする
        # last_update = (
        #     self.contacts_sheet.cell(row=self.contacts_count - 1, column=1).value +
        #     timedelta(days=1)
        # ).strftime("%Y/%m/%d %H:%M")
        last_update = self.last_update

        # contacts_summaryとhealth_center_summaryを同時に生成する。
        # スクリプト実行時間短縮のため、同時に生成している。
        self._contacts_summary_json = template_json(last_update)
        self._health_center_summary_json = template_json(last_update)

        column_name = self.contacts_sheet.cell(row=contacts_first_cell - 1, column=2).value.replace("\n", "")
        health_center_field = 6

        for i in range(contacts_first_cell, self.contacts_count):
            # 日時の取得
            # date = excel_date(self.contacts_sheet.cell(row=i, column=1).value)
            date = self.contacts_sheet.cell(row=i, column=1).value + timedelta(hours=8)
            if "健康相談窓口" in column_name and "帰国者・接触者相談センター" in column_name:
                # 日別窓口(相談センター)相談者数の取得
                contacts = self.contacts_sheet.cell(row=i, column=2).value
                # Excelのセル内に0すら入っていないときはNoneが返ってくるので、0を代入しなおす。
                if contacts is None:
                    contacts = 0
                health_center_field = 4
            else:
                # 日別窓口相談者数の取得
                window_contacts = self.contacts_sheet.cell(row=i, column=2).value
                # 日別帰国者・接触者コールセンター相談者数の取得
                center_contacts = self.contacts_sheet.cell(row=i, column=4).value
                # Excelのセル内に0すら入っていないときはNoneが返ってくるので、0を代入しなおす。
                if window_contacts is None:
                    window_contacts = 0
                if center_contacts is None:
                    center_contacts = 0
                contacts = window_contacts + center_contacts
            # 日別保健所・保健センター相談者数の取得
            health_center = self.contacts_sheet.cell(row=i, column=health_center_field).value
            # Excelのセル内に0すら入っていないときはNoneが返ってくるので、0を代入しなおす。
            if health_center is None:
                health_center = 0
            self._contacts_summary_json["data"].append(make_data(date.isoformat() + "Z", contacts))
            self._health_center_summary_json["data"].append(make_data(date.isoformat() + "Z", health_center))

    def make_patients(self) -> None:
        # HTMLから最終更新日を取得する
        # last_update_str = [x.get_text() for x in self.patients_html.find_all("p") if "更新日" in x.get_text()][0][4:]
        # last_update = datetime.strptime(last_update_str, "%Y年%m月%d日").strftime("%Y/%m/%d %H:%M")
        last_update = self. last_update
        # patientsを生成する
        self._patients_json = template_json(last_update)

        # patientsは現状HTMLの表を使用して作成しているので、テーブル(レコード一覧)を取得する
        tables = self.patients_html.find_all("tr")
        # レコード(セル一覧)を取得する
        for cells in tables:
            # データの初期化
            data = {}
            # セルを取得する
            for i, cell in enumerate(cells.find_all("td")):
                # 何もないセルは"\u3000"が埋め込まれているのでリプレースして消す
                text = cell.get_text().replace("\u3000", "")
                # カラム名は飛ばす
                if text == "番号":  # i == 0と同意
                    break
                # 日付を取得する
                elif i == 1:
                    try:
                        date = datetime.strptime("2020年" + text, "%Y年%m月%d日") + timedelta(hours=8)
                        data["判明日"] = date.isoformat() + "Z"
                        data["date"] = date.strftime("%Y-%m-%d")
                    except Exception:
                        data["判明日"] = None
                        data["date"] = None
                # 年代を取得する
                elif i == 2:
                    data["年代"] = text + "代"
                # 性別を取得する
                elif i == 3:
                    data["性別"] = text
                # 備考を取得する
                elif i == 5:
                    # 市外在住を除外するため、備考欄を利用
                    if "市外在住" in text:
                        # 下のif文で引っかからないようデータを初期化
                        data = {}
                        break
                    data["備考"] = text if text != "\xa0" and text else None
            if data:
                data["退院"] = None  # TODO: 退院データが現状ないため保留
                self._patients_json["data"].append(data)
        # 市外発表者も含むため、日時順でソート
        self._patients_json["data"].sort(key=lambda x: (x["date"] is None, x["date"]))

    def make_summaries(self) -> None:
        # 最終データの日の次の日を最終更新日とする
        # last_update = (
        #     self.main_summary_sheet.cell(row=self.summary_count - 1, column=1).value +
        #     timedelta(days=1)
        # ).strftime("%Y/%m/%d %H:%M")
        last_update = self.last_update

        # patients_summaryとinspections_summaryを同時に生成する
        # スクリプト実行時間短縮のため、同時に生成している。
        self._patients_summary_json = template_json(last_update)
        self._inspections_summary_json = template_json(last_update)

        for i in range(summary_first_cell, self.summary_count):
            date = self.main_summary_sheet.cell(row=i, column=1).value + timedelta(hours=8)
            # 陽性患者数を取得する
            patients = self.main_summary_sheet.cell(row=i, column=4).value
            # 検査人数を取得する
            inspections = self.main_summary_sheet.cell(row=i, column=2).value
            self._patients_summary_json["data"].append(make_data(date.isoformat() + "Z", patients))
            self._inspections_summary_json["data"].append(make_data(date.isoformat() + "Z", inspections))

    def make_main_summary(self) -> None:
        # 神戸市のサイト形式変更に伴い、self.summary_xlsxに"all"シートが追加され、これが使えるようになるので、
        # allが取得できるようになり次第、自動で切り替えるようにする
        if self.all_summary_sheet:
            # main_summaryの生成
            self._main_summary_json = SUMMARY_INIT
            self.main_summary_values = self.get_main_summary_values()
        else:
            # main_summaryの生成
            self._main_summary_json = OLD_SUMMARY_INIT
            # main_summaryはHTMLの表を使用して作成しているので、テーブル(レコード一覧)を取得する
            tables = self.main_summary_html.find_all("tr")
            # レコード(セル一覧)を取得する
            for i, cells in enumerate(tables):
                # https://www.city.kobe.lg.jp/a73576/kenko/health/infection/protection/covid_19.html の
                # 検査件数総数(i == 3, j == 0の場所)のデータと神戸市内在住者合計(i == 5, j == 0以降)のデータを使うので、
                # それ以外の行は読み飛ばす
                if i not in [3, 5]:
                    continue
                for j, cell in enumerate(cells.find_all("td")):
                    # 検査件数総数以外は使わないのでbreakさせる
                    if i == 3 and j > 0:
                        break
                    # 一番最初に「神戸市内在住者合計」とあって、データではないので読み飛ばす
                    if i == 5 and j == 0:
                        continue
                    # テキストをリストとして取得
                    text_list = cell.get_text().split()
                    # text_list[0]が数字のみの場合(「10」など)はtryでそのまま成功するが、「10人」などの場合はexpectで処理させる。
                    try:
                        value = int(text_list[0])
                    except Exception:
                        value = int(text_list[0][:-1])
                    self.main_summary_values.append(value)
        self.set_summary_values(self._main_summary_json)

    def set_summary_values(self, obj) -> None:
        # リストの先頭の値を"value"にセットする
        obj["value"] = self.main_summary_values[0]
        # objが辞書型で"children"を持っている場合のみ実行
        if isinstance(obj, dict) and obj.get("children"):
            for child in obj["children"]:
                # 再起させて値をセット
                self.main_summary_values = self.main_summary_values[1:]
                self.set_summary_values(child)

    def get_main_summary_values(self) -> List:
        values = []
        for i in range(2, 9):
            values.append(self.all_summary_sheet.cell(row=self.all_summary_count - 1, column=i).value)
        return values

    # 検査件数、陽性患者数はmain_summary_sheetから取ることになったのでコメントアウト
    # def get_inspections(self) -> None:
    #     # 何行分検査数のデータがあるかを取得
    #     while self.inspections_sheet:
    #         self.inspections_count += 1
    #         value = self.inspections_sheet.cell(row=self.inspections_count, column=1).value
    #         if value is None:
    #             break

    def get_contacts(self) -> None:
        # 何行分相談数のデータがあるかを取得
        while self.contacts_sheet:
            self.contacts_count += 1
            value = self.contacts_sheet.cell(row=self.contacts_count, column=1).value
            if value is None:
                break

    def get_summary_count(self) -> None:
        # 何行分サマリーのデータがあるかを取得
        while self.main_summary_sheet:
            self.summary_count += 1
            value = self.main_summary_sheet.cell(row=self.summary_count, column=1).value
            if not value:
                break

    def get_all_summary_count(self) -> None:
        # 何行分サマリーのデータがあるかを取得
        while self.all_summary_sheet:
            self.all_summary_count += 1
            value = self.all_summary_sheet.cell(row=self.all_summary_count, column=1).value
            if not value:
                break


if __name__ == '__main__':
    dumps_json("data.json", DataJson().data_json())
