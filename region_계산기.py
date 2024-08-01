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


t1_1 = t1[:]
t1_2 = t2[:]
t3 = t1_2[0] - t1_1[0]
t4 = t1_2[1] - t1_1[1]
print(t1_1[0],',',t1_1[1],',',t3,',',t4)

