import pyautogui
import keyboard
import time
import threading

# 종료 플래그
running = True

def click_continuously():
    while running:
        pyautogui.click(500, 500)
        time.sleep(0.1)  # 클릭 간격을 조정할 수 있습니다.

def press_e_key():
    while running:
        time.sleep(1)  # 300초 대기
        if running:  # 종료 플래그 확인
            keyboard.press('e')  # 'e' 키 누르기
            time.sleep(5)  # 3초 동안 누르고 있음
            keyboard.release('e')  # 'e' 키 떼기
        time.sleep(1)  # 300초 대기

def stop_program():
    global running
    running = False

# F2 키가 눌리면 프로그램 종료
keyboard.add_hotkey('F2', stop_program)

# 스레드 생성
click_thread = threading.Thread(target=click_continuously)
press_thread = threading.Thread(target=press_e_key)

# 스레드 시작
click_thread.start()
press_thread.start()

# 메인 스레드가 종료되지 않도록 대기
click_thread.join()
press_thread.join()
