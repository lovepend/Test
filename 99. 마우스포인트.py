import pyautogui as pag
import time
import keyboard

while True:
    if keyboard.is_pressed("F4"): # F4 누른게 감지되면
        t1 = pag.position() # 위치 뽑아서 저장
        print(t1)
        time.sleep(0.5)
        break        
while True:
    if keyboard.is_pressed("F4"): 
        t2 = pag.position()
        print(t2)
        time.sleep(0.5)
        break      
while True:
    if keyboard.is_pressed("F4"): 
        t3 = pag.position()
        print(t3)
        time.sleep(0.5)
        break    

while True:
    if keyboard.is_pressed("F4"): 
        t4 = pag.position()
        print(t4)
        time.sleep(0.5)
        break   

while True:
    if keyboard.is_pressed("F4"): 
        t5 = pag.position()
        print(t5)
        time.sleep(0.5)
        break   

while True:
    if keyboard.is_pressed("F4"): 
        t6 = pag.position()
        print(t6)
        time.sleep(0.5)
        break   

