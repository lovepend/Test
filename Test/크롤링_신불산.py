from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui as pag
import pyperclip
import keyboard
import random
import time

#아이디 입력
#▶▶▶▶▶▶▶▶▶
global 크롤링_id
크롤링_id = "pend"
global 크롤링_pw
크롤링_pw = "*Zoavld4fkd" 

크롤링_사이트 = 0  

def 크롤링_Log_Id1():
  global 크롤링_id
  크롤링_id = "pend"
  print(크롤링_id)

def 크롤링_Log_Id2():
  global 크롤링_id
  크롤링_id = "lovepend2"
  print(크롤링_id)

def 크롤링_Log_Id3():
  global 크롤링_id
  크롤링_id = "lovepend1"
  print(크롤링_id)

def 크롤링_Log_Id4():
  global 크롤링_id
  크롤링_id = "parkmc7"
  print(크롤링_id)

def 크롤링_Log_Guest():
  global 크롤링_id
  크롤링_id = "jhrep1201"
  global 크롤링_pw
  크롤링_pw = "j1902217**"
  print(크롤링_id)
  print(크롤링_pw)


#날짜 입력
#▶▶▶▶▶▶▶▶▶                                                몇주차                       6: 금요일 7 : 토요일
#       //*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[6]
#date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[7]'
  
def 크롤링_Day11():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[1]/table/tbody/tr/td[6]'

def 크롤링_Day12():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[1]/table/tbody/tr/td[7]'

def 크롤링_Day21():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[1]/table/tbody/tr/td[6]'

def 크롤링_Day22():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[1]/table/tbody/tr/td[7]'

def 크롤링_Day31():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/div[1]/table/tbody/tr/td[6]'

def 크롤링_Day32():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/div[1]/table/tbody/tr/td[7]'

def 크롤링_Day41():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[6]'

def 크롤링_Day42():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[7]'

def 크롤링_Day51():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[1]/table/tbody/tr/td[6]'

def 크롤링_Day52():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[1]/table/tbody/tr/td[7]'

#캠핑장 입력
#▶▶▶▶▶▶▶▶▶                           
#//*[@id="divAjaxTable"]/input[1] 작괘
#//*[@id="divAjaxTable"]/input[2] 등억
#//*[@id="divAjaxTable"]/input[3] 달빛

def 크롤링_작괘():
  global camp
  camp = '//*[@id="divAjaxTable"]/input[1]'

def 크롤링_등억():
  global camp
  camp = '//*[@id="divAjaxTable"]/input[2]'

def 크롤링_달빛():
  global camp
  camp = '//*[@id="divAjaxTable"]/input[3]'

#순서 입력
#▶▶▶▶▶▶▶▶▶ 
def 크롤링_첫번쨰():
  global 크롤링_select
  크롤링_select = 1

def 크롤링_두번쨰():
  global 크롤링_select
  크롤링_select = 2

def 크롤링_세번쨰():
  global 크롤링_select
  크롤링_select = 3

def 크롤링_첫째달():
  global 크롤링_mon
  크롤링_mon = 1

def 크롤링_둘째달():
  global 크롤링_mon
  크롤링_mon = 2  

#사이트 입력
#▶▶▶▶▶▶▶▶▶ 
def 크롤링_사이트():
  global 크롤링_사이트
  크롤링_사이트 = 1  

def 크롤링_시작():
  # Chrome 웹 드라이버 생성
  driver = webdriver.Chrome()
  #크롬 사이즈 변경
  #driver.set_window_size(1920, 1080) 
  driver.maximize_window()
  #크롬 브라우저 꺼짐 방지


  # 웹 페이지로 이동
  driver.get("https://camping.ulju.ulsan.kr/")
  time.sleep(0.2)
  #driver.execute_script("document.body.style.zoom='zoom %'")

  # 웹 페이지에서 작업 수행
  # 예: 웹 페이지의 요소를 찾아 클릭하거나 데이터를 입력할 수 있음

  ###########################로그인 클릭
  button = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/ul/li[1]/a')
  # 버튼 클릭
  button.click()
  time.sleep(0.2)

    ###########################로그인 클릭 1
  button = driver.find_element(By.XPATH, '//*[@id="login_ulsan"]/img')
  # 버튼 클릭
  button.click()
  time.sleep(0.5)

  ###########################로그인 ID입력
  button = driver.find_element(By.XPATH, '//*[@id="loginfrm"]/fieldset/label/span/input')
  # 버튼 클릭
  button.click()
  pyperclip.copy(크롤링_id)
  time.sleep(0.5)
  pag.hotkey('ctrl','v')

  ###########################로그인 PW입력
  button = driver.find_element(By.XPATH, '//*[@id="password"]')
  # 버튼 클릭
  button.click()
  pyperclip.copy(크롤링_pw)
  time.sleep(0.5)
  pag.hotkey('ctrl','v')

  ###########################로그인 클릭
  button = driver.find_element(By.XPATH, '//*[@id="loginfrm"]/div/input')
  # 버튼 클릭
  button.click()
  time.sleep(0.5)
  
  ###########################온라인 예약 클릭
  button = driver.find_element(By.XPATH, '//*[@id="main_menu"]/li[4]/a')
  # 버튼 클릭
  button.click()
  time.sleep(0.5)
  
  ###########################달력 클릭
  if 크롤링_mon == 2 :
    button = driver.find_element(By.XPATH, '//*[@id="calendar"]/div[1]/div[2]/button/span')
    # 버튼 클릭
    button.click()
    time.sleep(2)
  else :
    None

  ###########################날짜 예약 클릭
  button = driver.find_element(By.XPATH, date)
  # 버튼 클릭
  button.click()
  time.sleep(2)

  if 크롤링_사이트 == 1 :
    ###########################사이트종류 오토 클릭
    button = driver.find_element(By.XPATH, '//*[@id="priceCode"]')
    # 버튼 클릭
    button.click()
    time.sleep(0.5)
    pag.hotkey('down')
    time.sleep(0.5)
    pag.hotkey('enter')
    time.sleep(2)
    

  ###########################캠핑장 선택
  button = driver.find_element(By.XPATH, camp)
  # 버튼 클릭
  button.click()
  time.sleep(2)

  if 크롤링_select == 2 or 크롤링_select == 3 :
    # ###########################예약가능 사이트만 보기 클릭
    button = driver.find_element(By.XPATH, '//*[@id="divAjaxTable"]/div/label')
    # 버튼 클릭
    button.click()
    time.sleep(0.2)
  else : 
    None

  while True:      
    try:
      if 크롤링_select == 1 :
        ###########################예약신청 클릭                            *맨처음 [1] 두번째[2] 
        button = driver.find_element(By.XPATH, '//*[@id="tableSite"]/tbody/tr[*]/td[*]/button')
      if 크롤링_select == 2 :
        button = driver.find_element(By.XPATH, '//*[@id="tableSite"]/tbody/tr[2]/td[*]/button')
      if 크롤링_select == 3 :
        button = driver.find_element(By.XPATH, '//*[@id="tableSite"]/tbody/tr[3]/td[*]/button')
      # 버튼 클릭
      button.click()
      time.sleep(0.3)

      ###########################예약신청 클릭
      button = driver.find_element(By.XPATH, '//*[@id="resModal"]/div[2]/div/div[3]/button[2]')
      # 버튼 클릭
      button.click()
    except:
        ###########################날짜 예약 클릭
        button = driver.find_element(By.XPATH, date)
        # 버튼 클릭
        button.click()

