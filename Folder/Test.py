# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from threading import Thread
# import time
# import pyperclip
# import pyautogui as pag
# from selenium.webdriver.common.by import By

# # Selenium 작업을 수행할 함수 정의
# def open_browser(url):
#     driver = webdriver.Chrome()
#     driver.get(url)
#     print(f"{url} - {driver.title}")
    
#     try:
#       while True:
#         print('로그인')
#         button = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/ul/li[1]/a')
#         # 버튼 클릭
#         button.click()
#         time.sleep(2)
#         pass
#     except:
#       pass
    
#     try:
#       while True:
#         print('로그인 클릭')
#         button = driver.find_element(By.XPATH, '//*[@id="login_ulsan"]/img')
#         # 버튼 클릭
#         button.click()
#         time.sleep(2)
#         print('로그인 ID')
#         button = driver.find_element(By.XPATH, '//*[@id="loginfrm"]/fieldset/label/span/input')
#         # 버튼 클릭
#         button.click()
#         pyperclip.copy('pend')
#         time.sleep(1)
#         pag.hotkey('ctrl','v')
#         time.sleep(100)
#         pass
#     except:
#       pass




#     driver.quit()

# # 실행할 URL 리스트
# urls = [
#     "https://camping.ulju.ulsan.kr/",
#     "https://camping.ulju.ulsan.kr/",
#     "https://camping.ulju.ulsan.kr/",
# ]

# # 쓰레드 리스트 초기화
# threads = []

# # 각 URL에 대해 쓰레드 생성 및 시작
# for url in urls:
#     # t = Thread(target=open_browser, args=(url,))
#     t = Thread(target=open_browser, args=(url,))
#     t.start()
#     threads.append(t)

# # 모든 쓰레드가 종료될 때까지 기다림
# for t in threads:
#     t.join()

# print("모든 페이지 로딩 완료.")


import pyautogui as pag
import cv2
import keyboard
import time



def 시작():
  while True:
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      break
    print("시작")
    test01() 
    test02()
    # test03()    
    

def test01():
  # while True:
    print("test01")
    # if keyboard.is_pressed("F2"): # F2 누른게 감지되면
    #   break
    try :
      button = pag.locateCenterOnScreen('./image/51. Kyungju/98.png', confidence=0.9)
      if (button == None) :
        None
      else :
        pag.click(button)
    except :
      None
  
def test02():
  # while True:
    print("test02")
    # if keyboard.is_pressed("F2"): # F2 누른게 감지되면
    #   break
    try :
      button = pag.locateCenterOnScreen('./image/51. Kyungju/99.png', confidence=0.9)
      if (button == None) :
        None
      else :
        pag.hotkey('enter')
    except :
      None

   

# def test03():
#   print("test03")
#   button3 = pag.locateCenterOnScreen('./image/51. Kyungju/99.png', confidence=0.9)
#   if (button3 == None) :
#     None 
#     test01()
#   else :
#     pag.hotkey('enter')
    


시작()












