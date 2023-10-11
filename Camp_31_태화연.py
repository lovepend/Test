from gettext import find
from tkinter import *
from kakao_01_api import *
import pyautogui as pag
import webbrowser
import win32con
import win32api
import win32gui
import keyboard
import requests
import clipboard
import schedule
import pyperclip
import time
import json

pag.FAILSAFE=False
import cv2
cv2.useOptimized()
True

#now = time.localtime()
#print( now.tm_hour ) 
#print( now.tm_min ) 
#print( now.tm_sec )
#current_time_m = now.tm_min

#태화연 Test 2022.11.10 #Viewer Size 50%

################################## 차량번호
global 중구_Car_No
중구_Car_No = "62소9403"


def 중구_차량번호_입력(차량번호):
  global 중구_Car_No
  중구_Car_No = 차량번호
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
    태화연_id = "jhrep2234@nate.com"
    time.sleep(1)
    global 태화연_pw
    태화연_pw = "*Zoavld4fkd"
    print(태화연_id)
    print(태화연_pw)

################################## 날짜
global 태화연_day1
태화연_day1 = 682,114

#★★★★★★★★★★★★★★★★★★★ 날짜 입력 (50%)
def 태화연_Day11():
    global 태화연_day2
    태화연_day2 = 775,180
    print(태화연_day2)

def 태화연_Day12():
    global 태화연_day2
    태화연_day2 = 800,180
    print(태화연_day2)

def 태화연_Day21():
    global 태화연_day2
    태화연_day2= 775,198
    print(태화연_day2)

def 태화연_Day22():
    global 태화연_day2
    태화연_day2= 800,198
    print(태화연_day2)

def 태화연_Day31():
    global 태화연_day2
    태화연_day2 = 775,214
    print(태화연_day2)

def 태화연_Day32():
    global 태화연_day2
    태화연_day2 = 800,214
    print(태화연_day2)

def 태화연_Day41():
    global 태화연_day2
    태화연_day2 = 775,228
    print(태화연_day2)

def 태화연_Day42():
    global 태화연_day2
    태화연_day2 = 800,228
    print(태화연_day2)

def 태화연_Day51():
    global 태화연_day2
    태화연_day2 = 775,243
    print(태화연_day2)

def 태화연_Day52():
    global 태화연_day2
    태화연_day2 = 800,243
    print(태화연_day2)

#★★★★★★★★★★★★★★★★★★★ 날짜 입력
def 태화연_Day():
    while True:
        if keyboard.is_pressed("F2"): 
            time.sleep(0.2)
            global 태화연_day1 
            태화연_day1  = pag.position()
            print(태화연_day1)
            break        
    while True:
        if keyboard.is_pressed("F2"): 
            time.sleep(0.2)
            global 태화연_day2
            태화연_day2  = pag.position()
            print(태화연_day2)
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

def 태화연_호수뷰():
    global 태화연_find_range
    태화연_find_range = 0,0,1069,361

#★★★★★★★★★★★★★★★★★★★ 장소선택
global 중구_장소
중구_장소 = 677,341

def 중구_태화연():
    global 중구_장소
    중구_장소 = 675,341
    print(중구_장소)

def 중구_황방산():
    global 중구_장소
    중구_장소 = 775,326
    print(중구_장소)

def 중구_별뜨락():
    global 중구_장소
    중구_장소 = 910,319
    print(중구_장소)

def 중구_입화산():
    global 중구_장소
    중구_장소 = 1018,331
    print(중구_장소)


