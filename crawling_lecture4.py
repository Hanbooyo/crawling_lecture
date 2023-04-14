from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=8pSC6QgxFzI&t=593s")

time.sleep(1.5)

driver.execute_script("window.scrollTo(0, 800)")
time.sleep(3)

last_height = driver.execute_script("return document.documentElement.scrollHeight") #현재페이지의 스크롤높이 저장

#스크롤을 2번 내리는 부문
#while True: # 끝까지 내릴때 
for i in range(0,2): # 2번만 내리겠다.
    # scroll을 내리고
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    
    # 댓글이 다 뜰때까지 기다리기 위해서 1.5초 기다림
    time.sleep(1.5)
    
    #내린 상태에서의 높이를 반환해서 new_height에 넣음
    new_height = driver.execute_script("return document.documentElement.scrollHeight")

    # new_height == last_height 둘이 같은 상태는? => 다 내렸을때, 더 이상 스크롤이 안내려감 => 스크롤을 다 내린것
    if new_height == last_height: 
        break # 스크롤을 다 내렸을때 반복문 탈출
    # 내린 상태의 높이값이 new height한테 있으니, last_height에 넣어줌 (마지막 높이로 정의)
    last_height = new_height

time.sleep(5)

# 유튜브 프리미엄 팝업이 뜨는 것을 닫아주는 역할
try:
    driver.find_element(By.CSS_SELECTOR,"#dismiss-button").click()
except:
    pass

# ================================ 여기까지 댓글이 다 렌더링 될때까지 기다림

html_source = driver.page_source #page source의 특징: 스크롤을 다 내리면서 댓글이 다 뜸 ( html에 댓글정보가 들어감 ) 렌더링을 다 하고 그 hmtl 소스를 여기 넣는것이다.
soup = BeautifulSoup(html_source, 'html.parser')

                        #div중에 id가 header-author인걸 찾고 id가 autor-text인걸 찾고, span부분
id_list = soup.select("#author-text > span")
content_list = soup.select("#content-text")
#len(id_list) == len(content_list)

import pandas as pd

id_list_zip =[]
content_list_zip = []

for i in range(0, len(id_list)):
    id_list_zip.append(str(id_list[i].text).strip())
    content_list_zip.append(content_list[i].text)


sdict = {'작성자':id_list_zip,
         '댓글' : content_list_zip
         }

you_tube = pd.DataFrame(sdict)

you_tube.to_csv("youtube.result.csv")

# for i in range(0, len(id_list)):
#     print("작성자:",str(id_list[i].text).strip(),'||',"댓글:",content_list[i].text)
#     print('---------------------------------')

#for i in content_list:
#    print(i.text)
#    print('---------------------------------')

#for i in id_list:
#    print(i.text) # i 는 bs4 의 객체이기 때문에 text 내장함수가 있다.
#    print(str(i.text).strip())
                        #yt-formatted-string 요소 중에 id가 content-text인것들 찾기
# comment_list = soup.select("yt-formatted-string#content-text")
# 
# print(comment_list)
