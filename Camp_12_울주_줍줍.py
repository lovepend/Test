from gettext import find
from tkinter import *
from kakao_01_api import *
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

#울주줍줍해양예약 시스템 2023.04.24 #Vier Size 67%

# 변수 설정
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

#차량번호 입력
#▶▶▶▶▶▶▶▶▶
global timesetting
timesetting = 0.3
울주_Car_No = "62소9403"

def 울주_차량번호_입력(차량번호):
  global 울주_Car_No
  울주_Car_No = 차량번호

#보안문자 입력
#▶▶▶▶▶▶▶▶▶
import random
t= random.choice(range(11111,99999))
울주_보안문자_No = t

def 울주_보안문자_입력(보안문자):
  global 울주_보안문자_No
  울주_보안문자_No = 보안문자

def 보안문자_자동입력():
  while True :
    try :
      print("보안문자_자동입력")
      button = pag.locateCenterOnScreen('./image/12. Ulju/15. jubjub.png', region=(960,0,1920,1080), confidence=0.9)
      if button == None :
        None
      else :
        time.sleep(1)
        pag.click(button.x,button.y) 
        time.sleep(1)
        pag.write(울주_보안문자_No)
        time.sleep(1)
        pag.hotkey('enter')
        time.sleep(1)
        pag.click(990,60)
        break
    except :
      None

#결제방법 입력
#▶▶▶▶▶▶▶▶▶
def 울주_앱결제():
  global Card
  Card = 1
  print("앱결제")

def 울주_간편결제():
  global Card
  Card = 0
  print("간편결제")

def 울주_NH_간편결제():
  global Card
  Card = 2
  print("NH간편결제")
  print(Card)
  
#함수 설정
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

#메인함수(시작_새로고침)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_새로고침():
  pag.hotkey('f5')
  울주줍줍_시작()

#메인함수(시작_새로고침)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_시작():
  while True:
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      break
    try :
      print("울주줍줍_시작")
      button = pag.locateCenterOnScreen('./image/12. Ulju/11. jubjub.png', region=(0,0,960,1080), confidence=0.9)
      if (button == None) :
        None
      else :
        print("검색")
        울주줍줍_검색()
    except :
      None

#메인함수(시작_오픈확인)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_검색():
  try :
    print("울주줍줍_검색")
    button = pag.locateCenterOnScreen('./image/12. Ulju/13. jubjub.png', region=(0,0,960,1080), confidence=0.9)
    if (button == None) :
      울주줍줍_새로고침()   
    else :
      print("검색")
      #아래는 일반
      울주줍줍_Page1_기간()
      #아래는 할인 30
      #울주줍줍_Page1_기간1()
  except :
    울주줍줍_새로고침()

#메인함수(할인)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page1_기간1():
  try :
    print("울주줍줍_Page1_기간_할인추가")
    button = pag.locateCenterOnScreen('./image/12. Ulju/99. jubjub.png', region=(1,1,960,1080), confidence=0.9)
    if (button == None) :
      울주줍줍_Page1_기간1()   
    else :
      pag.click(button.x,button.y)
      pag.click(button.x,button.y)
      print("할인추가")
      울주줍줍_Page1_기간()
  except :
    울주줍줍_Page1_기간1()

#메인함수(기간)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page1_기간():
  try :
    print("울주줍줍_Page1_기간")
    button = pag.locateCenterOnScreen('./image/12. Ulju/13. jubjub.png', region=(1,1,960,1080), confidence=0.9)
    if (button == None) :
      울주줍줍_Page1_기간()   
    else :
      pag.click(button.x,button.y)
      pag.hotkey('down')
      #pag.hotkey('end')
      print("기간")
      울주줍줍_Page1_총인원()
  except :
    울주줍줍_Page1_기간()

#메인함수(기간)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page1_기간_할인추가():
  try :
    print("울주줍줍_Page1_기간")
    button = pag.locateCenterOnScreen('./image/12. Ulju/13. jubjub.png', region=(1,1,960,1080), confidence=0.9)
    if (button == None) :
      울주줍줍_Page1_기간()   
    else :
      pag.click(button.x,button.y)
      pag.hotkey('down')
      #pag.hotkey('end')
      print("기간")
      울주줍줍_Page1_총인원()
  except :
    울주줍줍_Page1_기간_할인추가()

