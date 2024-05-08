import urllib.request
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': user_agent, }

def po(url : str):
    f = open('test.txt', 'w',encoding='utf-8')
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    html = response.read()

    # 解析网页内容
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    pageurls = soup.find_all('div', "HotReListTit")

    resUrls = []
    for a in pageurls:
        t = a.find('a')
        resUrls.append(t.get('href'))

    for ur in resUrls:

        request = urllib.request.Request(ur, None, headers)
        response = urllib.request.urlopen(request)
        html = response.read()

        # 解析网页内容
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        pageurls = soup.find('div', "pItemsName")
        print(pageurls.text)
        jieshaoMap = {}
        jihe = []
        list = []
        for i in [1, 2, 3, 4]:
            str = "brand" + i.__str__()
            b = soup.find('a', id=str)
            list.append(b.text)
            jieshaoMap[b.text] = []
        # 找到四个box标签
        box = soup.find_all('div', "article-box")
        # 建立一个字典用来存储信息

        # 遍历box
        for bo in box:
            # 为了处理第一个box里有两个big——title特殊处理
            start_div = bo.find('div', 'big-title')

            if start_div:
                # 获取洗一个big-title的div元素
                next_div = start_div.find_next_sibling('div', 'big-title')
                # 判断是否有next_div，没有的话说明该box只有一个big-title
                if next_div:
                    re = start_div.find_next_siblings(['p'])
                    l1 = []
                    l2 = []
                    # 遍历，判断p标签下一个是不是next_div，分别加入不同的map之中
                    for r in re:
                        if r.find_next_sibling('div', class_='big-title') == next_div:
                            l1.append(r.text)
                        else:
                            l2.append(r.text)
                    if l1.__len__() > 0:
                        jihe.append(l1)

                    if l2.__len__() > 0:
                        jihe.append(l2)
                else:
                    l4 = []
                    res = bo.find_all('p')
                    for re in res:
                        l4.append(re.text)
                    jihe.append(l4)
        # 进行映射处理，l2集合的元素加入到div字典之中
        for i1, i2 in zip(jieshaoMap, jihe):
            jieshaoMap[i1] = i2
        # 输出dic
        print(jieshaoMap)

        f.write("-" * 50)
        f.write(pageurls.text)
        for key, value in jieshaoMap.items():
            f.write("-" * 10 + key  + "-" * 10 + '\n')
            for v in value:
                f.write(v + '\n')

        f.write("-" * 50)

sum = [1]
# sum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in sum:
    url = "https://www.mengruyun.com/xm/lsjd/p" + i.__str__() + ".html"
    po(url)
