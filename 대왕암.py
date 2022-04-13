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

#대왕암 Test 2022.03.17 #Viewer Size 80% #화면 맨아래로 통일

def 대왕암_검색():
    #검색
    button = pag.locateCenterOnScreen("./image/02._1. reservation.png", region = find_range_대왕암, confidence=0.85) 
    if (button == None) :
        None      
    else : 
        time.sleep(0.05) 
        pag.click(button.x,button.y, button='left', clicks=1, interval=0.1) 
        대왕암_확인()
        
def 대왕암_확인() :
    button1 = pag.locateCenterOnScreen('./image/02._2. next.png', confidence=0.7)   
    print(button1)
    if (button1 == None) :
        대왕암_확인()      
    else :
        pag.click(1084,283)
        time.sleep(0.05)
        pag.click(1084,283)
        time.sleep(0.05)
        pag.click(1084,283)
        time.sleep(0.05)
        pag.click(1084,283)
        time.sleep(0.05)
        pag.click(1084,283)
        time.sleep(0.05)
        pag.click(button1.x,button1.y, button='left', clicks=5, interval=0.1)
        refresh_token()
        kakao_message_you()
        global end_command
        end_command = 1
        print('end')
    
def 대왕암_날짜선택():
    while True:
        if keyboard.is_pressed("F4"): 
            global 대왕암_day1 
            대왕암_day1  = pag.position()
            print(대왕암_day1)
            time.sleep(0.5)
            break         

def 대왕암_커서선택():
    while True:
        if keyboard.is_pressed("F4"): 
            global 대왕암_position_up
            대왕암_position_up  = pag.position()
            print(대왕암_position_up)
            time.sleep(0.5)
            break 
    
    while True:
        if keyboard.is_pressed("F4"): 
            global 대왕암_position_down
            대왕암_position_down  = pag.position()
            print(대왕암_position_down)
            time.sleep(0.5)
            break 

def 대왕암_범위선택():
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
    global find_range_대왕암
    find_range_대왕암 = (find_range1.x,find_range1.y,find_range2.x,find_range2.y)
 
def 대왕암_카라반():
    while True:
        if end_command == 1 : # end_command 가 1이 되면
            break
        #날짜 클릭
        pag.click(대왕암_day1)
        time.sleep(0.2)
        #검색
        대왕암_검색()
        #page 아래 
        pag.click(대왕암_position_down)
        time.sleep(0.2)
        대왕암_검색()
        #page 업 
        pag.click(대왕암_position_up)
        time.sleep(0.2)
        if keyboard.is_pressed("F4"): # F4 누른게 감지되면
            break
        
def 대왕암_오토():
    while True:
        if end_command == 1 : # end_command 가 1이 되면
            break
        #날짜 클릭
        pag.click(대왕암_day1)
        time.sleep(0.5)
        #검색
        대왕암_검색()
        time.sleep(0.2)
        #page 위
        pag.click(대왕암_position_up)
        time.sleep(0.2)
        대왕암_검색()
        time.sleep(0.2)
        #page 위
        pag.click(대왕암_position_up)
        time.sleep(0.2)
        대왕암_검색()
        time.sleep(0.2)
        #page 위
        pag.click(대왕암_position_up)
        time.sleep(0.2)
        대왕암_검색()
        #page 위
        pag.click(대왕암_position_up)
        time.sleep(0.2)
        대왕암_검색()
        #page 아래
        pag.click(대왕암_position_down)
        time.sleep(0.2)
        pag.click(대왕암_position_down)
        time.sleep(0.2)
        pag.click(대왕암_position_down)
        time.sleep(0.2)
        pag.click(대왕암_position_down)
        time.sleep(0.2)
        pag.click(대왕암_position_down)
        time.sleep(0.2)
        pag.click(대왕암_position_down)
        time.sleep(0.2)
        if keyboard.is_pressed("F4"): # F4 누른게 감지되면
            break


