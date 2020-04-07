# COVID19 Scraping Script for Kobe

## What's this?
神戸市公式サイト<!--や、神戸市オープンデータカタログサイト-->で公開されている情報を集め、jsonとして出力するPythonスクリプトです。
[神戸市 新型コロナウイルス感染症 対策サイト](https://kobe.stopcovid19.jp/)で使用する形に整形し、出力します。  
なお、データ参照元URLは適宜、[config.py](config.py)で変えることができます。

## Make date
```shell script
pip install -r requirements.txt
python3 main.py
```

## Reference data list
このスクリプトでは、以下のデータを参照し、jsonを出力しています。

|jsonデータ|データの詳細|データの参照元|
|---|---|---|
|window_contacts|新型コロナ健康相談窓口 相談件数|[神戸市公式サイト](https://www.city.kobe.lg.jp/a73576/kenko/health/infection/protection/covid_19.html)|
|center_contacts|帰国者・接触者相談センター 相談件数|[神戸市公式サイト](https://www.city.kobe.lg.jp/a73576/kenko/health/infection/protection/covid_19.html)|
|health_center_summary|保健所・保健センターでの一般相談件数|[神戸市公式サイト](https://www.city.kobe.lg.jp/a73576/kenko/health/infection/protection/covid_19.html)|
|patients|患者についての情報|[神戸市公式サイト](https://www.city.kobe.lg.jp/a57337/kenko/health/corona_zokusei.html)|
|patients_summary|日別患者数|[神戸市公式サイト](https://www.city.kobe.lg.jp/a73576/kenko/health/infection/protection/covid_19.html)|
|inspections_summary|PCR検査の陰性/陽性状況|[神戸市公式サイト](https://www.city.kobe.lg.jp/a73576/kenko/health/infection/protection/covid_19.html)|
|main_summary|検査状況/患者状況の総まとめ|[神戸市公式サイト](https://www.city.kobe.lg.jp/a73576/kenko/health/infection/protection/covid_19.html)|
|lastUpdate|データの最終更新日|スクリプト実行日時|


## License
このスクリプトは[MITライセンス](LICENSE)で公開されています。
