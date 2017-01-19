from bs4 import BeautifulSoup
import requests,random
import os,re,time
st = time.time()
time.sleep(random.randint(1, 10))
time.sleep(random.randint(1, 10))
end = time.time()
f = open('/Users/user/Desktop/cs.txt','a')
f.write(str([1,'ss']))
f.close()
print(end - st)