from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome("chromedriver.exe") 

driver.get('https://www.google.com')

elem = driver.find_element(By.CSS_SELECTOR, '#APjFqb')

elem.send_keys("대한민국") #검색어 입력
elem.send_keys(Keys.RETURN) #엔터키 입력
time.sleep(15)

