from tkinter import *
from kakao_01_api import *
from Camp_12_울주_줍줍 import *
import pyautogui as pag
import win32con
import win32api
import win32gui
import keyboard
import requests
import clipboard
import schedule
import pyperclip
import time
import json
import random
import cv2

#울주해양예약 시스템 2022.01.11 #Vier Size 67%

#변수 설정
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

#아이디 입력
#▶▶▶▶▶▶▶▶▶
global 울주_id
울주_id = "lovepend@nate.com"
global 울주_pw
울주_pw = "*Zoavld4fkd" 

def 울주_log_id1():
  global 울주_id
  울주_id = "lovepend@nate.com"
  print(울주_id)

def 울주_log_id2():
  global 울주_id
  울주_id = "lovepend@kakao.com"
  print(울주_id)
    
def 울주_log_id3():
  global 울주_id
  울주_id = "lovepend@naver.com"
  print(울주_id)

def 울주_log_id4():
  global 울주_id
  울주_id = "parkmc7@naver.com"
  print(울주_id)

def 울주_log_guest():
  global 울주_id
  울주_id = "jhrep2234@nate.com"
  time.sleep(1)
  global 울주_pw
  울주_pw = "*qwer1234"
  print(울주_id)
  print(울주_pw)

#범위 입력
#▶▶▶▶▶▶▶▶▶

def 울주_범위선택():
  while True:
    if keyboard.is_pressed("F2"): 
      global find_range1 
      find_range1  = pag.position()
      print(find_range1)
      time.sleep(0.5)
      break  
  while True:
    if keyboard.is_pressed("F2"): 
      global find_range2 
      find_range2  = pag.position()
      print(find_range2)
      time.sleep(0.5)
      break  
  global find_range
  find_range = (find_range1.x,find_range1.y,find_range2.x,find_range2.y)

def 울주_금요일():
  global find_range
  global reservation
  reservation = './image/11. Ulju/01_0. reservation2.png'
  #find_range = 1164,102,1263,1080 #토요일만 검색 
  find_range = (618,114,96,914) #토요일만 검색 
  print(find_range)

def 울주_토요일():
  global find_range
  global reservation
  reservation = './image/11. Ulju/01_0. reservation1.png'
  #find_range = 1164,102,1263,1080 #토요일만 검색 
  find_range = (715,113,97,913) #토요일만 검색 
  print(find_range)

#함수 설정
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

#메인함수(검색_토요일)
#▶▶▶▶▶▶▶▶▶
def 울주_검색_메인():
  try :
    print("울주_검색_메인")
    button = pag.locateCenterOnScreen(reservation, region = find_range, confidence=0.95)
    if (button == None) :
      None        
    else :
      global Friday
      global Saturday
      Saturday = button.x, button.y
      Friday = (button.x)-150, (button.y)-8, (button.x)-100, (button.y+8)
      #button_1 = pag.locateCenterOnScreen('./image/11. Ulju/01_0. reservation1.png', region = Friday,confidence=0.9) #토요일 찾을 범위 설정      
      울주_검색_2박()
  except :
    None

#메인함수(검색_금요일)
#▶▶▶▶▶▶▶▶▶
def 울주_검색_2박():
  try :
    print("울주_검색_2박")
    button = pag.locateCenterOnScreen(reservation, region = Friday,confidence=0.9) #토요일 찾을 범위 설정   
    if (button == None) :
      None
      pag.click(Saturday)
    else:
      pag.click(button)        
      print("검색")
      울주_예약알림()
  except :
    None

#메인함수(카톡알람)
#▶▶▶▶▶▶▶▶▶
def 울주_예약알림():
  try :
    print("울주_예약알림")   
    button = pag.locateCenterOnScreen('./image/12. Ulju/12. jubjub.png', confidence=0.9)
    if (button == None) :
      울주_예약알림()   
    else :
      time.sleep(0.2)
      #URL 클릭
      pag.click(316,60)
      #URL 복사
      pag.hotkey('ctrl','c')
      pag.hotkey('ctrl','c')
      예약날짜 = pyperclip.paste() 
      # date_1 = 예약날짜[70:78]
      # date_2 = 예약날짜[95:98]
      # date_3 = date_1 +" // " + date_2
      date_3 = (예약날짜[70:78] +" // " + 예약날짜[95:98])
      print(date_3)
      refresh_token()
      kakao_message_you(date_3)
      print("검색")
      울주줍줍_Page1_기간()
  except :
    울주_예약알림()

