from tkinter import *
from Folder.kakao_01_api import *
import pyautogui as pag
import win32con
import win32api
import win32gui
import keyboard
import clipboard
import schedule
import pyperclip
import time 
import cv2


#태화연 Test 2023.11.17 #Viewer Size 50%

# 변수 설정
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★


#아이디입력
#▶▶▶▶▶▶▶▶▶
태화연_id = "lovepend@nate.com"
#태화연_id = "lovepend@kakao.com"
#태화연_id = "lovepend@naver.com"
#태화연_id = "parkmc7@naver.com"
#태화연_id = "jhrep2234@nate.com"
print(태화연_id)
태화연_pw = "*Zoavld4fkd" 

#장소입력
# #▶▶▶▶▶▶▶▶▶
중구_url = 'https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=1030300'

#중구_태화연(): 중구_url = 'https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=1030300'
#중구_별뜨락(): 중구_url = 'https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=2010400'
#중구_입화산(): 중구_url = 'https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=2030300'
  
#날짜입력
#▶▶▶▶▶▶▶▶▶
태화연_day1 = 205,128
태화연_day2 = 317,149 #다음달 선택
태화연_day3 = 1163,128 #금요일 297,238
태화연_day4 = 319,238
태화연_day5 = 1278,149#다음달 선택
태화연_day6 = 1280,238 #금요일 1257,238

#차량번호 입력
#▶▶▶▶▶▶▶▶▶
중구_Car_No = "62소9403"

#범위입력
#▶▶▶▶▶▶▶▶▶
태화연_find_rangeA = 0,0,960,1080
#태화연_find_rangeB = 960,0,1920,1080
태화연_find_rangeB = 960,0,960,1080

#함수 설정
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

#자동입력(로그인)
#▶▶▶▶▶▶▶▶▶
def 중구_자동입력():
  #webbrowser.get("windows-default").open('https://www.junggu.ulsan.kr/camping')  
  time.sleep(10)
  #url 클릭
  pag.click(300,60)
  time.sleep(1)
  pag.hotkey('ctrl','a')
  #로그인페이지 이동 
  pyperclip.copy('https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=5010000')
  time.sleep(1)
  pyperclip.copy('https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=5010000')
  time.sleep(1)
  pag.hotkey('ctrl','v')
  time.sleep(1)
  pag.hotkey('enter')
  time.sleep(5)
  #ID입력
  pag.click(536,347)
  time.sleep(1)
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pyperclip.copy(태화연_id)
  time.sleep(1)
  pyperclip.copy(태화연_id)
  time.sleep(1)
  pag.hotkey('ctrl','v')
  pag.click(655,350)
  time.sleep(5)
  #PW입력
  pag.click(493,370)
  time.sleep(1)
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pyperclip.copy(태화연_pw)
  time.sleep(1)
  pyperclip.copy(태화연_pw)
  time.sleep(1)
  pag.hotkey('ctrl','v')
  #로그인
  time.sleep(1)
  pag.hotkey('enter')
  time.sleep(5)
  중구예약_A()

