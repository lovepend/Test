from gettext import find
from tkinter import *
from kakao_api import *
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

#신불산 Test 2022.03.21 #Viewer Size 67%

def 신불산_검색():
    button = pag.locateCenterOnScreen("./image/04._1. reservation.png", region = find_range, confidence=0.7) 
    if (button == None) :
        None      
    else : 
        time.sleep(0.05)
        pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
        신불산_확인()
        
def 신불산_확인() : 
    button1 = pag.locateCenterOnScreen('./image/04._2. next.png',  confidence=0.8)   #region = (510,100,1324,333),
    print(button1)
    if (button1 == None) :
        신불산_확인()      
    else :
        pag.click(1225,281)
        time.sleep(0.05)
        pag.click(1225,281)
        time.sleep(0.05)
        pag.click(1225,281)
        time.sleep(0.05)
        pag.click(1225,281)
        time.sleep(0.05)
        pag.click(1225,281)
        time.sleep(0.05)
        pag.click(button1.x,button1.y+27, button='left', clicks=5, interval=0.1)
        refresh_token()
        kakao_message_you()
        time.sleep(60) 

#버튼 기능
def 신불산_날짜선택():
    while True:
        if keyboard.is_pressed("F4"): 
            global 신불산_day1
            신불산_day1  = pag.position()
            print(신불산_day1)
            time.sleep(0.5)
            break         
        
def 금요일():
    global week
    week = 1342,114

def 토요일():
    global week
    week = 1390,114

def 신불산_범위선택():
    while True:
        if keyboard.is_pressed("F4"): 
            global find_range1 
            find_range1  = pag.position()
            print(find_range1)
            time.sleep(0.5)
            break  
    while True:
        if keyboard.is_pressed("F4"): 
            global find_range2 
            find_range2  = pag.position()
            print(find_range2)
            time.sleep(0.5)
            break  
        
    global find_range
    find_range = (find_range1.x,find_range1.y,find_range2.x,find_range2.y)

def 신불산_전체():
    global find_range
    find_range = (630,474,1419,1079)

def 신불산_job():
    while True:
        #날짜 클릭
        pag.click(신불산_day1)
        time.sleep(0.2)
        #검색
        신불산_검색()
        if keyboard.is_pressed("F4"): # F4 누른게 감지되면
            break

