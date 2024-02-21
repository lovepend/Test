from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui as pag
import pyperclip
import keyboard
import random
import time
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

time_sleep = 3

#아이디 입력
#▶▶▶▶▶▶▶▶▶
schedule_mobile_id = "pend"
schedule_mobile_pw = "*Zoavld4fkd" 

#날짜 입력
#▶▶▶▶▶▶▶▶▶
#3월 29일   / schedule_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[1]/table/tbody/tr/td[6]'
#3월 30일   / schedule_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[1]/table/tbody/tr/td[7]'
#3월 31일   / schedule_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[6]/div[1]/table/tbody/tr/td[1]'
schedule_mobile_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[2]/table/thead/tr/td[7]/span' #30일 토

#시간 
tm = time.localtime()

def 크롤링_모바일_타임(크롤링_min,크롤링_sec):
  global schedule_mobile_start_time_min, schedule_mobile_start_time_sec, schedule_mobile_end_time_min
  schedule_mobile_start_time_min = int(크롤링_min)
  schedule_mobile_start_time_sec = int(크롤링_sec)
  schedule_mobile_end_time_min = 35

#캠핑장 입력
#▶▶▶▶▶▶▶▶▶                           
#//*[@id="divAjaxTable"]/input[1] 작괘
#//*[@id="divAjaxTable"]/input[2] 등억
#//*[@id="divAjaxTable"]/input[3] 달빛
schedule_mobile_camp = '//*[@id="divAjaxTable"]/input[2]'

#검색범위 입력 
#▶▶▶▶▶▶▶▶▶ 
schedule_mobile_select = 1 # (1 : 첫번째 / 2 : 두번째  / 3 :  세번째)

#달력 입력 
#▶▶▶▶▶▶▶▶▶ 
schedule_mobile_month = 2 #  (1 : 첫째달 / 2 : 다음달)



def schedule_mobile_start():
  # # Chrome 웹 드라이버 생성
  # global driver
  # driver = webdriver.Chrome()
  # #크롬 사이즈 변경
  # #driver.set_window_size(1920, 1080) 
  # #driver.maximize_window()
  # driver.get("https://camping.ulju.ulsan.kr/")
  # time.sleep(0.2)
  # pag.keyDown('ctrl')
  # j: int = 1
  # for j in range(4):
  #     pag.press('-')
  #     time.sleep(0.05)
  # #크롬 브라우저 꺼짐 방지
  # #웹 페이지로 이동
  # #driver.execute_script("document.body.style.zoom='zoom %'")
  # #웹 페이지에서 작업 수행
  # #예: 웹 페이지의 요소를 찾아 클릭하거나 데이터를 입력할 수 있음
  options = Options()
  # 1
  mobile_emulation = {"deviceName": "Galaxy S8"}
  options.add_experimental_option("mobileEmulation", mobile_emulation)

  # 2
  user_agent = "Mozilla/5.0 (Linux; Android 12; SM-S9060) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Mobile Safari/537.36"
  options.add_argument(f"user-agent={user_agent}")

  #options.add_experimental_option("detach", True)  # 화면이 꺼지지 않고 유지

  # options.add_argument("--start-maximized")  # 최대 크기로 시작

  #service = Service(ChromeDriverManager().install())

  global driver

  driver = webdriver.Chrome(options=options)
  #driver = webdriver.Chrome(service=service, options=options)

  driver.get("https://camping.ulju.ulsan.kr/")


  ###########################로그인 클릭
  print('로그인')
  button = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/ul/li[1]/a')
  # 버튼 클릭
  button.click()
  time.sleep(time_sleep)

  ###########################로그인 클릭 1
  print('로그인 클릭')
  button = driver.find_element(By.XPATH, '//*[@id="login_ulsan"]/img')
  # 버튼 클릭
  button.click()
  time.sleep(time_sleep)

  ###########################로그인 ID입력
  print('로그인 ID')
  button = driver.find_element(By.XPATH, '//*[@id="loginfrm"]/fieldset/label/span/input')
  # 버튼 클릭
  button.click()
  pyperclip.copy(schedule_mobile_id)
  time.sleep(time_sleep)
  pag.hotkey('ctrl','v')

  ###########################로그인 PW입력
  print('로그인 PW')
  button = driver.find_element(By.XPATH, '//*[@id="password"]')
  # 버튼 클릭
  button.click()
  pyperclip.copy(schedule_mobile_pw)
  time.sleep(time_sleep)
  pag.hotkey('ctrl','v')

  ###########################로그인 클릭
  print('로그인 접속')
  button = driver.find_element(By.XPATH, '//*[@id="loginfrm"]/div/input')
  # 버튼 클릭
  button.click()
  time.sleep(time_sleep)

  ###########################온라인 예약 클릭
  print('온라인 예약')
  button = driver.find_element(By.XPATH, '//*[@id="subWrap"]/div[2]/ul/li[3]/a/span')
  # 버튼 클릭
  button.click()
  time.sleep(time_sleep)

  #########################달력 클릭
  print('달력 클릭')
  button = driver.find_element(By.XPATH, '//*[@id="calendar"]/div[1]/div[2]/button/span')
  # 버튼 클릭
  button.click()
  time.sleep(time_sleep)

  ###########################날짜 예약 클릭
  print('날짜예약 클릭')
  button = driver.find_element(By.XPATH, schedule_mobile_date)
  # 버튼 클릭
  button.click()
  time.sleep(time_sleep)

  #########################사이트종류 오토 클릭
  print('사이트 종류 클릭')
  button = driver.find_element(By.XPATH, '//*[@id="priceCode"]')
  # 버튼 클릭
  button.click()
  time.sleep(1)
  pag.hotkey('down')
  time.sleep(1)
  pag.hotkey('enter')
  time.sleep(2)
 

  ###########################캠핑장 선택
  print('캠핑장 클릭')
  button = driver.find_element(By.XPATH, schedule_mobile_camp)
  # 버튼 클릭
  button.click()
  time.sleep(time_sleep)
  print('예약하기')
  예약하기()

def 예약하기():
  print('예약하기')
  while True :
    global schedule_mobile_start_time_min, schedule_mobile_start_time_sec
    print(schedule_mobile_start_time_min,schedule_mobile_start_time_sec)
    tm = time.localtime()
    if keyboard.is_pressed("F2"):
      print("종료") 
      break  
    if (tm.tm_min == schedule_mobile_start_time_min and tm.tm_sec == schedule_mobile_start_time_sec ) : #9시 56분 및 15시 56분 시작
      print('예약하기11111')
      예약하기1()
    
def 예약하기1():  
  try:
    while True:  
      print('예약하기1')  
      ###########################날짜 예약 클릭
      button = driver.find_element(By.XPATH,schedule_mobile_date)
      # 버튼 클릭
      button.click()
      time.sleep(0.05)
      try:
        tm = time.localtime()
        if (tm.tm_min == schedule_mobile_end_time_min ) : #9시 56분 및 15시 56분 시작
          time.sleep(3600)
        ###########################예약신청 클릭                            *맨처음 [1] 두번째[2] 
        print('버튼1')
        button = driver.find_element(By.XPATH, '//*[@id="tableSite"]/tbody/tr[*]/td[*]/button')
        button.click()
        # 버튼 클릭
        time.sleep(0.15)
        print('버튼2')
        button = driver.find_element(By.XPATH, '//*[@id="resModal"]/div[2]/div/div[3]/button[2]')
        print('버튼3')
        button.click()
        print('버튼4')
        time.sleep(60)
        print('끝')
      except:
        print('except1')
        예약하기1()
  except:
    print('땡1')
    time.sleep(5000)
    exit()
   
