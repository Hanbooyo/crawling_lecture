import requests
from bs4 import BeautifulSoup
# 네이버 지식인에 파이썬을 검색한 url. 
url = 'https://kin.naver.com/search/list.nhn?query=파이썬'
response = requests.get(url)

# 200(성공): 서버가 요청을 제대로 처리했다는 뜻
#응답 코드가 200 일때
if response.status_code == 200:
    html = response.text 
    soup = BeautifulSoup(html, 'html.parser') # html 을 받아와 soup 객체로 변환.    

    # ul 태그중 basic1 클래스를 가진 녀석을 뽑아오는 선택자
    ul = soup.select_one('ul.basic1')
    #li > dl > dt > a 는 자식 선택자를 이용한 것
    titles = ul.select('li > dl > dt >a')
    for title in titles:
        print(title.get_text())

else : 
    print(response.status_code) # 에러발생시 상태코드 (400, 500, 404 등)