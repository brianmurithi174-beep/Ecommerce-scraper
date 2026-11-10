#checking for response 200
import requests

def response_code(response):
    if response.status_code == 200:
        print("page fetched successfully")
    else:
        print("Failed to retrieve page:",response.status_code)
URL = "http://books.toscrape.com"
url_response = requests.get(URL)

#checking the error 403 -->>blocked by cloudflare
#Error 404 ----->>> page doesn't exist


#>>>>>CHECKING THE Robots.txt file


#look for delays>>>pip install urlib
#rp = urlib.robotparser.RobotFileParser()
#rp.set_url("https://www.amazon.com")
#rp.read()
#delay = rp.crawl_delay("*")
#print(delay)

#>>>>Checking if you can scrape a page<<<,
#rp  = urllib.robotparser.RobotFileParser()
#rp.set_url("https://www.amazon.com/robots.txt")
#rp.read()
#print(rp.can_fetch("*",https://www.amazon,,,,)
#response should be true or fa;se based on the link

#>>>>>headers<<<<
#headers = {
    #'user-agent':'mozilla/5.0(Windows NT 10.0; win64;x64'
#}
#requests.get(url, headers = headers

