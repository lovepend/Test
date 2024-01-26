import time
import pyperclip
import pyautogui as pag
from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import random

def test():
  # Chrome 웹 드라이버 생성
  driver = webdriver.Chrome()
  #driver.set_window_size(1920, 1080) 
  driver.maximize_window()




  # 웹 페이지로 이동
  driver.get("https://cafe.naver.com/ulsanallcamp")
  time.sleep(0.2)

  # 웹 페이지에서 작업 수행
  # 예: 웹 페이지의 요소를 찾아 클릭하거나 데이터를 입력할 수 있음

  ###########################로그인 클릭
  button = driver.find_element(By.XPATH, '//*[@id="gnb_login_button"]/span[3]')
  # 버튼 클릭
  button.click()
  time.sleep(0.2)

  ###########################로그인 ID입력
  button = driver.find_element(By.XPATH, '//*[@id="id"]')
  # 버튼 클릭
  button.click()
  pyperclip.copy('lovepend2')
  time.sleep(0.2)
  pag.hotkey('ctrl','v')

  ###########################로그인 PW입력
  button = driver.find_element(By.XPATH, '//*[@id="pw"]')
  # 버튼 클릭
  button.click()
  pyperclip.copy('*qkqh4fkd')
  time.sleep(0.2)
  pag.hotkey('ctrl','v')

  ###########################로그인 클릭
  button = driver.find_element(By.XPATH, '//*[@id="log.login"]')
  # 버튼 클릭
  button.click()
  time.sleep(5)
  


while True:
  
  if keyboard.is_pressed("F2"): # F2 누른게 감지되면
    break 
  test()
  if keyboard.is_pressed("F2"): # F2 누른게 감지되면
    break 
  num = random.randrange(1800,1810)
  #num1 = num/100
  #time.sleep(num1)
  time.sleep(num)
  time.sleep(0.2)
  if keyboard.is_pressed("F2"): # F2 누른게 감지되면
    break 
  