#메인함수(로그인체크_이번달)
#▶▶▶▶▶▶▶▶▶
def 울주_log():
  try :
    print("울주_log")
    loggin = pag.locateCenterOnScreen('./image/11. Ulju/01_10. loggin.png', region = (712,96,82,58), confidence=0.8)
    if (loggin == None):
      None
    else :
      time.sleep(2)
      #코드보내기
      pag.click(loggin.x,loggin.y)
      time.sleep(1)
      #아이디 입력
      pag.click(548,454)
      time.sleep(1)
      pag.hotkey("ctrl","a")
      time.sleep(1)
      pag.hotkey("delete")
      time.sleep(1)
      pag.write(울주_id)
      print(울주_id)
      time.sleep(1)
      #페이지 선택
      pag.doubleClick(10,800)
      time.sleep(1)
      #비밀번호 입력
      pag.click(548,495)
      time.sleep(1)
      pag.hotkey("ctrl","a")
      time.sleep(1)
      pag.hotkey("delete")
      time.sleep(1)
      pag.write(울주_pw)
      print(울주_pw)
      time.sleep(1)
      #로그인 클릭
      pag.hotkey('enter')
      time.sleep(1)  
      #예약하기      
      pag.click(775,172)
      time.sleep(1)    
  except :
    None

#메인함수(로그인체크_다음달)
#▶▶▶▶▶▶▶▶▶
def 울주_log1():
  try :
    print("울주_log1")
    loggin = pag.locateCenterOnScreen('./image/11. Ulju/01_10. loggin.png', region = (712,96,82,58), confidence=0.8)
    if (loggin == None):
      None
    else :
      time.sleep(2)
      #코드보내기
      pag.click(loggin.x,loggin.y)
      time.sleep(1)
      #아이디 입력
      pag.click(548,454)
      time.sleep(1)
      pag.hotkey("ctrl","a")
      time.sleep(1)
      pag.hotkey("delete")
      time.sleep(1)
      pag.write(울주_id)
      print(울주_id)
      time.sleep(1)
      #페이지 선택
      pag.doubleClick(14,129)
      time.sleep(1)
      #비밀번호 입력
      pag.click(548,495)
      time.sleep(1)
      pag.hotkey("ctrl","a")
      time.sleep(1)
      pag.hotkey("delete")
      time.sleep(1)
      pag.write(울주_pw)
      print(울주_pw)
      time.sleep(1)
      #로그인 클릭
      pag.hotkey('enter')
      time.sleep(1)  
      #예약하기      
      pag.click(775,172)
      time.sleep(1)          
      #다음달 선택
      pag.click(535,439)
      time.sleep(2)
  except :
    None

#메인함수(보안문자입력)
#▶▶▶▶▶▶▶▶▶
def 보안문자_카톡입력():
  #셋팅
  pag.click(1800,800)
  time.sleep(0.3)
  pag.hotkey("home")
  time.sleep(1)
  pag.hotkey("f5")
  time.sleep(1)
  print("1")
  button = pag.locateCenterOnScreen('./image/12. Ulju/14. jubjub.png', region=(960,0,1920,1080), confidence=0.9)
  time.sleep(0.5)
  pag.click(button.x,button.y) 
  print("2")
  time.sleep(0.3)
  pag.hotkey("end")
  time.sleep(0.3)
  #페이지 클릭
  pag.click(1800,800)
  time.sleep(0.3)
  pag.hotkey("end")
  time.sleep(1)
  print("3")
  #보안문자 복사 #3000회
  button = pag.locateCenterOnScreen('./image/12. Ulju/15. jubjub.png', region=(960,0,1920,1080), confidence=0.9)
  time.sleep(1)
  pag.rightClick(button.x-80,button.y-15) 
  time.sleep(1)
  pag.click(button.x+20,button.y+80) 
  time.sleep(0.3)
  #카카오 클릭 및 사진 전송
  pag.click(74,1055)
  time.sleep(0.3)
  pag.hotkey('ctrl','v')
  time.sleep(0.3)
  pag.hotkey('enter')
  time.sleep(1)
  #문자 입력 
  while True :
    button = pag.locateCenterOnScreen('./image/11. Ulju/01_11. text.png', region=(0,240,960,1080),  confidence=0.9)
    if button == None :
      None
    else :
      pag.doubleClick(82,294)
      time.sleep(0.3)      
      pag.hotkey('ctrl','c')
      pag.hotkey('ctrl','c')
      카카오_보안문자 = pyperclip.paste()
      울주_보안문자_No = 카카오_보안문자  
      print(울주_보안문자_No)
      울주_보안문자_입력(울주_보안문자_No)
      print(울주_보안문자_No)
      time.sleep(1)
      button = pag.locateCenterOnScreen('./image/12. Ulju/15. jubjub.png', region=(960,0,1920,1080), confidence=0.9)
      time.sleep(1)
      pag.click(button.x,button.y) 
      time.sleep(1)
      pag.hotkey('ctrl','v')
      time.sleep(1)
      pag.hotkey('enter')
      time.sleep(1)
      pag.click(990,60)
      break


