from gettext import find
from re import A
from tkinter import *
from turtle import goto
from kakao_01_api import *
from urllib3 import encode_multipart_formdata
import pyautogui as pag
import webbrowser
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

pag.FAILSAFE=False

#신불산 Test 2022.03.21 #Viewer Size 67%
#56분 36초

def 시간입력_시작(min,sec):
    global 신불산_min
    global 신불산_sec
    신불산_min = int(min)
    신불산_sec = int(sec)
    print(신불산_min)
    print(신불산_sec)
    신불산_Start(신불산_min,신불산_sec)

################################## 리셋 
global 신불산_end_command
신불산_end_command = 0

################################## 리셋 

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

################################## 스캔타임
global time_controll
time_controll = 0.1

################################## 횟수 
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
    신불산_id = "lovepend1"
    print(신불산_id)

def 신불산_Log_Id4():
    global 신불산_id
    신불산_id = "parkmc7"
    print(신불산_id)

def 신불산_Log_Guest():
    global 신불산_id
    신불산_id = "jhrep1201"
    global 신불산_pw
    신불산_pw = "j1902217**"
    print(신불산_id)
    print(신불산_pw)

#★★★★★★★★★★★★★★★★★★★ 날짜 입력
def 신불산_Day():
    while True:
        if keyboard.is_pressed("F2"):
            global 신불산_day
            신불산_day  = pag.position()
            print(신불산_day)
            time.sleep(0.5)
            break 
#★★★★★★★★★★★★★★★★★★★ 날짜 입력
       
def 신불산_Day11():
    global 신불산_day
    신불산_day = 870, 660
    print(신불산_day)

def 신불산_Day12():
    global 신불산_day
    신불산_day = 920, 660
    print(신불산_day)

def 신불산_Day21():
    global 신불산_day
    신불산_day = 870, 715
    print(신불산_day)

def 신불산_Day22():
    global 신불산_day
    신불산_day = 922, 715
    print(신불산_day)

def 신불산_Day31():
    global 신불산_day
    신불산_day = 870, 760
    print(신불산_day)

def 신불산_Day32():
    global 신불산_day
    신불산_day = 922, 760
    print(신불산_day)

def 신불산_Day41():
    global 신불산_day
    신불산_day = 870, 805
    print(신불산_day)

def 신불산_Day42():
    global 신불산_day
    신불산_day = 922, 805
    print(신불산_day)

def 신불산_Day51():
    global 신불산_day
    신불산_day = 870, 850
    print(신불산_day)

def 신불산_Day52():
    global 신불산_day
    신불산_day = 922, 850
    print(신불산_day)

#★★★★★★★★★★★★★★★★★★★ 타임 설정
def 신불산_time_controll_01():
    global time_controll
    time_controll =  0.1
    print(time_controll)

def 신불산_time_controll_02():
    global time_controll
    time_controll =  0.2
    print(time_controll)

def 신불산_time_controll_03():
    global time_controll
    time_controll =  0.3
    print(time_controll)

def 신불산_time_controll_05():
    global time_controll
    time_controll =  0.5
    print(time_controll)

def 신불산_time_controll_07():
    global time_controll
    time_controll =  0.7
    print(time_controll)

def 신불산_time_controll_09():
    global time_controll
    time_controll =  0.9
    print(time_controll)

def 신불산_time_controll_10():
    global time_controll
    time_controll =  1
    print(time_controll)

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
  webbrowser.get("windows-default").open('https://camping.ulju.ulsan.kr/')
  time.sleep(1)
  button = pag.locateCenterOnScreen("./image/11. Sinbul/00. loggin.png",  confidence=0.9)
  print(button)
  if (button == None) :
    #로그인 클릭
    button = pag.locateCenterOnScreen("./image/11. Sinbul/01. loggin.png",  confidence=0.9)
    pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)  
    time.sleep(1)
    #통합회원 로그인
    button = pag.locateCenterOnScreen("./image/11. Sinbul/02. loggin.png",  confidence=0.9)
    pag.click(button.x,button.y+40, button='left', clicks=1, interval=0.1)
    time.sleep(1)
    #아이디  
    button = pag.locateCenterOnScreen("./image/11. Sinbul/03. loggin.png",  confidence=0.9)
    pag.click(button.x,button.y+60, button='left', clicks=1, interval=0.1)
    time.sleep(1)
    pag.dragTo(100,304, 1, button='left')
    pag.hotkey('delete')
    time.sleep(1)
    pag.write(신불산_id)
    print(신불산_id)  
    #페이지 선택
    pag.doubleClick(1600,800)
    #비번
    pag.click(button.x,button.y+90, button='left', clicks=1, interval=0.1)
    time.sleep(1)
    pag.dragTo(100,352, 1, button='left')
    pag.hotkey('delete')
    time.sleep(1)
    pag.write(신불산_pw)
    print(신불산_pw)
    time.sleep(1)
    #로그인 클릭
    button = pag.locateCenterOnScreen("./image/11. Sinbul/04. loggin.png",  confidence=0.8)
    print(button)
    pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
    time.sleep(1)
    온라인예약()
  else :
    print(button)
    time.sleep(1)
    온라인예약()

