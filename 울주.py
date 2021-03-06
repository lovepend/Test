from gettext import find
from tkinter import *
from kakao_api import *
import pyautogui as pag
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

#울주해양예약 시스템 2022.01.11 #Vier Size 67%

################################## 아이디
global 울주_id
울주_id = "lovepend@nate.com"
global 울주_pw
울주_pw = "*Zoavld4fkd" 
global find_range

################################## 범위
find_range = 0,0,1904,1079

################################## 아이디



#★★★★★★★★★★★★★★★★★★★ 아이디 입력
def 울주_log_id1():
    global 울주_id
    울주_id = "lovepend@nate.com"
    print(울주_id)

def 울주_log_id2():
    global 울주_id
    울주_id = "lovepend@kakao.com"
    print(울주_id)
    
def 울주_log_id3():
    global 울주_id
    울주_id = "lovepend@naver.com"
    print(울주_id)

def 울주_log_id4():
    global 울주_id
    울주_id = "parkmc7@naver.com"
    print(울주_id)

def 울주_log_guest():
    global 울주_id
    울주_id = "suld2000@naver.com"
    time.sleep(1)
    global 울주_pw
    울주_pw = "Sm88410000!"
    print(울주_id)
    print(울주_pw)

#★★★★★★★★★★★★★★★★★★★ 범위 입력
def 울주_범위선택():
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
        
    global find_range
    find_range = (find_range1.x,find_range1.y,find_range2.x,find_range2.y)

def 울주_토요일():
    global find_range
    find_range = 1164,102,1263,1080 #토요일만 검색 

#★★★★★★★★★★★★★★★★★★★ 메인 함수
def 울주_검색():
    #Saturday = 1164,102,1263,1080 #토요일만 검색 
    button = pag.locateCenterOnScreen('./image/01_0. reservation1.png', region = find_range, confidence=0.9)
    if (button == None) :
        None        
    else :
        Friday = ((button.x)-150, (button.y)-8, (button.x)-100, (button.y+8))
        button_1 = pag.locateCenterOnScreen('./image/01_0. reservation2.png', region = Friday,confidence=0.9) #토요일 찾을 범위 설정      
        pag.click(button_1,button='left')     
        울주_page1()

def 울주_page1():
    pag.click(859,50)
    pag.hotkey('ctrl','c')
    refresh_token()
    kakao_message_you(pyperclip.paste())
    #기간
    pag.click(x=907, y=750)
    pag.sleep(0.1)
    pag.hotkey('end')
    pag.sleep(0.1)
    #총인원
    pag.click(x=1019, y=747)
    pag.sleep(0.1)
    pag.hotkey('end')
    #페이지 선택
    pag.doubleClick(1600,800)
    #페이지 아래
    pag.hotkey('end')
    time.sleep(0.3)    
    pag.click(1175,850, button='left', interval=0.1, clicks=1)
    time.sleep(0.1) 
    #다음 페이지
    울주_page2()

def 울주_page2():
    #페이지 선택
    pag.doubleClick(1600,800)
    #페이지 아래
    pag.hotkey('end')
    time.sleep(0.3)
    #방문차량번호
    pyperclip.copy('62소9403')
    pag.click(766,285)
    time.sleep(0.3)
    pag.hotkey('ctrl','v')
    #도착예정시간
    pag.click(772,243)
    time.sleep(0.1)
    pag.hotkey('down')
    pag.click(587,637)
    time.sleep(0.1)
    pag.click(1177,851)
    울주_page3()
 
#신용카드결제
def 울주_page3():
    #신용카드결제 
    buttonpostion3_1 = pag.locateCenterOnScreen('./image/01_3. next1.png', region = (0,0,1920,1680), confidence=0.7) 
    if (buttonpostion3_1 == None):
        울주_page3()
    else :        
        pag.click(buttonpostion3_1.x-35,buttonpostion3_1.y) 
        #전체동의
        buttonpostion3_2 = pag.locateCenterOnScreen('./image/01_3. next2.png', region = (0,0,1920,1680), confidence=0.7) 
        #다음
        time.sleep(0.1)
        pag.click(buttonpostion3_2.x+30,buttonpostion3_2.y)
        time.sleep(0.1)
        울주_page4()
        
