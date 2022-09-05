import sys, os, time, requests
import pandas as pd
import numpy as np
from database import data
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from set_chromedriver import set_chrome_driver

address_list = []; text_list = []; deal_list = []
price_list = []; kind_list = []; area_list = []
subregion_list = []
# 브라우저 정보 확인하는 사이트 : https://www.whatismybrowser.com/
# 네이버 부동산 URL: https://land.naver.com/
driver = set_chrome_driver()                                                                            # 크롬드라이버 자동 연결 및 크롬 실행
driver.implicitly_wait(15)                                                                              # 묵시적 대기, 활성화를 최대 15초까지 기다린다.
BASE_URL = 'https://new.land.naver.com/complexes?ms=37.514592,127.105863,15&a=APT:ABYG:JGC&e=RETAIL'    # 사이트 주소

driver.get(url=BASE_URL)
time.sleep(2)

# -도 설정 -- 현재는 반드시 서울시!
driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div[2]/div/div[1]/div/div/a/span[1]').click(); time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div[2]/div/div[1]/div/div/div/div[2]/ul/li[1]/label').click(); time.sleep(1)
# -구 설정 -- 현재는 반드시 양천구!
driver.find_element(By.XPATH, data.gu_dict['양천구']).click(); time.sleep(1)
# -동 설정 -- 현재는 반드시 신정동!
driver.find_element(By.XPATH, data.yangcheongu_dict['신정동']).click(); time.sleep(1)

# 가나다순에서 목록하나씩 긁어오기
items = driver.find_element(By.CLASS_NAME, 'area_list--complex').text.split()
#item_list = items.split('\n')

for item in items:
    print(item)
time.sleep(1)

#driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div[2]/div/div[1]/div/div/div/div[4]').click(); time.sleep(1)

# item = driver.find_element(By.CSS_SELECTOR, ".item_list.item_list--article").text
# print(item)

while(True):
    pass

# # 하위 지역 가져오기 # subregion_list = driver.find_element(By.CLASS_NAME, 'area_list--district').text.split() # print(subregion_list[-1])

driver.quit()