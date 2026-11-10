import requests

url = "https://catalog.app.iherb.com/recommendations/v2/specials-personalized?page=1&pageSize=30"

# Adding headers helps bypass basic bot detection
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    # Remember the parentheses here!
    data = response.json()

    # To see the data clearly, you can look at the keys first
    print("Data Keys:", data.keys())

    # Example: Accessing the products list (adjust based on actual JSON structure)
    # print(data)
else:
    print("Failed to retrieve data.")