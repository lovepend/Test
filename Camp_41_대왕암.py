from gettext import find
from tkinter import *
from kakao_01_api import *
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

pag.FAILSAFE=False
import cv2
cv2.useOptimized()
True

#대왕암 Test 2022.03.17 #Viewer Size 67% #화면 맨아래로 통일

################################## 리셋 
global 대왕암_end_command
대왕암_end_command = 0

################################## 범위 
global 대왕암_find_range
대왕암_find_range = 921,657,1387,1025

################################## 아이디
global 대왕암_id
대왕암_id = "pend"
global 대왕암_pw
대왕암_pw = "*Zoavld4fkd" 

################################## 커서
global 대왕암_position_up
대왕암_position_up  = 1335,780
global 대왕암_position_down
대왕암_position_down  = 1335,979

#★★★★★★★★★★★★★★★★★★★ 리셋 입력
def 대왕암_Reset():
    global 대왕암_end_command
    대왕암_end_command = 0

#★★★★★★★★★★★★★★★★★★★ 아이디 입력
def 대왕암_Log_Id1():
    global 대왕암_id
    대왕암_id = "pend"
    print(대왕암_id)

def 대왕암_Log_Id2():
    global 대왕암_id
    대왕암_id = "lovepend2"
    print(대왕암_id)

def 대왕암_Log_Id3():
    global 대왕암_id
    대왕암_id = "lovepend3"
    print(대왕암_id)

def 대왕암_Log_Id4():
    global 대왕암_id
    대왕암_id = "parkmc7"
    print(대왕암_id)

def 대왕암_Log_Guest():
    global 대왕암_id
    대왕암_id = "ssss8841"
    global 대왕암_pw
    대왕암_pw = "sm@884100!"
    print(대왕암_id)
    print(대왕암_pw)

global 대왕암_i 
대왕암_i = 0       

#★★★★★★★★★★★★★★★★★★★ 날짜 입력
def 대왕암_Day1():
    global 대왕암_day1
    대왕암_day1 = 913,761
    print(대왕암_day1)

def 대왕암_Day2():
    global 대왕암_day1
    대왕암_day1= 913,807
    print(대왕암_day1)

def 대왕암_Day3():
    global 대왕암_day1
    대왕암_day1 = 913,852
    print(대왕암_day1)

def 대왕암_Day4():
    global 대왕암_day1
    대왕암_day1 = 913,892
    print(대왕암_day1)

def 대왕암_Day5():
    global 대왕암_day5
    대왕암_Day5 = 913,947
    print(대왕암_day5)
#★★★★★★★★★★★★★★★★★★★ 날짜 입력
def 대왕암_Day():
    while True:
        if keyboard.is_pressed("F2"): 
            global 대왕암_day1 
            대왕암_day1  = pag.position()
            print(대왕암_day1)
            time.sleep(0.5)
            break         

#★★★★★★★★★★★★★★★★★★★ 커서 입력
def 대왕암_커서선택():
    while True:
        if keyboard.is_pressed("F2"): 
            global 대왕암_position_up
            대왕암_position_up  = pag.position()
            print(대왕암_position_up)
            time.sleep(0.5)
            break 
    
    while True:
        if keyboard.is_pressed("F2"): 
            global 대왕암_position_down
            대왕암_position_down  = pag.position()
            print(대왕암_position_down)
            time.sleep(0.5)
            break 

#★★★★★★★★★★★★★★★★★★★ 범위 입력
def 대왕암_범위선택():
    while True:
        if keyboard.is_pressed("F2"): 
            global 대왕암_find_range1 
            대왕암_find_range1  = pag.position()
            print(대왕암_find_range1)
            time.sleep(0.5)
            break  
    while True:
        if keyboard.is_pressed("F2"): 
            global 대왕암_find_range2 
            대왕암_find_range2  = pag.position()
            print(대왕암_find_range2)
            time.sleep(0.5)
            break  
    global 대왕암_find_range
    대왕암_find_range = (대왕암_find_range1.x,대왕암_find_range1.y,대왕암_find_range2.x,대왕암_find_range2.y)
 
