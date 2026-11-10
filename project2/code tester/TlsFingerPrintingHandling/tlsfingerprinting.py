from curl_cffi import requests

url = "https://catalog.app.iherb.com/recommendations/v2/specials-personalized?page=1&pageSize=30"
response = requests.get(url, impersonate="chrome")
print(response)
if response.status_code == 200:
    data = response.json()
    print(data)