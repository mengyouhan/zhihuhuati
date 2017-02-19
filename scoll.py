from bs4 import BeautifulSoup
import requests,time,random
import os
from unit import GetPrice
class Scollection(object):

    def get_urlQ(self,url):
        # url = 'https://www.zhihu.com/collection/132331007'
        print(url)
        spider = GetPrice(url)
        try:

            select2 = '.border-pager .zm-invite-pager span a'
            pay2 = spider.getPrice(select2)
            print(pay2)
            listQ = []
            num = int(pay2[-2].get_text())
            for j in range(1, num + 1):
                print(j)
                page = j
                url_collection = url + '?page={}'.format(page)

                spider_collection = GetPrice(url_collection)
                spider_collection_select = ' div.zm-item h2 a '
                pa = spider_collection.getPrice(spider_collection_select)
                xx = [y['href'] for y in pa if y['href'][0] == '/']
                listQ += xx
            urlQ = ['https://www.zhihu.com/' + i for i in listQ]
            print('scoll.py try 完成')
            time.sleep(random.randint(1, 3))
        except:

            spider_collection_select = ' div.zm-item h2 a '
            pa = spider.getPrice(spider_collection_select)
            xx = [y['href'] for y in pa if y['href'][0] == '/']

            urlQ = ['https://www.zhihu.com/' + i for i in xx]
            print('scoll.py except 完成')


        return urlQ
oneScollection = Scollection()
oneUrl = oneScollection.get_urlQ('https://www.zhihu.com/collection/38887091')
f = open('/Users/user/Desktop/cs3.txt', 'a', encoding='utf8')
f.write(str(oneUrl))
f.close()
print(oneUrl)
# class Inter(object):
#     def start(self,url):
#         # url = 'https://www.zhihu.com/question/54370154'
#         spider = GetPrice(url)
#         select1 = '.zm-tag-editor-labels.zg-clear a '
#         pay = spider.getPrice(select1)
#
#         return [a.get_text().strip() for a in pay]