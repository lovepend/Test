from gettext import find
import imp
from tkinter import *
#from main_캠핑_Rev_0 import *
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
import datetime
import sys

#신불산 Test 2022.03.21 #Viewer Size 67%

################################## 리셋 
global 신불산_end_command
신불산_end_command = 0

################################## 범위 
global 신불산_find_range
신불산_find_range = 860,521,1515,968

################################## 아이디
global 신불산_id
신불산_id = "pend"
global 신불산_pw
신불산_pw = "*Zoavld4fkd" 

################################## 날짜
global 신불산_day
신불산_day = 890, 824

################################## 횟수 
global 신불산_i 
신불산_i = 0

def 신불산_i_end():  
    global i 
    i = 0
    global i_end
    i_end = 5000
    
#★★★★★★★★★★★★★★★★★★★ 리셋 입력
def 신불산_Reset():
    global 신불산_end_command
    신불산_end_command = 0

#★★★★★★★★★★★★★★★★★★★ 아이디 입력
def 신불산_Log_Id1():
    global 신불산_id
    신불산_id = "pend"
    print(신불산_id)

def 신불산_Log_Id2():
    global 신불산_id
    신불산_id = "lovepend2"
    print(신불산_id)

def 신불산_Log_Id3():
    global 신불산_id
    신불산_id = "lovepend3"
    print(신불산_id)

def 신불산_Log_Id4():
    global 신불산_id
    신불산_id = "parkmc7"
    print(신불산_id)

def 신불산_Log_Guest():
    global 신불산_id
    신불산_id = "suld2000@naver.com"
    global 신불산_pw
    신불산_pw = "Sm88410000!"
    print(신불산_id)
    print(신불산_pw)

#★★★★★★★★★★★★★★★★★★★ 날짜 입력
       
def 신불산_Day1():
    global 신불산_day
    신불산_day = 890, 685
    print(신불산_day)

def 신불산_Day2():
    global 신불산_day
    신불산_day = 890, 730
    print(신불산_day)

def 신불산_Day3():
    global 신불산_day
    신불산_day = 890, 773
    print(신불산_day)

def 신불산_Day4():
    global 신불산_day
    신불산_day = 890, 824
    print(신불산_day)

#★★★★★★★★★★★★★★★★★★★ 날짜 입력
def 신불산_Day():
    while True:
        if keyboard.is_pressed("F2"):
            global 신불산_day
            신불산_day  = pag.position()
            print(신불산_day)
            time.sleep(0.5)
            break 
 
#★★★★★★★★★★★★★★★★★★★ 범위 입력 
def 신불산_범위선택():
    while True:
        if keyboard.is_pressed("F2"): 
            global 신불산_find_range1 
            신불산_find_range1  = pag.position()
            print(신불산_find_range1)
            time.sleep(0.5)
            break  
    while True:
        if keyboard.is_pressed("F2"): 
            global 신불산_find_range2 
            신불산_find_range2  = pag.position()
            print(신불산_find_range2)
            time.sleep(0.5)
            break  
    global 신불산_find_range
    신불산_find_range = (신불산_find_range1.x,신불산_find_range1.y,신불산_find_range2.x,신불산_find_range2.y)
   
#★★★★★★★★★★★★★★★★★★★ 자동 입력
def 신불산_자동입력():      
    time.sleep(2)
    #로그인 클릭
    pag.click(1112,115)
    time.sleep(5)
    #통합회원 로그인
    pag.click(669,1064)
    time.sleep(5)
    #아이디 입력
    pag.moveTo(1000,304)
    time.sleep(2)
    pag.dragTo(100,304, 5, button='left')
    time.sleep(2)
    pag.hotkey('delete')
    time.sleep(2)
    pag.write(신불산_id)
    print(신불산_id)
    time.sleep(2)
    #페이지 선택
    pag.doubleClick(1600,800)
    time.sleep(1)
    #비밀번호 입력
    pag.moveTo(1000,352)
    time.sleep(2)
    pag.dragTo(100,352, 5, button='left')
    time.sleep(2)
    pag.hotkey('delete')
    time.sleep(2)
    pag.write(신불산_pw)
    print(신불산_pw)
    time.sleep(2)
    #로그인 클릭
    pag.click(900,403)
    time.sleep(5)
    #온라인 예약 클릭
    pag.click(851,785)
    time.sleep(5)
    #아무 날짜 선택
    pag.click(892,821)
    time.sleep(5)
    #예약가능 사이트만 보기
    pag.click(1201,693)
    time.sleep(5)
    #등억 선택
    pag.click(970,692)
    time.sleep(5)
   
#★★★★★★★★★★★★★★★★★★★ 메인 함수
def 신불산_Start():
    while True:
        global 신불산_end_command
        global 신불산_find_range
        global 신불산_i
        tm = time.localtime()
        #날짜 클릭
        pag.click(신불산_day)
        time.sleep(0.5)        
        #시간 표현
        print(tm)
        #횟수 표현
        신불산_i = 신불산_i + 1
        print(신불산_i)
        #종료 조건
        if (tm.tm_hour == 10 and tm.tm_min == 50) or (tm.tm_hour == 14 and tm.tm_min == 50) : #10시 50분 및 14시 50분 종료
            print("minute 중지")
            print(tm.tm_hour ,"시", tm.tm_min ,"분", tm.tm_sec,"초")
            break
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            print("F2 종료")
            break
        if 신불산_end_command == 1: # end_command = 1이면 종료
            print("end_command = 1 종료")
            break
        #검색
        button = pag.locateCenterOnScreen("./image/04._1. reservation.png", region = 신불산_find_range, confidence=0.7) 
        if (button == None) :
            None      
        else : 
            time.sleep(0.05)
            pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
            신불산_StepA()
                
def 신불산_StepA() : 
    button1 = pag.locateCenterOnScreen('./image/04._2. next.png',  confidence=0.8)   #region = (510,100,1324,333),
    print(button1)
    if (button1 == None) :
        신불산_StepA()      
    else :
        pag.click(1225,281)
        time.sleep(0.05)
        pag.click(1225,281)
        time.sleep(0.05)
        pag.click(1225,281)
        time.sleep(0.05)
        pag.click(1225,281)
        time.sleep(0.05)
        pag.click(1225,281)
        time.sleep(0.05)
        pag.click(button1.x,button1.y+27, button='left', clicks=5, interval=0.1)
        refresh_token()
        kakao_message_you("신불산")
        time.sleep(30)
        #다음 액션 
        print("Again")        
        #뒤로
        pag.hotkey('esc')
        time.sleep(1)
        pag.hotkey('esc')
        time.sleep(1)
        #온라인 예약 클릭
        pag.click(851,785)
        time.sleep(5)
        #아무 날짜 선택
        pag.click(신불산_day)
        time.sleep(5)
        #예약가능 사이트만 보기
        pag.click(1201,693)
        time.sleep(5)
        #등억 선택
        pag.click(970,692)
        time.sleep(5)
        신불산_Start()

#★★★★★★★★★★★★★★★★★★★ 스케쥴러
  
def 신불산_자동():
    신불산_Reset()
    #접속
    pag.click(466,84)
    time.sleep(5)
    pag.click(496,185)
    time.sleep(5)
    신불산_자동입력()
    신불산_Start()




