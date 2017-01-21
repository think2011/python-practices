import requests as r
from bs4 import BeautifulSoup
import re
import pymysql.cursors

# 连接数据库
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db='wiki',
    charset='utf8'
)

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

try:
    # 写入数据库
    for url in urls:
        with connection.cursor() as cursor:
            sql = 'INSERT INTO urls(name,url) VALUES(%s,%s)'
            cursor.execute(sql, (url.get_text(), url['href']))

    connection.commit()
finally:
    connection.close()
