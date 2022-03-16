from lib2to3.pgen2 import driver
import logging
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pyautogui as pag

id = "lovepend@nate"
password = "12345678"


chrome = webdriver.Chrome('chromedriver.exe')
chrome.get('https://xn--om2bi2o9qdy7a48exzk3vf68fzzd.kr/reserve/month')

loggin = chrome.find_element_by_css_selector('#container > div.calendar_w > table > tbody > tr:nth-child(5) > td:nth-child(5) > div > li:nth-child(17) > a > img')
loggin.click()
pag.hotkey('enter')

#m_id


##############################################################
#link = chrome.find_element_by_css_selector('#container > div.calendar_w > table > tbody > tr:nth-child(5) > td:nth-child(5) > div > li:nth-child(17) > a > img')
#link.click()


#input_box = chrome.find_element_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
#input_box.send_keys('python')
#print(input_box)

time.sleep(100)

driver.quit()