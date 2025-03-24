# Exploring fantasy API
# <SThis is the old version of Fantasy F1 from 2022 power by PlayOn. It doesn't work for the current version. Ignore. >
import requests

url = "https://api.formula1.com/6657193977244c13?d=account.formula1.com"

payload = "{\"solution\":{\"interrogation\":{\"st\":162229509,\"sr\":1959639815,\"cr\":78830557},\"version\":\"stable\"},\"error\":null,\"performance\":{\"interrogation\":185}}"
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

