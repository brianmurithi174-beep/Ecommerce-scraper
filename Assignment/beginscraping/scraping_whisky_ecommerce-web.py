import requests
import pandas as pd
from bs4 import BeautifulSoup
import random
from time import sleep


baseurl = "https://www.thewhiskeyexchange.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
product_links = []
for page in range(1,6):
    #we move to the next page for page identifier in the link to be displayed then we put an f string
    url = f"https://www.thewhiskeyexchange.com/c/35/japanese-whisky?pg-[page]"
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.content,'lxml')

    product_list = soup.find_all('div',class_='item')

    for item in product_list:
        for link in item.find_all('a',href=True):
            product_links.append(baseurl+link['href'])


whisky_list = []
for link in product_links:
    r = requests.get(link, headers = headers)
    soup = BeautifulSoup(r.content,'lxml')
    name = soup.find('h1',class_='product-main__name').text.strip()
    price = soup.find('p',class_='product-action__price').text.strip()
    try:
        rating = soup.find('div', class_='review-overview').text.strip()
    except AttributeError:
        rating =  'no rating'
    whisky = {
        'name':name,
        'rating':rating,
        'price':price
    }

    whisky_list.append(whisky)
    print('saving:',whisky['_name_'])

    delay = random.uniform(1, 5)
    sleep(delay)  # polite delay to avoid overloading the server

df = pd.DataFrame(whisky_list)
print(df.head(15))
df.to_csv("whiskys")

