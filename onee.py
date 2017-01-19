from bs4 import BeautifulSoup
import requests
import os,re
from collections import Counter
import count
from unit import GetPrice
from scoll import Scollection
# print(count.urlQs)
class Inter(object):
    def start(self,url):
        # url = 'https://www.zhihu.com/question/54370154'
        spider = GetPrice(url)
        select1 = '.zm-tag-editor-labels.zg-clear a '
        pay = spider.getPrice(select1)

        return [a.get_text().strip() for a in pay]
oneScollection = Scollection()
jiedian = []
for yy in count.urlQs:
    oneUrl = oneScollection.get_urlQ(yy)
    # print(oneUrl)

    for o in oneUrl:
        oneInter = Inter()
        print('提取节点')
        jiedian += oneInter.start(o)
    # print(jiedian)
c3 = Counter(jiedian)
c4 = c3.most_common(111111)
print(c4)

