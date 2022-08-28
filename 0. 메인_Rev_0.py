from gettext import find
import pyautogui as pag
import win32con
import win32api
import win32gui
import keyboard
import time
import pyperclip
from tkinter import *
import requests
import json
import clipboard
import schedule

################################# 포지션    ##################################
x0, y0 = 0, 0
x1, y1 = 597, 0
x2, y2 = 1196, 0 #597,0
x3, y3 = 1920, 0 #1920 1080
################################# 인게임위치 ##################################
#인게임 위치
인게임_메뉴_X, 인게임_메뉴_Y = 543,53
출석체크_X, 출석체크_Y = 475,119
오늘그만보기_X, 오늘그만보기_Y = 19,335
화면가운데_X, 화면가운데_Y = 300,175
입장하기_X, 입장하기_Y = 478,323
물약클릭_X, 물약클릭_Y = 147,61
스케줄자동_X, 스케줄자동_Y = 514,178
절전모드시작_X, 절전모드시작_Y = 509,147
월드보스클릭_X, 월드보스클릭_Y = 375,55
월드보스입장_X, 월드보스입장_Y = 283,318
오토클릭_X, 오토클릭_Y = 424, 263
귀환클릭_X, 귀환클릭_Y = 539,312

################################# LD 위치    ##################################
#메뉴위치
추가기능_X, 추가기능_Y = 581,118
멀티컨트롤_X, 멀티컨트롤_Y = 505,153
홈_X, 홈_Y = 580,283
최근앱_X, 최근앱_Y = 581,321
앱닫기_X, 앱닫기_Y = 386,102
뒤로_X, 뒤로_Y = 580,245
리니지M_X, 리니지M_Y = 209,123
#녹화 관련
녹화설정_X, 녹화설정_Y = 467,106
녹화닫기_X, 녹화닫기_Y = 505,17
#녹화 순서 위에서부터
Record_No01_X ,Record_No01_Y = 434, 142 #메인 시련던전
Record_No02_X ,Record_No02_Y = 436, 179 
Record_No03_X ,Record_No03_Y = 436, 211 
Record_No04_X ,Record_No04_Y = 434, 247
Record_No05_X ,Record_No05_Y = 434, 282
Record_No06_X ,Record_No06_Y = 435, 319
Record_No07_X ,Record_No07_Y = 435, 353
Record_Next_X ,Record_Next_Y = 521, 336
Record_No08_X ,Record_No08_Y = 435, 155
Record_No09_X ,Record_No09_Y = 436, 188
Record_No10_X ,Record_No10_Y = 436, 224
Record_No11_X ,Record_No11_Y = 434, 261
Record_No12_X ,Record_No12_Y = 434, 295
Record_No13_X ,Record_No13_Y = 435, 328


################################# 기능 ##################################
def 앱초기화(x,y):
    pag.click(최근앱_X+x, 최근앱_Y+y)
    time.sleep(15)
    pag.click(앱닫기_X+x, 앱닫기_Y+y)
    time.sleep(5)
    pag.click(앱닫기_X+x, 앱닫기_Y+y)
    time.sleep(10)
    pag.click(리니지M_X+x, 리니지M_Y+y)   
    time.sleep(90)
    pag.click(오늘그만보기_X+x, 오늘그만보기_Y+y)
    time.sleep(10)
    pag.click(화면가운데_X+x, 화면가운데_Y+y)
    time.sleep(10)
    pag.click(입장하기_X+x, 입장하기_Y+y)
    time.sleep(30)
    pag.click(귀환클릭_X+x, 귀환클릭_Y+y)
    time.sleep(5)
    
def 시련던전(x,y):
    pag.click(인게임_메뉴_X+x, 인게임_메뉴_Y+y)
    time.sleep(10)
    pag.click(출석체크_X+x, 출석체크_Y+y)
    time.sleep(10)
    pag.hotkey('esc')
    time.sleep(5)
    pag.hotkey('esc')
    time.sleep(5)
    pag.click(추가기능_X+x, 추가기능_Y+y)
    time.sleep(5)
    pag.click(녹화설정_X+x, 녹화설정_Y+y)
    time.sleep(5)
    
def 스케줄실행(x,y):
    pag.click(물약클릭_X+x, 물약클릭_Y+y)
    time.sleep(5)
    pag.click(스케줄자동_X+x, 스케줄자동_Y+y)
    time.sleep(5)
    
def 절전모드실행(x,y):
    pag.click(물약클릭_X+x, 물약클릭_Y+y)
    time.sleep(5)
    pag.click(절전모드시작_X+x, 절전모드시작_Y+y)
    time.sleep(5)

def 월드보스(x,y):
    pag.click(월드보스클릭_X+x, 월드보스클릭_Y+y)
    time.sleep(5)
    pag.click(월드보스입장_X+x, 월드보스입장_Y+y)
    time.sleep(5)
    pag.click(오토클릭_X+x, 오토클릭_Y+y)
    time.sleep(5)
    
    
    