#메인함수(총인원)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page1_총인원():
  try :
    print("울주줍줍_Page1_총인원")
    button = pag.locateCenterOnScreen('./image/12. Ulju/14. jubjub.png', region=(0,0,960,1080), confidence=0.9)
    if (button == None) :
      울주줍줍_Page1_총인원()   
    else :
      pag.click(button.x,button.y) 
      pag.hotkey('end')
      #페이지 선택
      pag.click(10,800)
      pag.hotkey('end')
      pag.hotkey('end')
      print("기간")
      time.sleep(0.5)
      울주줍줍_Page1_다음()
  except :
    울주줍줍_Page1_총인원()

#메인함수(보안문자)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page1_다음():
  try :
    print("울주줍줍_Page1_다음")
    button = pag.locateCenterOnScreen('./image/12. Ulju/15. jubjub.png', region=(0,0,960,1080), confidence=0.9)
    if (button == None) :
      울주줍줍_Page1_다음()   
    else :
      pag.click(button.x,button.y) 
      pyperclip.copy(울주_보안문자_No)
      print(울주_보안문자_No)
      pag.hotkey('ctrl','v')
      time.sleep(0.1)
      pag.hotkey('enter')
      time.sleep(0.3)
      울주줍줍_Page2_도착예정시간()
  except :
    울주줍줍_Page1_다음()


#메인함수(도착시간)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page2_도착예정시간():
  try :
    print("울주줍줍_Page2_도착예정시간")
    #페이지 선택
    pag.hotkey('end')
    pag.hotkey('end')
    time.sleep(timesetting)
    button = pag.locateCenterOnScreen('./image/12. Ulju/21. jubjub.png', region=(0,0,960,1080), confidence=0.9)
    if (button == None) :
      울주줍줍_Page2_도착예정시간()   
    else :
      pag.click(button.x,button.y) 
      pag.hotkey('end')
      #페이지 선택
      pag.click(10,800)
      print("도착시간")
      울주줍줍_Page2_차량방문번호()
  except :
    울주줍줍_Page2_도착예정시간()

#메인함수(차량방문)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page2_차량방문번호():
  try :
    print("울주줍줍_Page1_차량방문번호")    
    button = pag.locateCenterOnScreen('./image/12. Ulju/22. jubjub.png', region=(0,0,960,1080), confidence=0.9)
    if (button == None) :
      울주줍줍_Page2_차량방문번호()   
    else :
      pag.click(button.x,button.y) 
      pyperclip.copy(울주_Car_No)
      pag.hotkey('ctrl','v')
      #페이지 선택
      pag.click(10,800)
      print("차량")
    울주줍줍_Page2_개인정보()
  except :
    울주줍줍_Page2_차량방문번호()

#메인함수(개인정보 수집 및 이용안내)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page2_개인정보():
  try :
    print("울주줍줍_Page2_개인정보")  
    button = pag.locateCenterOnScreen('./image/12. Ulju/23. jubjub.png', region=(0,0,960,1080), confidence=0.9)
    if (button == None) :
      울주줍줍_Page2_개인정보()   
    else :
      pag.click(button.x,button.y) 
      print("개인정보")
      울주줍줍_Page2_예약하기()
  except :
    울주줍줍_Page2_개인정보()

#메인함수(예약하기 클릭)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page2_예약하기():
  try :
    print("울주줍줍_Page2_예약하기") 
    button = pag.locateCenterOnScreen('./image/12. Ulju/24. jubjub.png', region=(0,0,960,1080), confidence=0.9)
    if (button == None) :
      울주줍줍_Page2_예약하기()   
    else :
      pag.click(button.x,button.y) 
      print("예약하기")
      울주줍줍_Page3_약관_전체동의()
  except :
    울주줍줍_Page2_예약하기()

