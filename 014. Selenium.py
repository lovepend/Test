from lib2to3.pgen2 import driver
import logging
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pyautogui as pag



id = "lovepend@nate.com"
password = "*"


chrome = webdriver.Chrome('chromedriver.exe')
time.sleep(1)


chrome.get('https://www.junggu.ulsan.kr/camping/member/login.do')

input_id = chrome.find_element_by_css_selector('#m_email')
input_id.send_keys(id)
print(input_id)
time.sleep(5)

input_pw = chrome.find_element_by_css_selector('#m_passwd')
input_pw.send_keys('*')
print(input_pw)
time.sleep(5)

logging_A = chrome.find_element_by_css_selector('#loginForm > fieldset > button')
logging_A.click()
time.sleep(60)

Re_1 = chrome.find_element_by_css_selector('#siteList > div.rsv_list > div > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(3) > button')
Re_1.click()



#m_id
#siteList > div.rsv_list > div > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(3) > a
#siteList > div.rsv_list > div > table.board_list.num2 > tbody > tr:nth-child(7) > td:nth-child(3) > button
#siteList > div.rsv_list > div > table.board_list.num2 > tbody > tr:nth-child(16) > td:nth-child(3) > button



##############################################################
#link = chrome.find_element_by_css_selector('#container > div.calendar_w > table > tbody > tr:nth-child(5) > td:nth-child(5) > div > li:nth-child(17) > a > img')
#link.click()





time.sleep(100)

#driver.quit()