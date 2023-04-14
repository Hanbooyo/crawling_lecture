import requests
from bs4 import BeautifulSoup

# openpyxl은 파이썬에서 엑셀을 다루는것을 쉽게 해주는 도구
from openpyxl import Workbook

# 네이버 파이낸셜 사이트
url = 'https://finance.naver.com/'

# url 요청
response = requests.get(url)

# 해당 url의 정보 모두 텍스트 형태로 가져옴
html = response.text

# HTML의 요소별로 파싱시켜줌
soup = BeautifulSoup(html, 'html.parser')

# 인기 검색 종목의 테이블 안의 요소를 가져옴
# #container > div.aside > div > div.aside_are.aside_popular > table > tbody
tbody = soup.select_one('#container > div.aside > div > div.aside_area.aside_popular > table > tbody')
price_list = tbody.select("td")
slist = tbody.select("a")

count = 0
for i in range(0,len(slist)*2,2):
    temp = slist[count] # 종목 코드 위치 가져와서 슬라이싱
    print('종목 이름:', temp.text ,'종목 코드:', str(temp)[str(temp).find("code=")+5:str(temp).find("code=")+11],
          '현재가:',price_list[i].text, "전일대비:",price_list[i+1].text)
    count += 1
#     print(i.text)