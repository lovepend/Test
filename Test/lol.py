import pyautogui as pag
import keyboard

def lol():
  while True:
    if keyboard.is_pressed("F2"): # F2 누른게 감지되면
      pag.keyUp('c')
    if keyboard.is_pressed("F3"): # F2 누른게 감지되면
      pag.keyDown('c')
    

lol()