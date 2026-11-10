import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

link = product_links[0]
r = requests.get(link, headers=headers)
soup = BeautifulSoup(r.content, "lxml")

name = soup.select_one("h1.product-title").text.strip()
price = soup.select_one("span.price").text.strip()

try:
    rating = soup.select_one("div.rating").text.strip()
except:
    rating = "no reviews"

product = {
    "name": name,
    "price": price,
    "rating": rating
}

print(product)
