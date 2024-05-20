import pyautogui as pag
import cv2
import keyboard
import time

#줌 67% 사용

a  = 0.02

#수강신청 호출 리스트
#https://afschool.use.go.kr/use1068/ltrReq?sv=LTR_NM&sw=%EC%BB%B4%EC%A7%B1%EB%B0%98B#
#수강신청 화면 호출 리스트
#https://afschool.use.go.kr/use1068/ltrReq/112905

def 수강신청시작():
  while True:
    print("시작")
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      break
    try :
      pag.hotkey('f5')
      새로고침()
    except :
      None


def 새로고침():
  print("새로고침")
  while True:
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      break
    try :
      button = pag.locateCenterOnScreen('./image/99. Afschool/00.png', confidence=0.95)
      if (button == None) :
        새로고침()
      else :
        print("새로고침 완료")
        신청하기()
    except :
      None

def 신청하기():
  time.sleep(a)
  while True:
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      break
    try :
      print("신청하기 클릭")
      button = pag.locateCenterOnScreen('./image/99. Afschool/02.png', confidence=0.7)
      if (button == None) :
        수강신청시작()
      else :
        print("신청하기 클릭완료")
        pag.click(button)
        신청확인()
    except :
      None

def 신청확인():
  time.sleep(a)
  while True:
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      break
    try :
      print("신청확인 클릭")
      button = pag.locateCenterOnScreen('./image/99. Afschool/03.png', confidence=0.8)
      if (button == None) :
        신청확인()
      else :
        print("신청확인 클릭완료1")
        pag.click(button1)
        
        time.sleep(360)
        신청확인()
    except :
      None


수강신청시작()
