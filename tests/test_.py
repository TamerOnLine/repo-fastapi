import requests
r = requests.post("http://localhost:8000/plugins/dummy/ping", json={"hello": "world"})
print(r.json())