from gettext import find
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
pag.FAILSAFE=False
import cv2
cv2.useOptimized()
True

i = 0
#울주해양예약 시스템 2022.01.11 #Vier Size 67%

################################## 아이디
global 울주_id
울주_id = "lovepend@nate.com"
global 울주_pw
울주_pw = "*Zoavld4fkd" 

################################## 아이디
#★★★★★★★★★★★★★★★★★★★ 아이디 입력
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

#★★★★★★★★★★★★★★★★★★★ 범위 입력
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

#★★★★★★★★★★★★★★★★★★★ 메인 함수
def 울주_검색():
  #Saturday = 1164,102,1263,1080 #토요일만 검색 
  global find_range
  print(find_range)
  #button = pag.locateCenterOnScreen('./image/11. Ulju/01_0. reservation1.png', region = find_range, confidence=0.95)
  button = pag.locateCenterOnScreen(reservation, region = find_range, confidence=0.95)
  if (button == None) :
    None        
  else :
    Friday = (button.x)-150, (button.y)-8, (button.x)-100, (button.y+8)
    #button_1 = pag.locateCenterOnScreen('./image/11. Ulju/01_0. reservation1.png', region = Friday,confidence=0.9) #토요일 찾을 범위 설정      
    button_1 = pag.locateCenterOnScreen(reservation, region = Friday,confidence=0.9) #토요일 찾을 범위 설정   
    if (button_1 == None) :
      None
      pag.click(button,button='left')
    else:
      pag.click(button_1,button='left')     
      print("검색")
      울주_검색1()

#새로고침 확인
def 울주_검색1():
  #Saturday = 1164,102,1263,1080 #토요일만 검색 
  button = pag.locateCenterOnScreen('./image/12. Ulju/12. jubjub.png', confidence=0.9)
  if (button == None) :
    울주_검색1()   
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



#★★★★★★★★★★★★★★★★★★★ 로그
def 울주_log():
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
    print("1")    


def 울주_log1():
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
    print("1")       
    #다음달 선택
    pag.click(535,439)
    time.sleep(2)
    print("2")

#★★★★★★★★★★★★★★★★★★★ 보안 문자

def 보안문자_자동입력():
  #보안문자 복사
  button = pag.locateCenterOnScreen('./image/12. Ulju/15. jubjub.png', region=(960,0,1920,1080), confidence=0.9)
  time.sleep(0.2)
  pag.rightClick(button.x-80,button.y-15) 
  time.sleep(0.2)
  pag.click(button.x+20,button.y+80) 
  time.sleep(0.2)
  #카카오 클릭 및 사진 전송
  pag.click(74,1055)
  time.sleep(0.2)
  pag.hotkey('ctrl','v')
  time.sleep(0.2)
  pag.hotkey('enter')

  #문자 입력 
  while True :
    button = pag.locateCenterOnScreen('./image/11. Ulju/01_11. text.png', confidence=0.9)
    if button == None :
      None
    else :
      pag.doubleClick(82,294)
      time.sleep(0.2)      
      pag.hotkey('ctrl','c')
      카카오_보안문자 = pyperclip.paste()
      울주_보안문자_No = 카카오_보안문자  
      print(울주_보안문자_No)
      울주_보안문자_입력(울주_보안문자_No)

#★★★★★★★★★★★★★★★★★★★ 메인 함수
def 울주_This_A_Back_up():
  while True:
    i = 1
    #페이지 선택
    pag.click(10,800)
    울주_log()
    #페이지 선택
    pag.click(10,800)
    pag.hotkey('f5')
    #울주_검색()
    time.sleep(5)
    pag.hotkey('end')
    ####
    time.sleep(5)
    while True: 
      if keyboard.is_pressed("F2"): # F2 누른게 감지되면
        break
      if i == 1000:
        pag.hotkey('home')
        time.sleep(0.5)
        pag.hotkey('home')
        time.sleep(0.5)
        울주_This_A_Back_up()
      if i < 1000:
        i = i+1
        pag.hotkey('f5')
        time.sleep(1)
        울주_검색()
        print(i)
      num = random.randrange(20,50)
      num1 = num/100
      time.sleep(num1)
      #print(num1)
      if keyboard.is_pressed("F2"): # F2 누른게 감지되면
        break
            
def 울주_This_A():
  while True:
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
    #print(num1)
    time.sleep(0.2)
    울주_검색()
    pag.hotkey('end')
    #*Zoavld4fkdpag.hotkey('pgdn')
    pag.hotkey('f5')
    #랜덤 새로고침
    num = random.randrange(20,40)
    num1 = num/100
    time.sleep(num1)
    #print(num1)
    울주_검색()
    pag.hotkey('home')
    time.sleep(0.2)
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
        break

