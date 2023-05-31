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


####################시간예제
tm = time.localtime()
tm.tm_year
tm.tm_mon
tm.tm_mday
tm.tm_hour
tm.tm_min
tm.tm_sec


def 시간체크():
  while True:
    tm = time.localtime()
    tm.tm_year
    tm.tm_mon
    tm.tm_mday
    tm.tm_hour
    tm.tm_min
    tm.tm_sec
    if keyboard.is_pressed("F2") : # F2 누른게 감지되면
      print("키 중지")
      break
    print(tm.tm_hour, tm.tm_min, tm.tm_sec)



# 예약날짜 = pyperclip.paste()
# #70,97
# date_1 = 예약날짜[70:78]
# date_2 = 예약날짜[96:97]
# print(date_1)
# print("1")

# date_2 = 예약날짜[95:98]
# print(date_2)
# print("2")

# print(date_1,date_2)
# print("3")

# date3 = date_1 +" // " + date_2
# print(date3)

# refresh_token
# kakao_message_you(date3)

#global i
# i = 0

# global end
# end = 0

# def Stop():
#     global end
#     end = 1
#     print(end)


def Test():
    while True:
        from datetime import datetime, timedelta
        시 = 16
        분 = 00
        초 = 58
        밀리초 = 800000 #383
        time1 = datetime(2022,10,14,시,분,초,밀리초) 
        time2 = datetime.now()

        # print(time1)
        # print(time2)
        # print(type(time1))
        # print(type(time2))
        if (time1 < time2 ):  # ) or (tm.tm_hour == 12 and tm.tm_min == 15) :
            pag.click(x=1399, y=1062)
            print("minute 중지")
            break
        if keyboard.is_pressed("F2") : # F2 누른게 감지되면
            print("키 중지")
            break
        # tm = time.localtime()
        # if (tm.tm_hour == 19 and tm.tm_min == 27 and tm.tm_sec == 57):  # ) or (tm.tm_hour == 12 and tm.tm_min == 15) :
        #     pag.click(x=1399, y=1062)
        #     print("minute 중지")
        #     print(tm.tm_hour ,"시", tm.tm_min ,"분", tm.tm_sec,"초")
        #     break
        # if keyboard.is_pressed("F2") : # F2 누른게 감지되면
        #     print("키 중지")
        #     break




# def Onekey():
#     while True:
#         if keyboard.is_pressed("F2"): # F2 누른게 감지되면
#             print("F2 종료")
#             break
#         time.sleep(5)
#         pag.click(x=1783, y=653)

#Onekey()
# def Tset1():
#     print("Tset1")
#     time.sleep(5)
#     tm = time.localtime()
#     if (tm.tm_hour == 12 and tm.tm_min == 8) or (tm.tm_hour == 12 and tm.tm_min == 14) :
#         print("minute 중지")
#         print(tm.tm_hour ,"시", tm.tm_min ,"분", tm.tm_sec,"초")
#         Test()
#     else:
#         None
#     print("종료")


# def 홀리데이_이벤트():
#     time.sleep(0.85)
#     pag.click(x=1436, y=407)
#     time.sleep(0.1)
#     pag.click(x=1436, y=407)
#     time.sleep(0.1)
#     pag.click(x=1436, y=407)
#     time.sleep(0.1)
#     pag.click(x=1436, y=407)
    
    
    
# schedule.every().day.at("14:30:59").do(홀리데이_이벤트) # 각종00 스케줄 스타트
# schedule.every().day.at("14:35:59").do(홀리데이_이벤트) # 각종00 스케줄 스타트
# schedule.every().day.at("14:40:59").do(홀리데이_이벤트) # 각종00 스케줄 스타트
# while True:
#     schedule.run_pending()
#     time.sleep(1)
    
    
# #네이버 구매
# def 네이버구매(): 
#     while True:
#         if keyboard.is_pressed("F2"): # F2 누른게 감지되면
#             print("F2 종료")
#             break
#         pag.hotkey('f5')
#         time.sleep(1)
#         pag.click(1800,800)
#         time.sleep(0.2)
#         pag.hotkey('pgdn')
#         time.sleep(1)
#         pag.click(x=1117, y=542)
#         time.sleep(0.5)
#         pag.click(x=1110, y=702)
#         time.sleep(0.5)
#         button1 = pag.locateCenterOnScreen('./image/naver.png',  confidence=0.8)   #region = (510,100,1324,333),
#         print(button1)
#         if (button1 == None) :
#             print("없다")
#             time.sleep(1)
#             네이버구매()      
#         else :
#             print("있다")
#             time.sleep(100)


