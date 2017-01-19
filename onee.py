from bs4 import BeautifulSoup
import requests,random
import os,re,time
from collections import Counter
import count
from unit import GetPrice
from scoll import Scollection
# print(count.urlQs)
st = time.time()
class Inter(object):
    def start(self,url):
        # url = 'https://www.zhihu.com/question/54370154'
        spider = GetPrice(url)
        select1 = '.zm-tag-editor-labels.zg-clear a '
        pay = spider.getPrice(select1)

        return [a.get_text().strip() for a in pay]
oneScollection = Scollection()
# jiedian = []
sss = ['https://www.zhihu.com//collection/115723985', 'https://www.zhihu.com//collection/113049070', 'https://www.zhihu.com//collection/68648939', 'https://www.zhihu.com//collection/97706444']
for yy in sss:
    oneUrl = oneScollection.get_urlQ(yy)
    # print(oneUrl)
    time.sleep(random.randint(1, 4))
    for o in oneUrl:
        oneInter = Inter()
        # print('提取节点...')
        print(oneInter.start(o))
    # print(jiedian)
# c3 = Counter(jiedian)
# c4 = c3.most_common(111111)
# print(c4)
end = time.time()
print(end - st)
