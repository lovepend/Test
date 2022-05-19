from gettext import find
import time
from re import I, S, T
from xml.etree.ElementPath import xpath_tokenizer_re
import keyboard
import pyautogui as pag
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, \
    ElementNotInteractableException

driver = webdriver.Chrome()
url = "https://camping.ulju.ulsan.kr/Pmreservation.do"
driver.get(url)

#로그인 클릭
driver.find_element_by_xpath('/html/body/header/div[1]/div/ul/ul/li[1]/a').click()

#통합 로그인 클릭
driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div/div/div/div[1]/a/img').click()

#아이디 입력
driver.find_element_by_xpath('/html/body/div/div/articel/section/div/div[1]/form/fieldset/label/span/input').send_keys('lovepend1')

driver.find_element_by_xpath('/html/body/div/div/articel/section/div/div[1]/form/fieldset/label/span/input').click()

#비밀번호 입력
driver.find_element_by_xpath('/html/body/div/div/articel/section/div/div[1]/form/fieldset/span/label/input').send_keys('*Zoavld4fkd')

driver.find_element_by_xpath('/html/body/div/div/articel/section/div/div[1]/form/fieldset/span/label/input').click()

#로그인 버튼 클릭
driver.find_element_by_xpath('/html/body/div/div/articel/section/div/div[1]/form/div/input').click()

#온라인 예약
driver.find_element_by_xpath('/html/body/div/div[2]/ul/li[3]/a/span/img').click()

#날짜 선택
#day = '/html/body/div/div[3]/div[2]/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr/td/div/div/div[3]/div[1]/table/tbody/tr/td[6]' #20
day = '/html/body/div/div[3]/div[2]/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr/td/div/div/div[3]/div[1]/table/tbody/tr/td[7]' #21
#day = '/html/body/div/div[3]/div[2]/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[1]' #22
#day = '/html/body/div/div[3]/div[2]/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[5]' #26
#day = '/html/body/div/div[3]/div[2]/div[2]/div/div[1]/div/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[2]/table/thead/tr/td[2]/span'
driver.find_element_by_xpath(day).click()
time.sleep(30)

#캠핑장 선택
#camp = '/html/body/div/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/input[1]' #작천정
camp = '/html/body/div/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/input[2]' #등억
#camp = '/html/body/div/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/input[3]' #달빛
driver.find_element_by_xpath(camp).click() 
time.sleep(30)
#예약가능 선택
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div/input').click()
time.sleep(30)

table = driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/table/tbody")
a = "t"+table.text+"t"


    

#for tr in table.find_elements_by_tag_name("tr"):
#    global td
#    td = tr.find_elements_by_tag_name("td")
#    global s
#    s = "{}".format(td[2].text)  
def last():
    try:
        xpath = '//*[@id="resModal"]/div[2]/div/div[3]/button[2]'
        driver.find_element_by_xpath(xpath).click()
        print("완료")                 
        time.sleep(50)
    except ElementNotInteractableException:
        print("except")
        last()    
                
def 신불산():
    driver.find_element_by_xpath(day).click()
    if (a == "tt"):
        print("예약불가")
        신불산()        
    else:
        print("예약가능")
        #click = 'tableSite > tbody > tr:nth-child(1) > td:nth-child(4) > button'
        click = '//*[@id="tableSite"]/tbody/tr[1]/td[4]/button'
        #click = '//*[@id="tableSite"]/tbody/tr[2]/td[4]/button' #두번째
        #click = '//*[@id="tableSite"]/tbody/tr[3]/td[4]/button' #세번째
        driver.find_element_by_xpath(click).click()
        last()

신불산()

def Test_job():
    while True:
        print(s)
        time.sleep(0.1)
        driver.find_element_by_xpath(day).click()
        try:
            if (s == None):
                print("종료")
            else :
                #click = 'tableSite > tbody > tr:nth-child(1) > td:nth-child(4) > button'
                click = '//*[@id="tableSite"]/tbody/tr[1]/td[4]/button'
                #click = '//*[@id="tableSite"]/tbody/tr[2]/td[4]/button' #두번째
                #click = '//*[@id="tableSite"]/tbody/tr[3]/td[4]/button' #두번째
                driver.find_element_by_xpath(click).click()
                last()
        except NameError:
            print("except")
            Test_job()

def job1():
    while True:
        driver.find_element_by_xpath(day).click()
        try:
            if (s == True):
                xpath = '//*[@id="tableSite"]/tbody/tr[1]/td[4]/button'
                driver.find_element_by_xpath(xpath).click()
                xpath = '//*[@id="resModal"]/div[2]/div/div[3]/button[2]'
                driver.find_element_by_xpath(xpath).click()
                print("if")
            else :
                print("종료")
        except NameError:
            print("except")
            job1()


 



