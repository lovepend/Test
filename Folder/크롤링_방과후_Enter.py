from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui as pag
import pyperclip
import keyboard
import random
import time

refresh_time_page = 1
refresh_time_click = 0.02

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
  driver.get("https://afschool.use.go.kr/")
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
  신청하기()

def 신청하기():
  try:
    while True:
      tm = time.localtime()
      print(tm.tm_min,tm.tm_sec)
      if keyboard.is_pressed("F2"): # F2 누른게 감지되면
        break
      print('로그인')
      pag.hotkey('f5')
      button = driver.find_element(By.XPATH, '//*[@id="vtab1"]/div[2]/button/span')
      # 버튼 클릭
      button.click()
      time.sleep(refresh_time_page)
      pag.hotkey('enter')
      time.sleep(refresh_time_click)
      pag.hotkey('enter')
      time.sleep(refresh_time_click)
      pag.hotkey('enter')
      #로그인클릭()
  except:
    pass

schedule_PC_start()