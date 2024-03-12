from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui as pag
import pyperclip
import keyboard
import random
import time

#시간 
global tm
tm = time.localtime()
refresh_time_click = 1
refresh_time_page = 1

#아이디 입력
#▶▶▶▶▶▶▶▶▶
global Sinbul_id
Sinbul_id = "pend"
global Sinbul_pw
Sinbul_pw = "*Zoavld4fkd" 
global Sinbul_date
Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[1]/table/tbody/tr/td[7]'
global Sinbul_live
Sinbul_live = 1 #1이 시간 / 2가 실시간
global Sinbul_mon
Sinbul_mon = 1 #1이 첫번째달 / 2가 둘쨋달
global Sinbul_camp
Sinbul_camp = '//*[@id="divAjaxTable"]/input[3]'
global 오토캠핑장 # 1이 오토캠핑장 셋팅 / 2가 오토캠핑장 해제
오토캠핑장 = 2
global 예약가능 # 1이 예약가능 사이트만 보기 셋팅 / 2가 예약가능 사이트만 보기 해제
예약가능 = 2
global Sinbul_time_min_tr, Sinbul_time_sec_tr #시간설정
Sinbul_time_min_tr = int(59)
Sinbul_time_sec_tr = int(30)
global 새로고침 # 1이 원클릭 / 2가 연타
새로고침 = 1




def Sinbul_Log_Id1():
  global Sinbul_id
  Sinbul_id = "pend"
  print(Sinbul_id)

def Sinbul_Log_Id2():
  global Sinbul_id
  Sinbul_id = "lovepend2"
  print(Sinbul_id)

def Sinbul_Log_Id3():
  global Sinbul_id
  Sinbul_id = "lovepend1"
  print(Sinbul_id)

def Sinbul_Log_Id4():
  global Sinbul_id
  Sinbul_id = "parkmc7"
  print(Sinbul_id)

# def Sinbul_Log_Id5():
#   global Sinbul_id
#   Sinbul_id = "jhrep1201"
#   global Sinbul_pw
#   Sinbul_pw = "j1902217**"
#   print(Sinbul_id, Sinbul_pw)

def Sinbul_Log_Id5():
  global Sinbul_id
  Sinbul_id = "allstar5"
  global Sinbul_pw
  Sinbul_pw = "hanamju1214!"
  print(Sinbul_id, Sinbul_pw)

def Sinbul_Day11():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[1]/table/tbody/tr/td[6]'
  print('1F')

def Sinbul_Day12():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[1]/table/tbody/tr/td[7]'
  print('1S')

def Sinbul_Day21():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[1]/table/tbody/tr/td[6]'
  print('2F')

def Sinbul_Day22():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[1]/table/tbody/tr/td[7]'
  print('2S')

def Sinbul_Day31():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/div[1]/table/tbody/tr/td[6]'
  print('3F')

def Sinbul_Day32():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/div[1]/table/tbody/tr/td[7]'
  print('3S')

def Sinbul_Day41():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[6]'
  print('4F')

def Sinbul_Day42():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[7]'
  print('4S')

def Sinbul_Day51():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[1]/table/tbody/tr/td[6]'
  print('5F')

def Sinbul_Day52():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[1]/table/tbody/tr/td[7]'
  print('5S')

def Sinbul_Day53():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[6]/div[1]/table/tbody/tr/td[1]'
  print('6S')
  
#캠핑장 입력
#▶▶▶▶▶▶▶▶▶                           
def Sinbul_작괘():
  global Sinbul_camp
  Sinbul_camp = '//*[@id="divAjaxTable"]/input[1]'
  print('작괘')

def Sinbul_등억():
  global Sinbul_camp
  Sinbul_camp = '//*[@id="divAjaxTable"]/input[2]'
  print('등억')

def Sinbul_달빛():
  global Sinbul_camp
  Sinbul_camp = '//*[@id="divAjaxTable"]/input[3]'
  print('달빛')

