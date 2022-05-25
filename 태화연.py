from gettext import find
from tkinter import *
from turtle import pendown
from cv2 import goodFeaturesToTrack
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
import datetime

#now = time.localtime()
#print( now.tm_hour ) 
#print( now.tm_min ) 
#print( now.tm_sec )
#current_time_m = now.tm_min

#태화연 Test 2022.05.24 #Viewer Size 67%

################################## 리셋 
global 태화연_end_command
태화연_end_command = 0

global 태화연_end_command1
태화연_end_command1 = 0
################################## 범위 
global 태화연_find_range
태화연_find_range = 0,0,1904,1079

################################## 아이디
global 태화연_id
태화연_id = "lovepend@nate.com"
global 태화연_pw
태화연_pw = "*Zoavld4fkd" 

################################## 날짜
global 태화연_day1
태화연_day1 = 557,116
global 태화연_day2
태화연_day2 = 716,264

################################## 횟수 
global 태화연_i
태화연_i = 0
    
#★★★★★★★★★★★★★★★★★★★ 리셋 입력
def 태화연_Reset():
    global 태화연_end_command
    태화연_end_command = 0
    global 태화연_end_command1
    태화연_end_command1 = 0

def 태화연_End():
    global 태화연_end_command1
    태화연_end_command1 = 1
    
#★★★★★★★★★★★★★★★★★★★ 아이디 입력
def 태화연_Log_Id1():
    global 태화연_id
    태화연_id = "lovepend@nate.com"
    print(태화연_id)

def 태화연_Log_Id2():
    global 태화연_id
    태화연_id = "lovepend@kakao.com"
    print(태화연_id)

def 태화연_Log_Id3():
    global 태화연_id
    태화연_id = "lovepend@naver.com"
    print(태화연_id)

def 태화연_Log_Id4():
    global 태화연_id
    태화연_id = "parkmc7"
    print(태화연_id)

def 태화연_Log_Guest():
    global 태화연_id
    태화연_id = "suld2000@naver.com"
    time.sleep(1)
    global 태화연_pw
    태화연_pw = "Sm88410000!"
    print(태화연_id)
    print(태화연_pw)
       
#★★★★★★★★★★★★★★★★★★★ 날짜 입력
def 태화연_Day1():
    global 태화연_day1
    태화연_day1 = 557,116
    global 태화연_day2
    태화연_day2 = 716,204
    print(태화연_day2)

def 태화연_Day2():
    global 태화연_day1
    태화연_day1 = 557,116
    global 태화연_day2
    태화연_day2= 716,224
    print(태화연_day2)

def 태화연_Day3():
    global 태화연_day1
    태화연_day1 = 557,116
    global 태화연_day2
    태화연_day2 = 716,244
    print(태화연_day2)

def 태화연_Day4():
    global 태화연_day1
    태화연_day1 = 557,116
    global 태화연_day2
    태화연_day2 = 716,264
    print(태화연_day2)
  
#★★★★★★★★★★★★★★★★★★★ 날짜 입력
def 태화연_Day():
    while True:
        if keyboard.is_pressed("F2"): 
            global 태화연_day1 
            태화연_day1  = pag.position()
            print(태화연_day1)
            time.sleep(0.2)
            break        
    while True:
        if keyboard.is_pressed("F2"): 
            global 태화연_day2
            태화연_day2  = pag.position()
            print(태화연_day2)
            time.sleep(0.2)
            break    

#★★★★★★★★★★★★★★★★★★★ 범위 입력
def 태화연_범위선택():
    while True:
        if keyboard.is_pressed("F2"): 
            global 태화연_find_range1 
            태화연_find_range1  = pag.position()
            print(태화연_find_range1)
            time.sleep(0.5)
            break  
    while True:
        if keyboard.is_pressed("F2"): 
            global 태화연_find_range2 
            태화연_find_range2  = pag.position()
            print(태화연_find_range2)
            time.sleep(0.5)
            break  
    global 태화연_find_range
    태화연_find_range = (태화연_find_range1.x,태화연_find_range1.y,태화연_find_range2.x,태화연_find_range2.y)
     
