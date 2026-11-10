import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import random

#Example 4 Books to scrape -static timer
titles = []
prices = []

page = 1

while page < 10:
    url = f"https://ke.iherb.com/c/childrens-health?p={page}"
    response = requests.get(url)
    if response.status_code == 404:
        break
    soup = BeautifulSoup(response.text,"html.parser")
    articles = soup.find_all("a",class_="absolute-link.productlink ")

    for article in articles:
        title = article.h3.a["title"]
        price = article.find("p", class_= "product-price text-nowrap").text.strip()
        titles.append(title)
        prices.append (price)

    delay = random.uniform(1, 5)
    sleep(delay)  # polite delay to avoid overloading the server


#creating a DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
})
df.to_csv("Prices")