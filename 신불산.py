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


global end_command
end_command = 0

global 신불산_id
신불산_id = "id"
global 신불산_pw
신불산_pw = "*Zoavld4fkd" 

global find_range
find_range = 860,521,1515,968

def 신불산_log_id1():
    global 신불산_id
    신불산_id = "pend"
    print(신불산_id)

def 신불산_log_id2():
    global 신불산_id
    신불산_id = "lovepend2"
    print(신불산_id)

def 신불산_log_id3():
    global 신불산_id
    신불산_id = "lovepend3"
    print(신불산_id)

def 신불산_log_id4():
    global 신불산_id
    신불산_id = "parkmc7"
    print(신불산_id)

def 신불산_log_guest():
    global 신불산_id
    신불산_id = "suld2000@naver.com"
    global 신불산_pw
    신불산_pw = "Sm88410000!"
    print(신불산_id)
    print(신불산_pw)
    
def 신불산_Reset():
    global end_command
    end_command = 0
    global log_id_no1
    log_id_no1 = "pend"
    global log_id_no2
    log_id_no2 = "lovepend2"
    global log_id_no3
    log_id_no3 = "lovepend3"
    global log_id_no4
    log_id_no4 = "parkmc7"
    global 신불산_pw
    신불산_pw = "*Zoavld4fkd"  
    global find_range
    find_range = 860,521,1515,968
    
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
        kakao_message_you("신불산")
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

def 신불산_자동입력():      
    #로그인 클릭
    pag.click(1112,115)
    time.sleep(5)
    #통합회원 로그인
    pag.click(669,1064)
    time.sleep(5)
    #아이디 입력
    pag.moveTo(1000,304)
    time.sleep(2)
    pag.dragTo(100,304, 5, button='left')
    time.sleep(2)
    pag.hotkey('delete')
    time.sleep(2)
    pag.write(신불산_id)
    print(신불산_id)
    time.sleep(2)
    #페이지 선택
    pag.doubleClick(1600,800)
    time.sleep(1)
    #비밀번호 입력
    pag.moveTo(1000,352)
    time.sleep(2)
    pag.dragTo(100,352, 5, button='left')
    time.sleep(2)
    pag.hotkey('delete')
    time.sleep(2)
    pag.write(신불산_pw)
    print(신불산_pw)
    time.sleep(2)
    #로그인 클릭
    pag.click(900,403)
    time.sleep(5)
    #온라인 예약 클릭
    pag.click(851,785)
    time.sleep(5)
    #아무 날짜 선택
    pag.click(892,821)
    time.sleep(5)
    #예약가능 사이트만 보기
    pag.click(1201,693)
    time.sleep(5)
    #등억 선택
    pag.click(970,692)
    time.sleep(5)
     
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
        time.sleep(0.5)
        #검색
        신불산_검색()
        if keyboard.is_pressed("F4"): # F4 누른게 감지되면
            break



