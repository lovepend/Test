import pyautogui as pag
import time
import keyboard
import random

# while True:w vw v
#   if keyboard.is_pressed("F2"): # F2 누른게 감지되면
#     break
#   pag.click(x=1440, y=444)
#   num1 = random.randrange(1,10)w
#   time.sleep(num1)
pag.click(1603.,927) 

# pag.hotkewwwwwwwwwwwwwwwwwwwsy('f')
# time.sleep(2) fwwa vww vwsd vw
# pag.hotkey('f')  vw
# pag.keyDown('w')   a
# time.sleep(10)fwsd vwsa vww vwsd vvw
# pag.keyUp('w')  vwwa

while True:
  num = random.randrange(1,6)
  num1 = random.randrange(1,2)
  print(num)
  pag.keyDown('w')   
  time.sleep(2)
  pag.keyUp('w') 
  if keyboard.is_pressed("F2"): # F2 누른게 감지되면
    break  
  if (num == 1) :  
    pag.keyDown('w')   
    pag.keyDown('d')  
    time.sleep(num1)
    pag.keyUp('w') 
    pag.keyUp('d') 
    pag.hotkey('space')
    pag.hotkey('v') 
  if (num == 2) :
    pag.keyDown('w')  
    pag.keyDown('a') 
    time.sleep(num1)
    pag.keyUp('w') 
    pag.keyUp('a') 
    pag.hotkey('space') 
    pag.hotkey('v') 
  if (num == 3) :
    pag.keyDown('w') 
    time.sleep(num1)
    pag.keyUp('w') 
    pag.hotkey('space') 
    pag.hotkey('v') 
  if (num == 4) :
    pag.keyDown('s') 
    pag.keyDown('d') 
    time.sleep(num1)
    pag.keyUp('s') 
    pag.keyUp('d') 
    pag.hotkey('space') 
    pag.hotkey('v') 
  if (num == 5) :
    pag.keyDown('s')  
    pag.keyDown('a') 
    time.sleep(num1)
    pag.keyUp('s') 
    pag.keyUp('a') 
    pag.hotkey('space')  
    pag.hotkey('v')
  if (num == 6) :
    pag.keyDown('s') 
    time.sleep(num1)
    pag.keyUp('s') 
    pag.hotkey('space')  
    pag.hotkey('v')
  if keyboard.is_pressed("F2"): # F2 누른게 감지되면
    break  
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