#카드선택
def 울주_page4():
    #국민 카드 선택
    buttonpostion4_1 = pag.locateCenterOnScreen('./image/01_4. next1.png', region = (0,0,1920,1680), confidence=0.7) 
    if (buttonpostion4_1 == None):
        울주_page4()
    else :
        #국민카드 선택
        time.sleep(0.1)
        pag.click(buttonpostion4_1.x,buttonpostion4_1.y)
        time.sleep(0.1)
        #결제 동의 
        buttonpostion4_2 = pag.locateCenterOnScreen('./image/01_4. next2.png', region = (0,0,1920,1680), confidence=0.7) 
        pag.click(buttonpostion4_2.x,buttonpostion4_2.y) 
        #다음
        buttonpostion4_3 = pag.locateCenterOnScreen('./image/01_4. next3.png', region = (0,0,1920,1680), confidence=0.7) 
        time.sleep(0.1)
        pag.click(buttonpostion4_3.x,buttonpostion4_3.y) 
        time.sleep(0.1)
        울주_page5()
        
#앱결제
def 울주_page5():
    buttonpostion5 = pag.locateCenterOnScreen('./image/01_5. payment.png', region = (0,0,1920,1680), confidence=0.7) #reservation 67%
    if (buttonpostion5 == None):
        울주_page5()
    else :
        #앱결제
        pag.click(buttonpostion5.x,buttonpostion5.y)
        울주_page6()

#결제코드보내기       
def 울주_page6():
    button6 = pag.locateCenterOnScreen('./image/01_6. payment.png', region = (0,0,1920,1680), confidence=0.7)
    if (button6 == None):
        울주_page6()
    else :
        #코드보내기
        time.sleep(0.1)
        pag.click(1034,603)
        time.sleep(0.1)
        pag.dragTo(1171,660, 0.2, button='left')
        time.sleep(0.1)
        pag.hotkey('ctrl', 'c')
        결제코드 = pyperclip.paste() 
        kakao_message_you(결제코드)
        울주_page7()
        
#이메일 확인
def 울주_page7():
    buttonpostion7 = pag.locateCenterOnScreen('./image/01_7. next1.png', confidence=0.7) #reservation 67%
    if (buttonpostion7 == None):
        울주_page7()
    else :
        #이메일 발송
        time.sleep(0.2)
        buttonpostion7_1 = pag.locateCenterOnScreen('./image/01_7. next2.png', confidence=0.7) #reservation 67%
        pag.click(buttonpostion7_1.x,buttonpostion7_1.y, button='left')
        울주_page8()

#완료!!!
def 울주_page8():
    buttonpostion8 = pag.locateCenterOnScreen('./image/01_8. next1.png', confidence=0.7) #reservation 67%
    if (buttonpostion8 == None):
        울주_page8()
    else :
        #이메일 발송
        time.sleep(1)
        pag.click(buttonpostion8.x+70,buttonpostion8.y, button='left')
        time.sleep(30)

#★★★★★★★★★★★★★★★★★★★ 로그
def 울주_log():
    loggin = pag.locateCenterOnScreen('./image/01_10. loggin.png', region = (1100,0,1250,204), confidence=0.8)
    if (loggin == None):
        None
    else :
        time.sleep(2)
        #코드보내기
        pag.click(loggin.x,loggin.y)
        time.sleep(1)
        #아이디 입력
        pag.moveTo(998,442)
        time.sleep(1)
        pag.dragTo(360,442, 5, button='left')
        time.sleep(1)
        pag.hotkey("delete")
        time.sleep(1)
        pag.write(울주_id)
        print(울주_id)
        time.sleep(1)
        #페이지 선택
        pag.doubleClick(1600,800)
        time.sleep(1)
        #비밀번호 입력
        pag.moveTo(998,486)
        time.sleep(1)
        pag.dragTo(360,486, 5, button='left')
        time.sleep(1)
        pag.write(울주_pw)
        print(울주_pw)
        time.sleep(1)
        #로그인 클릭
        pag.hotkey('enter')
        time.sleep(1)  
        #예약하기      
        pag.click(1239,162)
        time.sleep(1)        
        pag.click(1239,162)       
       
def 울주_log1():
    loggin = pag.locateCenterOnScreen('./image/01_10. loggin.png', region = (1100,0,1250,204), confidence=0.8)
    if (loggin == None):
        None
    else :
        time.sleep(2)
        #코드보내기
        pag.click(loggin.x,loggin.y)
        time.sleep(1)
        #아이디 입력
        pag.moveTo(998,442)
        time.sleep(1)
        pag.dragTo(360,442, 5, button='left')
        time.sleep(1)
        pag.hotkey("delete")
        time.sleep(1)
        pag.write(울주_id)
        time.sleep(1)
        #페이지 선택
        pag.doubleClick(1600,800)
        time.sleep(1)
        #비밀번호 입력
        pag.moveTo(998,486)
        time.sleep(1)
        pag.dragTo(360,486, 5, button='left')
        time.sleep(1)
        pag.write(울주_pw)
        time.sleep(1)
        #로그인 클릭
        pag.hotkey('enter')
        time.sleep(1)  
        #예약하기      
        pag.click(1239,162)
        time.sleep(1)        
        pag.click(1239,162) 
        #다음달 선택
        time.sleep(2)
        pag.click(986,429)
        #페이지 선택
        time.sleep(2)
        pag.doubleClick(1600,800)

