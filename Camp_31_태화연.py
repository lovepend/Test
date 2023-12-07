from tkinter import *
from kakao_01_api import *
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

#차량번호 입력
#▶▶▶▶▶▶▶▶▶
global 중구_Car_No
중구_Car_No = "62소9403"

def 중구_차량번호_입력(차량번호):
  global 중구_Car_No
  중구_Car_No = 차량번호

#범위입력
#▶▶▶▶▶▶▶▶▶
global 태화연_find_rangeA
태화연_find_rangeA = 0,0,960,1080
global 태화연_find_rangeB
태화연_find_rangeB = 960,0,1920,1080

#아이디입력
#▶▶▶▶▶▶▶▶▶
global 태화연_id
태화연_id = "lovepend@nate.com"
global 태화연_pw
태화연_pw = "*Zoavld4fkd" 

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
  태화연_id = "parkmc7@naver.com"
  print(태화연_id)

def 태화연_Log_Guest():
  global 태화연_id
  태화연_id = "jhrep2234@nate.com"
  time.sleep(1)
  global 태화연_pw
  태화연_pw = "*Zoavld4fkd"
  print(태화연_id)
  print(태화연_pw)

#날짜입력
#▶▶▶▶▶▶▶▶▶
global 태화연_day1
태화연_day1 = 205,128
global 태화연_day3
태화연_day3 = 1163,128

def 태화연_Day():
  while True:
    if keyboard.is_pressed("F2"): 
      time.sleep(0.2)
      global 태화연_day1 
      #태화연_day1  = pag.position()
      태화연_day1 = 200,130
      print(태화연_day1)
      break        
  while True:
    if keyboard.is_pressed("F2"): 
      time.sleep(0.2)
      global 태화연_day2
      태화연_day2  = pag.position()
      print(태화연_day2)
      break    
  while True:
    if keyboard.is_pressed("F2"): 
      time.sleep(0.2)
      global 태화연_day3 
      #태화연_day3  = pag.position()
      태화연_day3 = 1167,130
      print(태화연_day3)
      break        
  while True:
    if keyboard.is_pressed("F2"): 
      time.sleep(0.2)
      global 태화연_day4
      태화연_day4  = pag.position()
      print(태화연_day4)
      break  

def 태화연_Day11():
  global 태화연_day2
  태화연_day2 = 297,192
  print(태화연_day2)
  global 태화연_day4
  태화연_day4 = 1257,192
  print(태화연_day4)

def 태화연_Day12():
  global 태화연_day2
  태화연_day2 = 319,192
  print(태화연_day2)
  global 태화연_day4
  태화연_day4 = 1280,192
  print(태화연_day4)

def 태화연_Day21():
  global 태화연_day2
  태화연_day2 = 297,206
  print(태화연_day2)
  global 태화연_day4
  태화연_day4 = 1257,206
  print(태화연_day4)

def 태화연_Day22():
  global 태화연_day2
  태화연_day2 = 319,206
  print(태화연_day2)
  global 태화연_day4
  태화연_day4 = 1280,206
  print(태화연_day4)

def 태화연_Day31():
  global 태화연_day2
  태화연_day2 = 297,222
  print(태화연_day2)
  global 태화연_day4
  태화연_day4 = 1257,222
  print(태화연_day4)

def 태화연_Day32():
  global 태화연_day2
  태화연_day2 = 319,222
  print(태화연_day2)
  global 태화연_day4
  태화연_day4 = 1280,222
  print(태화연_day4)

def 태화연_Day41():
  global 태화연_day2
  태화연_day2 = 297,238
  print(태화연_day2)
  global 태화연_day4
  태화연_day4 = 1257,238
  print(태화연_day4)

def 태화연_Day42():
  global 태화연_day2
  태화연_day2 = 319,238
  print(태화연_day2)
  global 태화연_day4
  태화연_day4 = 1280,238
  print(태화연_day4)

#범위입력
#▶▶▶▶▶▶▶▶▶
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
  global 태화연_find_rangeA
  태화연_find_rangeA = (0,태화연_find_range1.y,960,태화연_find_range2.y)
  while True:
    if keyboard.is_pressed("F2"): 
      global 태화연_find_range3 
      태화연_find_range3  = pag.position()
      print(태화연_find_range3)
      time.sleep(0.5)
      break  
  while True:
    if keyboard.is_pressed("F2"): 
      global 태화연_find_range4 
      태화연_find_range4  = pag.position()
      print(태화연_find_range4)
      time.sleep(0.5)
      break  
  global 태화연_find_rangeB
  태화연_find_rangeB = (960,태화연_find_range3.y,1920,태화연_find_range4.y)

