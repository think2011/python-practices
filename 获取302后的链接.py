import json
from urllib import parse
import requests

urls = [
    'https://tb.cn/Tt1ou8x'
]
cookies = [
    {
        "domain": ".taobao.com",
        "expirationDate": 1518243330.096928,
        "hostOnly": False,
        "httpOnly": False,
        "name": "_cc_",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "V32FPkk%2Fhw%3D%3D",
        "id": 1
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "_l_g_",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "Ug%3D%3D",
        "id": 2
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "_nk_",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "%5Cu667A%5Cu53CB%5Cu8BBE%5Cu8BA1",
        "id": 3
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "_tb_token_",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "0pFmnascGS21bLTVSSzL",
        "id": 4
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1802077591.263633,
        "hostOnly": False,
        "httpOnly": False,
        "name": "ali_ab",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "219.136.144.169.1457063587521.2",
        "id": 5
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1800092206,
        "hostOnly": False,
        "httpOnly": False,
        "name": "cna",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "IuVeD/3vzBcCAduIkkCnXdb+",
        "id": 6
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "cookie1",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "BxSjS%2F%2BSvCNjZ%2BHUfanhClBNR8j0Cp9uILmp5VV7hhM%3D",
        "id": 7
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "cookie17",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "UUwQkA1lNFYXbQ%3D%3D",
        "id": 8
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "cookie2",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "1c8c558911c07dbd85a71ac9e04ff053",
        "id": 9
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "existShop",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "MTQ4NjcwNzMzMA%3D%3D",
        "id": 10
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1515566745.102436,
        "hostOnly": False,
        "httpOnly": False,
        "name": "hng",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "CN%7Czh-cn%7CCNY",
        "id": 11
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1502269595,
        "hostOnly": False,
        "httpOnly": False,
        "name": "isg",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "Ap6eJVzmSlSmCJ4o59TN6mtk7zLEfGLZ3Xd360gnCuHcaz5FsO-y6cSLDcAd",
        "id": 12
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1896134400,
        "hostOnly": False,
        "httpOnly": False,
        "name": "l",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "AtfX-zfAGWwFd7b2eGI7y38T50EhHKt-",
        "id": 13
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1489299330.09552,
        "hostOnly": False,
        "httpOnly": False,
        "name": "lgc",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "%5Cu667A%5Cu53CB%5Cu8BBE%5Cu8BA1",
        "id": 14
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1788578914,
        "hostOnly": False,
        "httpOnly": False,
        "name": "lzstat_uv",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "18677630473752898585|2144678",
        "id": 15
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1547604613.128304,
        "hostOnly": False,
        "httpOnly": False,
        "name": "miid",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "8179496107237979619",
        "id": 16
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1487312130.09665,
        "hostOnly": False,
        "httpOnly": False,
        "name": "mt",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "np=&ci=-1_0",
        "id": 17
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "sg",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "%E8%AE%A185",
        "id": 18
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "skt",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "4c6edb67165e0f37",
        "id": 19
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1494483330.096829,
        "hostOnly": False,
        "httpOnly": False,
        "name": "t",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "7118535fd794053ff6ccbb629c903ef9",
        "id": 20
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1540707330.097025,
        "hostOnly": False,
        "httpOnly": False,
        "name": "tg",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "0",
        "id": 21
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1488591934.357312,
        "hostOnly": False,
        "httpOnly": False,
        "name": "thw",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "cn",
        "id": 22
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1518243330.096185,
        "hostOnly": False,
        "httpOnly": False,
        "name": "tracknick",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "%5Cu667A%5Cu53CB%5Cu8BBE%5Cu8BA1",
        "id": 23
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "uc1",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=UtASsssmfaCONGki4KTH3w%3D%3D&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=True&pas=0&cookie14=UoW%2FW0EQf43aDQ%3D%3D&tag=0&lng=zh_CN",
        "id": 24
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1489299330.094986,
        "hostOnly": False,
        "httpOnly": True,
        "name": "uc3",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "sg2=BYjZvYYDr4DdEKP27wcbgDU8xyLkx0uDfmYgbI3kLDo%3D&nk2=tYzvT6WaNFM%3D&id2=UUwQkA1lNFYXbQ%3D%3D&vt3=F8dARHtKN0oeTyR0%2F4I%3D&lg2=W5iHLLyFOGW7aA%3D%3D",
        "id": 25
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": True,
        "name": "unb",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "2406822118",
        "id": 26
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1489299330.095419,
        "hostOnly": False,
        "httpOnly": True,
        "name": "uss",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "BYTsp9xZMo9C6QqKiE%2Fx2Mem4PPTcJbHBWPDR1dxqWMACt1g5FfqqgVFoQ%3D%3D",
        "id": 27
    },
    {
        "domain": ".taobao.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "v",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": True,
        "storeId": "0",
        "value": "0",
        "id": 28
    },
    {
        "domain": ".taobao.com",
        "expirationDate": 1512213739,
        "hostOnly": False,
        "httpOnly": False,
        "name": "x",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0",
        "id": 29
    },
    {
        "domain": "fuwu.taobao.com",
        "expirationDate": 1502438716,
        "hostOnly": True,
        "httpOnly": False,
        "name": "CNZZDATA1254543239",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "2102521484-1457924617-null%7C1486713529",
        "id": 30
    },
    {
        "domain": "fuwu.taobao.com",
        "expirationDate": 1502438716,
        "hostOnly": True,
        "httpOnly": False,
        "name": "CNZZDATA1254544523",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "1734102489-1479281045-https%253A%252F%252Ffuwu.taobao.com%252F%7C1486712937",
        "id": 31
    },
    {
        "domain": "fuwu.taobao.com",
        "expirationDate": 1499758894,
        "hostOnly": True,
        "httpOnly": False,
        "name": "CNZZDATA1254544540",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "871041520-1457921900-null%7C1484033106",
        "id": 32
    },
    {
        "domain": "fuwu.taobao.com",
        "expirationDate": 1502442393,
        "hostOnly": True,
        "httpOnly": False,
        "name": "CNZZDATA1254544575",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "1496472377-1483664143-%7C1486714286",
        "id": 33
    },
    {
        "domain": "fuwu.taobao.com",
        "expirationDate": 1499758894,
        "hostOnly": True,
        "httpOnly": False,
        "name": "CNZZDATA1254544594",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": False,
        "session": False,
        "storeId": "0",
        "value": "1564681719-1457919792-null%7C1484031461",
        "id": 34
    }
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
}

newCookies = {}
for item in cookies:
    newCookies[item['name']] = item['value']

results = []
for url in urls:
    r = requests.get(url, headers=headers, cookies=newCookies)
    results.append({
        'url': url.replace('https://', '//'),
        'qnUrl': parse.unquote(r.url.replace('https://', '//qianniu.'))
    })

print(json.dumps(results, indent=2, ensure_ascii=False))
