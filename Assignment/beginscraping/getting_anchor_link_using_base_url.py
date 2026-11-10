import requests
from bs4 import BeautifulSoup

baseurl = 'https://www.thewhiskyexchange.com/'

#we send headers first to avoid bot detection
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

r = requests.get('https://"the navigational link at the top be here"')
soup = BeautifulSoup(r.content,'lxml')

product_list = soup.find_all('div',class_='item')

product_links=[]

for item in product_list:
    for link in item.find_all('a',href=True):
        print(link['href'])





