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

#대왕암 Test 2022.03.17 #Viewer Size 80% #화면 맨아래로 통일

################################## 리셋 
global 대왕암_end_command
대왕암_end_command = 0

################################## 범위 
global 대왕암_find_range
대왕암_find_range = 860,521,1515,968

################################## 아이디
global 대왕암_id
대왕암_id = "pend"
global 대왕암_pw
대왕암_pw = "*Zoavld4fkd" 

################################## 커서
global 대왕암_position_up
대왕암_position_up  = 1300,706
global 대왕암_position_down
대왕암_position_down  = 1300,909

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
    대왕암_day1 = 878,673
    print(대왕암_day1)

def 대왕암_Day2():
    global 대왕암_day1
    대왕암_day1= 878,729
    print(대왕암_day1)

def 대왕암_Day3():
    global 대왕암_day1
    대왕암_day1 = 878,763
    print(대왕암_day1)

def 대왕암_Day4():
    global 대왕암_day1
    대왕암_day1 = 878,809
    print(대왕암_day1)

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
        tm = time.localtime()
        if 대왕암_end_command == 1 : # 대왕암_end_command 가 1이 되면
            print("end_command = 1 종료")
            break
        if keyboard.is_pressed("F2") : # F2 누른게 감지되면
            print("F2 종료")
            break
        #종료 조건
        if (tm.tm_hour == 13 and tm.tm_min == 40) or (tm.tm_hour == 8 and tm.tm_min == 40) : #10시 50분 및 14시 50분 종료
            print("minute 중지")
            print(tm.tm_hour ,"시", tm.tm_min ,"분", tm.tm_sec,"초")
            break
        global 대왕암_i
        대왕암_i = 대왕암_i + 1
        print(대왕암_i)
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
    button = pag.locateCenterOnScreen("./image/02._1. reservation.png", region = 대왕암_find_range, confidence=0.85) 
    if (button == None) :
        None      
    else : 
        time.sleep(0.05) 
        pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 
        대왕암_확인()
        
def 대왕암_확인() :
    button1 = pag.locateCenterOnScreen('./image/02._2. next.png', confidence=0.7)   
    print(button1)
    if (button1 == None) :
        대왕암_확인()      
    else :
        pag.click(1084,283)
        time.sleep(0.05)
        pag.click(1084,283)
        time.sleep(0.05)
        pag.click(1084,283)
        time.sleep(0.05)
        pag.click(1084,283)
        time.sleep(0.05)
        pag.click(1084,283)
        time.sleep(0.05)
        pag.click(button1.x,button1.y, button='left', clicks=5, interval=0.1)
        refresh_token()
        kakao_message_you("대왕암")
        time.sleep(30)
        print('enter')
        time.sleep(5)
        pag.click(1078,198)
        time.sleep(5)
        pag.click(1078,198)
        대왕암_Start()

#★★★★★★★★★★★★★★★★★★★ 서브 함수
def 대왕암_Karavan():
    while True:
        if 대왕암_end_command == 1 : # 대왕암_end_command 가 1이 되면
            break
        if keyboard.is_pressed("F2") : # F2 누른게 감지되면
            print("중지")
            break
        global i
        i = i + 1
        #날짜 클릭
        pag.click(대왕암_day1)
        time.sleep(0.2)
        #검색
        대왕암_검색()
        #page 아래 
        pag.click(대왕암_position_down)
        time.sleep(0.2)
        대왕암_검색()
        #page 업 
        pag.click(대왕암_position_up)
        time.sleep(0.2)
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
