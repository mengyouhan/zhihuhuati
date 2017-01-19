from bs4 import BeautifulSoup
import requests
import os
from unit import GetPrice
class Scollection(object):

    def get_urlQ(self,url):
        # url = 'https://www.zhihu.com/collection/132331007'
        print('解析'+url)
        spider = GetPrice(url)
        try:
            print('1')
            select2 = '.border-pager .zm-invite-pager span a'
            pay2 = spider.getPrice(select2)
            print(pay2)
            listQ = []
            num = int(pay2[-2].get_text())
            for j in range(1, num + 1):
                # print(j)
                page = j
                url_collection = url + '?page={}'.format(page)

                spider_collection = GetPrice(url_collection)
                spider_collection_select = ' div.zm-item h2 a '
                pa = spider_collection.getPrice(spider_collection_select)
                xx = [y['href'] for y in pa if y['href'][0] == '/']
                listQ += xx
            urlQ = ['https://www.zhihu.com/' + i for i in listQ]
            print('scoll.py try 完成')
        except:

            spider_collection_select = ' div.zm-item h2 a '
            pa = spider.getPrice(spider_collection_select)
            xx = [y['href'] for y in pa if y['href'][0] == '/']

            urlQ = ['https://www.zhihu.com/' + i for i in xx]
            print('scoll.py except 完成')

        return urlQ
oneScollection = Scollection()
oneUrl = oneScollection.get_urlQ('www.zhihu.com//collection/132331007')
print(oneUrl)