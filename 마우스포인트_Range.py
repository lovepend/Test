import pyautogui as pag
import time
import keyboard
import random

while True:
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
        t1 = pag.position() # 위치 뽑아서 저장
        print(t1)
        time.sleep(0.5)
        break     

while True:
    if keyboard.is_pressed("F2"): 
        t2 = pag.position()
        print(t2)
        time.sleep(0.5)
        break      

a = t1[0] - t2[0]
b = t1[1] - t2[1]
print(a,b)
