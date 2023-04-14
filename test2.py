from selenium import webdriver
from selenium.webdriver.common.by import By
import time #time 도구 import
#크롬드라이버를 이용해 드라이버객체 생성
driver = webdriver.Chrome("chromedriver.exe") 

url = "https://www.naver.com"

driver.get(url)

driver.find_element(By.CSS_SELECTOR,'#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(8) > a').click() #해당요소를 click 하겠다.

time.sleep(5)

driver.find_element(By.CSS_SELECTOR,'#menu > li:nth-child(3) > a').click()

time.sleep(200)

#인터넷 통신이 불안정할때는 time을 이용해 딜레이를 줘서 안정화하는 방법도 있음
# time.sleep(3) #여기서 N초간 멈춤
#타임은 논리적으로 잘 이용해야합니다. 예를들어, 로그인 전 페이지로딩이 느리거나 등등 그런 부분들을 잘 고려해서 설계해야합니다.



# url = "https://www.daum.net"
# driver.get(url)
# 
# driver.quit

#driver.quit() 스크래핑을 끝내고 웹브라우져를 종료하고싶다면 quit 메서드를 사용