#메인함수(약관전체동의)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page3_약관_전체동의():
  try :
    print("울주줍줍_Page3_약관_전체동의") 
    time.sleep(0.5)
    button = pag.locateCenterOnScreen('./image/12. Ulju/31. jubjub.png', confidence=0.9)
    if (button == None) :
      울주줍줍_Page3_약관_전체동의()   
    else :
      pag.click(button.x,button.y) 
      print("신용카드")
      울주줍줍_Page3_KB_Pay()
  except :
    울주줍줍_Page3_약관_전체동의()

#메인함수(신용카드선택)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page3_KB_Pay():
  try :
    print("울주줍줍_Page3_KB_Pay") 
    button = pag.locateCenterOnScreen('./image/12. Ulju/32. jubjub.png', confidence=0.9)
    if (button == None) :
      울주줍줍_Page3_KB_Pay()   
    else :
      global Card 
      print(Card)
      if (Card == 2) :
        button1 = pag.locateCenterOnScreen('./image/12. Ulju/32. jubjub_NH.png', confidence=0.9)
        pag.click(button1.x,button1.y) 
        print(Card)
        print("농협선택")
        울주줍줍_Page4_NH_Next() 
      else :
        pag.click(button.x,button.y) 
        print(Card)
        print("카드선택")
        울주줍줍_Page4_다음() 
  except :
    울주줍줍_Page3_KB_Pay()
  
#메인함수(신용카드선택)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page4_다음():
  try :
    print("울주줍줍_Page4_다음") 
    button = pag.locateCenterOnScreen('./image/12. Ulju/41. jubjub.png', confidence=0.9)
    if (button == None) :
      울주줍줍_Page4_다음()   
    else :
      pag.click(button.x,button.y) 
      print("기간")
      global Card
      if (Card == 1) :
        울주줍줍_Page5_앱결제() 
      if (Card == 0) :
        울주줍줍_Page5_간편결제()  
  except :
    울주줍줍_Page4_다음()  

####################################국민카드 앱결제######################################
#메인함수(앱결제)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page5_앱결제():
  try :
    print("울주줍줍_Page5_앱결제")   
    button = pag.locateCenterOnScreen('./image/12. Ulju/51. jubjub.png', confidence=0.9)
    if (button == None) :
      울주줍줍_Page5_앱결제()   
    else :
      pag.click(button.x,button.y)
      print("앱결제")
      울주줍줍_Page6_결제코드()   
  except :
    울주줍줍_Page5_앱결제() 

#메인함수(앱결제_결제코드)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page6_결제코드():
  try :
    print("울주줍줍_Page6_결제코드") 
    button = pag.locateCenterOnScreen('./image/12. Ulju/61. jubjub.png', confidence=0.9)
    if (button == None) :
      울주줍줍_Page6_결제코드()   
    else :
      #코드보내기
      time.sleep(0.1)
      pag.click(1034,603)
      time.sleep(0.1)
      pag.dragTo(1171,660, 0.2, button='left')
      time.sleep(0.1)
      pag.hotkey('ctrl', 'c')
      결제코드 = pyperclip.paste() 
      print("결제코드")
      kakao_message_you(결제코드)
      울주줍줍_Page7_확인()
  except :
    울주줍줍_Page6_결제코드()  

#메인함수(앱결제_결제결제완료)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page7_확인():
  try :
    print("울주줍줍_Page7_확인") 
    time.sleep(timesetting)
    button = pag.locateCenterOnScreen('./image/12. Ulju/71. jubjub.png', confidence=0.9)
    if (button == None) :
      울주줍줍_Page7_확인() 
    else :
      pag.click(button.x,button.y)
      print("확인")
      울주줍줍_Page8_확인()
  except :
    울주줍줍_Page7_확인()  

#메인함수(앱결제_결제결제완료)
#▶▶▶▶▶▶▶▶▶
def 울주줍줍_Page8_확인():
  try :
    print("울주줍줍_Page8_확인") 
    time.sleep(timesetting)
    button = pag.locateCenterOnScreen('./image/12. Ulju/72. jubjub.png', confidence=0.9)
    if (button == None) :
      울주줍줍_Page8_확인() 
    else :
      pag.click(button.x,button.y)
      print("확인")
      time.sleep(10000)
  except :
    울주줍줍_Page8_확인()

