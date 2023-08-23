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
    pag.click(10,500)
    time.sleep(num1)
    #맨끝이동
    pag.hotkey('end')
    time.sleep(num1)
    #글쓰기 클릭
    pag.doubleClick(845,466)
    pag.doubleClick(845,466)
    time.sleep(num1)
    pag.doubleClick(845,466)
    pyperclip.copy(꼬잡문구)
    pag.hotkey('ctrl','v')
    time.sleep(num1)
    #등록
    pag.click(1187,484)
    time.sleep(0.5)
    #도배금지 확인
    pag.doubleClick(1138,231)

꼬리잡기()