################################# 스케쥴    ##################################

#서브02 시련 스타트
def 서브02_시련():
    서브02_시련_(x3,y3)
       
def 서브02_시련_(x,y):
    앱초기화(x,y)
    시련던전(x,y)
    pag.click(Record_No01_X+x ,Record_No01_Y+y)
    time.sleep(5)
    pag.click(녹화닫기_X+x, 녹화닫기_Y+y)
    time.sleep(5)
    
#서브02 스케줄 스타트
def 서브02_스케줄():
    서브02_스케줄_(x3,y3)
    
def 서브02_스케줄_(x,y):
    앱초기화(x,y)
    스케줄실행(x,y)
    절전모드실행(x,y)

#서브01 시련 스타트  
def 서브01_시련():
    서브01_시련_(x2,y2)
    
def 서브01_시련_(x,y):
    앱초기화(x,y)
    시련던전(x,y)
    pag.click(Record_No01_X+x ,Record_No01_Y+y)
    time.sleep(5)
    pag.click(녹화닫기_X+x, 녹화닫기_Y+y)
    time.sleep(5)
    
#메인00 시련 스타트  
def 메인00_시련():
    메인00_시련_(x0,y0)
    pag.click(Record_No01_X+x0 ,Record_No01_Y+y0)  
    time.sleep(5)
    pag.click(녹화닫기_X+x0, 녹화닫기_Y+y0)
    time.sleep(5)

def 메인00_시련_(x,y):
    앱초기화(x,y)
    시련던전(x,y) 

#메인00 스케줄 스타트
def 메인00_스케줄():
    메인00_스케줄_(x0,y0)
    
def 메인00_스케줄_(x,y):
    앱초기화(x,y)
    스케줄실행(x,y)
    절전모드실행(x,y)
   
    
#서브01 스케줄 스타트
def 서브01_스케줄():
    서브01_스케줄_(x2,y2)
    
def 서브01_스케줄_(x,y):
    앱초기화(x,y)
    스케줄실행(x,y)
    절전모드실행(x,y)
    
#서브00 월드보스
def job_1251():
    job_1251_(x3,y3)
    job_1251_(x2,y2)
    
def job_1251_(x,y):
    앱초기화(x,y)
    월드보스(x,y)
    절전모드실행(x,y)
    
#각종00 스케줄 스타트
def job_1303():
    job_1303_(x2,y2)
    job_1303_(x3,y3)
    
def job_1303_(x,y):
    앱초기화(x,y)
    스케줄실행(x,y)
    절전모드실행(x,y)
    
#각종00 월드보스
def job_1851():
    job_1851_(x3,y3)
    job_1851_(x2,y2)
    job_1851_(x0,y0)
    
def job_1851_(x,y):
    앱초기화(x,y)
    월드보스(x,y)
    절전모드실행(x,y)
    
#각종00 스케줄 스타트
def job_1903():
    job_1903_(x0,y0)
    job_1903_(x2,y2)
    job_1903_(x3,y3)
    
def job_1903_(x,y):
    앱초기화(x,y)
    스케줄실행(x,y)
    절전모드실행(x,y)
    
schedule.every().day.at("05:00").do(서브02_시련) # 서브02 시련던전 스타트
schedule.every().day.at("09:00").do(서브02_스케줄) # 서브02 스케쥴러 스타트

schedule.every().day.at("09:05").do(메인00_시련) # 메인00 시련던전 스타트
schedule.every().day.at("09:10").do(서브01_시련) # 서브01 시련던전 스타트

schedule.every().day.at("12:49").do(job_1851) # 월드보스
schedule.every().day.at("13:03").do(job_1903) # 각종00 스케줄 스타트

schedule.every().day.at("18:49").do(job_1851) # 월드보스
schedule.every().day.at("19:03").do(job_1903) # 각종00 스케줄 스타트

schedule.every().day.at("19:49").do(job_1851) # 월드보스
schedule.every().day.at("20:03").do(job_1903) # 각종00 스케줄 스타트

schedule.every().day.at("20:49").do(job_1851) # 월드보스
schedule.every().day.at("21:03").do(job_1903) # 각종00 스케줄 스타트

schedule.every().day.at("21:49").do(job_1851) # 월드보스
schedule.every().day.at("22:03").do(job_1903) # 각종00 스케줄 스타트

# 10초에 한번씩 실행
#schedule.every(10).second.do(job)
# 10분에 한번씩 실행
#schedule.every(10).minutes.do(job)
# 매 시간 실행
#schedule.every().hour.do(job)
# 매일 05:00 에 실행
#schedule.every().day.at("05:00").do(job_0500)
# 매주 월요일 실행
#schedule.every().monday.do(job)
# 매주 수요일 05:00 에 실행
#schedule.every().wednesday.at("5:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    if keyboard.is_pressed("F2"): 
        break