#순서 입력
#▶▶▶▶▶▶▶▶▶ 
def Sinbul_첫번쨰():
  global Sinbul_select
  Sinbul_select = '//*[@id="tableSite"]/tbody/tr[*]/td[*]/button'
  print('첫번째 검색')

def Sinbul_두번쨰():
  global Sinbul_select
  Sinbul_select = '//*[@id="tableSite"]/tbody/tr[2]/td[4]/button'
  print('두번째 검색')

def Sinbul_세번쨰():
  global Sinbul_select
  Sinbul_select = '//*[@id="tableSite"]/tbody/tr[*]/td[3]/button'
  print('세번째 검색')

#달력 선택
#▶▶▶▶▶▶▶▶▶
def Sinbul_첫째달():
  global Sinbul_mon
  Sinbul_mon = 1
  print('첫째달 선택')

def Sinbul_둘째달():
  global Sinbul_mon
  Sinbul_mon = 2  
  print('둘째달 선택')

#실시간 입력
#▶▶▶▶▶▶▶▶▶
def Sinbul_라이브():
  global Sinbul_live
  Sinbul_live = 2
  schedule_PC_start()

def Sinbul_라이브_시간():
  global Sinbul_live
  Sinbul_live = 3
  schedule_PC_start()

#시작시간 입력
#▶▶▶▶▶▶▶▶▶
def Sinbul_Time_변수(Sinbul_time_min,Sinbul_time_sec):
  global Sinbul_time_min_tr, Sinbul_time_sec_tr
  Sinbul_time_min_tr = Sinbul_time_min
  Sinbul_time_sec_tr = Sinbul_time_sec

#오토캠핑장만 보기
#▶▶▶▶▶▶▶▶▶
def 오토사이트(Auto_Site):
  global 오토캠핑장
  오토캠핑장 = Auto_Site
  print(오토캠핑장)

#예약가능 사이트만 보기
#▶▶▶▶▶▶▶▶▶
def 예약가능사이트(Only_Site):
  global 예약가능
  예약가능 = Only_Site
  print(예약가능)

#새로고침 셋팅
#▶▶▶▶▶▶▶▶▶
def 새로고침_셋팅(Refesh):
  global 새로고침
  새로고침 = Refesh
  print(새로고침)

  ##################################################################################
def schedule_PC_start():

  # Chrome 웹 드라이버 생성
  global driver
  #driver = webdriver.Chrome()
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--window-position=0,0')  # 좌측 상단에 위치

  # Chrome WebDriver 인스턴스 생성
  driver = webdriver.Chrome(options=chrome_options)

  #크롬 사이즈 변경
  #driver.set_window_size(1920, 1080) 
  #driver.maximize_window()
  driver.get("https://camping.ulju.ulsan.kr/")
  time.sleep(0.2)
  
  pag.keyDown('ctrl')
  j: int = 1
  for j in range(4):
      pag.press('-')
      time.sleep(0.05)
  
  pag.keyUp('ctrl')
  #크롬 브라우저 꺼짐 방지

  # 웹 페이지로 이동
  #driver.execute_script("document.body.style.zoom='zoom %'")

  # 웹 페이지에서 작업 수행
  # 예: 웹 페이지의 요소를 찾아 클릭하거나 데이터를 입력할 수 있음
  로그인()

###########################로그인 클릭
def 로그인():
  try:
    while True:
      print('로그인')
      button = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/ul/li[1]/a')
      # 버튼 클릭
      button.click()
      time.sleep(refresh_time_page)
      로그인클릭()
  except:
    pass

###########################로그인 클릭 1
def 로그인클릭():
  try:
    while True:
      print('로그인 클릭')
      button = driver.find_element(By.XPATH, '//*[@id="login_ulsan"]/img')
      # 버튼 클릭
      button.click()
      time.sleep(refresh_time_page)
      로그인ID()
  except:
    pass

