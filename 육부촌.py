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

#육부촌 Test 2022.06.28 #Viewer Size 50% #화면 맨아래로 통일

#★★★★★★★★★★★★★★★★★★★ 날짜 입력
def 육부촌_Day1():
    global 육부촌_day1
    육부촌_day1 = 945,379
    print(육부촌_day1)

def 육부촌_Day2():
    global 육부촌_day2
    육부촌_day2= 945,402
    print(육부촌_day2)

def 육부촌_Day3():
    global 육부촌_day3
    육부촌_day3 = 945,419
    print(육부촌_day3)

def 육부촌_Day4():
    global 육부촌_day4
    육부촌_day4 = 945,439
    print(육부촌_day4)

def 육부촌_Day5():
    global 육부촌_day5
    육부촌_day5 = 945,461
    print(육부촌_day5)

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
#육부촌_day1 = 945,379 #첫주
육부촌_day1 = 943, 416 # 21일
global 육부촌_day2
육부촌_day2 = 660,439 # 22일
global 육부촌_day3
육부촌_day3 = 709,439 # 23일
global 육부촌_day4
육부촌_day4 = 945,439 #
global 육부촌_day5
육부촌_day5 = 25,49 #뒤로
#육부촌_day5 = 709, 442 #23일
#육부촌_day5 = 902,441
#★★★★★★★★★★★★★★★★★★★ 날짜 입력
def 육부촌_Day():
    while True:
        if keyboard.is_pressed("F2"): 
            global 육부촌_day1 
            육부촌_day1  = pag.position()
            print(육부촌_day1)
            time.sleep(1)
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

global i 
i = 0    
#★★★★★★★★★★★★★★★★★★★ 메인 함수 
def 육부촌_Start():
    while True:
        global 육부촌_day1
        global 육부촌_day2
        global 육부촌_day3
        global 육부촌_day4
        global 육부촌_day5
        global i
        i = i +1
        print(i)
        if keyboard.is_pressed("F2") : # F2 누른게 감지되면
            print("F2 종료")
            break
        #날짜 클릭
        time.sleep(0.5)
        pag.click(육부촌_day1)
        time.sleep(1)
        육부촌_검색()
        pag.click(육부촌_day2)
        time.sleep(1)
        육부촌_검색()
        pag.click(육부촌_day3)
        time.sleep(1)
        육부촌_검색()
        pag.click(육부촌_day4)
        time.sleep(1)
        육부촌_검색()
        pag.click(육부촌_day5)
        time.sleep(1)
        육부촌_검색()


def 육부촌_검색():
    #검색
    button = pag.locateCenterOnScreen("./image/05._1. reservation.png", region = 육부촌_find_range)#, confidence=0.85) 
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
    time.sleep(0.5)
    #주소검색
    pag.click(837,699)
    pyperclip.copy('반구로55')
    time.sleep(0.2)
    #예)판교역로235
    pag.click(315,139)
    time.sleep(0.4)
    #반구로 55 붙이기
    pag.hotkey('ctrl','v')
    time.sleep(0.4)
    #입력
    pag.hotkey('enter')
    time.sleep(0.4)
    #주소클릭
    pag.click(295,263)   
    time.sleep(0.4)
    #기본주소 클릭
    pag.click(862,746) 
    pyperclip.copy('107동 1001호')
    pag.hotkey('ctrl','v')
    time.sleep(0.4)
    #예약신청
    pag.click(1021,939)
    button2 = pag.locateCenterOnScreen('./image/05._3. next.png', confidence=0.7)   
    pag.click(button2.x,button2.y, button='left', clicks=1, interval=0.1) 
    time.sleep(0.4)
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
