import time
import pyperclip
import pyautogui as pag
from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import random


id = 'pend'
password = '*Zoavld4fkd'


# 날짜 설정                                                      몇주차                       6: 금요일 7 : 토요일
#       //*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[6]
date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[7]'

# 캠핑장 설정                         
#//*[@id="divAjaxTable"]/input[1] 작괘
#//*[@id="divAjaxTable"]/input[2] 등억
#//*[@id="divAjaxTable"]/input[3] 달빛
camp = '//*[@id="divAjaxTable"]/input[1]'




def test():
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
  time.sleep(0.2)

  ###########################로그인 ID입력
  button = driver.find_element(By.XPATH, '//*[@id="loginfrm"]/fieldset/label/span/input')
  # 버튼 클릭
  button.click()
  pyperclip.copy(id)
  time.sleep(0.2)
  pag.hotkey('ctrl','v')

  ###########################로그인 PW입력
  button = driver.find_element(By.XPATH, '//*[@id="password"]')
  # 버튼 클릭
  button.click()
  pyperclip.copy(password)
  time.sleep(0.2)
  pag.hotkey('ctrl','v')

  ###########################로그인 클릭
  button = driver.find_element(By.XPATH, '//*[@id="loginfrm"]/div/input')
  # 버튼 클릭
  button.click()
  time.sleep(0.2)
  
  ###########################온라인 예약 클릭
  button = driver.find_element(By.XPATH, '//*[@id="main_menu"]/li[4]/a')
  # 버튼 클릭
  button.click()
  time.sleep(0.2)
  
  ###########################날짜 예약 클릭
  button = driver.find_element(By.XPATH, date)
  # 버튼 클릭
  button.click()
  time.sleep(1)

  # ###########################예약가능 사이트만 보기 클릭
  # button = driver.find_element(By.XPATH, '//*[@id="divAjaxTable"]/div/label')
  # # 버튼 클릭
  # button.click()
  # time.sleep(0.2)

  while True:      
    try:
      ###########################예약신청 클릭
      button = driver.find_element(By.XPATH, '//*[@id="tableSite"]/tbody/tr[*]/td[*]/button')
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
  














###########################예약하기 클릭
# button = driver.find_element(By.XPATH, '//*[@id="subWrap"]/div[2]/ul/li[3]/a/span/img')
# # 버튼 클릭
# button.click()
# time.sleep(0.2)

# ###########################날짜 클릭
# button = driver.find_element(By.XPATH, '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/div[1]/table/tbody/tr/td[6]')
# # 버튼 클릭
# button.click()
# time.sleep(1)

# ###########################예약가능사이트만  클릭
# button = driver.find_element(By.XPATH, '//*[@id="divAjaxTable"]/div/label')
# # 버튼 클릭
# button.click()
# time.sleep(5)


# ###########################예약신청 
# button = driver.find_element(By.XPATH, '//*[@id="tableSite"]/tbody/tr[1]/td[4]/button')
# #button = driver.find_element(By.TAG_NAME, '예약신청')


# # 버튼 클릭
# button.click()
# time.sleep(2)

# ###########################예약 클릭
# button = driver.find_element(By.XPATH, '//*[@id="resModal"]/div[2]/div/div[3]/button[2]')
# #button = driver.find_element(By.CLASS_NAME,'btn btn-primary')
# # 버튼 클릭
# button.click()
# time.sleep(1)










#############################################
time.sleep(5)
# 브라우저 닫기
#driver.quit()