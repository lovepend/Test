from tkinter import *
from kakao_01_api import *
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
import cv2
import easyocr
import cv2




#육부촌 Test 2023.11.17 #Viewer Size 50% #화면 맨아래로 통일 / 일반
#육부촌 Test 2023.11.17 #Viewer Size 100% #화면 맨아래로 통일 / 줍줍

# 변수 설정
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

#url 입력
#▶▶▶▶▶▶▶▶▶
url = 'https://www.gyeongju.go.kr/hwarang/page.do?mnu_uid=3516&csr_date=2023-11-24&cs_uid=26&csr_numday=1&step=write&initYear=2023&initMonth=11&currentDay='

#날짜입력
#▶▶▶▶▶▶▶▶▶
global 육부촌_day
육부촌_day = 900, 402 # 21일

def 육부촌_Day():
  while True:
    if keyboard.is_pressed("F2"): 
      global 육부촌_day
      육부촌_day  = pag.position()
      print(육부촌_day)
      time.sleep(1)
      break     

def 육부촌_Day1():
  global 육부촌_day
  육부촌_day = 945,379
  print(육부촌_day)

def 육부촌_Day2():
  global 육부촌_day
  육부촌_day= 945,402
  print(육부촌_day)

def 육부촌_Day3():
  global 육부촌_day
  육부촌_day = 945,419
  print(육부촌_day)

def 육부촌_Day4():
  global 육부촌_day
  육부촌_day = 945,439
  print(육부촌_day)

def 육부촌_Day5():
  global 육부촌_day
  육부촌_day = 945,461
  print(육부촌_day)

#범위입력
#▶▶▶▶▶▶▶▶▶
global 육부촌_find_range
육부촌_find_range = 0,0,1800,1000

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

#커서입력
#▶▶▶▶▶▶▶▶▶
global 육부촌_position_up
육부촌_position_up  = 1300,706
global 육부촌_position_down
육부촌_position_down  = 1300,909

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


#함수 설정
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

#자동입력
#▶▶▶▶▶▶▶▶▶
def 육부촌_자동입력():
  time.sleep(2)

#메인함수(시작)
#▶▶▶▶▶▶▶▶▶
def 육부촌_Start():
  while True:
    global 육부촌_day
    global i
    i = i +1
    print(i)
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("F2 종료")
      break
    pag.hotkey('f5')
    #날짜 클릭
    time.sleep(0.2)
    pag.click(육부촌_day)
    육부촌_검색()

  #메인함수(시작)

#▶▶▶▶▶▶▶▶▶
def 육부촌_Start1():
  while True:
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("F2 종료")
      break
    pyperclip.copy('https://www.gyeongju.go.kr/hwarang/page.do?mnu_uid=3516&csr_date=2023-12-09&cs_uid=30&csr_numday=1&step=write&initYear=2023&initMonth=9&currentDay=')
    button = pag.locateCenterOnScreen("./image/51. Kyungju/05._99. reservation.png", region = 육부촌_find_range, confidence=0.85) 
    if (button == None) :
      None  
    else : 
      육부촌_Start2()
      pag.hotkey('enter')     
      time.sleep(0.1)   
      pag.click(815,47) 
      time.sleep(0.1)   
      pag.hotkey('ctrl','v')
      time.sleep(0.1)
      pag.hotkey('enter') 
      time.sleep(0.3)
      육부촌_주소()

#▶▶▶▶▶▶▶▶▶      
def 육부촌_Start2(): 
  while True:
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("F2 종료")
      break
    button = pag.locateCenterOnScreen("./image/51. Kyungju/05._0. reservation.png", region = 육부촌_find_range, confidence=0.85) 
    if (button == None) :
      pag.hotkey('enter')     
      time.sleep(0.1)   
      pag.click(815,47) 
      time.sleep(0.1)   
      pag.hotkey('ctrl','v')
      time.sleep(0.1)
      pag.hotkey('enter') 
      time.sleep(0.3)
      육부촌_Start1()
    else: 
      육부촌_주소()

#▶▶▶▶▶▶▶▶▶
def 육부촌_검색():
  #검색
  button = pag.locateCenterOnScreen("./image/51. Kyungju/05._1. reservation.png", region = 육부촌_find_range)#, confidence=0.85) 
  if (button == None) :
    None      
  else : 
    time.sleep(0.05) 
    pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 
    pag.hotkey('enter')
    육부촌_주소()

#▶▶▶▶▶▶▶▶▶        
def 육부촌_확인() :
  time.sleep(0.2)
  button1 = pag.locateCenterOnScreen('./image/51. Kyungju/05._2. next.png', confidence=0.7)   
  print(button1)
  if (button1 == None) :
    육부촌_확인()      
  else :
    pag.click(button1.x,button1.y, button='left', clicks=5, interval=0.1)
    #refresh_token()
    #kakao_message_you("육부촌")
    육부촌_주소()
    time.sleep(0.3)

