from lib2to3.pgen2 import driver
import logging
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pyautogui as pag

import urllib.request
import urllib.parse


with urllib.request.urlopen("https://camping.ulju.ulsan.kr/Pmreservation.do") as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    test = soup.find_all('div', class_='li')
    print(test)
    
#//*[@id="tableSite"]/tbody/tr[1]/td[3]