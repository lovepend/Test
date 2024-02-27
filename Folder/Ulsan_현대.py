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


#150 %


num = random.randrange(20,40)
num1 = num/100
time.sleep(num1)


def Test_Click1():
    while True:
        if keyboard.is_pressed("F2"):
            global Click1
            Click1  = pag.position()
            print(Click1)
            time.sleep(0.5)
            break 
        
def Test_Click2():
    while True:
        if keyboard.is_pressed("F2"):
            global Click2
            Click2  = pag.position()
            print(Click2)
            time.sleep(0.5)
            break 

def Test_Click3():
    while True:
        if keyboard.is_pressed("F2"):
            global Click3
            Click3  = pag.position()
            print(Click3)
            time.sleep(0.5)
            break 
        
def Test_Click4():
    while True:
        if keyboard.is_pressed("F2"):
            global Click4
            Click4  = pag.position()
            print(Click4)
            time.sleep(0.5)
            break

def Test_Click5():
    while True:
        if keyboard.is_pressed("F2"):
            global Click5
            Click5  = pag.position()
            print(Click5)
            time.sleep(0.5)
            break

def Test_Click6():
    while True:
        if keyboard.is_pressed("F2"):
            global Click6
            Click6  = pag.position()
            print(Click6)
            time.sleep(0.5)
            break


def Test_Click7():
    while True:
        if keyboard.is_pressed("F2"):
            global Click7
            Click7  = pag.position()
            print(Click7)
            time.sleep(0.5)
            break 

def 티켓예매():
  try:
    pag.click(Click1)#구역선택
    time.sleep(num1)
    pag.click(Click2)#직접선택
    time.sleep(num1)
    while True:
      if keyboard.is_pressed("F2") : # F2 누른게 감지되면
        print("키 중지")
        break
      pag.click(Click3)#새로그침
      time.sleep(num1)
      time.sleep(0.2)
      검색1()
      매크로 = pag.locateCenterOnScreen('./image/99. Ulsan_Foot/03. 1.png', confidence=0.7)
      if (매크로 == None) :
        None 
      else :
        time.sleep(0.2)
        pag.click(매크로.x,매크로.y)
        time.sleep(2)
        pag.hotkey('f5')
        time.sleep(2)
        티켓예매()
  except:
     pass


    
def 검색():
  #좌석찾기
  button = pag.locateCenterOnScreen('./image/99. Ulsan_Foot/01. 1.png', confidence=1)
  if (button == None) :
    None 
  else :
    time.sleep(0.2)
    pag.click(button.x-1.5,button.y)
    time.sleep(0.5)
    pag.click(button.x+4,button.y)
    time.sleep(0.2)
    직접선택()

def 검색1():
  #좌석찾기
  button1 = pag.locateCenterOnScreen('./image/99. Ulsan_Foot/01. 1.png', confidence=1)
  if (button1 == None) :
    None 
  else :
    pag.click(button1.x-1.5,button1.y)
    time.sleep(0.5)
    pag.click(button1.x+4,button1.y)
    time.sleep(0.2)
    직접선택()
    
def 검색2():
  #좌석찾기
  button2 = pag.locateCenterOnScreen('./image/99. Ulsan_Foot/01. 1.png', confidence=0.99)
  if (button2 == None) :
    None 
  else :
    pag.click(button2.x-1.5,button2.y)
    time.sleep(0.5)
    pag.click(button2.x+4,button2.y)
    time.sleep(0.2)
    직접선택()

def 직접선택():
  button = pag.locateCenterOnScreen('./image/99. Ulsan_Foot/02. 1.png', confidence=0.9)
  if (button == None) :
    None 
  else :
    pag.click(button.x,button.y)
    time.sleep(100)

  



Test_Click1() # 사이트 클릭
Test_Click2() # 직접선택
Test_Click3() # 좌석도 새로고침
티켓예매()   

#소이산 예약
# def 소이산예약():
#    while True:
#     if keyboard.is_pressed("F2") : # F2 누른게 감지되면
#       print("키 중지")
#       break
#     pag.click(Click)
#     time.sleep(1)
#     if keyboard.is_pressed("F2") : # F2 누른게 감지되면
#       print("키 중지")
#       break
#     소이산검색()

# def 소이산검색():
#   button = pag.locateCenterOnScreen('./image/99. Ulsan_Foot/99. 1.png', region = (963,565,1891,1068), confidence=0.9 )
#   if (button == None) :
#     None 
#   else :
#     refresh_token
#     kakao_message_you("모노레일")
#     time.sleep(100)

# Test_Click()
# 소이산예약()