#▶▶▶▶▶▶▶▶▶  
def 육부촌_주소():
  #주소검색
  button = pag.locateCenterOnScreen('./image/51. Kyungju/05._4. Adress.png', confidence=0.7)   
  pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 
  pyperclip.copy('반구로55')
  time.sleep(0.3)
  #예)판교역로235
  button = pag.locateCenterOnScreen('./image/51. Kyungju/05._5. Adress.png', confidence=0.7)   
  pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 
  #pag.click(197,135)
  time.sleep(0.2)
  #반구로 55 붙이기
  pag.hotkey('ctrl','v')
  time.sleep(0.2)
  #입력
  pag.hotkey('enter')
  time.sleep(0.2)
  #주소클릭
  button = pag.locateCenterOnScreen('./image/51. Kyungju/05._6. Adress.png', confidence=0.7)   
  pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 
  #pag.click(295,263)   
  time.sleep(0.2)
  #자동입력방지
  pag.click(982,797)
  #예약신청
  time.sleep(500)

#▶▶▶▶▶▶▶▶▶
def 육부촌_Karavan():
  while True:
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("중지")
      break
    global i
    i = i + 1
    #날짜 클릭
    pag.click(육부촌_day)
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
                    
#▶▶▶▶▶▶▶▶▶
def 육부촌_자동():
  time.sleep(5)


#메인함수(시작_줍줍)
#▶▶▶▶▶▶▶▶▶
def 육부촌_줍줍():
  while True:
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("F2 종료")
      break
    try : 
      print("육부촌_줍줍")
      pyperclip.copy(url)
      button = pag.locateCenterOnScreen("./image/51. Kyungju/05._99. reservation.png", region = 육부촌_find_range, confidence=0.85) 
      if (button == None) :
        None  
      else : 
        육부촌_줍줍_refresh()
    except :
      None

#메인함수(검색)
#▶▶▶▶▶▶▶▶▶  
def 육부촌_줍줍_refresh(): 
  while True:
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("F2 종료")
      break
    try : 
      print("육부촌_줍줍_refresh")
      button = pag.locateCenterOnScreen("./image/51. Kyungju/05._91. reservation.png", region = 육부촌_find_range, confidence=0.85) 
      if (button == None) :
        pag.hotkey('enter')     
        time.sleep(0.1)   
        pag.click(815,47) 
        time.sleep(0.1)   
        pag.hotkey('ctrl','v')
        time.sleep(0.1)
        pag.hotkey('enter') 
        time.sleep(0.1)
        pag.hotkey('enter') 
        time.sleep(0.3)
        육부촌_줍줍()
      else: 
        육부촌_주소_AI()
    except :
        pag.hotkey('enter')     
        time.sleep(0.1)   
        pag.click(815,47) 
        time.sleep(0.1)   
        pag.hotkey('ctrl','v')
        time.sleep(0.1)
        pag.hotkey('enter') 
        time.sleep(0.1)
        pag.hotkey('enter') 
        time.sleep(0.3)
        육부촌_줍줍() 

#메인함수(검색)
#▶▶▶▶▶▶▶▶▶  
def 육부촌_주소_AI(): 
  while True:
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("F2 종료")
      break
    try :   
      print("육부촌_주소_AI")
      print("주소검색")
      time.sleep(0.1)
      pag.click(150,551)
      time.sleep(0.1)
      pag.hotkey('end')
      time.sleep(0.5)
      #주소검색
      print("주소입력")
      button = pag.locateCenterOnScreen('./image/51. Kyungju/05._92. reservation.png', confidence=0.7)   
      pag.click(button.x,button.y-90, button='left', clicks=1, interval=0.1) 
      pyperclip.copy('반구로55')
      time.sleep(0.3)
      #예)판교역로235
      print("반구로55 입력")
      button = pag.locateCenterOnScreen('./image/51. Kyungju/05._5. Adress.png', confidence=0.7)   
      pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 
      #pag.click(197,135)
      time.sleep(0.2)
      #반구로 55 붙이기
      pag.hotkey('ctrl','v')
      time.sleep(0.2)
      #입력
      pag.hotkey('enter')
      time.sleep(0.2)
      #주소클릭
      print("주소선택")
      button = pag.locateCenterOnScreen('./image/51. Kyungju/05._6. Adress.png', confidence=0.7)   
      pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 
      time.sleep(0.2)
      #자동입력방지
      print("자동방지입력")
      button = pag.locateCenterOnScreen('./image/51. Kyungju/05._93. reservation.png', confidence=0.8)   
      pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 
      im1 =  pag.screenshot('captcha.png', region=(727,281,200,70))
      #file = r"C:\Users\LinkTech\Documents\Visual Studio Code\Test\captcha.png"
      file = r"captcha.png"
      reader = easyocr.Reader(['en'], gpu=True)
      #reader = easyocr.Reader(['ko', 'en'], gpu=True, model_storage_directory= 'korean_g2.pth')
      img = cv2.imread(file)
      #img = cv2.imread(im1)
      text = reader.readtext(img, detail=0)
      input_text = str(text)
      input_text1 = input_text.strip('[')
      input_text2 = input_text1.strip(']')
      input_text3 = input_text2.strip("'")                      
      print(text)
      pyperclip.copy(input_text3)
      pag.hotkey('ctrl','v')
      time.sleep(0.1)
      pag.hotkey('enter')
      time.sleep(500)
    except :
      None



