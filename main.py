## 天気予報を取得します。

import requests
import json

url = 'https://www.jma.go.jp/bosai/forecast/data/overview_forecast/020000.json'

tenki_data = requests.get(url)

print(tenki_data)
print(tenki_data.text)
print(tenki_data.headers)