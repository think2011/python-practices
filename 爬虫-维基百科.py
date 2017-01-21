import requests as r
from bs4 import BeautifulSoup
import re

origin = 'https://en.wikipedia.org'
url = origin + '/wiki/Main_Page'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, sdch, br',
    'accept-language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6,en;q=0.4,sr;q=0.2',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'referer': 'https://www.google.com/',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
}

# 请求内容
res = r.get(url, headers=headers)
# 解析html
soup = BeautifulSoup(res.text, 'lxml')
# 提取有效链接
urls = soup.findAll('a', href=re.compile('^/wiki/'))

for url in urls:
    print(origin + url['href'])