#★★★★★★★★★★★★★★★★★★★ 자동 입력
def 중구_자동입력():
  webbrowser.get("windows-default").open('https://www.junggu.ulsan.kr/camping')  
  time.sleep(10)
  button = pag.locateCenterOnScreen("./image/31. Junggu/00. loggin.png",  confidence=0.9)
  print(button)
  if (button == None) :
    time.sleep(2)
    #로그인 클릭
    button = pag.locateCenterOnScreen("./image/31. Junggu/01. loggin.png",  confidence=0.9)
    pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)  
    time.sleep(2)
    #아이디  
    button = pag.locateCenterOnScreen("./image/31. Junggu/02. loggin.png",  confidence=0.9)
    print(button)
    pag.click(button.x+40,button.y+25, button='left', clicks=1, interval=0.1)
    time.sleep(1)
    pag.dragTo(100,304, 1, button='left')
    pag.hotkey('delete')
    time.sleep(2)
    pag.write(태화연_id)
    print(태화연_id)  
    #페이지 선택
    pag.doubleClick(1600,800)
    #비번
    pag.click(button.x+40,button.y+50, button='left', clicks=1, interval=0.1)
    time.sleep(2)
    pag.dragTo(100,352, 1, button='left')
    pag.hotkey('delete')
    time.sleep(2)
    pag.write(태화연_pw)
    print(태화연_pw)
    time.sleep(2)
    #로그인 클릭
    button = pag.locateCenterOnScreen("./image/31. Junggu/03. loggin.png",  confidence=0.8)
    print(button)
    pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
    time.sleep(2)
    중구예약()
  else :
    print(button)
    time.sleep(2)
    중구예약()

