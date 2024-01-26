import keyboard
import pyautogui as pag
import time



print("키보드 1번 지정")

while True:
  if keyboard.is_pressed("F2"): # F2 누른게 감지되면
    t1 = pag.position() # 위치 뽑아서 저장
    print(t1)
    time.sleep(0.5)
    break     

print("키보드 2번 지정")
while True:  
  if keyboard.is_pressed("F2"): 
    t2 = pag.position()
    print(t2)
    time.sleep(0.5)
    break      

print("키보드 3번 지정")
while True:
  if keyboard.is_pressed("F2"): 
    t3 = pag.position()
    print(t3)
    time.sleep(0.5)
    break    


print("종료는 F4 누를것")

print("시작")

# while True:
#   print("키보드 4번 지정") 
#   if keyboard.is_pressed("F2"): 
#     t4 = pag.position()
#     print(t4)
#     time.sleep(0.5)
#     break   

# while True:
#     if keyboard.is_pressed("F2"): 
#         t5 = pag.position()
#         print(t5)
#         time.sleep(0.5)
#         break  
    

while True:
  if keyboard.is_pressed("1"):
    pag.click(t1)
    print("1번위치 클릭")
  if keyboard.is_pressed("2"):
    pag.click(t2)
    print("2번위치 클릭")
  if keyboard.is_pressed("3"):
    pag.click(t3)
    print("3번위치 클릭")
  # if keyboard.is_pressed("4"):
  #   pag.click(t4)
  # if keyboard.is_pressed("5"):
  #   pag.click(t5)
  if keyboard.is_pressed("F4"): # F2 누른게 감지되면
    print("끝 ")
    break     





