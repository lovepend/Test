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

#고래불 Test 2023.05.15 #Viewer Size 50% #화면 맨아래로 통일


#★★★★★★★★★★★★★★★★★★★ 서브 함수

def 고래불_day1():
    while True:
        if keyboard.is_pressed("F2"):
            global 고래불_day_1
            고래불_day_1  = pag.position()
            print(고래불_day_1)
            time.sleep(0.5)
            break 
        
def 고래불_day2():
    while True:
        if keyboard.is_pressed("F2"):
            global 고래불_day_2
            고래불_day_2  = pag.position()
            print(고래불_day_2)
            time.sleep(0.5)
            break 

def 고래불_범위선택():
    while True:
        if keyboard.is_pressed("F2"): 
            global 고래불_find_range1 
            고래불_find_range1  = pag.position()
            print(고래불_find_range1)
            time.sleep(0.5)
            break  
    while True:
        if keyboard.is_pressed("F2"): 
            global 고래불_find_range2 
            고래불_find_range2  = pag.position()
            print(고래불_find_range2)
            time.sleep(0.5)
            break  
    global 고래불_find_range
    고래불_find_range = (고래불_find_range1.x,고래불_find_range1.y,고래불_find_range2.x,고래불_find_range2.y)


def 고래불_시작():
  while True:
   if keyboard.is_pressed("F2"):
      break
   pag.click(10,900)
   pag.hotkey("f5")
   time.sleep(0.3)
   #pag.click(10,900)
   #pag.hotkey("pgdn")
   print("1")
   고래불_검색()


def 고래불_검색():
  
  #검색
    print("2")
    button = pag.locateCenterOnScreen("./image/81. Dolphin/01. Icon.png" , confidence=0.95) 
    print(button)
    if (button == None) :
        None      
        print("3")
        고래불_시작()
    else : 
        time.sleep(0.3) 
        pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
        print("4")
        고래불_예매하기() 

def 고래불_예매하기():
  while True:
    if keyboard.is_pressed("F2"):
      break
    #검색
    pag.click(10,900)
    pag.click(10,900)
    #pag.hotkey("end")
    #pag.hotkey("end")
    time.sleep(0.3)
    #코뿔소 15번 클릭
    #pag.doubleClick(1042,644)
    #토끼 18번 클릭
    pag.doubleClick(1109,647)
    button = pag.locateCenterOnScreen("./image/81. Dolphin/02. Reservation.png" , confidence=0.7) 
    print(button)
    if (button == None) :
        None      
    else : 
        time.sleep(0.3) 
        pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 
        고래불_방지문자()

def 고래불_방지문자():
  #검색
  button = pag.locateCenterOnScreen("./image/81. Dolphin/03. Reservation.png" , confidence=0.8) 
  print(button)
  if (button == None) :
      None      
  else : 
      time.sleep(0.3) 
      pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 
      time.sleep(100)





고래불_시작()

#★★★★★★★★★★★★★★★★★★★ 서브 함수
def 고래불_Karavan():
  while True:
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("중지")
      break
    global i
    i = i + 1

    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      break

