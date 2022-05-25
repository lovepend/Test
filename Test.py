from cgitb import reset
from gettext import find
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

####################시간예제
#tm = time.localtime()
#tm.tm_year
#tm.tm_mon
#tm.tm_mday
#tm.tm_hour
#tm.tm_min
#tm.tm_sec

global i
i = 0

global end
end = 0

def Stop():
    global end
    end = 1
    print(end)
    
def Test():
    while True:
        global i
        global end
        i = i +1
        print(i)
        tm = time.localtime()
        if i > 50000 :
            print("50000 중지")
            break
        if (tm.tm_hour == 12 and tm.tm_min == 8) or (tm.tm_hour == 12 and tm.tm_min == 15) :
            print("minute 중지")
            print(tm.tm_hour ,"시", tm.tm_min ,"분", tm.tm_sec,"초")
            break
        if keyboard.is_pressed("F2") : # F2 누른게 감지되면
            print("키 중지")
            break
        if i == 60 :
            Tset1()
        if i == 120 :
            Tset1()
        if i == 180 :
            Tset1()
        time.sleep(1)

def Tset1():
    print("Tset1")
    time.sleep(5)
    tm = time.localtime()
    if (tm.tm_hour == 12 and tm.tm_min == 8) or (tm.tm_hour == 12 and tm.tm_min == 14) :
        print("minute 중지")
        print(tm.tm_hour ,"시", tm.tm_min ,"분", tm.tm_sec,"초")
        Test()
    else:
        None
    print("종료")



