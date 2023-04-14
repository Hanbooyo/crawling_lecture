from selenium import webdriver
import time #time 도구 import

driver = webdriver.Chrome("chromedriver.exe") #크롬드라이버를 이용해 드라이버객체 생성
driver.get("https://www.naver.com")

time.sleep(200) #여기서 10초간 멈춤

#driver.quit() 스크래핑을 끝내고 웹브라우져를 종료하고싶다면 quit 메서드를 사용