# def 꼬잡():
#     while True:
#         if keyboard.is_pressed("F2"): # F2 누른게 감지되면
#             print("F2 종료")
#             break
#         pag.hotkey('end')
#         time.sleep(0.5)
#         pag.hotkey('pageup')
#         time.sleep(0.5)
#         pag.click("좌표입력")
#         time.sleep(0.5)
# #         pag.hotkey('ctrl','v')



# def 이미지_검색():
#     while True:
#         if keyboard.is_pressed("F2") : # F2 누른게 감지되면
#             break
#         pag.click(1379,346)
#         time.sleep(0.5)
#         #검색
#         button1 = pag.locateCenterOnScreen("./image/222.png", confidence=0.85, region=(0,0,1623,596)) 
#         button2 = pag.locateCenterOnScreen("./image/222.png", confidence=0.85, region=(0,0,1623,596)) 
#         if (button1 == None and button2 == None) :
#             None      
#         else : 
#             time.sleep(0.5) 
#             refresh_token()
#             kakao_message_you("이미지")
#             time.sleep(10000)
#             print('찾')
        



# 이미지_검색()
# def 이미지_Start():
#     while True:
#         if keyboard.is_pressed("F2") : # F2 누른게 감지되면
#             print("F2 종료")
#         ################################    
#         time.sleep(5)
#         pag.click(x=1783, y=653)
#         이미지_검색()
#         #################
#         if keyboard.is_pressed("F2"): # F2 누른게 감지되면
#             break      

# def 카카오차단():
#     while True:
#         if keyboard.is_pressed("F2") : # F2 누른게 감지되면
#             print("F2 종료")
#         ################################    
#         pag.rightClick(232,310)
#         time.sleep(0.2)
#         pag.click(280,538)
#         time.sleep(0.2)
#         pag.click(132,390)
#         time.sleep(0.2)
#         if keyboard.is_pressed("F2"): # F2 누른게 감지되면
#             break      

# def 카카오삭제():
#     while True:
#         if keyboard.is_pressed("F2") : # F2 누른게 감지되면
#             print("F2 종료")
#         ################################    
#         pag.click(844,448)
#         time.sleep(0.2)
#         pag.click(568,350)
#         time.sleep(0.2)
#         pag.click(589,411)
#         time.sleep(0.2)
#         pag.click(711,363)
#         time.sleep(0.2)
#         if keyboard.is_pressed("F2"): # F2 누른게 감지되면
#             break      



def 울주_범위선택():
    global find_range
    
    while True:
        if keyboard.is_pressed("F2"): 
            global find_range1 
            find_range1  = pag.position()
            print(find_range1)
            time.sleep(0.5)
            break  
    while True:
        if keyboard.is_pressed("F2"): 
            global find_range2 
            find_range2  = pag.position()
            print(find_range2)
            time.sleep(0.5)
            break  
    find_range = (find_range1.x,find_range1.y,find_range2.x,find_range2.y)
    print(find_range)
        
    
    


def test_검색():
  global find_range
  print(find_range)
  button = pag.locateCenterOnScreen('./image/11. Ulju/01_0. reservation1.png', region = (801, 577, 903, 850), confidence=0.95)
  img_capture = pag.locateOnScreen("./image/11. Ulju/01_0. reservation1.png", region=(801, 577, 903, 850))
  pag.moveTo(img_capture)
  print(button)
  if (button == None) :
    None        
  else :
    pag.click(button)
    
    # Friday = (button.x-150, button.y-8, button.x-100, button.y+8)
    # print(Friday)
    # button_1 = pag.locateCenterOnScreen('./image/11. Ulju/01_0. reservation1.png', region = Friday,confidence=0.9) #토요일 찾을 범위 설정      
    # if (button_1 == None) :
    #     None
    #     pag.click(button,button='left')
    # else:
    #     pag.click(button_1,button='left')     
    #     print("검색")


울주_범위선택()
test_검색()