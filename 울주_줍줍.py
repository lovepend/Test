from gettext import find
from tkinter import *
from kakao_api import *
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

#울주줍줍해양예약 시스템 2023.04.24 #Vier Size 67%

#★★★★★★★★★★★★★★★★★★★ 차량번호 
global timesetting
timesetting = 0.2
Car_No = "62소9403"


def 차량번호_입력(차량번호):
  global Car_No
  Car_No = 차량번호
 
#pyperclip.copy('62소9403')

#★★★★★★★★★★★★★★★★★★★ 메인 함수

#새로고침
def 울주줍줍_새로고침():
  pag.hotkey('f5')
  button = pag.locateCenterOnScreen('./image/91. Ulju/11. jubjub.png', confidence=0.9)
  if (button == None) :
    울주줍줍_새로고침()   
    print("dd")
  else :
    print("검색")
    울주줍줍_검색()

#새로고침 확인
def 울주줍줍_검색():
  #Saturday = 1164,102,1263,1080 #토요일만 검색 
  button = pag.locateCenterOnScreen('./image/91. Ulju/13. jubjub.png', confidence=0.9)
  if (button == None) :
    울주줍줍_새로고침()   
  else :
    print("검색")
    울주줍줍_Page1_기간()

#기간
def 울주줍줍_Page1_기간():
  button = pag.locateCenterOnScreen('./image/91. Ulju/13. jubjub.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page1_기간()   
  else :
    pag.click(button.x,button.y) 
    pag.hotkey('end')
    print("기간")
    울주줍줍_Page1_총인원()

#총인원
def 울주줍줍_Page1_총인원():
  button = pag.locateCenterOnScreen('./image/91. Ulju/14. jubjub.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page1_총인원()   
  else :
    pag.click(button.x,button.y) 
    pag.hotkey('end')
    #페이지 선택
    pag.doubleClick(1600,800)
    pag.hotkey('end')
    pag.hotkey('end')
    print("기간")
    time.sleep(0.3)
    울주줍줍_Page1_다음()

#총인원
def 울주줍줍_Page1_다음():
  button = pag.locateCenterOnScreen('./image/91. Ulju/15. jubjub.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page1_다음()   
  else :
    pag.click(button.x,button.y) 
    pag.click(button.x,button.y) 
    pag.hotkey('end')
    print("다음")
    time.sleep(timesetting)
    울주줍줍_Page2_도착예정시간()

#총인원
def 울주줍줍_Page2_도착예정시간():
  pag.hotkey('end')
  pag.hotkey('end')
  time.sleep(timesetting)
  button = pag.locateCenterOnScreen('./image/91. Ulju/21. jubjub.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page2_도착예정시간()   
  else :
    pag.click(button.x,button.y) 
    pag.hotkey('end')
    #페이지 선택
    pag.doubleClick(1600,800)
    print("도착시간")
    울주줍줍_Page1_차량방문번호()

#차량방문번호
def 울주줍줍_Page1_차량방문번호():
  button = pag.locateCenterOnScreen('./image/91. Ulju/22. jubjub.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page1_차량방문번호()   
  else :
    pag.click(button.x,button.y) 
    pyperclip.copy(Car_No)
    pag.hotkey('ctrl','v')
    #페이지 선택
    pag.doubleClick(1600,800)
    print("차량")
    울주줍줍_Page2_개인정보()

#개인정보 수집 및 이용안내
def 울주줍줍_Page2_개인정보():
  button = pag.locateCenterOnScreen('./image/91. Ulju/23. jubjub.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page2_개인정보()   
  else :
    pag.click(button.x,button.y) 
    print("개인정보")
    울주줍줍_Page2_예약하기()

#예약하기
def 울주줍줍_Page2_예약하기():
  button = pag.locateCenterOnScreen('./image/91. Ulju/24. jubjub.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page2_예약하기()   
  else :
    pag.click(button.x,button.y) 
    print("예약하기")
    울주줍줍_Page3_약관_전체동의()
 
#신용카드결제
def 울주줍줍_Page3_약관_전체동의():
  time.sleep(timesetting)
  button = pag.locateCenterOnScreen('./image/91. Ulju/31. jubjub.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page3_약관_전체동의()   
  else :
    pag.click(button.x,button.y) 
    print("신용카드")
    울주줍줍_Page3_KB_Pay()

#신용카드선택
def 울주줍줍_Page3_KB_Pay():
  button = pag.locateCenterOnScreen('./image/91. Ulju/32. jubjub.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page3_KB_Pay()   
  else :
    pag.click(button.x,button.y) 
    print("카드선택")
    울주줍줍_Page4_다음()

#다음
def 울주줍줍_Page4_다음():
  button = pag.locateCenterOnScreen('./image/91. Ulju/41. jubjub.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page4_다음()   
  else :
    pag.click(button.x,button.y) 
    print("기간")
    울주줍줍_Page5_앱결제()   

#앱결제
def 울주줍줍_Page5_앱결제():
  button = pag.locateCenterOnScreen('./image/91. Ulju/51. jubjub.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page5_앱결제()   
  else :
    pag.click(button.x,button.y)
    print("앱결제")
    울주줍줍_Page6_결제코드()   
        
#결제코드
def 울주줍줍_Page6_결제코드():
  button = pag.locateCenterOnScreen('./image/91. Ulju/61. jubjub.png', confidence=0.9)
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

#앱결제
def 울주줍줍_Page7_확인():
  time.sleep(timesetting)
  button = pag.locateCenterOnScreen('./image/91. Ulju/71. jubjub.png', confidence=0.9)
  if (button == None) :
    울주줍줍_Page7_확인()   
  else :
    pag.click(button.x,button.y)
    print("확인")
