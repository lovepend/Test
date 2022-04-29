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

#태화연 Test 2022.04.01 #Viewer Size 67%

global end_command
end_command = 0

def Reset():
    global end_command
    end_command = 0

def 태화연_검색():
    button = pag.locateCenterOnScreen("./image/03._1. reservation.png", region=find_range ,confidence=0.7) 
    print(button)
    if (button == None) :
        None      
    else :
        pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
        태화연_StepA()
        
def 태화연_StepA():
    button1 = pag.locateCenterOnScreen("./image/03._2. check.png", confidence=0.7) 
    if (button1 == None) :
        None
        태화연_StepA()
    else :    
        #pag.click(button1.x,button1.y, button='left', clicks=1, interval=0.1)
        print(button1)
        time.sleep(0.1) 
        pag.hotkey('enter')
        time.sleep(0.1)
        pag.click(1800,800)#추가
        #time.sleep(0.5)#추가
        #pag.hotkey('pagedown')#추가
        태화연_StepB()
            
def 태화연_StepB() : 
    button2 = pag.locateCenterOnScreen('./image/03._3. next.png', confidence=0.7)   
    print(button2)
    if (button2 == None) :
        태화연_StepB()      
    else : 
        pag.click(1800,800)
        time.sleep(0.5)
        pag.hotkey('end')
        time.sleep(1)
        button3 = pag.locateCenterOnScreen('./image/03._4. next.png', confidence=0.7)   
        pag.click(button3.x,button3.y, button='left', clicks=1, interval=0.1)
        refresh_token()
        kakao_message_you("태화연")
        global end_command
        end_command = 1
        print('end')

def 태화연_날짜선택():
    while True:
        if keyboard.is_pressed("F4"): 
            global 태화연_day1 
            태화연_day1  = pag.position()
            print(태화연_day1)
            time.sleep(0.2)
            break        
    while True:
        if keyboard.is_pressed("F4"): 
            global 태화연_day2
            태화연_day2  = pag.position()
            print(태화연_day2)
            time.sleep(0.2)
            break       
        
def 태화연_자동입력():
    #캠핑장 선택
    pag.click(1005,356)
    time.sleep(1)
    pag.click(1013,392)
    time.sleep(1)
    #차량 넘버 입력
    pag.click(704,928)
    time.sleep(1)
    pyperclip.copy("62소9403")
    time.sleep(1)
    pag.hotkey('ctrl', 'v')
    time.sleep(1)
    #다음페이지
    pag.click(1847,897)
    time.sleep(1)
    #이용준수사항
    pag.click(480,316)
    time.sleep(1)
    #입실정원
    pag.click(480,538)
    time.sleep(1)
    #취소 및 환불 규정
    pag.click(480,760)
    time.sleep(1)
    #개인정보 수집 이용 동의
    pag.click(875,983)
    time.sleep(1)
    #페이지 클릭
    pag.click(1800,800)
    #페이지 위로
    pag.hotkey("home")
    
    

def 태화연_범위선택():
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


        
def 태화연_job():
    while True:
        if end_command == 1 : # end_command 가 1이 되면
            break
        #날짜 클릭
        pag.click(태화연_day1)
        time.sleep(0.1)
        pag.click(태화연_day2)
        time.sleep(0.3)
        #pag.hotkey('mousewheel', 'down')
        #time.sleep(0.3)
        #검색
        태화연_검색()   
        #pag.hotkey('mousewheel', 'up')
        #time.sleep(0.3)
        if keyboard.is_pressed("F4") : # F4 누른게 감지되면
            break