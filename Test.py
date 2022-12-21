from kakao_api import *
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
from kakao_api import kakao_message_you


####################시간예제
tm = time.localtime()
tm.tm_year
tm.tm_mon
tm.tm_mday
tm.tm_hour
tm.tm_min
tm.tm_sec



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




def Onekey():
    while True:
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            print("F2 종료")
            break
        time.sleep(5)
        pag.click(x=1783, y=653)

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
#         pag.hotkey('ctrl','v')



def 이미지_검색():
    #검색
    button = pag.locateCenterOnScreen("./image/naver.png", confidence=0.85) 
    if (button == None) :
        None      
    else : 
        time.sleep(1) 
        refresh_token()
        kakao_message_you("이미지")

def 이미지_Start():
    while True:
        if keyboard.is_pressed("F2") : # F2 누른게 감지되면
            print("F2 종료")
        ################################    
        time.sleep(5)
        pag.click(x=1783, y=653)
        이미지_검색()
        #################
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break      

def 카카오차단():
    while True:
        if keyboard.is_pressed("F2") : # F2 누른게 감지되면
            print("F2 종료")
        ################################    
        pag.rightClick(232,310)
        time.sleep(0.2)
        pag.click(280,538)
        time.sleep(0.2)
        pag.click(132,390)
        time.sleep(0.2)
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break      

def 카카오삭제():
    while True:
        if keyboard.is_pressed("F2") : # F2 누른게 감지되면
            print("F2 종료")
        ################################    
        pag.click(844,448)
        time.sleep(0.2)
        pag.click(568,350)
        time.sleep(0.2)
        pag.click(589,411)
        time.sleep(0.2)
        pag.click(711,363)
        time.sleep(0.2)
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break      


카카오삭제()