def 태화연_호수뷰():
  global 태화연_find_rangeA
  태화연_find_rangeA = 0,0,960,362
  global 태화연_find_rangeB
  태화연_find_rangeB = 960,0,1920,362

def 태화연_2_3층():
  global 태화연_find_rangeA
  태화연_find_rangeA = 0,362,960,1080
  global 태화연_find_rangeB
  태화연_find_rangeB = 960,362,1920,1080

#장소입력
#▶▶▶▶▶▶▶▶▶
global 중구_장소
중구_장소 = 677,341

def 중구_태화연():
  global 중구_url
  중구_url = 'https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=1030300'
  print(중구_url)

def 중구_황방산():
  global 중구_url
  중구_url = 'https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=1020300'
  print(중구_url)

def 중구_별뜨락():
  global 중구_url
  중구_url = 'https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=2010400'
  print(중구_url)

def 중구_입화산():
  global 중구_url
  중구_url = 'https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=2030300'
  print(중구_url)

#함수 설정
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★

#자동입력(로그인)
#▶▶▶▶▶▶▶▶▶
def 중구_자동입력():
  #webbrowser.get("windows-default").open('https://www.junggu.ulsan.kr/camping')  
  time.sleep(1)
  #url 클릭
  pag.click(300,60)
  time.sleep(0.2)
  pag.hotkey('ctrl','a')
  #로그인페이지 이동 
  pyperclip.copy('https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=5010000')
  time.sleep(0.2)
  pyperclip.copy('https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=5010000')
  time.sleep(0.2)
  pag.hotkey('ctrl','v')
  time.sleep(0.2)
  pag.hotkey('enter')
  time.sleep(5)
  #ID입력
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pyperclip.copy(태화연_id)
  time.sleep(0.2)
  pyperclip.copy(태화연_id)
  time.sleep(1)
  pag.hotkey('ctrl','v')
  pag.click(655,350)
  time.sleep(1)
  #PW입력
  pag.click(493,370)
  time.sleep(1)
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pag.hotkey('ctrl','a')
  time.sleep(1)
  pyperclip.copy(태화연_pw)
  time.sleep(0.2)
  pyperclip.copy(태화연_pw)
  time.sleep(1)
  pag.hotkey('ctrl','v')
  #로그인
  time.sleep(0.5)
  pag.hotkey('enter')
  time.sleep(5)
  중구예약_A()