###########################로그인 ID입력
def 로그인ID():
  try:
    while True:
      print('로그인 ID')
      button = driver.find_element(By.XPATH, '//*[@id="loginfrm"]/fieldset/label/span/input')
      # 버튼 클릭
      button.click()
      pyperclip.copy(Sinbul_id)
      time.sleep(refresh_time_click)
      pag.hotkey('ctrl','v')
      로그인PW()
  except:
    pass

###########################로그인 PW입력
def 로그인PW():
  try:
    while True:
      print('로그인 PW')
      button = driver.find_element(By.XPATH, '//*[@id="password"]')
      # 버튼 클릭
      button.click()
      pyperclip.copy(Sinbul_pw)
      time.sleep(refresh_time_click)
      pag.hotkey('ctrl','v')
      로그인접속()
  except:
    pass

###########################로그인 접속
def 로그인접속():
  try:
    while True:
      print('로그인 접속')
      button = driver.find_element(By.XPATH, '//*[@id="loginfrm"]/div/input')
      # 버튼 클릭
      button.click()
      time.sleep(refresh_time_page)
      온라인예약클릭()      
  except:
    pass

###########################온라인 예약 클릭
def 온라인예약클릭():
  try:
    while True:
      print('온라인 예약')
      button = driver.find_element(By.XPATH, '//*[@id="main_menu"]/li[4]/a')
      # 버튼 클릭
      button.click()
      time.sleep(refresh_time_page)
      달력클릭()
  except:
    pass

###########################달력 클릭
def 달력클릭():
  try:
    while True:
      print('달력 클릭')
      if Sinbul_mon == 2 :
        button = driver.find_element(By.XPATH, '//*[@id="calendar"]/div[1]/div[2]/button/span')
        # 버튼 클릭
        button.click()
        time.sleep(refresh_time_click)
        예약날짜클릭()
      else:
        예약날짜클릭()
  except:
    pass

###########################예약 날짜 클릭
def 예약날짜클릭():
  try:
    while True:
      print('날짜 클릭')
      button = driver.find_element(By.XPATH, Sinbul_date)
      # 버튼 클릭
      button.click()
      time.sleep(refresh_time_page)
      캠핑장선택()
  except:
    pass

###########################캠핑장 선택
def 캠핑장선택():
  try:
    while True:
      print('캠핑장 클릭')
      time.sleep(refresh_time_page)
      button = driver.find_element(By.XPATH, Sinbul_camp)
      # 버튼 클릭
      button.click()
      time.sleep(refresh_time_page)
      print('except2')
      셋팅_오토사이트()
  except:
    print('except1')
    pass

###########################사이트종류 오토 클릭
def 셋팅_오토사이트 ():
  try:
    while True:
      if ( 오토캠핑장 == 1):
        print("오토 사이트만 보기") 
        button = driver.find_element(By.XPATH, '//*[@id="priceCode"]')
        # 버튼 클릭
        button.click()
        time.sleep(refresh_time_click)
        pag.hotkey('down')
        time.sleep(refresh_time_click)
        pag.hotkey('enter')
        셋팅_예약가능사이트()
      else :
        셋팅_예약가능사이트()
  except:
    pass

def 셋팅_예약가능사이트():
  try:
    while True:
      if ( 예약가능 == 1 ):
        print("예약 가능 사이트만 보기") 
        button = driver.find_element(By.XPATH, '//*[@id="divAjaxTable"]/div/label') #예약가능 사이트만 보기 클릭
        # 버튼 클릭
        button.click()
        time.sleep(refresh_time_page)
        시작타임()
      else :
        시작타임()
  except :
    pass