def 울주_This_N():
    while True:
        #페이지 선택
        pag.doubleClick(10,800)
        울주_log()        
        #A사이트 * 2
        #pag.click(620,510)
        #time.sleep(0.2)
        #울주_검색()
        #pag.hotkey('pgdn')
        #time.sleep(0.2)
        #울주_검색()    

        #B사이트 * 2
        pag.click(690,510)
        #pag.click(690,120)
        time.sleep(0.5)
        울주_검색()
        pag.hotkey('pgdn')
        time.sleep(0.5)
        울주_검색()
        
        #C사이트
        #pag.click(760,510)
        pag.click(765,120)   
        time.sleep(0.5)
        울주_검색()
        
        #D사이트 * 2
        pag.click(840,510)
        #pag.click(840,120)
        time.sleep(0.5)
        울주_검색()
        pag.hotkey('pgdn')
        time.sleep(0.5)
        울주_검색()
        
        #E사이트  * 2
        #pag.click(920,510)
        pag.click(920,120)
        time.sleep(0.5)
        울주_검색()
        pag.hotkey('pgdn')
        time.sleep(0.5)
        울주_검색()
        
        #F사이트
        #pag.click(990,510)
        pag.click(990,120)
        time.sleep(0.5)#페이지 선택
        pag.doubleClick(1600,800)
        pag.hotkey('home')
        time.sleep(0.5)
        pag.hotkey('home')
        time.sleep(0.5)
        
        울주_검색()
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break

def 울주_Next_A():
    while True:
        #페이지 선택
        pag.doubleClick(10,800)
        울주_log1()
        pag.hotkey('f5')
        time.sleep(0.2)
        울주_검색()
        #랜덤 새로고침
        num = random.randrange(20,40)
        num1 = num/100
        time.sleep(num1)
        print(num1)
        pag.hotkey('pgdn')
        pag.hotkey('f5')
        time.sleep(0.2)
        울주_검색()
        pag.hotkey('home')
        time.sleep(0.2)
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break

def 울주_Next_N():
    while True:
        #페이지 선택
        pag.doubleClick(10,800)
        울주_log1()
        
        #A사이트 * 2
        #pag.click(620,510)
        #time.sleep(0.2)
        #울주_검색()
        #pag.hotkey('pgdn')
        #time.sleep(0.2)
        #울주_검색()    
        
        #B사이트 * 2
        pag.click(690,510)
        #pag.click(690,120)
        #time.sleep(0.5)
        울주_검색()
        pag.hotkey('pgdn')
        time.sleep(0.5)
        울주_검색()
        
        #C사이트
        pag.click(760,510)
        pag.click(765,120)   
        time.sleep(0.5)
        울주_검색()
        
        #D사이트 * 2
        pag.click(840,510)
        #pag.click(840,120)
        time.sleep(0.5)
        울주_검색()
        pag.hotkey('pgdn')
        time.sleep(0.5)
        울주_검색()
        
        #E사이트  * 2
        #pag.click(920,510)
        pag.click(920,120)
        time.sleep(0.5)
        울주_검색()
        pag.hotkey('pgdn')
        time.sleep(0.5)
        울주_검색()
        
        #F사이트
        #pag.click(990,510)
        pag.click(990,120)
        time.sleep(0.5)#페이지 선택
        pag.doubleClick(10,800)
        pag.hotkey('home')
        time.sleep(0.5)
        pag.hotkey('home')
        time.sleep(0.5)
        
        울주_검색()
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break

def 울주_특정데이():
    while True:
        #페이지 선택
        pag.doubleClick(10,800)
        울주_log()
        
        #A사이트 * 2
        #pag.click(620,510)
        #time.sleep(0.2)
        #울주_검색()
        #pag.hotkey('pgdn')
        #time.sleep(0.2)
        #울주_검색()    
        
        #B사이트 * 2
        pag.click(690,510)
        #pag.click(690,120)
        time.sleep(1)
        #울주_검색()
        pag.hotkey('pgdn')
        time.sleep(1)
        global find_range
        find_range = (1162,660,1920,1080)
        울주_검색()
        
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break

        #C사이트
        #pag.click(760,510)
        pag.click(765,120)   
        time.sleep(1)
        pag.hotkey('pgdn')
        time.sleep(1)
        find_range = (1164,763,1920,1080)
        울주_검색()
        
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break

        #D사이트 * 2
        #pag.click(840,510)
        #pag.click(840,120)
        pag.click(846,215)
        #울주_검색()
        time.sleep(1)
        pag.doubleClick(10,800)
        pag.hotkey('pgdn')
        time.sleep(1)
        pag.hotkey('pgdn')
        time.sleep(1)
        find_range = (1162,542,1920,1080)
        울주_검색()
        
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break

        #E사이트  * 2
        #pag.click(920,510)
        pag.click(920,120)
        time.sleep(1)
        #울주_검색()
        pag.hotkey('pgdn')
        time.sleep(1)
        
        find_range = (1164,709,1920,1080)
        울주_검색()

        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break
        #F사이트
        #pag.click(990,510)
        pag.click(990,120)
        time.sleep(1)#페이지 선택
        #울주_검색()
        pag.hotkey('pgdn')
        time.sleep(1)
        find_range = (1164,750,1920,1080)
        울주_검색()
        pag.doubleClick(1600,800)
        pag.hotkey('home')
        time.sleep(1)
        pag.hotkey('home')
        time.sleep(1)
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break

#★★★★★★★★★★★★★★★★★★★ 스케쥴러      
def 울주_자동():
    pag.click(466,84)
    time.sleep(5)
    pag.click(500,115)
    time.sleep(5)
    울주_Next_A()
    