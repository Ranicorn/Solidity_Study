import string
import urllib.error, urllib.request, urllib.parse
import http.cookiejar as cookiejar
from bs4 import BeautifulSoup


id = 'wlfks369'
psw = 'rksmd0221'
url = 'https://www.acmicpc.net/user/wlfks369'

hdr = {'User-Agent': 'Mozilla/5.0'}

cj = cookiejar.CookieJar()

cookieProcessor = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookieProcessor)
login_data = urllib.parse.urlencode({'id':id, 'pw':psw}).encode('utf-8')
req = urllib.request.Request(url, data = login_data, headers = hdr)
response = urllib.request.urlopen(req)
txt = response.read().decode('utf-8')
print((txt.find("a href='/status?user_id=wlfks369&amp;result_id=4'")))

bsObj = BeautifulSoup(response.read(), "html.parser")
print(bsObj.h1)

# with urllib.request.urlopen(req, login_data) as f:
#     resp = f.read().decode('utf-8')
#     print(resp)
