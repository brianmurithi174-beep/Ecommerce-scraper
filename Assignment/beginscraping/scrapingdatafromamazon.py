import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = 'https://www.amazon.com/'
#Headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
#HTTP Request
webpage = requests.get(baseurl, headers=headers)
soup = BeautifulSoup(webpage.content, 'html.parser')


#function to extract title
def get_info(soup):
    title = soup.find('span', attrs={'id': 'productTitle'}).text.strip()
    price = soup.find('span', attrs={'id': 'priceblock_ourprice'}).text.strip()
    try:
        rating = soup.find('span', attrs={'id': ''}).text.strip()
    except AttributeError:
        rating = 'no rating '

    try:
        review = soup.find('div', class_='').text.strip()
    except AttributeError:
        review = 'no review'


#fetch links as list of Tag Objects
links = soup.find_all('a', attrs={'class': 'a-link-normal s-no-outline'})

#store the links
links_list = []

#loop for extracting links from tag objects
for link in links_list:
    links_list.append(link.get('href'))

products = {
    'title': [],
    'price': [],
    'rating': [],
    'review': [],

}
product_list = []
#loop for extracting product details for each link
for link in links_list:
    new_webpage = requests.get(baseurl + link, headers=headers)
    new_soup = BeautifulSoup(new_webpage.content, 'html.parser')

    product_list.append(products)

df = pd.DataFrame(products)
print(df.head)
df.to_csv('Amazondata.csv', header=True, index=False)