#★★★★★★★★★★★★★★★★★★★ 메인 함수
def 울주_This_A():
    while True:
        #페이지 선택
        pag.doubleClick(1600,800)
        울주_log()
        pag.hotkey('f5')
        time.sleep(0.2)
        울주_검색()
        pag.hotkey('pgdn')
        time.sleep(0.2)
        울주_검색()
        pag.hotkey('home')
        time.sleep(0.2)
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break

def 울주_This_N():
    while True:
        #페이지 선택
        pag.doubleClick(1600,800)
        울주_log()
        
        #A사이트 * 2
        #pag.click(620,510)
        #time.sleep(0.2)
        #울주_검색()
        #pag.hotkey('pgdn')
        #time.sleep(0.2)
        #울주_검색()    
        
        #B사이트 * 2
        pag.click(690,510)
        #pag.click(690,120)
        time.sleep(0.5)
        울주_검색()
        pag.hotkey('pgdn')
        time.sleep(0.5)
        울주_검색()
        
        #C사이트
        #pag.click(760,510)
        pag.click(765,120)   
        time.sleep(0.5)
        울주_검색()
        
        #D사이트 * 2
        pag.click(840,510)
        #pag.click(840,120)
        time.sleep(0.5)
        울주_검색()
        pag.hotkey('pgdn')
        time.sleep(0.5)
        울주_검색()
        
        #E사이트  * 2
        #pag.click(920,510)
        pag.click(920,120)
        time.sleep(0.5)
        울주_검색()
        pag.hotkey('pgdn')
        time.sleep(0.5)
        울주_검색()
        
        #F사이트
        #pag.click(990,510)
        pag.click(990,120)
        time.sleep(0.5)#페이지 선택
        pag.doubleClick(1600,800)
        pag.hotkey('home')
        time.sleep(0.5)
        pag.hotkey('home')
        time.sleep(0.5)
        
        울주_검색()
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break

def 울주_Next_A():
    while True:
        #페이지 선택
        pag.doubleClick(1600,800)
        울주_log1()
        pag.hotkey('f5')
        time.sleep(0.2)
        울주_검색()
        pag.hotkey('pgdn')
        time.sleep(0.2)
        울주_검색()
        pag.hotkey('home')
        time.sleep(0.2)
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break

def 울주_Next_N():
    while True:
        #페이지 선택
        pag.doubleClick(1600,800)
        울주_log1()
        
        #A사이트 * 2
        #pag.click(620,510)
        #time.sleep(0.2)
        #울주_검색()
        #pag.hotkey('pgdn')
        #time.sleep(0.2)
        #울주_검색()    
        
        #B사이트 * 2
        pag.click(690,510)
        #pag.click(690,120)
        time.sleep(0.5)
        울주_검색()
        pag.hotkey('pgdn')
        time.sleep(0.5)
        울주_검색()
        
        #C사이트
        #pag.click(760,510)
        pag.click(765,120)   
        time.sleep(0.5)
        울주_검색()
        
        #D사이트 * 2
        pag.click(840,510)
        #pag.click(840,120)
        time.sleep(0.5)
        울주_검색()
        pag.hotkey('pgdn')
        time.sleep(0.5)
        울주_검색()
        
        #E사이트  * 2
        #pag.click(920,510)
        pag.click(920,120)
        time.sleep(0.5)
        울주_검색()
        pag.hotkey('pgdn')
        time.sleep(0.5)
        울주_검색()
        
        #F사이트
        #pag.click(990,510)
        pag.click(990,120)
        time.sleep(0.5)#페이지 선택
        pag.doubleClick(1600,800)
        pag.hotkey('home')
        time.sleep(0.5)
        pag.hotkey('home')
        time.sleep(0.5)
        
        울주_검색()
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
            break
        
#★★★★★★★★★★★★★★★★★★★ 스케쥴러      
def 울주_자동():
    pag.click(466,84)
    time.sleep(5)
    pag.click(500,115)
    time.sleep(5)
    울주_Next_A()
    