#자동입력(A화면셋팅)
#▶▶▶▶▶▶▶▶▶
def 중구예약_A():
  #######################첫번째##########################
  #url 클릭
  pag.click(300,60)
  time.sleep(0.2)
  pag.hotkey('ctrl','a')
  #장소 url 이동 
  pyperclip.copy(중구_url)
  time.sleep(0.2)
  pyperclip.copy(중구_url)
  time.sleep(0.5)
  pag.hotkey('ctrl','v')
  time.sleep(0.2)
  pag.hotkey('enter')
  time.sleep(5)
  #차량넘버 입력
  global 중구_Car_No
  print("3")  
  button = pag.locateCenterOnScreen("./image/31. Junggu/11. input.png", region=(0,0,960,1080) , confidence=0.8)
  print("4")  
  print(button)
  time.sleep(2)
  pag.click(button.x,button.y, button='left', clicks=2, interval=0.1)
  time.sleep(2)
  pyperclip.copy(중구_Car_No)
  pag.hotkey('ctrl','v')
  time.sleep(2)
  #이용준수사항
  button = pag.locateCenterOnScreen("./image/31. Junggu/12. input.png", region=(0,0,960,1080) , confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
  time.sleep(1)
  #페이지 클릭
  pag.click(10,800)
  time.sleep(2)
  pag.hotkey('end')
  time.sleep(3)
  #입실정원준수안내
  button = pag.locateCenterOnScreen("./image/31. Junggu/13. input.png", region=(0,0,960,1080) , confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
  time.sleep(1)  
  #취소 및 환불규정
  button = pag.locateCenterOnScreen("./image/31. Junggu/14. input.png", region=(0,0,960,1080) , confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
  time.sleep(1)  
  #재난상황별 지침
  button = pag.locateCenterOnScreen("./image/31. Junggu/14_1. input.png", region=(0,0,960,1080) , confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
  time.sleep(1)  
  #개인정보 수집 
  button = pag.locateCenterOnScreen("./image/31. Junggu/15. input.png", region=(0,0,960,1080) , confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
  time.sleep(1)  
  #페이지 클릭
  pag.click(10,800)
  time.sleep(1)
  #페이지 위로
  pag.hotkey("home")
  time.sleep(1)
  #날짜 맞추기
  pag.hotkey('down')
  time.sleep(1)
  pag.hotkey('down')
  time.sleep(1)
  pag.hotkey('down')
  time.sleep(1)
  중구예약_B()

#자동입력(B화면셋팅)
#▶▶▶▶▶▶▶▶▶
def 중구예약_B():
  #######################두번째##########################
  #url 클릭
  time.sleep(1)
  pag.click(1300,60)
  time.sleep(0.2)
  pag.hotkey('ctrl','a')
  #장소 url 이동 
  pyperclip.copy(중구_url)
  time.sleep(0.2)
  pyperclip.copy(중구_url)
  time.sleep(0.5)
  pag.hotkey('ctrl','v')
  time.sleep(0.2)
  pag.hotkey('enter')
  time.sleep(5)
  #차량넘버 입력
  global 중구_Car_No
  print("3")  
  button = pag.locateCenterOnScreen("./image/31. Junggu/11. input.png", region=(960,0,1920,1080) , confidence=0.8)
  print("4")  
  print(button)
  time.sleep(2)
  pag.click(button.x,button.y, button='left', clicks=2, interval=0.1)
  time.sleep(2)
  pyperclip.copy(중구_Car_No)
  pag.hotkey('ctrl','v')
  time.sleep(2)
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
  time.sleep(3)
  #입실정원준수안내
  button = pag.locateCenterOnScreen("./image/31. Junggu/13. input.png", region=(960,0,1920,1080) , confidence=0.9)
  print(button)
  time.sleep(1)
  pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
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
  time.sleep(1)
  #날짜 맞추기
  pag.hotkey('down')
  time.sleep(1)
  pag.hotkey('down')
  time.sleep(1)
  pag.hotkey('down')
  time.sleep(1)
  global 태화연_day1
  global 태화연_day3
  time.sleep(3)
  pag.click(태화연_day1)
  time.sleep(1)
  pag.click(태화연_day2)
  time.sleep(3)
  pag.click(태화연_day3)
  time.sleep(1)
  pag.click(태화연_day4)


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
  #달력 A화면 클릭 
  # time.sleep(1)
  # pag.click(태화연_day1)
  # time.sleep(1)
  # pag.hotkey('enter')
  # #달력 B화면 클릭
  # pag.click(태화연_day3)
  # time.sleep(0.2)
  # pag.hotkey('enter')     
  # time.sleep(1)
  태화연_Start_검색()  
  

#메인함수(검색)
#▶▶▶▶▶▶▶▶▶
def 태화연_Start_검색():
  while True:
    #종료 조건
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      print("F2 종료")
      time.sleep(60)
      break
    #검색
    태화연_검색A()
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      print("F2 종료")
      time.sleep(60)
      break
    태화연_검색B()

#메인함수(A화면 검색)
#▶▶▶▶▶▶▶▶▶
def 태화연_검색A():
  try :
    print("태화연_검색A")
    button = pag.locateCenterOnScreen("./image/31. Junggu/21. reservation.png", region=태화연_find_rangeA ,confidence=0.8) 
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
    button = pag.locateCenterOnScreen("./image/31. Junggu/21. reservation.png", region=태화연_find_rangeB ,confidence=0.8) 
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
    button = pag.locateCenterOnScreen("./image/31. Junggu/22. reservation.png", region=태화연_find_rangeA ,confidence=0.9) 
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
    button = pag.locateCenterOnScreen("./image/31. Junggu/22. reservation.png", region=태화연_find_rangeB ,confidence=0.9) 
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
    #로그아웃
    pag.click(1455,138)
    time.sleep(5)
    #접속 
    pag.click(476,84)
    time.sleep(5)
    pag.click(536,152)
    time.sleep(5)
  
    태화연_Start()






# #백업
# #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
# #★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★



# #태화연 Test 2022.11.10 #Viewer Size 50%

# ################################## 차량번호
# global 중구_Car_No
# 중구_Car_No = "62소9403"


# def 중구_차량번호_입력(차량번호):
#   global 중구_Car_No
#   중구_Car_No = 차량번호
# ################################## 리셋 
# global 태화연_end_command
# 태화연_end_command = 0

# global 태화연_end_command1
# 태화연_end_command1 = 0
# ################################## 범위 
# global 태화연_find_rangeA
# 태화연_find_rangeA = 0,0,960,1080
# global 태화연_find_rangeB
# 태화연_find_rangeB = 960,0,1920,1080
# ################################## 아이디
# global 태화연_id
# 태화연_id = "lovepend@nate.com"
# global 태화연_pw
# 태화연_pw = "*Zoavld4fkd" 


# ################################## 횟수 
# global 태화연_i
# 태화연_i = 0
    
# #★★★★★★★★★★★★★★★★★★★ 리셋 입력
# def 태화연_Reset():
#     global 태화연_end_command
#     태화연_end_command = 0
#     global 태화연_end_command1
#     태화연_end_command1 = 0

# def 태화연_End():
#     global 태화연_end_command1
#     태화연_end_command1 = 1
    
# #★★★★★★★★★★★★★★★★★★★ 아이디 입력
# def 태화연_Log_Id1():
#     global 태화연_id
#     태화연_id = "lovepend@nate.com"
#     print(태화연_id)

# def 태화연_Log_Id2():
#     global 태화연_id
#     태화연_id = "lovepend@kakao.com"
#     print(태화연_id)

# def 태화연_Log_Id3():
#     global 태화연_id
#     태화연_id = "lovepend@naver.com"
#     print(태화연_id)

# def 태화연_Log_Id4():
#     global 태화연_id
#     태화연_id = "parkmc7"
#     print(태화연_id)

# def 태화연_Log_Guest():
#     global 태화연_id
#     태화연_id = "jhrep2234@nate.com"
#     time.sleep(1)
#     global 태화연_pw
#     태화연_pw = "*Zoavld4fkd"
#     print(태화연_id)
#     print(태화연_pw)

# ################################## 날짜
# global 태화연_day1
# 태화연_day1 = 205,128
# global 태화연_day3
# 태화연_day3 = 1163,128



# #★★★★★★★★★★★★★★★★★★★ 날짜 입력 (50%)
# def 태화연_Day11():
#   global 태화연_day2
#   태화연_day2 = 297,192
#   print(태화연_day2)
#   global 태화연_day4
#   태화연_day4 = 1257,192
#   print(태화연_day4)

# def 태화연_Day12():
#   global 태화연_day2
#   태화연_day2 = 319,192
#   print(태화연_day2)
#   global 태화연_day4
#   태화연_day4 = 1280,192
#   print(태화연_day4)

# def 태화연_Day21():
#   global 태화연_day2
#   태화연_day2 = 297,206
#   print(태화연_day2)
#   global 태화연_day4
#   태화연_day4 = 1257,206
#   print(태화연_day4)

# def 태화연_Day22():
#   global 태화연_day2
#   태화연_day2 = 319,206
#   print(태화연_day2)
#   global 태화연_day4
#   태화연_day4 = 1280,206
#   print(태화연_day4)

# def 태화연_Day31():
#   global 태화연_day2
#   태화연_day2 = 297,222
#   print(태화연_day2)
#   global 태화연_day4
#   태화연_day4 = 1257,222
#   print(태화연_day4)

# def 태화연_Day32():
#   global 태화연_day2
#   태화연_day2 = 319,222
#   print(태화연_day2)
#   global 태화연_day4
#   태화연_day4 = 1280,222
#   print(태화연_day4)

# def 태화연_Day41():
#   global 태화연_day2
#   태화연_day2 = 297,238
#   print(태화연_day2)
#   global 태화연_day4
#   태화연_day4 = 1257,238
#   print(태화연_day4)

# def 태화연_Day42():
#   global 태화연_day2
#   태화연_day2 = 319,238
#   print(태화연_day2)
#   global 태화연_day4
#   태화연_day4 = 1280,238
#   print(태화연_day4)

# #★★★★★★★★★★★★★★★★★★★ 날짜 입력
# def 태화연_Day():
#     while True:
#         if keyboard.is_pressed("F2"): 
#             time.sleep(0.2)
#             global 태화연_day1 
#             #태화연_day1  = pag.position()
#             태화연_day1 = 200,130
#             print(태화연_day1)
#             break        
#     while True:
#         if keyboard.is_pressed("F2"): 
#             time.sleep(0.2)
#             global 태화연_day2
#             태화연_day2  = pag.position()
#             print(태화연_day2)
#             break    
#     while True:
#         if keyboard.is_pressed("F2"): 
#             time.sleep(0.2)
#             global 태화연_day3 
#             #태화연_day3  = pag.position()
#             태화연_day3 = 1167,130
#             print(태화연_day3)
#             break        
#     while True:
#         if keyboard.is_pressed("F2"): 
#             time.sleep(0.2)
#             global 태화연_day4
#             태화연_day4  = pag.position()
#             print(태화연_day4)
#             break    

# #★★★★★★★★★★★★★★★★★★★ 범위 입력
# def 태화연_범위선택():
#     while True:
#         if keyboard.is_pressed("F2"): 
#             global 태화연_find_range1 
#             태화연_find_range1  = pag.position()
#             print(태화연_find_range1)
#             time.sleep(0.5)
#             break  
#     while True:
#         if keyboard.is_pressed("F2"): 
#             global 태화연_find_range2 
#             태화연_find_range2  = pag.position()
#             print(태화연_find_range2)
#             time.sleep(0.5)
#             break  
#     global 태화연_find_rangeA
#     태화연_find_rangeA = (0,태화연_find_range1.y,960,태화연_find_range2.y)
#     while True:
#         if keyboard.is_pressed("F2"): 
#             global 태화연_find_range3 
#             태화연_find_range3  = pag.position()
#             print(태화연_find_range3)
#             time.sleep(0.5)
#             break  
#     while True:
#         if keyboard.is_pressed("F2"): 
#             global 태화연_find_range4 
#             태화연_find_range4  = pag.position()
#             print(태화연_find_range4)
#             time.sleep(0.5)
#             break  
#     global 태화연_find_rangeB
#     태화연_find_rangeB = (960,태화연_find_range3.y,1920,태화연_find_range4.y)

# def 태화연_호수뷰():
#     global 태화연_find_rangeA
#     태화연_find_rangeA = 0,0,960,362
#     global 태화연_find_rangeB
#     태화연_find_rangeB = 960,0,1920,362

# def 태화연_2_3층():
#     global 태화연_find_rangeA
#     태화연_find_rangeA = 0,362,960,1080
#     global 태화연_find_rangeB
#     태화연_find_rangeB = 960,362,1920,1080





# #★★★★★★★★★★★★★★★★★★★ 장소선택
# global 중구_장소
# 중구_장소 = 677,341

# def 중구_태화연():
#     global 중구_url
#     중구_url = 'https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=1030300'
#     print(중구_url)

# def 중구_황방산():
#     global 중구_url
#     중구_url = 'https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=1020300'
#     print(중구_url)

# def 중구_별뜨락():
#     global 중구_url
#     중구_url = 'https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=2010400'
#     print(중구_url)

# def 중구_입화산():
#     global 중구_url
#     중구_url = 'https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=2030300'
#     print(중구_url)


# #★★★★★★★★★★★★★★★★★★★ 자동 입력
# def 중구_자동입력():
#   #webbrowser.get("windows-default").open('https://www.junggu.ulsan.kr/camping')  
#   time.sleep(1)
#   #url 클릭
#   pag.click(300,60)
#   time.sleep(0.2)
#   pag.hotkey('ctrl','a')
#   #로그인페이지 이동 
#   pyperclip.copy('https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=5010000')
#   time.sleep(0.2)
#   pyperclip.copy('https://camping.junggu.ulsan.kr/camping/pageCont.do?menuNo=5010000')
#   time.sleep(0.2)
#   pag.hotkey('ctrl','v')
#   time.sleep(0.2)
#   pag.hotkey('enter')
#   time.sleep(5)
#   #ID입력
#   pag.hotkey('ctrl','a')
#   time.sleep(1)
#   pag.hotkey('ctrl','a')
#   time.sleep(1)
#   pyperclip.copy(태화연_id)
#   time.sleep(0.2)
#   pyperclip.copy(태화연_id)
#   time.sleep(1)
#   pag.hotkey('ctrl','v')
#   pag.click(655,350)
#   time.sleep(1)
#   #PW입력
#   pag.click(493,370)
#   time.sleep(1)
#   pag.hotkey('ctrl','a')
#   time.sleep(1)
#   pag.hotkey('ctrl','a')
#   time.sleep(1)
#   pyperclip.copy(태화연_pw)
#   time.sleep(0.2)
#   pyperclip.copy(태화연_pw)
#   time.sleep(1)
#   pag.hotkey('ctrl','v')
#   #로그인
#   time.sleep(0.5)
#   pag.click(479,406)
#   중구예약_A()

# def 중구예약_A():
#   #######################첫번째##########################
#   #url 클릭
#   pag.click(300,60)
#   time.sleep(0.2)
#   pag.hotkey('ctrl','a')
#   #장소 url 이동 
#   pyperclip.copy(중구_url)
#   time.sleep(0.2)
#   pyperclip.copy(중구_url)
#   time.sleep(0.5)
#   pag.hotkey('ctrl','v')
#   time.sleep(0.2)
#   pag.hotkey('enter')
#   time.sleep(5)
#   #차량넘버 입력
#   global 중구_Car_No
#   print("3")  
#   button = pag.locateCenterOnScreen("./image/31. Junggu/11. input.png", region=(0,0,960,1080) , confidence=0.8)
#   print("4")  
#   print(button)
#   time.sleep(2)
#   pag.click(button.x,button.y, button='left', clicks=2, interval=0.1)
#   time.sleep(2)
#   pyperclip.copy(중구_Car_No)
#   pag.hotkey('ctrl','v')
#   time.sleep(2)
  
#   #이용준수사항
#   button = pag.locateCenterOnScreen("./image/31. Junggu/12. input.png", region=(0,0,960,1080) , confidence=0.9)
#   print(button)
#   time.sleep(1)
#   pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
#   time.sleep(1)
#   #페이지 클릭
#   pag.click(10,800)
#   time.sleep(2)
#   pag.hotkey('end')
#   time.sleep(3)

#   #입실정원준수안내
#   button = pag.locateCenterOnScreen("./image/31. Junggu/13. input.png", region=(0,0,960,1080) , confidence=0.9)
#   print(button)
#   time.sleep(1)
#   pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
#   time.sleep(1)  
#   #취소 및 환불규정
#   button = pag.locateCenterOnScreen("./image/31. Junggu/14. input.png", region=(0,0,960,1080) , confidence=0.9)
#   print(button)
#   time.sleep(1)
#   pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
#   time.sleep(1)  
#   #재난상황별 지침
#   button = pag.locateCenterOnScreen("./image/31. Junggu/14_1. input.png", region=(0,0,960,1080) , confidence=0.9)
#   print(button)
#   time.sleep(1)
#   pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
#   time.sleep(1)  
#   #개인정보 수집 
#   button = pag.locateCenterOnScreen("./image/31. Junggu/15. input.png", region=(0,0,960,1080) , confidence=0.9)
#   print(button)
#   time.sleep(1)
#   pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
#   time.sleep(1)  
#   #페이지 클릭
#   pag.click(10,800)
#   time.sleep(1)
#   #페이지 위로
#   pag.hotkey("home")
#   time.sleep(1)
#   #날짜 맞추기
#   pag.hotkey('down')
#   time.sleep(1)
#   pag.hotkey('down')
#   time.sleep(1)
#   pag.hotkey('down')
#   time.sleep(1)
#   # pag.moveTo(1910,187)    
#   # time.sleep(1)
#   # pag.dragTo(1910,359, 6, button='left')
#   중구예약_B()

# def 중구예약_B():
#   #######################두번째##########################
#   #url 클릭
#   time.sleep(1)
#   pag.click(1300,60)
#   time.sleep(0.2)
#   pag.hotkey('ctrl','a')
#   #장소 url 이동 
#   pyperclip.copy(중구_url)
#   time.sleep(0.2)
#   pyperclip.copy(중구_url)
#   time.sleep(0.5)
#   pag.hotkey('ctrl','v')
#   time.sleep(0.2)
#   pag.hotkey('enter')
#   time.sleep(5)
#   #차량넘버 입력
#   global 중구_Car_No
#   print("3")  
#   button = pag.locateCenterOnScreen("./image/31. Junggu/11. input.png", region=(960,0,1920,1080) , confidence=0.8)
#   print("4")  
#   print(button)
#   time.sleep(2)
#   pag.click(button.x,button.y, button='left', clicks=2, interval=0.1)
#   time.sleep(2)
#   pyperclip.copy(중구_Car_No)
#   pag.hotkey('ctrl','v')
#   time.sleep(2)
  
#   #이용준수사항
#   button = pag.locateCenterOnScreen("./image/31. Junggu/12. input.png", region=(960,0,1920,1080) , confidence=0.9)
#   print(button)
#   time.sleep(1)
#   pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
#   time.sleep(1)
#   #페이지 클릭
#   pag.click(1850,800)
#   time.sleep(2)
#   pag.hotkey('end')
#   time.sleep(3)

#   #입실정원준수안내
#   button = pag.locateCenterOnScreen("./image/31. Junggu/13. input.png", region=(960,0,1920,1080) , confidence=0.9)
#   print(button)
#   time.sleep(1)
#   pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
#   time.sleep(1)  
#   #취소 및 환불규정
#   button = pag.locateCenterOnScreen("./image/31. Junggu/14. input.png", region=(960,0,1920,1080) , confidence=0.9)
#   print(button)
#   time.sleep(1)
#   pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
#   time.sleep(1)  
#   #재난상황별 지침
#   button = pag.locateCenterOnScreen("./image/31. Junggu/14_1. input.png", region=(960,0,1920,1080) , confidence=0.9)
#   print(button)
#   time.sleep(1)
#   pag.click(button.x,button.y+130, button='left', clicks=1, interval=0.1)
#   time.sleep(1)  
#   #개인정보 수집 
#   button = pag.locateCenterOnScreen("./image/31. Junggu/15. input.png", region=(960,0,1920,1080) , confidence=0.9)
#   print(button)
#   time.sleep(1)
#   pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
#   time.sleep(1)  
#   #페이지 클릭
#   pag.click(1850,800)
#   time.sleep(1)
#   #페이지 위로
#   pag.hotkey("home")
#   time.sleep(1)
#   #날짜 맞추기
#   pag.hotkey('down')
#   time.sleep(1)
#   pag.hotkey('down')
#   time.sleep(1)
#   pag.hotkey('down')
#   time.sleep(1)
#   global 태화연_day1
#   global 태화연_day3
#   time.sleep(3)
#   pag.click(태화연_day1)
#   time.sleep(1)
#   pag.click(태화연_day2)
#   time.sleep(3)
#   pag.click(태화연_day3)
#   time.sleep(1)
#   pag.click(태화연_day4)
#   # pag.moveTo(1910,187)    
#   # time.sleep(1)
#   # pag.dragTo(1910,359, 6, button='left')
#   #태화연_Start()

# #★★★★★★★★★★★★★★★★★★★ 메인 함수
# def 태화연_Start():
#   #달력 A클릭 
#   time.sleep(1)
#   pag.click(태화연_day1)
#   time.sleep(0.2)
#   pag.hotkey('enter')
#   pag.click(태화연_day3)
#   time.sleep(0.2)
#   pag.hotkey('enter')     
#   time.sleep(0.1)
#   태화연_Start1()  


# def 태화연_JubJub():
#   pag.click(태화연_day1)
#   time.sleep(0.2) 
#   pag.click(797,142)
#   태화연_Start1()   


# # 메인 
# def 태화연_Start1():
#   while True:
#     #종료 조건
#     if keyboard.is_pressed("F2"): # F2 누른게 감지되면
#       print("F2 종료")
#       time.sleep(60)
#       break
#     #검색
#     태화연_검색A()
#     if keyboard.is_pressed("F2"): # F2 누른게 감지되면
#       print("F2 종료")
#       time.sleep(60)
#       break
#     태화연_검색B()

# def 태화연_Start2():
#   while True:
#     global 태화연_i
#     tm = time.localtime()
#     #날짜 클릭
#     pag.click(태화연_day2)
#     time.sleep(0.1)
#     pag.click(10,500)
#     #횟수 표현
#     태화연_i = 태화연_i + 1
#     #종료 조건
#     if keyboard.is_pressed("F2"): # F2 누른게 감지되면
#         print("F2 종료")
#         break
#     if (tm.tm_hour == 11 and tm.tm_min == 5) or (tm.tm_hour == 19 and tm.tm_min == 5) : #9시 50분 및 16시 50분 종료
#         print("minute 중지")
#         print(tm.tm_hour ,"시", tm.tm_min ,"분", tm.tm_sec,"초")
#         break        
#     #날짜 클릭
#     pag.click(태화연_day1)
#     time.sleep(0.1)
#     #검색
#     태화연_검색A()

# def 태화연_검색A():
#   print("검색A")
#   button = pag.locateCenterOnScreen("./image/31. Junggu/21. reservation.png", region=태화연_find_rangeA ,confidence=0.8) 
#   if (button == None) :
#     #태화연A_검색()
#     None     
#   else :
#     #pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
#     태화연_StepA_A()

# def 태화연_검색B():
#   print("검색B")
#   button = pag.locateCenterOnScreen("./image/31. Junggu/21. reservation.png", region=태화연_find_rangeB ,confidence=0.8) 
#   if (button == None) :
#     #태화연B_검색()
#     None     
#   else :
#     #pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
#     태화연_StepA_B()



# #예약하기 클릭 A
# def 태화연_StepA_A():
#   print("태화연_StepA")
#   button = pag.locateCenterOnScreen("./image/31. Junggu/22. reservation.png", region=태화연_find_rangeA ,confidence=0.9) 
#   print(button)
#   if (button == None) :
#     pag.click(태화연_day1)
#     time.sleep(0.1)
#     pag.hotkey('enter')     
#     time.sleep(0.1)
#     None     
#   else :
#     pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
#     태화연_StepB_A()

# #예약하기 클릭 B    
# def 태화연_StepA_B():
#   print("태화연_StepB")
#   button = pag.locateCenterOnScreen("./image/31. Junggu/22. reservation.png", region=태화연_find_rangeB ,confidence=0.9) 
#   print(button)
#   if (button == None) :
#     pag.click(태화연_day3)
#     time.sleep(0.1)
#     pag.hotkey('enter')     
#     time.sleep(0.1)
#     None     
#   else :
#     pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
#     태화연_StepB_A()


# #체크 확인 A
# def 태화연_StepB_A():
#   global button1
#   button1 = pag.locateCenterOnScreen("./image/31. Junggu/23. check.png", confidence=0.7) 
#   if (button1 == None) :
#     태화연_StepB_A()
#   else :    
#     time.sleep(0.1)
#     pag.hotkey('enter')
#     time.sleep(0.5)
#     button1_1 = pag.locateCenterOnScreen("./image/31. Junggu/90. Reject.png", confidence=0.7) 
#     time.sleep(0.1)
#     if (button1_1 == None) :
#       태화연_StepC()
#     else :
#       pag.hotkey('enter')
#       time.sleep(0.2)
#       pag.hotkey('enter')
#       time.sleep(0.2)
#       태화연_Start()
#       #pag.click(button1.x,button1.y, button='left', clicks=1, interval=0.1)
#       #print(button1)
#       #time.sleep(0.1) 
#       #pag.hotkey('enter', clicks=50, interval=0.1)
#       #time.sleep(0.1)
#       #pag.click(1800,800)#추가
#       #time.sleep(0.5)#추가
#       #pag.hotkey('pagedown')#추가
#     #태화연_StepC()




# #체크 확인 B
# def 태화연_StepC() : 
#   button2 = pag.locateCenterOnScreen('./image/31. Junggu/24. next.png', confidence=0.8)   
#   print(button2)
#   if (button2 == None) :
#     태화연_StepC()      
#   else : 
#     # i = 0
#     # while i < 1:
#     #     i = i +1
#     #     pag.hotkey('down')

#     #     if i == 1 :
#     #       break
#     pag.hotkey('down')
#     time.sleep(0.1)
#     pag.click(button2.x-270 ,button2.y)
#     #pag.click(1800,800)
#     time.sleep(0.2)
#     pag.hotkey('end')
#     time.sleep(0.4)
#     태화연_StepD()
#     # button3 = pag.locateCenterOnScreen('./image/31. Junggu/25. next.png', confidence=0.9)  
#     # time.sleep(0.2) 
#     # pag.click(button3.x,button3.y, button='left', clicks=1, interval=0.1)
#     # print('button3')
#     # print(button3)
#     # # refresh_token()
#     # # kakao_message_you("태화연")
#     # time.sleep(5000)


# def 태화연_StepD() : 
#   button3 = pag.locateCenterOnScreen('./image/31. Junggu/25. next.png', confidence=0.9)  
#   print(button3)
#   if (button3 == None) :
#     태화연_StepD()      
#   else : 
#     # i = 0
#     # while i < 1:
#     #     i = i +1
#     #     pag.hotkey('down')

#     #     if i == 1 :
#     #       break
#     # pag.hotkey('down')
#     # time.sleep(0.1)
#     # pag.click(1800,800)
#     # time.sleep(0.2)
#     # pag.hotkey('end')
#     # time.sleep(0.3)
#     # button3 = pag.locateCenterOnScreen('./image/31. Junggu/25. next.png', confidence=0.9)  
#     # time.sleep(0.2) 
#     pag.click(button3.x,button3.y, button='left', clicks=1, interval=0.1)
#     print('button3')
#     print(button3)
#     time.sleep(0.1)
#     pag.hotkey('enter')
#     time.sleep(0.1)
#     pag.hotkey('enter')
#     time.sleep(0.1)
#     refresh_token()
#     kakao_message_you("태화연")
#     time.sleep(500)





# #★★★★★★★★★★★★★★★★★★★ 서브 함수
# def 태화연_job1():
#     while True:
#         pag.hotkey('enter')
#         time.sleep(0.05)
#         if keyboard.is_pressed("F2") : # F2 누른게 감지되면
#             print("중지")
#             break

# #★★★★★★★★★★★★★★★★★★★ 스케쥴러
# def 태화연_자동():
#     time.sleep(5)
#     #페이지 클릭
#     pag.click(1800,800)
#     time.sleep(5)
#     #페이지 클릭
#     pag.click(1800,800)
#     time.sleep(5)
#     #로그인
#     pag.click(476,84)
#     time.sleep(5)
#     pag.click(536,152)
#     time.sleep(5)
#     태화연_Reset()
#     #로그아웃
#     pag.click(1455,138)
#     time.sleep(5)
#     #접속 
#     pag.click(476,84)
#     time.sleep(5)
#     pag.click(536,152)
#     time.sleep(5)
  
#     태화연_Start()