import requests
import json
from types import SimpleNamespace

url = "http://127.0.0.1:5000/api/v1/resources/node-cpu"

response = requests.get(url)
data = response.text
parsed = json.loads(data)
raw_data = json.loads(parsed, object_hook=lambda d: SimpleNamespace(**d))

list_data = raw_data.data.result
for i in list_data:
    print(i.value[1])
