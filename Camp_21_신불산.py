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
import cv2
cv2.useOptimized()
True

#신불산 Test 2022.03.21 #Viewer Size 67%
#56분 36초

def 시간입력_실시간(min,sec):
  global 신불산_min
  global 신불산_sec
  신불산_min = int(min)
  신불산_sec = int(sec)
  print(신불산_min)
  print(신불산_sec)
  신불산_실시간(신불산_min,신불산_sec)

def 시간입력_줍기(min,sec):
  global 신불산_min
  global 신불산_sec
  신불산_min = int(min)
  신불산_sec = int(sec)
  print(신불산_min)
  print(신불산_sec)
  신불산_줍기(신불산_min,신불산_sec)

def 시간입력_줍기1(min,sec):
  global 신불산_min
  global 신불산_sec
  신불산_min = int(min)
  신불산_sec = int(sec)
  print(신불산_min)
  print(신불산_sec)
  신불산_줍기1(신불산_min,신불산_sec)

################################## 리셋 
global 신불산_end_command
신불산_end_command = 0

################################## 범위 
global 신불산_find_range
신불산_find_range = 0,0,1920,1080

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

def 신불산_range1():
  global 신불산_find_range
  신불산_find_range = 0,720,1920,1080
  #신불산_find_range = (0,685,1910,1010)

def 신불산_range2():
  global 신불산_find_range
  신불산_find_range = 0,760,1920,1080
  #신불산_find_range = (0,730,1910,1010)

def 신불산_range3():
  global 신불산_find_range
  신불산_find_range = 0,790,1920,1080
  #신불산_find_range = (0,777,1910,1010)

################################## 아이디
global 신불산_id
신불산_id = "pend"
global 신불산_pw
신불산_pw = "*Zoavld4fkd" 

################################## 날짜
global 신불산_day1
신불산_day1 = 440, 670
global 신불산_day2
신불산_day2 = 1400, 670

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
      global 신불산_day1
      신불산_day1  = pag.position()
      print(신불산_day1)
      time.sleep(0.5)
      break 
  while True:
    if keyboard.is_pressed("F2"):
      global 신불산_day2
      신불산_day2  = pag.position()
      print(신불산_day2)
      time.sleep(0.5)
      break 
#★★★★★★★★★★★★★★★★★★★ 날짜 입력
       
def 신불산_Day11():
  global 신불산_day1
  신불산_day1 = 385, 670
  print(신불산_day1)
  global 신불산_day2
  신불산_day2 = 1340, 670
  print(신불산_day2)

def 신불산_Day12():
  global 신불산_day1
  신불산_day1 = 440, 670
  print(신불산_day1)
  global 신불산_day2
  신불산_day2 = 1400, 670
  print(신불산_day2)

def 신불산_Day21():
  global 신불산_day1
  신불산_day1 = 385, 715
  print(신불산_day1)
  global 신불산_day2
  신불산_day2 = 1340, 715
  print(신불산_day2)

def 신불산_Day22():
  global 신불산_day1
  신불산_day1 = 440, 715
  print(신불산_day1)
  global 신불산_day2
  신불산_day2 = 1400, 715
  print(신불산_day2)

def 신불산_Day31():
  global 신불산_day1
  신불산_day1 = 385, 760
  print(신불산_day1)
  global 신불산_day2
  신불산_day2 = 1340, 760
  print(신불산_day2)

def 신불산_Day32():
  global 신불산_day1
  신불산_day1 = 440, 760
  print(신불산_day1)
  global 신불산_day2
  신불산_day2 = 1400, 760
  print(신불산_day2)

def 신불산_Day41():
  global 신불산_day1
  신불산_day1 = 385, 800
  print(신불산_day1)
  global 신불산_day2
  신불산_day2 = 1340, 800
  print(신불산_day2)

def 신불산_Day42():
  global 신불산_day1
  신불산_day1 = 440, 800
  print(신불산_day1)
  global 신불산_day2
  신불산_day2 = 1400, 800
  print(신불산_day2)

#★★★★★★★★★★★★★★★★★★★ 타임 설정
def 신불산_time_controll_01():
  global time_controll
  time_controll =  0.1
  print(time_controll)

def 신불산_time_controll_02():
  global time_controll
  time_controll =  0.2
  print(time_controll)

#★★★★★★★★★★★★★★★★★★★ 자동 입력
def 신불산_자동입력():  
  시간_동기화()
  #webbrowser.get("windows-default").open('https://camping.ulju.ulsan.kr/')
  time.sleep(1)
  #url 클릭
  pag.click(300,60)
  time.sleep(0.2)
  #로그인페이지 이동 
  pyperclip.copy('https://camping.ulju.ulsan.kr/login.do')
  time.sleep(0.2)
  pyperclip.copy('https://camping.ulju.ulsan.kr/login.do')
  time.sleep(0.2)
  pag.hotkey('ctrl','v')
  time.sleep(0.2)
  pag.hotkey('enter')
  time.sleep(5)
  #로그인 클릭
  pag.click(202,1025)
  time.sleep(5)
  #ID입력
  pag.click(600,272)
  time.sleep(1)
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pyperclip.copy(신불산_id)
  time.sleep(0.2)
  pyperclip.copy(신불산_id)
  time.sleep(1)
  pag.hotkey('ctrl','v')
  #Pw입력
  pag.click(600,321)
  time.sleep(1)
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pyperclip.copy(신불산_pw)
  time.sleep(0.2)
  pyperclip.copy(신불산_pw)
  time.sleep(1)
  pag.hotkey('ctrl','v')
  #로그인
  time.sleep(0.5)
  pag.click(485,371)
  #온라인예약
  time.sleep(5)
  pag.click(410,534)
  #날짜 클릭
  time.sleep(3)
  pag.click(신불산_day1)
  ##################두번째####################
  #url 클릭
  pag.click(1300,60)
  time.sleep(0.2)
  #예약페이지 이동 
  pyperclip.copy('https://camping.ulju.ulsan.kr/Pmreservation.do')
  time.sleep(0.2)
  pyperclip.copy('https://camping.ulju.ulsan.kr/Pmreservation.do')
  time.sleep(0.2)
  pag.hotkey('ctrl','v')
  time.sleep(0.2)
  pag.hotkey('enter')
  time.sleep(5)
  #날짜 클릭
  pag.click(신불산_day2)
  