#자동입력(A화면셋팅)
#▶▶▶▶▶▶▶▶▶
def 중구예약_A():
  #######################첫번째##########################
  #url 클릭
  pag.click(300,60)
  time.sleep(1)
  pag.hotkey('ctrl','a')
  #장소 url 이동 
  pyperclip.copy(중구_url)
  time.sleep(1)
  pyperclip.copy(중구_url)
  time.sleep(1)
  pag.hotkey('ctrl','v')
  time.sleep(1)
  pag.hotkey('enter')
  time.sleep(5)
  #차량넘버 입력
  global 중구_Car_No
  print("3")  
  button = pag.locateCenterOnScreen("./image/31. Junggu/11. input.png", region=(0,0,960,1080) , confidence=0.8)
  print("4")  
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y, button='left', clicks=2, interval=0.1)
  time.sleep(1)
  pyperclip.copy(중구_Car_No)
  pag.hotkey('ctrl','v')
  time.sleep(1)
  #이용준수사항
  button = pag.locateCenterOnScreen("./image/31. Junggu/12. input.png", region=(0,0,960,1080) , confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
  time.sleep(1)
  #페이지 클릭
  pag.click(10,800)
  time.sleep(1)
  pag.hotkey('end')
  time.sleep(5)
  #입실정원준수안내
  button = pag.locateCenterOnScreen("./image/31. Junggu/13. input.png", region=(0,0,960,1080) , confidence=0.8)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+90, button='left', clicks=1, interval=0.1)
  time.sleep(1)  
  #취소 및 환불규정
  button = pag.locateCenterOnScreen("./image/31. Junggu/14. input.png", region=(0,0,960,1080) , confidence=0.8)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
  time.sleep(1)  
  #재난상황별 지침
  button = pag.locateCenterOnScreen("./image/31. Junggu/14_1. input.png", region=(0,0,960,1080) , confidence=0.8)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
  time.sleep(1)  
  #개인정보 수집 
  button = pag.locateCenterOnScreen("./image/31. Junggu/15. input.png", region=(0,0,960,1080) , confidence=0.8)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
  time.sleep(1)  
  #페이지 클릭
  pag.click(10,800)
  time.sleep(1)
  #페이지 위로
  pag.hotkey("home")
  time.sleep(5)
  #날짜 맞추기
  pag.scroll(-413)
  time.sleep(3)
  중구예약_B()