#★★★★★★★★★★★★★★★★★★★ 자동 입력
def 대왕암_자동입력():
    time.sleep(2)
    #로그인 선택
    pag.click(1296,117)
    time.sleep(5)
    #통합회원 로그인
    pag.click(815,602)
    time.sleep(5)
    #아이디 입력
    pag.moveTo(1000,300)
    time.sleep(2)
    pag.dragTo(100,300, 5, button='left')
    time.sleep(2)
    pag.hotkey('delete')
    time.sleep(2)
    pag.write(대왕암_id)
    print(대왕암_id)
    time.sleep(2)
    #페이지 선택
    pag.doubleClick(1600,800)
    time.sleep(1)
    #비밀번호 입력
    pag.moveTo(1000,353)
    time.sleep(2)
    pag.dragTo(100,353, 5, button='left')
    time.sleep(2)
    pag.hotkey('delete')
    time.sleep(2)
    pag.write(대왕암_pw)
    print(대왕암_pw)
    time.sleep(2)
    #로그인 버튼 클릭
    pag.click(927,403)
    time.sleep(5)
    #온라인 예약
    pag.click(1080,200)
    time.sleep(5)   
    
#★★★★★★★★★★★★★★★★★★★ 메인 함수 
def 대왕암_Start():
    while True:
        if keyboard.is_pressed("F2") : # F2 누른게 감지되면
            print("F2 종료")
            break
        #날짜 클릭
        pag.click(대왕암_day1)
        time.sleep(0.5)
        #검색
        대왕암_검색()
        time.sleep(0.2)
        #page 위
        pag.click(대왕암_position_up)
        time.sleep(0.2)
        대왕암_검색()
        time.sleep(0.2)
        #page 위
        pag.click(대왕암_position_up)
        time.sleep(0.2)
        대왕암_검색()
        time.sleep(0.2)
        #page 위
        pag.click(대왕암_position_up)
        time.sleep(0.2)
        대왕암_검색()
        #page 위
        pag.click(대왕암_position_up)
        time.sleep(0.2)
        대왕암_검색()
        #page 아래
        pag.hotkey('end')
        time.sleep(0.3)
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break        

def 대왕암_검색():
    #검색
    button = pag.locateCenterOnScreen("./image/41. Donggu/02._1. reservation.png", region = 대왕암_find_range, confidence=0.85) 
    if (button == None) :
        None      
    else : 
        time.sleep(0.05) 
        pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 
        대왕암_확인()
        
def 대왕암_확인() :
    button1 = pag.locateCenterOnScreen('./image/41. Donggu/02._2. next.png', confidence=0.7)   
    print(button1)
    if (button1 == None) :
        대왕암_확인()      
    else :
        time.sleep(0.05)
        pag.click(button1.x,button1.y, button='left', clicks=5, interval=0.1)
        refresh_token()
        kakao_message_you("대왕암")
        time.sleep(30)
        pag.hotkey('esc')
        time.sleep(5)
        pag.hotkey('esc')
        time.sleep(5)
        pag.hotkey('esc')
        time.sleep(5)
        pag.click(1082,198)
        time.sleep(5)
        pag.click(1078,198)
        time.sleep(5)
        pag.click(1082,198)
        time.sleep(5)
        pag.click(대왕암_day1)
        time.sleep(5)
        pag.click(1302,712)
        대왕암_Start()

#★★★★★★★★★★★★★★★★★★★ 서브 함수
def 대왕암_Karavan():
    while True:
        if keyboard.is_pressed("F2") : # F2 누른게 감지되면
            print("중지")
            break
        #날짜 클릭
        pag.click(대왕암_day1)
        time.sleep(0.5)
        #검색
        대왕암_검색()
        #page 아래 
        pag.click(대왕암_position_down)
        time.sleep(0.5)
        대왕암_검색()
        #page 업 
        pag.click(대왕암_position_up)
        time.sleep(0.5)
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break
                    
#★★★★★★★★★★★★★★★★★★★ 스케쥴러
def 대왕암_자동():
    time.sleep(5)
    #접속
    pag.click(466,84)
    time.sleep(5)
    pag.click(523,211)
    time.sleep(5)
    #로그아웃
    pag.click(1363,120)
    time.sleep(5)
    대왕암_Reset()
    #접속
    pag.click(466,84)
    time.sleep(5)
    pag.click(523,211)
    time.sleep(5)
    #대왕암공원캠핑장 선택
    pag.click(751,117)
    time.sleep(5)
    대왕암_자동입력()
    대왕암_Start()
