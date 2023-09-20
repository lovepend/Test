from kakao_01_api import *
from cgi import print_arguments
from cgitb import reset
from ctypes.wintypes import PINT
from gettext import find
from re import I
from tkinter import *
import tkinter
from math import *
from tracemalloc import stop
from turtle import bgcolor, color, width
import pyautogui as pag
import win32con
import win32api
import win32gui
import keyboard
import clipboard
import pyperclip
import requests
import schedule
import json
import time
import datetime
from kakao_01_api import kakao_message_you
import random

#50% 윈도우 화면
def 마우스셋팅():
  while True:
      if keyboard.is_pressed("F2"): # F2 누른게 감지되면
          global t1
          t1 = pag.position() # 위치 뽑아서 저장
          print(t1)
          time.sleep(0.5)
          break     
          #페이지 클릭
  while True:
      if keyboard.is_pressed("F2"): 
          global t2
          t2 = pag.position()
          print(t2)
          time.sleep(0.5)
          break  
          #글쓰기 클릭

  while True:
      if keyboard.is_pressed("F2"): 
          global t3
          t3 = pag.position()
          print(t3)
          time.sleep(0.5)
          break   
          #등록 클릭
  while True:
      if keyboard.is_pressed("F2"): 
          global t4
          t4 = pag.position()
          print(t4)
          time.sleep(0.5)
          break   
          #도배금지

def 꼬리잡기():
  꼬잡문구 = "울모캠은 사계절 내내 선물이 팡팡 🎉🎉사계절 팡팡님 선물 감사합니다🎁🎁"
  num = random.randrange(50,80)
  num1 = num/100
  time.sleep(num1)
  while True:
    if keyboard.is_pressed("F2"):
      print("종료") 
      break 
    #페이지선택
    pag.click(t1)
    time.sleep(num1)
    #맨끝이동
    pag.hotkey('end')
    time.sleep(num1)
    #글쓰기 클릭
    pag.doubleClick(t2)
    pag.doubleClick(t2)
    time.sleep(num1)
    pag.doubleClick(t2)
    pyperclip.copy(꼬잡문구)
    pag.hotkey('ctrl','v')
    time.sleep(num1)
    #등록
    pag.click(t3)
    time.sleep(0.5)
    #도배금지 확인
    pag.doubleClick(1138,231)

#마우스셋팅()
#꼬리잡기()

Saturday = 1164,102,1263,1080 #토요일만 검색 

button = pag.locateCenterOnScreen('./image/11. Ulju/01_0. reservation1.png', region = Saturday, confidence=0.95)
print(button)
if (button == None) :
  
  None        
else :
  None          
  Friday = (button.x)-150, (button.y)-8, (button.x)-100, (button.y+8)
  print(Friday)
  button_1 = pag.locateCenterOnScreen('./image/11. Ulju/01_0. reservation1.png', region = Friday,confidence=0.9) #토요일 찾을 범위 설정      
  print(button_1)
  if (button_1 == None) :
      None
      pag.click(button,button='left')
  else:
      pag.click(button_1,button='left')     
      print("검색")


