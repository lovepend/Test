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
x1, y1 = 0, 0
x2, y2 = 1920, 0 #1920 1080
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
월드보스클릭_X, 월드보스클릭_Y = 384,53###############################확인
월드보스입장_X, 월드보스입장_Y = 384,53##############################확인
오토클릭_X, 오토클릭_Y = 424, 263

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
    time.sleep(10)
    pag.click(앱닫기_X+x, 앱닫기_Y+y)
    time.sleep(10)
    pag.click(리니지M_X+x, 리니지M_Y+y)   
    time.sleep(90)
    pag.click(오늘그만보기_X+x, 오늘그만보기_Y+y)
    time.sleep(10)
    pag.click(화면가운데_X+x, 화면가운데_Y+y)
    time.sleep(10)
    pag.click(입장하기_X+x, 입장하기_Y+y)
    time.sleep(60)
    
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

def 월드보스(x,y):
    pag.click(월드보스클릭_X+x, 월드보스클릭_Y+y)
    time.sleep(5)
    pag.click(월드보스입장_X+x, 월드보스입장_Y+y)
    time.sleep(5)
    pag.click(오토클릭_X+x, 오토클릭_Y+y)
    time.sleep(5)
    
    
    
################################# 스케쥴    ##################################
#5시 서브02 시련 스타트
def job_0500():
    job_0500_(x2,y2)
       
def job_0500_(x,y):
    앱초기화(x,y)
    시련던전(x,y)
    pag.click(Record_No01_X ,Record_No01_Y)

#7시 서브02 스케줄 스타트
def job_0700():
    job_0700_(x2,y2)
    
def job_0700_(x,y):
    앱초기화(x,y)
    스케줄실행(x,y)
    절전모드실행(x,y)

#7시 05분 서브01 시련 스타트  
def job_0705():
    job_0705_(x1,y1)
    
def job_0705_(x,y):
    앱초기화(x,y)
    시련던전(x,y)
    pag.click(Record_No02_X ,Record_No02_Y)
    
#7시 10분 메인00 시련 스타트  
def job_0710():
    job_0710_(x0,y0)
    
def job_0710_(x,y):
    앱초기화(x,y)
    시련던전(x,y)
    pag.click(Record_No01_X ,Record_No01_Y)  

#12시 51분 서브00 월드보스
def job_1251():
    job_1251_(x2,y2)
    job_1251_(x1,y1)
    
def job_1251_(x,y):
    앱초기화(x,y)
    월드보스(x,y)
    절전모드실행(x,y)
    
#13시 03분 각종00 스케줄 스타트
def job_1303():
    job_1303_(x1,y1)
    job_1303_(x2,y2)
    
def job_1303_(x,y):
    앱초기화(x,y)
    스케줄실행(x,y)
    절전모드실행(x,y)
    

schedule.every().day.at("05:00").do(job_0500) # 서브02 시련던전 스타트
schedule.every().day.at("07:00").do(job_0700) # 서브02 스케쥴러 스타트

schedule.every().day.at("07:05").do(job_0705) # 서브01 시련던전 스타트
schedule.every().day.at("07:05").do(job_0710) # 메인00 시련던전 스타트
schedule.every().day.at("07:05").do(job_0710) # 메인00 시련던전 스타트

schedule.every().day.at("12:51").do(job_1251) # 월드보스
schedule.every().day.at("13:03").do(job_1303) # 각종00 스케줄 스타트

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