#자동입력(B화면셋팅)
#▶▶▶▶▶▶▶▶▶
def 중구예약_B():
  #######################두번째##########################
  #url 클릭
  time.sleep(1)
  pag.click(1300,60)
  time.sleep(1)
  pag.hotkey('ctrl','a')
  #장소 url 이동 
  pyperclip.copy(중구_url)
  time.sleep(1)
  pyperclip.copy(중구_url)
  time.sleep(1)
  pag.hotkey('ctrl','v')
  time.sleep(1)
  pag.hotkey('enter')
  time.sleep(5)
  #차량넘버 입력
  global 중구_Car_No
  print("3")  
  button = pag.locateCenterOnScreen("./image/31. Junggu/11. input.png", region=(960,0,1920,1080) , confidence=0.8)
  print("4")  
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y, button='left', clicks=2, interval=0.1)
  time.sleep(1)
  pyperclip.copy(중구_Car_No)
  pag.hotkey('ctrl','v')
  time.sleep(1)
  #이용준수사항
  button = pag.locateCenterOnScreen("./image/31. Junggu/12. input.png", region=(960,0,1920,1080) , confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
  time.sleep(1)
  #페이지 클릭
  pag.click(1850,800)
  time.sleep(2)
  pag.hotkey('end')
  time.sleep(5)
  #입실정원준수안내
  button = pag.locateCenterOnScreen("./image/31. Junggu/13. input.png", region=(960,0,1920,1080) , confidence=0.8)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+90, button='left', clicks=1, interval=0.1)
  time.sleep(1)   
  #취소 및 환불규정
  button = pag.locateCenterOnScreen("./image/31. Junggu/14. input.png", region=(960,0,1920,1080) , confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
  time.sleep(1)  
  #재난상황별 지침
  button = pag.locateCenterOnScreen("./image/31. Junggu/14_1. input.png", region=(960,0,1920,1080) , confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
  time.sleep(1)  
  #개인정보 수집 
  button = pag.locateCenterOnScreen("./image/31. Junggu/15. input.png", region=(960,0,1920,1080) , confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
  time.sleep(1)  
  #페이지 클릭
  pag.click(1850,800)
  time.sleep(1)
  #페이지 위로
  pag.hotkey("home")
  time.sleep(5)
  #날짜 맞추기
  pag.scroll(-413)
  time.sleep(3)
  pag.click(태화연_day1)
  time.sleep(1)
  pag.click(태화연_day2)
  time.sleep(1)
  pag.click(태화연_day3)
  time.sleep(3)
  pag.click(태화연_day4)
  time.sleep(1)
  pag.click(태화연_day5)
  time.sleep(1)
  pag.click(태화연_day6)
  태화연_Start_검색()#스케쥴

#줍줍함수(시작)
#▶▶▶▶▶▶▶▶▶
def 태화연_JubJub():
  pag.click(태화연_day1)
  time.sleep(0.2) 
  pag.click(797,142)
  태화연_Start_검색()   

#메인함수(시작)
#▶▶▶▶▶▶▶▶▶
def 태화연_Start():
  while True:
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      print("F2 종료")
      time.sleep(60)
      break
    태화연_Start_검색()  
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      print("F2 종료")
      time.sleep(60)
      break


#메인함수(검색)
#▶▶▶▶▶▶▶▶▶
def 태화연_Start_검색():
  while True:
    #종료 조건
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      print("F2 종료")
      break
    #검색
    태화연_검색A()
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      print("F2 종료")
      break
    태화연_검색B()

#메인함수(A화면 검색)
#▶▶▶▶▶▶▶▶▶
def 태화연_검색A():
  try :
    print("태화연_검색A")
    button = pag.locateCenterOnScreen("./image/31. Junggu/21. reservation.png", region=태화연_find_rangeA ,confidence=0.9) 
    if (button == None) :
      None     
    else :
      태화연_StepA_A()
  except :
    None

#메인함수(B화면 검색)
#▶▶▶▶▶▶▶▶▶
def 태화연_검색B():
  try :
    print("태화연_검색B")
    button = pag.locateCenterOnScreen("./image/31. Junggu/21. reservation.png", region=태화연_find_rangeB ,confidence=0.9) 
    if (button == None) :
      None     
    else :
      태화연_StepA_B()
  except :
    None

#메인함수(A화면 예약하기 클릭)
#▶▶▶▶▶▶▶▶▶
def 태화연_StepA_A():
  try :
    print("태화연_StepA_A")
    button = pag.locateCenterOnScreen("./image/31. Junggu/22. reservation.png", region=태화연_find_rangeA ,confidence=0.95) 
    if (button == None) :
      pag.click(태화연_day1)
      time.sleep(0.1)
      pag.hotkey('enter')     
      time.sleep(0.1)
    else :
      pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
      태화연_StepB()
  except :
    pag.click(태화연_day1)
    time.sleep(0.1)
    pag.hotkey('enter')     
    time.sleep(0.1)

#메인함수(B화면 예약하기 클릭)
#▶▶▶▶▶▶▶▶▶    
def 태화연_StepA_B():
  try :
    print("태화연_StepA_B")
    button = pag.locateCenterOnScreen("./image/31. Junggu/22. reservation.png", region=태화연_find_rangeB ,confidence=0.95) 
    print(button)
    if (button == None) :
      pag.click(태화연_day3)
      time.sleep(0.1)
      pag.hotkey('enter')     
      time.sleep(0.1)  
    else :
      pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
      태화연_StepB()
  except :
    pag.click(태화연_day3)
    time.sleep(0.1)
    pag.hotkey('enter')     
    time.sleep(0.1)

#메인함수(확인 클릭)
#▶▶▶▶▶▶▶▶▶   
def 태화연_StepB():
  while True : 
    try :
      print("태화연_StepB")
      button = pag.locateCenterOnScreen("./image/31. Junggu/23. check.png", confidence=0.7) 
      if (button == None) :
        태화연_StepB()
      else :    
        time.sleep(0.1)
        pag.hotkey('enter')
        time.sleep(0.5)
        태화연_StepC()
    except :
      태화연_StepB()

#메인함수(숙박일 확인)
#▶▶▶▶▶▶▶▶▶  
def 태화연_StepC() : 
  while True :
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      print("F2 종료")
      time.sleep(60)
      break
    태화연_StepC_A()
    태화연_StepC_B()

#메인함수(이미 예약된)
#▶▶▶▶▶▶▶▶▶  
def 태화연_StepC_A() : 
  #이미 예약된 상태 리셋 
  print("이미예약된")
  try :
    button = pag.locateCenterOnScreen("./image/31. Junggu/90. Reject.png", confidence=0.7) 
    if (button == None) :
      None
    else :    
      time.sleep(1)
      pag.hotkey('enter')
      time.sleep(1)
      pag.click(태화연_day1)
      time.sleep(1)
      pag.hotkey('enter')
      time.sleep(1)
      pag.click(태화연_day3)
      time.sleep(1)
      pag.hotkey('enter')
      태화연_Start()
  except :
    None

#메인함수(숙박클릭)
#▶▶▶▶▶▶▶▶▶  
def 태화연_StepC_B() : 
  try :  
    print("태화연_StepC_B")
    button = pag.locateCenterOnScreen('./image/31. Junggu/24. next.png', confidence=0.8)   
    print(button)
    if (button == None) :
      태화연_StepC()
    else : 
      pag.hotkey('down')
      time.sleep(0.2)
      pag.click(button.x+500 ,button.y)
      time.sleep(0.2)
      pag.hotkey('end')
      time.sleep(0.4)
      태화연_StepD()
  except :
    태화연_StepC()

#메인함수(숙박일 확인)
#▶▶▶▶▶▶▶▶▶  
def 태화연_StepD() : 
  try :
    print("태화연_StepD")
    button = pag.locateCenterOnScreen('./image/31. Junggu/25. next.png', confidence=0.9)  
    print(button)
    if (button == None) :
      태화연_StepD()      
    else : 
      pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
      print(button)
      time.sleep(0.1)
      refresh_token()
      kakao_message_you("태화연")
      time.sleep(500)
  except :
    태화연_StepD()

#★★★★★★★★★★★★★★★★★★★ 서브 함수
def 태화연_job1():
    while True:
        pag.hotkey('enter')
        time.sleep(0.05)
        if keyboard.is_pressed("F2") : # F2 누른게 감지되면
            print("중지")
            break



#스케줄러
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
import subprocess
import os

def 태화연_자동():
  # Microsoft Edge의 실행 파일 경로 설정 (Windows의 기본 경로)
  edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

  # URL 설정
  url = "https://www.example.com"

  # Edge 브라우저 실행
  try:
    subprocess.Popen([edge_path, "--new-window", url])
    print("Microsoft Edge가 실행되었습니다.")
    time.sleep(5)
    pag.hotkey('win','left')    
    time.sleep(5)
    pag.click(600,25)
    time.sleep(5)
  except FileNotFoundError:
    print("Microsoft Edge 실행 파일을 찾을 수 없습니다. 경로를 확인하세요.")
  except Exception as e:
    print(f"오류 발생: {e}")  

  # Microsoft Edge의 실행 파일 경로 설정 (Windows의 기본 경로)
  edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

  # URL 설정
  url = "https://www.example.com"

  # Edge 브라우저 실행
  try:
    subprocess.Popen([edge_path, "--new-window", url])
    print("Microsoft Edge가 실행되었습니다.")
    time.sleep(5)
    pag.hotkey('win','right')
    time.sleep(5)
    중구_자동입력()  
  except FileNotFoundError:
    print("Microsoft Edge 실행 파일을 찾을 수 없습니다. 경로를 확인하세요.")
  except Exception as e:
    print(f"오류 발생: {e}")  


def schedule_job():    
  schedule.every().day.at("08:40:00").do(태화연_자동) 
  schedule.every().day.at("21:40:00").do(태화연_자동) 
  while True:
    schedule.run_pending()

schedule_job()