def 중구예약():
  global 중구_장소
  global 중구_Car_No
  time.sleep(15)
  print("1")  
  print(중구_장소)  
  pag.click(중구_장소)
  print("2")  
  time.sleep(5)
  #로그인 클릭
  print("3")  
  button = pag.locateCenterOnScreen("./image/31. Junggu/11. input.png",  confidence=0.8)
  print("4")  
  print(button)
  time.sleep(2)
  pag.click(button.x,button.y, button='left', clicks=2, interval=0.1)
  time.sleep(2)
  pyperclip.copy(중구_Car_No)
  pag.hotkey('ctrl','v')
  time.sleep(2)
  
  #이용준수사항
  button = pag.locateCenterOnScreen("./image/31. Junggu/12. input.png",  confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
  time.sleep(1)
  #페이지 클릭
  pag.click(1800,800)
  time.sleep(2)
  pag.hotkey('end')
  time.sleep(2)
  #입실정원준수안내
  button = pag.locateCenterOnScreen("./image/31. Junggu/13. input.png",  confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
  time.sleep(1)  
  #취소 및 환불규정
  button = pag.locateCenterOnScreen("./image/31. Junggu/14. input.png",  confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
  time.sleep(1)  
  #재난상황별 지침
  button = pag.locateCenterOnScreen("./image/31. Junggu/14_1. input.png",  confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
  time.sleep(1)  
  #개인정보 수집 
  button = pag.locateCenterOnScreen("./image/31. Junggu/15. input.png",  confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
  time.sleep(1)  
  #페이지 클릭
  pag.click(1800,800)
  time.sleep(1)
  #페이지 위로
  pag.hotkey("home")
  time.sleep(1)
  #날짜 맞추기
  pag.moveTo(1910,187)    
  time.sleep(1)
  pag.dragTo(1910,359, 6, button='left')
  #태화연_Start()
     
#★★★★★★★★★★★★★★★★★★★ 메인 함수
def 태화연_Start():
  pag.click(태화연_day1)
  time.sleep(0.2) 
  pag.click(태화연_day2)
  time.sleep(5)
  pag.click(태화연_day1)
  태화연_Start1()   

def 태화연_JubJub():
  pag.click(태화연_day1)
  time.sleep(0.2) 
  pag.click(797,142)
  태화연_Start1()   


# 메인 
def 태화연_Start1():
  while True:
    #종료 조건
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      print("F2 종료")
      break
    pag.hotkey('enter')     
    time.sleep(0.1)
    #검색
    태화연_검색()

def 태화연_Start2():
    while True:
        global 태화연_i
        tm = time.localtime()
        #날짜 클릭
        pag.click(태화연_day2)
        time.sleep(0.1)
        pag.click(10,500)
        #횟수 표현
        태화연_i = 태화연_i + 1
        #종료 조건
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            print("F2 종료")
            break
        if (tm.tm_hour == 11 and tm.tm_min == 5) or (tm.tm_hour == 19 and tm.tm_min == 5) : #9시 50분 및 16시 50분 종료
            print("minute 중지")
            print(tm.tm_hour ,"시", tm.tm_min ,"분", tm.tm_sec,"초")
            break        
        #날짜 클릭
        pag.click(태화연_day1)
        time.sleep(0.1)
        #검색
        태화연_검색()

def 태화연_검색():
    print("검색")
    button = pag.locateCenterOnScreen("./image/31. Junggu/21. reservation.png", region=태화연_find_range ,confidence=0.8) 
    if (button == None) :
        태화연_검색()
        #None     
    else :
        #pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
        태화연_StepA()
       
def 태화연_StepA():
    print("태화연_StepA")
    button = pag.locateCenterOnScreen("./image/31. Junggu/22. reservation.png", region=태화연_find_range ,confidence=0.9) 
    print(button)
    if (button == None) :
        None     
    else :
        pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
        태화연_StepB()
        
def 태화연_StepB():
    button1 = pag.locateCenterOnScreen("./image/31. Junggu/23. check.png", confidence=0.7) 
    if (button1 == None) :
        태화연_StepB()
    else :    
        time.sleep(0.1)
        pag.hotkey('enter')
        time.sleep(0.2)
        #pag.click(button1.x,button1.y, button='left', clicks=1, interval=0.1)
        #print(button1)
        #time.sleep(0.1) 
        #pag.hotkey('enter', clicks=50, interval=0.1)
        #time.sleep(0.1)
        #pag.click(1800,800)#추가
        #time.sleep(0.5)#추가
        #pag.hotkey('pagedown')#추가
        태화연_StepC()

def 태화연_StepC() : 
    button2 = pag.locateCenterOnScreen('./image/31. Junggu/24. next.png', confidence=0.8)   
    print(button2)
    if (button2 == None) :
        태화연_StepC()      
    else : 
        # i = 0
        # while i < 1:
        #     i = i +1
        #     pag.hotkey('down')

        #     if i == 1 :
        #       break
        pag.hotkey('down')
        time.sleep(0.1)
        pag.click(1800,800)
        time.sleep(0.2)
        pag.hotkey('end')
        time.sleep(0.4)
        태화연_StepD()
        # button3 = pag.locateCenterOnScreen('./image/31. Junggu/25. next.png', confidence=0.9)  
        # time.sleep(0.2) 
        # pag.click(button3.x,button3.y, button='left', clicks=1, interval=0.1)
        # print('button3')
        # print(button3)
        # # refresh_token()
        # # kakao_message_you("태화연")
        # time.sleep(5000)

def 태화연_StepD() : 
    button3 = pag.locateCenterOnScreen('./image/31. Junggu/25. next.png', confidence=0.9)  
    print(button3)
    if (button3 == None) :
        태화연_StepD()      
    else : 
        # i = 0
        # while i < 1:
        #     i = i +1
        #     pag.hotkey('down')

        #     if i == 1 :
        #       break
        # pag.hotkey('down')
        # time.sleep(0.1)
        # pag.click(1800,800)
        # time.sleep(0.2)
        # pag.hotkey('end')
        # time.sleep(0.3)
        # button3 = pag.locateCenterOnScreen('./image/31. Junggu/25. next.png', confidence=0.9)  
        # time.sleep(0.2) 
        pag.click(button3.x,button3.y, button='left', clicks=1, interval=0.1)

        print('button3')
        print(button3)
        refresh_token()
        kakao_message_you("태화연")
        time.sleep(5000)


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
    time.sleep(5)
    #페이지 클릭
    pag.click(1800,800)
    time.sleep(5)
    #페이지 클릭
    pag.click(1800,800)
    time.sleep(5)
    #로그인
    pag.click(476,84)
    time.sleep(5)
    pag.click(536,152)
    time.sleep(5)
    태화연_Reset()
    #로그아웃
    pag.click(1455,138)
    time.sleep(5)
    #접속 
    pag.click(476,84)
    time.sleep(5)
    pag.click(536,152)
    time.sleep(5)
  
    태화연_Start()











