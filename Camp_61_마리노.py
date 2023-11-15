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
import cv2
cv2.useOptimized()
True
#마리노 Test 2023.05.15 #Viewer Size 50% #화면 맨아래로 통일


#★★★★★★★★★★★★★★★★★★★ 서브 함수
def 마리노_검색():
  #검색
  button = pag.locateCenterOnScreen("./image/61. Marino/05._1. reservation.png" , confidence=0.85) 
  print(button)
  if (button == None) :
      None      
  else : 
      time.sleep(0.05) 
      pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 

마리노_검색()

#★★★★★★★★★★★★★★★★★★★ 서브 함수
def 마리노_Karavan():
  while True:
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("중지")
      break
    global i
    i = i + 1

    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      break
