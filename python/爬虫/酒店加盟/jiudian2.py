import urllib.request
import pandas as pd
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': user_agent, }

url = "https://dev.platenogroup.com/xiangmu/zhongduan/455.html"



request = urllib.request.Request(url, None, headers)
response = urllib.request.urlopen(request)
html = response.read()

# 解析网页内容
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# pageurls = soup.find('div', "pItemsName")

total_name_div = soup.find('div', "phRight")
# 酒店名称
total_name = total_name_div.find('small')
# 题目列表
page_div = soup.find('div', "pageNav")
span_list = page_div.find_all('span', 'menuItem')

pageList = {}
for span in span_list:
    page_name = span.find('a').text
    pageList[page_name] = []

pagezhengce = soup.find('div', 'pagezhengce')
table_tiaojia = pagezhengce.find('table')
str_tiaojia = str(table_tiaojia)
df = pd.read_html(str_tiaojia, header=0)[0]
df = df.reset_index(drop=True)
pageList['加盟政策'] = df


# 加盟条件
pagetiaojia = soup.find('div', 'pagetiaojia')
tr_list = pagetiaojia.find_all('tr')
# print(tr_list)
jiameng_val = []
for tr in tr_list:
    td_list = tr.find_all('td')
    for td in td_list:
        jiameng_val.append(td.text.replace('\r', '').replace('\t', ''))
pageList['加盟条件'] = jiameng_val

def underline(title, length=40):
    """为标题添加下划线"""
    return title + '\n' + '-' * length + '\n'

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(underline(total_name.text))
    for key, val in pageList.items():
        f.write(underline(key))

        if key == '加盟政策':
            f.write("加盟政策详情:\n")
            for index, row in df.iterrows():
                for col_name, cell_value in row.items():
                    f.write(f"{cell_value}\t")
                f.write('\n')
            f.write('\n' * 2)
        else:
            for v in val:
                f.write(v)
                f.write('\n')
            f.write('\n' * 2)
