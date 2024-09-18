import pyautogui as pag
import time
import keyboard
import random

#플레이 (1603.,927)
 
#스페이스 pag.click('space')
pag.click(1603.,927) 
while True:
  num = random.randrange(1,6)
  num1 = random.randrange(1,2)
  print(num)
  if keyboard.is_pressed("F2"): # F2 누른게 감지되면
    break  
  if (num == 1) :
    pag.keyDown('w') 
    pag.keyDown('d') 
    time.sleep(num1)
    pag.keyUp('w') 
    pag.keyUp('d') 
    pag.hotkey('space')  
  if (num == 2) :
    pag.keyDown('w')  
    pag.keyDown('a') 
    time.sleep(num1)
    pag.keyUp('w') 
    pag.keyUp('a') 
    pag.hotkey('space')  
  if (num == 3) :
    pag.keyDown('w') 
    time.sleep(num1)
    pag.keyUp('w') 
    pag.hotkey('space')  
  if (num == 4) :
    pag.keyDown('s') 
    pag.keyDown('d') 
    time.sleep(num1)
    pag.keyUp('s') 
    pag.keyUp('d') 
    pag.hotkey('space')  
  if (num == 5) :
    pag.keyDown('s')  
    pag.keyDown('a') 
    time.sleep(num1)
    pag.keyUp('s') 
    pag.keyUp('a') 
    pag.hotkey('space')  
  if (num == 6) :
    pag.keyDown('s') 
    time.sleep(num1)
    pag.keyUp('s') 
    pag.hotkey('space')  
  button1 = pag.locateCenterOnScreen("./image/99. Brol/01. Next.png", confidence=0.7) 
  if (button1 == None) :
    None
  else : 
    pag.click(button1.x,button1.y)
    time.sleep(3)
    button2 = pag.locateCenterOnScreen("./image/99. Brol/02. Again.png", confidence=0.7)  
    if (button2 == None) :
      None
    else : 
      pag.click(button2.x,button2.y)


