import tkinter
import pyautogui as pag
import win32con
import win32api
import win32gui
import keyboard
import clipboard
import pyperclip
import schedule
import time
import cv2


a = 0.1

# def 카카오톡():
#   while True:
#     if keyboard.is_pressed("F2"): # F2 누른게 감지되면
#       break
#     pag.rightClick(x=210, y=381)
#     time.sleep(a)

#     pag.click(x=258, y=613)
#     time.sleep(a)
#     pag.click(x=382, y=617)
#     time.sleep(a)
#     pag.hotkey('enter')
#     time.sleep(a)



def 카카오톡():
  while True:
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      break
    pag.click(x=447, y=405)
    time.sleep(a)
    pag.click(x=164, y=354)
    time.sleep(a)
    pag.click(x=196, y=413)
    time.sleep(a)
    pag.click(x=314, y=357)
    time.sleep(a)




카카오톡()