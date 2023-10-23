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
#대왕암_find_range = 921,657,1387,1025
대왕암_find_range = 0,0,1920,1080

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
    대왕암_id = "jhrep1201"
    global 대왕암_pw
    대왕암_pw = "j1902217**"
    print(대왕암_id)
    print(대왕암_pw)

global 대왕암_i 
대왕암_i = 0       

#★★★★★★★★★★★★★★★★★★★ 날짜 입력
def 대왕암_Day1():
  global 대왕암_day1
  대왕암_day1 =  433,766
  print(대왕암_day1)
  global 대왕암_day2
  대왕암_day2 = 1390,766
  print(대왕암_day2)

def 대왕암_Day2():
  global 대왕암_day1
  대왕암_day1 =  433,814
  print(대왕암_day1)
  global 대왕암_day2
  대왕암_day2 = 1390,814
  print(대왕암_day2)

def 대왕암_Day3():
  global 대왕암_day1
  대왕암_day1 =  433,855
  print(대왕암_day1)
  global 대왕암_day2
  대왕암_day2 = 1390,855
  print(대왕암_day2)

def 대왕암_Day4():
  global 대왕암_day1
  대왕암_day1 =  433,905
  print(대왕암_day1)
  global 대왕암_day2
  대왕암_day2 = 1390,905
  print(대왕암_day2)


#★★★★★★★★★★★★★★★★★★★ 날짜 입력
def 대왕암_Day():
  while True:
    if keyboard.is_pressed("F2"): 
      global 대왕암_day1 
      대왕암_day1  = pag.position()
      print(대왕암_day1)
      time.sleep(0.5)
      break         
  while True:
    if keyboard.is_pressed("F2"): 
      global 대왕암_day2
      대왕암_day2  = pag.position()
      print(대왕암_day2)
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
  time.sleep(1)
  #url 클릭
  pag.click(300,60)
  time.sleep(0.2)
  #로그인페이지 이동 
  pyperclip.copy('https://daewangam.donggu.ulsan.kr/login.do?prePage=/camping/main.do')
  time.sleep(0.2)
  pyperclip.copy('https://daewangam.donggu.ulsan.kr/login.do?prePage=/camping/main.do')
  time.sleep(0.2)
  pag.hotkey('ctrl','v')
  time.sleep(0.2)
  pag.hotkey('enter')
  time.sleep(5)
  #통합회원 로그인
  pag.click(367,612)
  time.sleep(5)
  #ID입력
  pag.click(493,270)
  time.sleep(1)
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pag.write(대왕암_id)
  print(대왕암_id) 
  pag.click(900,272)
  time.sleep(1)
  #PW입력
  pag.click(493,320)
  time.sleep(1)
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pag.write(대왕암_pw)
  print(대왕암_pw) 
  time.sleep(2)
  #로그인 선택
  pag.click(487,373)
  time.sleep(5)

  #url 클릭
  pag.click(300,60)
  time.sleep(0.2)
  #로그인페이지 이동 
  pyperclip.copy('https://daewangam.donggu.ulsan.kr/camping/Pmreservation.do')
  time.sleep(0.2)
  pyperclip.copy('https://daewangam.donggu.ulsan.kr/camping/Pmreservation.do')
  time.sleep(0.2)
  pag.hotkey('ctrl','v')
  time.sleep(0.2)
  pag.hotkey('enter')
  time.sleep(5)
  #날짜 클릭
  pag.click(대왕암_day1)

##################두번째####################
  #url 클릭
  pag.click(1300,60)
  time.sleep(0.2)
  #예약페이지 이동 
  pyperclip.copy('https://daewangam.donggu.ulsan.kr/camping/Pmreservation.do')
  time.sleep(0.2)
  pyperclip.copy('https://daewangam.donggu.ulsan.kr/camping/Pmreservation.do')
  time.sleep(0.2)
  pag.hotkey('ctrl','v')
  time.sleep(0.2)
  pag.hotkey('enter')
  time.sleep(5)
  #날짜 클릭
  pag.click(대왕암_day2)

################################################검색#############################################

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
        print("a")
        pag.click(button1.x,button1.y, button='left', clicks=1, interval=0.1)
        button1 = pag.locateCenterOnScreen('./image/41. Donggu/02._2. next.png', confidence=0.7)   
        time.sleep(0.05)
        print("b")
        pag.click(button1.x,button1.y, button='left', clicks=1, interval=0.1)
        # button1 = pag.locateCenterOnScreen('./image/41. Donggu/02._2. next.png', confidence=0.7)   
        # time.sleep(0.05)
        # print("c")
        # pag.click(button1.x,button1.y, button='left', clicks=5, interval=0.1)
        # button1 = pag.locateCenterOnScreen('./image/41. Donggu/02._2. next.png', confidence=0.7)  
        # time.sleep(0.05)
        # print("d") 
        # pag.click(button1.x,button1.y, button='left', clicks=5, interval=0.1)
        # button1 = pag.locateCenterOnScreen('./image/41. Donggu/02._2. next.png', confidence=0.7)   
        # time.sleep(0.05)
        # print("e")
        # pag.click(button1.x,button1.y, button='left', clicks=5, interval=0.1)
        # button1 = pag.locateCenterOnScreen('./image/41. Donggu/02._2. next.png', confidence=0.7)   
        # time.sleep(0.05)
        # print("f")
        # pag.click(button1.x,button1.y, button='left', clicks=5, interval=0.1)
        refresh_token()
        kakao_message_you("대왕암")
        time.sleep(300)
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
 
    
#★★★★★★★★★★★★★★★★★★★ 메인 함수 
def 대왕암_Start():
  global i
  i = 0 
  while True:
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("중지")
      break
    #날짜 클릭
    pag.click(대왕암_day1)
    time.sleep(0.5)
    #검색
    대왕암_검색()
    pag.click(대왕암_day2)
    time.sleep(0.5)
    #검색
    대왕암_검색()
    if i == 200 :
      #첫번째 리셋
      time.sleep(1)
      pag.click(855,803)  
      time.sleep(1)
      pag.hotkey('end')
      #두번째 리셋
      time.sleep(1)
      pag.click(1816,807)  
      time.sleep(1)
      pag.hotkey('end')
      time.sleep(1)
      pag.hotkey('pgup')
      i = 1
    else : 
      i = i + 1
      print(i)
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
        break  



#★★★★★★★★★★★★★★★★★★★ 서브 함수
def 대왕암_Karavan():
  global i
  i = 0 
  while True:
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("중지")
      break
    #날짜 클릭
    pag.click(대왕암_day1)
    time.sleep(0.5)
    #검색
    대왕암_검색()
    pag.click(대왕암_day2)
    time.sleep(0.5)
    #검색
    대왕암_검색()
    if i == 200 :
      #첫번째 리셋
      time.sleep(1)
      pag.click(855,803)  
      time.sleep(1)
      pag.hotkey('home')
      #두번째 리셋
      time.sleep(1)
      pag.click(1816,807)  
      time.sleep(1)
      pag.hotkey('home')
      time.sleep(1)
      pag.hotkey('pgdn')
      i = 1
    else : 
      i = i + 1
      print(i)
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