####################################국민카드 간편결제######################################
def 울주줍줍_Page5_간편결제():
  button = pag.locateCenterOnScreen('./image/12. Ulju/51. jubjub_Pass.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page5_간편결제()   
  else :
    pag.click(button.x,button.y)
    print("간편결제")
    울주줍줍_Page6_인증서결제()   

def 울주줍줍_Page6_인증서결제():
  button = pag.locateCenterOnScreen('./image/12. Ulju/61. jubjub_Pass.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page6_인증서결제()   
  else :
    pag.click(button.x,button.y)
    print("간편결제")
    울주줍줍_Page7_결제비밀번호()   

def 울주줍줍_Page7_결제비밀번호():
  button = pag.locateCenterOnScreen('./image/12. Ulju/71. jubjub_Pass.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page7_결제비밀번호()   
  else :
    pag.click(button.x,button.y)
    print("결제비밀번호")
    pyperclip.copy("170416")
    pag.hotkey('ctrl','v')
    울주줍줍_Page7_결제진행()   

def 울주줍줍_Page7_결제진행():
  button = pag.locateCenterOnScreen('./image/12. Ulju/71. jubjub_Next.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page7_결제진행()   
  else :
    pag.click(button.x,button.y)
    print("결제진행")
    pyperclip.copy("170416")
    pag.hotkey('ctrl','v')
    울주줍줍_Page8_확인()  

#앱결제
def 울주줍줍_Page8_확인():
  time.sleep(timesetting)
  button = pag.locateCenterOnScreen('./image/12. Ulju/71. jubjub.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page8_확인()   
  else :
    pag.click(button.x,button.y)
    print("확인")
    time.sleep(10000)

####################################농협 간편결제######################################
#다음
def 울주줍줍_Page4_NH_Next():
  time.sleep(0.1)
  print("1")
  button = pag.locateCenterOnScreen('./image/12. Ulju/41. jubjub_NH.png', confidence=0.7)
  if (button == None) :
    울주줍줍_Page4_NH_Next()   
  else :
    pag.click(button.x,button.y) 
    print("기간")
    울주줍줍_Page5_NH_다른결제()

def 울주줍줍_Page5_NH_다른결제():
  button = pag.locateCenterOnScreen('./image/12. Ulju/51. jubjub_NH_Pass.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page5_NH_다른결제()   
  else :
    pag.click(button.x,button.y)
    print("다른결제")
    울주줍줍_Page6_NH_원클릭간편결제()   

def 울주줍줍_Page6_NH_원클릭간편결제():
  button = pag.locateCenterOnScreen('./image/12. Ulju/52. jubjub_NH_Pass.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page6_NH_원클릭간편결제()   
  else :
    pag.click(button.x,button.y)
    print("간편결제")
    울주줍줍_Page7_NH_입력()   

def 울주줍줍_Page7_NH_입력():
  button = pag.locateCenterOnScreen('./image/12. Ulju/71. jubjub_NH_Pass.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page7_NH_입력()   
  else :
    pag.click(button.x,button.y)
    print("결제입력")
    pyperclip.copy("lovepend83")
    pag.hotkey('ctrl','v')
    울주줍줍_Page7_NH_입력1()   

def 울주줍줍_Page7_NH_입력1():
  button = pag.locateCenterOnScreen('./image/12. Ulju/72. jubjub_NH_Pass.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page7_NH_입력1()   
  else :
    pag.click(button.x,button.y)
    print("결제입력1")
    pyperclip.copy("*1111o")
    pag.write("*111dgo")
   # 울주줍줍_Page7_NH_확인()

def 울주줍줍_Page7_NH_확인():
  button = pag.locateCenterOnScreen('./image/12. Ulju/72. jubjub_NH_Pass.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page7_NH_확인()   
  else :
    pag.click(button.x,button.y)
    print("확인")
    time.sleep(10000)

#앱결제
def 울주줍줍_Page8_NH_확인():
  time.sleep(timesetting)
  button = pag.locateCenterOnScreen('./image/12. Ulju/73. jubjub_NH_Pass.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page8_NH_확인()   
  else :
    pag.click(button.x,button.y)
    print("확인")
    time.sleep(10000)