def 온라인예약():
  time.sleep(1)
  button = pag.locateCenterOnScreen("./image/11. Sinbul/11. reservation.png",  confidence=0.9)
  pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
  time.sleep(1)
  #마지막날 클릭
  pag.click(922,891)
  time.sleep(10)

  
#★★★★★★★★★★★★★★★★★★★ 메인 함수
def 신불산_Start(신불산_min,신불산_sec):
  while True:
    tm = time.localtime()
    global time_controll
    print(time_controll)
    if keyboard.is_pressed("F2"):
      print("종료") 
      break  
    if (tm.tm_hour == 9 and tm.tm_min == 신불산_min and tm.tm_sec == 신불산_sec) or (tm.tm_hour == 13 and tm.tm_min == 신불산_min and tm.tm_sec == 신불산_sec) : #9시 56분 및 15시 56분 시작
    #if (tm.tm_hour == 10 and tm.tm_min == 19 and tm.tm_sec == 10) or (tm.tm_hour == 14 and tm.tm_min == 56 and tm.tm_sec == 37) : #TEST
      pag.click(신불산_day)
      for i in range(1000):
        button = pag.locateCenterOnScreen("./image/11. Sinbul/21. reservation.png", region = 신불산_find_range, confidence=0.7) 
        print(i)
        if (button == None) :
          None
        else : 
          print("else")
          pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
          신불산_StepA()
    #날짜 클릭
    pag.click(신불산_day)  
    time.sleep(time_controll)
    신불산_검색()     

def 신불산_검색():                    
  button = pag.locateCenterOnScreen("./image/11. Sinbul/21. reservation.png", region = 신불산_find_range, confidence=0.7) #region = 신불산_find_range,
  if (button == None) :
    None      
  else : 
    pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
    신불산_StepA()
                
def 신불산_StepA() : ## 예약하기 버튼 순간 정할것
  button1 = pag.locateCenterOnScreen('./image/11. Sinbul/22. next.png',  confidence=0.8)   #region = (510,100,1324,333),
  print(button1)
  if (button1 == None) :
    신불산_StepA()      
  else :  
    tm1 = time.localtime()
    print(tm1.tm_hour,tm1.tm_min,tm1.tm_sec)
    kakao_tm = tm1.tm_hour,tm1.tm_min,tm1.tm_sec
    text = str(kakao_tm)
    print(text)
    refresh_token()
    kakao_message_you(text)
    time.sleep(0.2)
    print(button1)
    button1 = pag.locateCenterOnScreen('./image/11. Sinbul/22. next.png',  confidence=0.8)
    pag.click(button1.x+10,button1.y, button='left', clicks=1, interval=0.1)        
    button1 = pag.locateCenterOnScreen('./image/11. Sinbul/22. next.png',  confidence=0.8)   #region = (510,100,1324,333),
    pag.click(button1.x+10,button1.y, button='left', clicks=1, interval=0.1)
    #pag.click(1264,276)
    print("끝")
        
    # c = 0
    # while True:
    #   if (c < 10) :
    #     c = c + 1
    #     print(c)
    #     pag.click(button1.x+20,button1.y+30, button='left', clicks=1, interval=0.1)
    #   else:
    #     print('end')
    #     print('kakao')
    #     break
  if keyboard.is_pressed("F2"):
    time.sleep(600)
  #신불산_StepB()

def 신불산_StepB() : ## 예약하기 버튼 순간 정할것
    time.sleep(300)
    # pag.click(1235,117)
    # pag.click(1235,117)
    # button1 = pag.locateCenterOnScreen('./image/11. Sinbul/23. Check.png',  confidence=0.8)   #region = (510,100,1324,333),
    # if (button1 == None) :
    #   time.sleep(10) 
    #   신불산_StepB()  
    # else :
    #   refresh_token()
    #   tm = time.localtime()
    #   kakao_tm = tm.tm_hour,tm.tm_min,tm.tm_sec
    #   text = str(kakao_tm)
    #   print(text)
    #   kakao_message_you(text)
    #   time.sleep(120)
      #다음 액션  

#★★★★★★★★★★★★★★★★★★★ 스케쥴러
  
def 신불산_자동():
    time.sleep(5)
    #페이지 클릭
    pag.click(1800,800)
    time.sleep(5)
    #접속
    pag.click(466,84)
    time.sleep(5)
    pag.click(496,185)
    time.sleep(5)
    신불산_Reset()
    #로그아웃
    pag.click(1246,118)
    time.sleep(5)
    pag.click('enter')
    time.sleep(5)
    pag.hotkey('enter')
    #접속
    pag.click(466,84)
    time.sleep(5)
    pag.click(496,185)
    time.sleep(5)
    신불산_자동입력()
    신불산_Start()