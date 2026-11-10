import requests
from bs4 import BeautifulSoup
# this is the url of the webpage to scrape
url = "https://www.thesun.co.uk/news/"
# this sends response to get data from the webpage
response = requests.get(url)

if response.status_code == 200:
   #parse HTML content using beautifulsoup
   soup = BeautifulSoup(response.content, "html.parser")

   #extract all headlines from the  site
   headlines = soup.find_all("h3")

   # print each headline
   for headline in headlines:
       print(headline.text)

   else:
       print(f"failed to retrieve the page. status_code: {response.status_code}")
