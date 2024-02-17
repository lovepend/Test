from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui as pag
import pyperclip
import keyboard
import random
import time
import schedule
from kakao_01_api import *


global schedule_i
schedule_i = 0

#아이디 입력
#▶▶▶▶▶▶▶▶▶
schedule_id = "pend"
schedule_pw = "*Zoavld4fkd" 


#날짜 입력
#▶▶▶▶▶▶▶▶▶
#3월 29일   / schedule_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[1]/table/tbody/tr/td[6]'
#3월 30일   / schedule_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[1]/table/tbody/tr/td[7]'
#3월 31일   / schedule_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[6]/div[1]/table/tbody/tr/td[1]'
schedule_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[1]/table/tbody/tr/td[7]' #30일 토

#오토사이트 입력
#▶▶▶▶▶▶▶▶▶
schedule_site = 1   # 0이면 그냥 1이면 오토사이트만 특정 / 오토사이트만

#시간 
tm = time.localtime()
schedule_start_time = 59
schedule_end_time = 35
#캠핑장 입력
#▶▶▶▶▶▶▶▶▶                           
#//*[@id="divAjaxTable"]/input[1] 작괘
#//*[@id="divAjaxTable"]/input[2] 등억
#//*[@id="divAjaxTable"]/input[3] 달빛
schedule_camp = '//*[@id="divAjaxTable"]/input[3]'

#검색범위 입력 
#▶▶▶▶▶▶▶▶▶ 
schedule_select = 1 # (1 : 첫번째 / 2 : 두번째  / 3 :  세번째)

#달력 입력 
#▶▶▶▶▶▶▶▶▶ 
schedule_month = 2 #  (1 : 첫째달 / 2 : 다음달)



def schedule_start():
  # Chrome 웹 드라이버 생성
  global driver
  driver = webdriver.Chrome()
  #크롬 사이즈 변경
  #driver.set_window_size(1920, 1080) 
  driver.maximize_window()
  driver.get("https://camping.ulju.ulsan.kr/")
  time.sleep(0.2)
  pag.keyDown('ctrl')
  j: int = 1
  for j in range(4):
      pag.press('-')
      time.sleep(0.05)
  #크롬 브라우저 꺼짐 방지
  #웹 페이지로 이동
  #driver.execute_script("document.body.style.zoom='zoom %'")
  #웹 페이지에서 작업 수행
  #예: 웹 페이지의 요소를 찾아 클릭하거나 데이터를 입력할 수 있음

  ###########################로그인 클릭
  print('로그인')
  button = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/ul/li[1]/a')
  # 버튼 클릭
  button.click()
  time.sleep(0.2)

  ###########################로그인 클릭 1
  print('로그인 클릭')
  button = driver.find_element(By.XPATH, '//*[@id="login_ulsan"]/img')
  # 버튼 클릭
  button.click()
  time.sleep(0.5)

  ###########################로그인 ID입력
  print('로그인 ID')
  button = driver.find_element(By.XPATH, '//*[@id="loginfrm"]/fieldset/label/span/input')
  # 버튼 클릭
  button.click()
  pyperclip.copy(schedule_id)
  time.sleep(0.5)
  pag.hotkey('ctrl','v')

  ###########################로그인 PW입력
  print('로그인 PW')
  button = driver.find_element(By.XPATH, '//*[@id="password"]')
  # 버튼 클릭
  button.click()
  pyperclip.copy(schedule_pw)
  time.sleep(0.5)
  pag.hotkey('ctrl','v')

  ###########################로그인 클릭
  print('로그인 접속')
  button = driver.find_element(By.XPATH, '//*[@id="loginfrm"]/div/input')
  # 버튼 클릭
  button.click()
  time.sleep(0.5)
  온라인예약()
  
def 온라인예약():
  print('온라인 예약')
  try:
    ###########################온라인 예약 클릭
    button = driver.find_element(By.XPATH, '//*[@id="main_menu"]/li[4]/a')
    # 버튼 클릭
    button.click()
    time.sleep(3)
    달력클릭()
  except:
    온라인예약()

def 달력클릭():
  print('달력 클릭')
  try:
    ###########################달력 클릭
    if schedule_month == 2 :
      button = driver.find_element(By.XPATH, '//*[@id="calendar"]/div[1]/div[2]/button/span')
      # 버튼 클릭
      button.click()
      time.sleep(3)
      날짜클릭()
    else :
      날짜클릭()
  except:
    달력클릭()

def 날짜클릭():
  print('날짜 클릭')
  try:
    ###########################날짜 예약 클릭
    button = driver.find_element(By.XPATH, schedule_date)
    # 버튼 클릭
    button.click()
    time.sleep(10)
    사이트클릭()
  except:
    날짜클릭()

def 사이트클릭():
  print('사이트 클릭')
  try:
    if schedule_site == 1 :
      ###########################사이트종류 오토 클릭
      button = driver.find_element(By.XPATH, '//*[@id="priceCode"]')
      # 버튼 클릭
      button.click()
      time.sleep(0.5)
      pag.hotkey('down')
      time.sleep(0.5)
      pag.hotkey('enter')
      time.sleep(2)
      캠핑장클릭()
    else:
      캠핑장클릭()    
  except:
    사이트클릭()

