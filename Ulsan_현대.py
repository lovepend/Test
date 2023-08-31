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


def Test_Click():
    while True:
        if keyboard.is_pressed("F2"):
            global Click
            Click  = pag.position()
            print(Click)
            time.sleep(0.5)
            break 

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
        

def 티켓예매():
  while True:
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("키 중지")
      break
    pag.click(Click)
    time.sleep(0.2)
    pag.click(Click1)
    time.sleep(0.2)
    검색()
    time.sleep(0.2)
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("키 중지")
      break
    pag.click(Click2)
    time.sleep(0.2)
    검색1()
    time.sleep(0.2)
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("키 중지")
      break
    pag.click(Click3)
    time.sleep(0.2)
    검색2()
    time.sleep(0.2)
    
def 검색():
  #좌석찾기
  button = pag.locateCenterOnScreen('./image/99. Ulsan_Foot/01. 1.png', confidence=0.98)
  if (button == None) :
    None 
  else :
    pag.click(button.x-1,button.y)
    time.sleep(0.5)
    pag.click(button.x+4,button.y)
    time.sleep(0.2)
    직접선택()

def 검색1():
  #좌석찾기
  button1 = pag.locateCenterOnScreen('./image/99. Ulsan_Foot/01. 1.png', confidence=0.98)
  if (button1 == None) :
    None 
  else :
    pag.click(button1.x-1,button1.y)
    time.sleep(0.5)
    pag.click(button1.x+4,button1.y)
    time.sleep(0.2)
    직접선택()
    
def 검색2():
  #좌석찾기
  button2 = pag.locateCenterOnScreen('./image/99. Ulsan_Foot/01. 1.png', confidence=0.98)
  if (button2 == None) :
    None 
  else :
    pag.click(button2.x-1,button2.y)
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

  




Test_Click1()
Test_Click2()
Test_Click3()
티켓예매()   




