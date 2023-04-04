# blot.replit.com 페이지에서 블로그 제목과 날짜/저자 정보를 추출

import requests
from bs4 import BeautifulSoup

res = requests.get("https://blog.replit.com")
soup = BeautifulSoup(res.content, 'html.parser')
'''
for tag in soup.find_all(class_='post-title'):
    print(tag.a.string.strip())
    print(tag.parent.h3.string.strip())
    print("----------------------------------")
'''

# 제목과 날짜/저자보다 상위 태그인 article을 찾아서 출력하는 방식
'''
for tag in soup.find_all("article"):
    print(tag.h1.a.string.strip())
    print(tag.h3.string.strip())
    print("----------------------------------")
'''


# 제목과 날짜/저자를 검색하여 resultset으로 저장하고 for문으로 출력하는 방법
'''
title = soup.find_all(class_='post-title')
info = soup.find_all(class_='post-author')
for tag in range(len(title)):
    print(title[tag].a.string.strip())
    print(info[tag].string.strip())
    print("----------------------------------")
'''

# select를 이용하는 방법
for tag in soup.select('.post-title'):
    print(tag.a.string.strip())
    print(tag.parent.h3.string.strip())
    print("----------------------------------")
