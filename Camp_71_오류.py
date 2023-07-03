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

#오류 Test 2023.05.15 #Viewer Size 100% #화면 맨아래로 통일


#★★★★★★★★★★★★★★★★★★★ 서브 함수

def 오류_day1():
    while True:
        if keyboard.is_pressed("F2"):
            global 오류_day_1
            오류_day_1  = pag.position()
            print(오류_day_1)
            time.sleep(0.5)
            break 
        
def 오류_day2():
    while True:
        if keyboard.is_pressed("F2"):
            global 오류_day_2
            오류_day_2  = pag.position()
            print(오류_day_2)
            time.sleep(0.5)
            break 

def 오류_범위선택():
    while True:
        if keyboard.is_pressed("F2"): 
            global 오류_find_range1 
            오류_find_range1  = pag.position()
            print(오류_find_range1)
            time.sleep(0.5)
            break  
    while True:
        if keyboard.is_pressed("F2"): 
            global 오류_find_range2 
            오류_find_range2  = pag.position()
            print(오류_find_range2)
            time.sleep(0.5)
            break  
    global 오류_find_range
    오류_find_range = (오류_find_range1.x,오류_find_range1.y,오류_find_range2.x,오류_find_range2.y)


def 오류_시작():
  while True:
   if keyboard.is_pressed("F2"):
      break
   pag.hotkey("f5")
   time.sleep(0.3)
   pag.click(오류_day_1)
   time.sleep(0.3)
   pag.click(오류_day_2)
   time.sleep(0.3)
   오류_검색()


def 오류_검색():
  #검색
  button = pag.locateCenterOnScreen("./image/71. Oryu/01. Icon.png" , region=오류_find_range,  confidence=0.5) 
  print(button)
  if (button == None) :
      None      
  else : 
      time.sleep(0.3) 
      pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
      오류_예매하기() 

def 오류_예매하기():
  #검색
  button = pag.locateCenterOnScreen("./image/71. Oryu/02. Reservation.png" , confidence=0.8) 
  print(button)
  if (button == None) :
      None      
  else : 
      time.sleep(0.3) 
      pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 
      오류_방지문자()

def 오류_방지문자():
  #검색
  button = pag.locateCenterOnScreen("./image/71. Oryu/03. Reservation.png" , confidence=0.8) 
  print(button)
  if (button == None) :
      None      
  else : 
      time.sleep(0.3) 
      pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 
      time.sleep(0.3)
      pag.moveTo(907,709)
      time.sleep(100)




오류_day1()
오류_day2()
오류_범위선택()
오류_시작()


#★★★★★★★★★★★★★★★★★★★ 서브 함수
def 오류_Karavan():
  while True:
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("중지")
      break
    global i
    i = i + 1

    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      break