###########################시작 신호 #####################################################
def 시작타임():
  print('예약하기')
  while True:
    print("시간에 맞추어 시작") 
    tm = time.localtime()
    button = driver.find_element(By.XPATH, Sinbul_date) #날짜 클릭
    if keyboard.is_pressed("F2"):
      print("종료") 
      break  
    if (새로고침 == 1 and tm.tm_min == Sinbul_time_min_tr and tm.tm_sec == Sinbul_time_sec_tr ) : 
      ###########################날짜 예약 클릭
      print("시간에 맞추어 시작//날짜") 
      #button = driver.find_element(By.XPATH, Sinbul_date) #날짜 클릭
      # 버튼 클릭
      button.click()
      time.sleep(0.1)
      예약하기_신청_원클릭()
    if (새로고침 == 1 and Sinbul_live == 3 and tm.tm_min == Sinbul_time_min_tr and tm.tm_sec == Sinbul_time_sec_tr ) :
      ###########################날짜 예약 클릭
      print("시간에 맞추어 시작//날짜") 
      #button = driver.find_element(By.XPATH, Sinbul_date) #날짜 클릭
      # 버튼 클릭
      button.click()
      time.sleep(0.1)
      예약하기_신청_원클릭()
    if (새로고침 == 2 and tm.tm_min == Sinbul_time_min_tr and tm.tm_sec == Sinbul_time_sec_tr ) : 
      ###########################날짜 예약 클릭
      print("시간에 맞추어 시작//날짜") 
      #button = driver.find_element(By.XPATH, Sinbul_date) #날짜 클릭
      # 버튼 클릭
      button.click()
      time.sleep(0.1)
      예약하기_신청_실시간()
    if (새로고침 == 2 and Sinbul_live == 3 and tm.tm_min == Sinbul_time_min_tr and tm.tm_sec == Sinbul_time_sec_tr ) :
      ###########################날짜 예약 클릭
      print("시간에 맞추어 시작//날짜") 
      #button = driver.find_element(By.XPATH, Sinbul_date) #날짜 클릭
      # 버튼 클릭
      button.click()
      time.sleep(0.1)
      예약하기_신청_실시간()
    if (Sinbul_live == 2 ) :
      print("실시간 시작//날짜") 
      예약하기_신청_실시간()


def 예약하기_신청_원클릭():
  try:
    while True:    
      try:
        tm = time.localtime()
        if (tm.tm_min == 35 ) : #9시 56분 및 15시 56분 시작
          print('35분 종료 ')
          time.sleep(3600)
        ########################### 우측 하단 예약신청 클릭 
        print('예약신청 클릭_원클릭')                           
        button = driver.find_element(By.XPATH, Sinbul_select)
        time.sleep(0.02)
        button.click()
        time.sleep(0.08)#time.sleep(0.07)###포인트 ㅇㅕ기조정
        ###########################예약신청 클릭
        print('예약확인 클릭_원클릭')
        button = driver.find_element(By.XPATH, '//*[@id="resModal"]/div[2]/div/div[3]/button[2]')
        time.sleep(0.05)#time.sleep(0.05)
        button.click()
        time.sleep(60)
        print(str(Sinbul_time_min_tr) + '분' + str(Sinbul_time_sec_tr) + '초' + str(Sinbul_camp))
      except:
        pass
  except:
      pass

      
def 예약하기_신청_실시간():
  try:
    while True:    
      global Sinbul_date
      global Sinbul_select
      ###########################날짜 예약 클릭
      button = driver.find_element(By.XPATH, Sinbul_date)
      #button = driver.find_element(By.XPATH, '//*[@id="divAjaxTable"]/div/label') #예약가능 사이트만 보기 클릭
      # 버튼 클릭
      button.click()
      time.sleep(0.1)
      try:
        if keyboard.is_pressed("F2"): # F2 누른게 감지되면
          time.sleep(3600)
          break
        ########################### 우측 하단 예약신청 클릭 
        print('예약신청 클릭_실시간')                           
        button = driver.find_element(By.XPATH, Sinbul_select)
        time.sleep(0.02)
        button.click()
        time.sleep(0.08)#time.sleep(0.07)###포인트 ㅇㅕ기조정
        ###########################예약신청 클릭
        print('예약확인 클릭_실시간')
        button = driver.find_element(By.XPATH, '//*[@id="resModal"]/div[2]/div/div[3]/button[2]')
        time.sleep(0.05)#time.sleep(0.05)
        button.click()
        time.sleep(3600)
      except:
        pass
  except:
    pass