#메인함수(보안문자입력)
#▶▶▶▶▶▶▶▶▶            
def 울주_This_A():
  i=0
  while True:
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      break 
    i=i+1
    print(i)
    #페이지 선택
    pag.click(10,800)
    울주_log()
    pag.hotkey('f5')
    #랜덤 새로고침
    num = random.randrange(20,40)
    num1 = num/100
    time.sleep(num1)
    time.sleep(0.2)
    #검색
    울주_검색_메인()
    #페이지 아래로
    pag.hotkey('end')
    time.sleep(0.3)
    #검색
    울주_검색_메인()
    #페이지 위로
    pag.hotkey('home')
    time.sleep(0.3)
    if i == 2000 :
      보안문자_자동입력()
      i=0
    else :
       None
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      break
    울주_검색_메인()

  
#메인함수(검색_30일)
#범위 설정 해줄 것 
#▶▶▶▶▶▶▶▶▶
def 울주_검색_Day1():
  reservation = './image/11. Ulju/01_0. reservation1.png'
  global button_Day1
  try :
    print("울주_검색_메인")
    button_Day1 = pag.locateCenterOnScreen(reservation, region = (5,555,215,1027), confidence=0.95)
    if (button_Day1 == None) :
      None        
    else :
      울주_검색_Day2()
  except :
    None

#메인함수(검색_31)
#▶▶▶▶▶▶▶▶▶
def 울주_검색_Day2():
  reservation = './image/11. Ulju/01_0. reservation1.png'
  global button_Day2
  try :
    print("울주_검색_메인")
    button_Day2 = pag.locateCenterOnScreen(reservation, region = (716,381,815,1028), confidence=0.95)
    if (button_Day2 == None) :
      pag.click(button_Day1)     
      울주_예약알림()     
    else :
      pag.click(button_Day2)  
      울주_예약알림()
  except :
    None

def 울주_검색_Day3():
  reservation = './image/11. Ulju/01_0. reservation1.png'
  global button_Day3
  try :
    print("울주_검색_메인")
    button_Day3 = pag.locateCenterOnScreen(reservation, region = (716,381,815,1028), confidence=0.95)
    if (button_Day3 == None) :
      None
    else :
      pag.click(button_Day3)  
      울주_예약알림()
  except :
    None

#메인함수(보안문자입력)
#▶▶▶▶▶▶▶▶▶            
def 울주_This_B():
  i=0
  while True:
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      break 
    i= i + 1
    print(i)
    #페이지 선택
    pag.click(10,800)
    time.sleep(0.5)    
    pag.hotkey('home')
    time.sleep(0.5)     
    #페이지 선택
    pag.click(10,800)
    울주_log()
    #페이지 아래로
    pag.hotkey('end')
    time.sleep(0.5)
    refresh_f5 = 0
    while True :
      refresh_f5 = refresh_f5 + 1
      pag.hotkey('f5')
      #랜덤 새로고침
      num = random.randrange(30,50)
      num1 = num/100
      time.sleep(num1)
      time.sleep(0.2)
      print("검색1")
      time.sleep(5)
      울주_검색_Day1()
      print("검색2")
      time.sleep(5)
      울주_검색_Day3()
      if refresh_f5 == 5 :
        print("보안문자")
        보안문자_자동입력()
        울주_This_B()
      if keyboard.is_pressed("F2"): # F2 누른게 감지되면
        break

def 울주_This_N():
  i=0
  while True:
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      break 
    i=i+1
    print(i)
    #페이지 선택
    pag.click(10,800)
    울주_log()
    pag.hotkey('f5')
    #랜덤 새로고침
    num = random.randrange(20,40)
    num1 = num/100
    time.sleep(num1)
    time.sleep(0.2)
    #검색
    울주_검색_메인()
    #페이지 아래로
    pag.hotkey('end')
    #검색
    울주_검색_메인()
    #페이지 위로
    pag.hotkey('home')
    time.sleep(0.3)
    if i == 2000 :
      보안문자_자동입력()
      i=0
    else :
       None
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      break
    울주_검색_메인()

def 울주_Next_A():
  print("공백")  
    
def 울주_Next_N():
  print("공백")  
    
def 울주_특정데이():
  print("공백")  

#스케쥴러
#▶▶▶▶▶▶▶▶▶       
def 울주_자동():
  print("공백")  

    
