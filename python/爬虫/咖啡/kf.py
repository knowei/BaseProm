import urllib.request
import pandas as pd
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': user_agent, }

url = "http://www.iecity.com/nanchang/brand/181105-360111.html"



request = urllib.request.Request(url, None, headers)
response = urllib.request.urlopen(request)
html = response.read()

# 解析网页内容
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
#
# li_list = [li for li in soup.find_all('li') if li.get('id', '').startswith('district_')]
# print(li_list)

life = soup.find("ul", "LifeList clearfix")
print(life)

# life_list = life.find_all("li", "clearfix")
# print(life_list)
# for item in life_list:
#     title = item.find("h3")
#     quyu = item.find("div", "type").find("span")
#     dizhi = item.find("div", "address").find("span")
#     print(title)
