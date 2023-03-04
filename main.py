import requests
import json

url = "https://x8ki-letl-twmt.n7.xano.io/api:GSAwrAoy:v1/links/get/today"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.content.decode('utf-8'))
    summary = data["summary"]
    text = data["link"]
    print("Summary:", summary)
    print("Text:", text)
else:
    print("Error occurred with status code:", response.status_code)
