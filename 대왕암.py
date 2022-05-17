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

global end_command
end_command = 0

global 대왕암_id
대왕암_id = "id"
global 대왕암_pw
대왕암_pw = "*Zoavld4fkd" 

global find_range_대왕암
find_range_대왕암 = 860,521,1515,968

def 대왕암_Reset():
    global end_command
    end_command = 0

def 대왕암_log_id1():
    global 대왕암_id
    대왕암_id = "pend"
    print(대왕암_id)

def 대왕암_log_id2():
    global 대왕암_id
    대왕암_id = "lovepend2"
    print(대왕암_id)

def 대왕암_log_id3():
    global 대왕암_id
    대왕암_id = "lovepend3"
    print(대왕암_id)

def 대왕암_log_id4():
    global 대왕암_id
    대왕암_id = "parkmc7"
    print(대왕암_id)

def 대왕암_log_guest():
    global 대왕암_id
    대왕암_id = "suld2000@naver.com"
    global 대왕암_pw
    대왕암_pw = "Sm88410000!"
    print(대왕암_id)
    print(대왕암_pw)
    
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
        kakao_message_you("대왕암")
        global end_command
        end_command = 1
        print('end')

def 대왕암_자동입력():
    #로그인 선택
    pag.click(1296,117)
    time.sleep(5)
    #통합회원 로그인
    pag.click(815,602)
    time.sleep(5)
    #아이디 입력
    pag.moveTo(1000,300)
    time.sleep(2)
    pag.dragTo(100,300, 5, button='left')
    time.sleep(2)
    pag.hotkey('delete')
    time.sleep(2)
    pag.write(대왕암_id)
    print(대왕암_id)
    time.sleep(2)
    #페이지 선택
    pag.doubleClick(1600,800)
    time.sleep(1)
    #비밀번호 입력
    pag.moveTo(1000,353)
    time.sleep(2)
    pag.dragTo(100,353, 5, button='left')
    time.sleep(2)
    pag.hotkey('delete')
    time.sleep(2)
    pag.write(대왕암_pw)
    print(대왕암_pw)
    time.sleep(2)
    #로그인 버튼 클릭
    pag.click(927,403)
    time.sleep(5)
    #온라인 예약
    pag.click(1080,200)
    time.sleep(5)   
    
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


