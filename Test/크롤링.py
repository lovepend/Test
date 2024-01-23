import time
import pyperclip
import pyautogui as pag
from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard

def test():
  # Chrome 웹 드라이버 생성
  driver = webdriver.Chrome()

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
  time.sleep(0.2)
  time.sleep(300)


while True:
  if keyboard.is_pressed("F2"): # F2 누른게 감지되면
    break 
  test()
  if keyboard.is_pressed("F2"): # F2 누른게 감지되면
    break 
  time.sleep(1800)
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