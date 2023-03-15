import pyautogui as pag
import time
import keyboard


def 태화연_Day():
    while True:
        if keyboard.is_pressed("F2"): 
            time.sleep(0.2)
            global 태화연_day1 
            태화연_day1  = pag.position()
            print(태화연_day1)
            break        
    while True:
        if keyboard.is_pressed("F2"): 
            time.sleep(0.2)
            global 태화연_day2
            태화연_day2  = pag.position()
            print(태화연_day2)
            break    

        