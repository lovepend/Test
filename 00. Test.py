from xml.etree.ElementPath import xpath_tokenizer_re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui as pag
import keyboard


        
def 태화연_job():
    while True:
        pag.click(1068,273)
        time.sleep(0.2)
        pag.hotkey('enter')
        time.sleep(0.2)
        pag.hotkey('enter')
        time.sleep(0.2)

        if keyboard.is_pressed("F4") : # F4 누른게 감지되면
            break

태화연_job()