from bs4 import BeautifulSoup
import requests
import os,re
class GetPrice(object):
    def __init__(self,url,headers=''):
        self.url = url
        self.headers = headers
    def getPrice(self,select):
        wb_data = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        pay = soup.select(select)
        return pay

# url = 'https://sanwen8.cn/p/17cVUBh.html'
# spider = GetPrice(url)
#
#
# select2 = 'a'
#
# pay2 = spider.getPrice(select2)
# print(pay2)