from gettext import find
from tkinter import *
from kakao_api import *
from urllib3 import encode_multipart_formdata
import pyautogui as pag
import win32con
import win32api
import win32gui
import keyboard
import pyperclip
import clipboard
import schedule
import requests
import time
import json

#육부촌 Test 2022.06.28 #Viewer Size 75% #화면 맨아래로 통일

#★★★★★★★★★★★★★★★★★★★ 날짜 입력
def 육부촌_Day1():
    global 육부촌_day1
    육부촌_day1 = 953, 513
    print(육부촌_day1)

def 육부촌_Day2():
    global 육부촌_day1
    육부촌_day1= 953, 545
    print(육부촌_day1)

def 육부촌_Day3():
    global 육부촌_day1
    육부촌_day1 = 953, 575
    print(육부촌_day1)

def 육부촌_Day4():
    global 육부촌_day1
    육부촌_day1 = 952, 608
    print(육부촌_day1)

def 육부촌_Day5():
    global 육부촌_day1
    육부촌_day1 = 952, 634
    print(육부촌_day1)

################################## 범위 
global 육부촌_find_range
육부촌_find_range = 0,0,1800,1000

################################## 커서
global 육부촌_position_up
육부촌_position_up  = 1300,706
global 육부촌_position_down
육부촌_position_down  = 1300,909

################################## 날짜
global 육부촌_day1
육부촌_day1 = 953, 513

#★★★★★★★★★★★★★★★★★★★ 날짜 입력
def 육부촌_Day():
    while True:
        if keyboard.is_pressed("F2"): 
            global 육부촌_day1 
            육부촌_day1  = pag.position()
            print(육부촌_day1)
            time.sleep(0.5)
            break         

#★★★★★★★★★★★★★★★★★★★ 커서 입력
def 육부촌_커서선택():
    while True:
        if keyboard.is_pressed("F2"): 
            global 육부촌_position_up
            육부촌_position_up  = pag.position()
            print(육부촌_position_up)
            time.sleep(0.5)
            break 
    
    while True:
        if keyboard.is_pressed("F2"): 
            global 육부촌_position_down
            육부촌_position_down  = pag.position()
            print(육부촌_position_down)
            time.sleep(0.5)
            break 

#★★★★★★★★★★★★★★★★★★★ 범위 입력
def 육부촌_범위선택():
    while True:
        if keyboard.is_pressed("F2"): 
            global 육부촌_find_range1 
            육부촌_find_range1  = pag.position()
            print(육부촌_find_range1)
            time.sleep(0.5)
            break  
    while True:
        if keyboard.is_pressed("F2"): 
            global 육부촌_find_range2 
            육부촌_find_range2  = pag.position()
            print(육부촌_find_range2)
            time.sleep(0.5)
            break  
    global 육부촌_find_range
    육부촌_find_range = (육부촌_find_range1.x,육부촌_find_range1.y,육부촌_find_range2.x,육부촌_find_range2.y)
 
#★★★★★★★★★★★★★★★★★★★ 자동 입력
def 육부촌_자동입력():
    time.sleep(2)
    
    
#★★★★★★★★★★★★★★★★★★★ 메인 함수 
def 육부촌_Start():
    while True:
        if keyboard.is_pressed("F2") : # F2 누른게 감지되면
            print("F2 종료")
            break
        #날짜 클릭
        pag.hotkey('f5')
        육부촌_검색()
        time.sleep(0.2)


     

def 육부촌_검색():
    #검색
    button = pag.locateCenterOnScreen("./image/05._1. reservation.png", region = 육부촌_find_range, confidence=0.85) 
    if (button == None) :
        None      
    else : 
        time.sleep(0.05) 
        pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 
        육부촌_확인()
        
def 육부촌_확인() :
    time.sleep(0.5)
    button1 = pag.locateCenterOnScreen('./image/05._2. next.png', confidence=0.7)   
    print(button1)
    if (button1 == None) :
        육부촌_확인()      
    else :
        pag.click(button1.x,button1.y, button='left', clicks=5, interval=0.1)
        refresh_token()
        kakao_message_you("육부촌")
        육부촌_주소()

def 육부촌_주소():
    time.sleep(1)
    pag.click(430,13)
    pyperclip.copy('반구로55')
    pag.click(809,896)   
    time.sleep(0.4)
    pag.hotkey('ctrl','v')
    time.sleep(0.4)
    pag.hotkey('enter')
    pag.click(358,267) 
    time.sleep(0.4)
    pag.click(816,954)
    time.sleep(0.4)
    pyperclip.copy('107동1001호')
    pag.hotkey('ctrl','v')
    time.sleep(0.4)
    pag.click(1700,900)
    pag.hotkey('pgdn')
    time.sleep(0.4)
    pag.click(1051,873)
    time.sleep(500)






#★★★★★★★★★★★★★★★★★★★ 서브 함수
def 육부촌_Karavan():
    while True:
        if keyboard.is_pressed("F2") : # F2 누른게 감지되면
            print("중지")
            break
        global i
        i = i + 1
        #날짜 클릭
        pag.click(육부촌_day1)
        time.sleep(0.2)
        #검색
        육부촌_검색()
        #page 아래 
        pag.click(육부촌_position_down)
        time.sleep(0.2)
        육부촌_검색()
        #page 업 
        pag.click(육부촌_position_up)
        time.sleep(0.2)
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break
                    
#★★★★★★★★★★★★★★★★★★★ 스케쥴러
def 육부촌_자동():
    time.sleep(5)