def 캠핑장클릭():
  print('캠핑장 클릭')
  try:
    ###########################캠핑장 선택
    button = driver.find_element(By.XPATH, schedule_camp)
    # 버튼 클릭
    button.click()
    time.sleep(10)
    예약가능()
  except:
    캠핑장클릭()

def 예약가능():
  print('예약가능')
  try:
    if schedule_select == 2 or schedule_select == 3 :
      # ###########################예약가능 사이트만 보기 클릭
      button = driver.find_element(By.XPATH, '//*[@id="divAjaxTable"]/div/label')
      # 버튼 클릭
      button.click()
      time.sleep(0.2)
      예약하기()
    else : 
      예약하기()
  except:
    예약가능()

def 예약하기():
  print('예약하기')
  while True:
    global schedule_start_time
    tm = time.localtime()
    if keyboard.is_pressed("F2"):
      print("종료") 
      break  
    if (tm.tm_min == schedule_start_time ) : #9시 56분 및 15시 56분 시작
      예약하기1()


def 예약하기1():
  try:
    while True:    
      ###########################날짜 예약 클릭
      button = driver.find_element(By.XPATH, schedule_date)
      # 버튼 클릭
      button.click()
      time.sleep(0.1)
      try:
        if schedule_select == 1 :
          ###########################예약신청 클릭                            *맨처음 [1] 두번째[2] 
          button = driver.find_element(By.XPATH, '//*[@id="tableSite"]/tbody/tr[*]/td[*]/button')
        if schedule_select == 2 :
          button = driver.find_element(By.XPATH, '//*[@id="tableSite"]/tbody/tr[2]/td[*]/button')
        if schedule_select == 3 :
          button = driver.find_element(By.XPATH, '//*[@id="tableSite"]/tbody/tr[3]/td[*]/button')
        # 버튼 클릭
        button.click()
        time.sleep(0.4)
        ###########################예약신청 클릭
        print('예약신청 클릭')
        button = driver.find_element(By.XPATH, '//*[@id="resModal"]/div[2]/div/div[3]/button[2]')
        # 버튼 클릭
        button.click()
        time.sleep(0.2)
        print('예약신청 클릭')
        ###########################예약신청 클릭
        button = driver.find_element(By.XPATH, '//*[@id="resModal"]/div[2]/div/div[3]/button[2]')
        # 버튼 클릭
        button.click()
        refresh_token()
        kakao_message_you(schedule_id) 
        time.sleep(60)
      except:
        예약하기1()
  except:
      예약하기1()

# def 예약하기():
#   print('예약하기')
#   while True:
#     global schedule_i
#     print(schedule_i)
#     global schedule_start_time
#     tm = time.localtime()
#     if keyboard.is_pressed("F2"):
#       print("종료") 
#       break  
#     예약하기1()
#     if (schedule_i ==  0 and tm.tm_min == schedule_start_time): #9시 56분 및 15시 56분 시작
#       print("스캔시작")
#       예약하기1()
#     if (schedule_i >=  1): 
#       예약하기1()        
#     #if (크롤링_실시간 == 1) :
#     #   예약하기1()


# def 예약하기1():
#   global schedule_i
#   schedule_i = schedule_i + 1
#   print(schedule_i)
#   print("예약하기1")
#   try:
#     while True: 
#       ###########################날짜 예약 클릭
#       button = driver.find_element(By.XPATH, schedule_date)
#       # 버튼 클릭
#       button.click()
#       time.sleep(0.1)
#       tm = time.localtime()
#       if (tm.tm_min == schedule_end_time ) : #9시 56분 및 15시 56분 시작
#         driver.quit()
#         break       
#       try:
#         if (tm.tm_min == schedule_end_time ) : #9시 56분 및 15시 56분 시작
#           driver.quit()
#           break
#         if schedule_select == 1 :
#           print("1")
#           ###########################예약신청 클릭                            *맨처음 [1] 두번째[2] 
#           button = driver.find_element(By.XPATH, '//*[@id="tableSite"]/tbody/tr[*]/td[*]/button')
#         if schedule_select == 2 :
#           print("2")
#           button = driver.find_element(By.XPATH, '//*[@id="tableSite"]/tbody/tr[2]/td[*]/button')
#         if schedule_select == 3 :
#           print("3")
#           button = driver.find_element(By.XPATH, '//*[@id="tableSite"]/tbody/tr[3]/td[*]/button')
#         # 버튼 클릭
#         button.click()
#         time.sleep(0.4)
#         ###########################예약신청 클릭
#         print('예약신청 클릭')
#         button = driver.find_element(By.XPATH, '//*[@id="resModal"]/div[2]/div/div[3]/button[2]')
#         # 버튼 클릭
#         button.click()
#         time.sleep(0.2)
#         print('예약신청 클릭')
#         ###########################예약신청 클릭
#         button = driver.find_element(By.XPATH, '//*[@id="resModal"]/div[2]/div/div[3]/button[2]')
#         # 버튼 클릭
#         button.click()
#         refresh_token()
#         kakao_message_you(schedule_id) 
#         time.sleep(60)
#       except:
#         print("except1")
#         tm = time.localtime()
#         if (tm.tm_min == schedule_end_time ) : #9시 56분 및 15시 56분 시작
#           driver.quit()
#           break   
#         예약하기1()
#   except:
#     driver.quit()
#     print("except2")
#     schedule_start()