#★★★★★★★★★★★★★★★★★★★ 자동 입력
def 태화연_자동입력():
    time.sleep(2)
    #로그인 선택
    pag.click(1400,128)
    time.sleep(2)
    #이메일 입력
    pag.moveTo(1000,427)
    time.sleep(2)
    pag.dragTo(360,427, 5, button='left')
    time.sleep(2)
    pag.hotkey('delete')
    time.sleep(2)
    pag.write(태화연_id)
    print(태화연_id)
    time.sleep(2)
    #페이지 클릭
    pag.click(1800,800)
    time.sleep(2)
    #비밀번호 입력
    pag.moveTo(1000,457)    
    time.sleep(2)
    pag.dragTo(360,457, 5, button='left')
    time.sleep(2)
    pag.hotkey('delete')
    time.sleep(2)
    pag.write(태화연_pw)
    print(태화연_pw)
    time.sleep(2)
    #로그인 클릭
    pag.click(931,499)
    time.sleep(2)
    #캠핑장 선택 
    pag.click(543,424)
    time.sleep(2)
    #세부 캠핑장 선택
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
    time.sleep(1)
    #페이지 위로
    pag.hotkey("home")
    time.sleep(1)
    #날짜 맞추기
    pag.moveTo(1850,130)    
    time.sleep(1)
    pag.dragTo(1847,339, 5, button='left')
       
#★★★★★★★★★★★★★★★★★★★ 메인 함수
def 태화연_Start():
    while True:
        global 태화연_find_range
        global 태화연_end_command
        global 태화연_end_command1
        global 태화연_i
        global 태화연_day1
        global 태화연_day2
        tm = time.localtime()
        #날짜 클릭
        pag.click(태화연_day1)
        time.sleep(0.1)
        pag.click(태화연_day2)
        time.sleep(0.3)
        #시간 표현
        print(tm)
        #횟수 표현
        태화연_i = 태화연_i + 1
        print(태화연_i)
        #종료 조건
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            print("F2 종료")
            break
        if 태화연_end_command == 1 : # end_command 가 1이 되면
            print("end_command = 1 종료")
            break
        if (tm.tm_hour == 9 and tm.tm_min == 50) or (tm.tm_hour == 16 and tm.tm_min == 50) : #9시 50분 및 16시 50분 종료
            print("minute 중지")
            print(tm.tm_hour ,"시", tm.tm_min ,"분", tm.tm_sec,"초")
            break        
        #검색
        button = pag.locateCenterOnScreen("./image/03_1. reservation.png", region=태화연_find_range ,confidence=0.7) 
        if (button == None) :
            None
        else :
            #pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
            태화연_StepA()
   
def 태화연_StepA():
    global 태화연_find_range
    button = pag.locateCenterOnScreen("./image/03_2. reservation.png", region=태화연_find_range ,confidence=0.7) 
    print(button)
    if (button == None) :
        태화연_Start()      
    else :
        pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
        태화연_StepB()
        
def 태화연_StepB():
    button1 = pag.locateCenterOnScreen("./image/03_3. check.png", confidence=0.7) 
    if (button1 == None) :
        태화연_StepB()
    else :    
        pag.click(1131,211,button='left', clicks=30, interval=0.1)
        #pag.click(button1.x,button1.y, button='left', clicks=1, interval=0.1)
        #print(button1)
        #time.sleep(0.1) 
        #pag.hotkey('enter', clicks=50, interval=0.1)
        time.sleep(0.1)
        pag.click(1800,800)#추가
        #time.sleep(0.5)#추가
        #pag.hotkey('pagedown')#추가
        태화연_StepC()
            
def 태화연_StepC() : 
    button2 = pag.locateCenterOnScreen('./image/03_4. next.png', confidence=0.7)   
    print(button2)
    if (button2 == None) :
        태화연_StepC()      
    else : 
        pag.click(1800,800)
        time.sleep(0.5)
        pag.hotkey('end')
        time.sleep(1)
        button3 = pag.locateCenterOnScreen('./image/03_5. next.png', confidence=0.7)   
        pag.click(button3.x,button3.y, button='left', clicks=1, interval=0.1)
        refresh_token()
        kakao_message_you("태화연")
        time.sleep(50)
        #다음액션
        #뒤로
        pag.hotkey('esc')
        pag.time(1)
        pag.hotkey('esc')
        pag.time(1)
        #홈으로
        pag.hotkey('home')
        pag.time(1)
        pag.hotkey
        태화연_Start()
        #세부 캠핑장 선택
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
        time.sleep(1)
        #페이지 위로
        pag.hotkey("home")
        time.sleep(1)
        #날짜 맞추기
        pag.moveTo(1850,130)    
        time.sleep(1)
        pag.dragTo(1847,339, 5, button='left')
        태화연_Start()

#★★★★★★★★★★★★★★★★★★★ 서브 함수
def 태화연_job1():
    while True:
        pag.hotkey('enter')
        time.sleep(0.05)
        if keyboard.is_pressed("F2") : # F2 누른게 감지되면
            print("중지")
            break

#★★★★★★★★★★★★★★★★★★★ 스케쥴러
def 태화연_자동():
    태화연_Reset()
    #접속 
    pag.click(476,84)
    time.sleep(5)
    pag.click(536,152)
    time.sleep(5)
    태화연_자동입력()
    태화연_Start()
