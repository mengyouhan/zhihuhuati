from bs4 import BeautifulSoup
import requests
import os
from selenium import webdriver

url = 'https://www.zhihu.com/people/yao-dao-1412/collections'
urlQs = []
num = 3
for j in range(1, num + 1):
    # print(j)
    page = j
    url_collection = url + '?page={}'.format(page)
    driver = webdriver.PhantomJS()
    driver.get(url_collection)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    pa = soup.select('#Profile-collections div h2 div a')
    # print(pa)
    urlQ = ['https://www.zhihu.com/' + i['href'] for i in pa]
    urlQs += urlQ
# print(urlQs)