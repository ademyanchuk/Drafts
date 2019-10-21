import requests

url = "http://localhost:8080/"
req = {"name": "alex"}
num = 100
for _ in range(num):
    res = requests.post(url, json=req)
    print(res.json())