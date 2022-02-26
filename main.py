## 天気予報を取得します。

import requests
import json

url = 'https://www.jma.go.jp/bosai/forecast/data/overview_forecast/020000.json'

r = requests.get(url)
tenki_data = r.json()

print(tenki_data['publishingOffice'] + "発表の天気予報です。")
print(tenki_data['targetArea'] + "の天気予報です。")
print(tenki_data['text'])