#★★★★★★★★★★★★★★★★★★★ 메인 함수


def 신불산_실시간(신불산_min,신불산_sec):
  while True:
    global 신불산_day1
    global 신불산_day2
    global time_controll
    print(time_controll)
    #tm = time.localtime()
    if keyboard.is_pressed("F2"):
      print("종료") 
      break  
    #날짜 클릭
    pag.click(신불산_day1)  
    time.sleep(0.1)
    신불산_검색()  
    time.sleep(0.1)
    pag.click(신불산_day2)  
    time.sleep(0.1)
    신불산_검색()     

def 신불산_줍기(신불산_min,신불산_sec):
  while True:
    tm = time.localtime()
    global time_controll    
    if keyboard.is_pressed("F2"):
      print("종료") 
      break  
    if (tm.tm_min == 신불산_min and tm.tm_sec == 신불산_sec) : #9시 56분 및 15시 56분 시작
    #if (tm.tm_hour == 10 and tm.tm_min == 19 and tm.tm_sec == 10) or (tm.tm_hour == 14 and tm.tm_min == 56 and tm.tm_sec == 37) : #TEST
      global 신불산_find_range
      #예약가능 사이트만 보기
      #button = pag.locateCenterOnScreen("./image/21. Sinbul/21_1. reservation.png", region = (860,521,1515,968), confidence=0.7) 
      #print("Check1")
      #print(button)
      #pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
      #print("Check2")
      #예약가능 사이트만 보기
      pag.click(800,686)
      time.sleep(0.2)
      pag.click(1750,686)
      time.sleep(0.2)
      while True:   
        if keyboard.is_pressed("F2"):
          print("종료") 
          break  
        button = pag.locateCenterOnScreen("./image/21. Sinbul/21. reservation.png", region= 신불산_find_range,  confidence=0.7) 
        if (button == None) :
          None
        else : 
          print("else")
          pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
          신불산_StepA()
    #날짜 클릭
    #pag.click(신불산_day1)  
    #time.sleep(time_controll)
    #신불산_검색()   

def 신불산_줍기1(신불산_min,신불산_sec):
  while True:
    tm = time.localtime()
    global time_controll
    global 신불산_find_range
    global 신불산_day1
    global 신불산_day2
    print(time_controll)
    if keyboard.is_pressed("F2"):
      print("종료") 
      break  
    #if (tm.tm_min == 신불산_min and tm.tm_sec == 신불산_sec) : #9시 56분 및 15시 56분 시작
    if (tm.tm_min == 신불산_min and tm.tm_sec == 신불산_sec) : 
      while True:
        pag.click(신불산_day1)  
        time.sleep(0.1)
        신불산_검색()  
        time.sleep(0.1)
        pag.click(신불산_day2)  
        time.sleep(0.1)
        신불산_검색()   
        if keyboard.is_pressed("F2"):
          print("종료") 
          break  
    else : 
      print("else")
      

def 신불산_검색():  
  global 신불산_find_range             
  button = pag.locateCenterOnScreen("./image/21. Sinbul/21. reservation.png", region= 신불산_find_range,  confidence=0.7)      
  if (button == None) :
    None      
  else : 
    pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
    신불산_StepA()

def 신불산_StepA() : ## 예약하기 버튼 순간 정할것
  button1 = pag.locateCenterOnScreen('./image/21. Sinbul/22. next.png',  confidence=0.8)   #region = (510,100,1324,333),
  print(button1)
  if (button1 == None) :
    신불산_StepA()      
  else :  
    time.sleep(0.2)
    print(button1)
    button1 = pag.locateCenterOnScreen('./image/21. Sinbul/22. next.png',  confidence=0.8)
    pag.click(button1.x+10,button1.y, button='left', clicks=1, interval=0.1)        
    # button1 = pag.locateCenterOnScreen('./image/21. Sinbul/22. next.png',  confidence=0.8)   #region = (510,100,1324,333),
    # pag.click(button1.x+10,button1.y, button='left', clicks=1, interval=0.1)
    #pag.click(1264,276)
    tm1 = time.localtime()
    print(tm1.tm_hour,tm1.tm_min,tm1.tm_sec)
    kakao_tm = tm1.tm_hour,tm1.tm_min,tm1.tm_sec
    text = str(kakao_tm)
    print(text)
    refresh_token()
    kakao_message_you(신불산_sec) 
    print("끝")
    time.sleep(600)
        
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
  신불산_실시간()

def 시간_동기화():
  time.sleep(2)
  pag.rightClick(1882,1055)
  time.sleep(3)
  pag.doubleClick(1830,974)
  time.sleep(3)
  pag.click(1573,236)
  time.sleep(5)
  pag.click(1573,236)
  time.sleep(5)
  pag.click(1805,18)  