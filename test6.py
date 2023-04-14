import requests
from bs4 import BeautifulSoup

#Request : 파이썬 프로그래밍 언어용 HTTP 요청등을 보낼 수 있도록 기능을 제공하는 라이브러리
#웹 파싱은 웹상의 자연어, 컴퓨터 언어들의 일련의 문자열들을 분석하는 프로세스

#BeautifulSoup : 웹페이즈의 정보를 십게 스크랩 할 수 있도록 기능을 제공하는 라이브러리
# 웹 스크래핑은 다양한 웹사이트로 부터 데이터를 추출하는 기술

url = "https://www.naver.com"
result = requests.get(url)
print(result)
# <Response [200]> 반환

html = result.text     # html 내용 반환
print(html)

soup = BeautifulSoup(html, "html.parser") # 파싱 (paring)은 즉, 규격화라고 할 수 있다.
print(soup)