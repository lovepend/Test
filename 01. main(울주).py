from gettext import find
import pyautogui as pag
import win32con
import win32api
import win32gui
import keyboard
import time
import pyperclip
#import clipboard
from tkinter import *
#import schedule

#울주해양예약 시스템 2022.01.11 #Vier Size 67%

# 카카오톡 관련 ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆

# 채팅방에 메시지 전송
def kakao_sendtext(chatroom_name, text):
    #핸들 _ 채팅방
    hwndMain = win32gui.FindWindow( None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)
    # hwndListControl = win32gui.FindWindowEx( hwndMai
    # n, None, "EVA_VH_ListControl_Dblclk", None)
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)

# 채팅방에 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

# 채팅방 열기
def open_chatroom(chatroom_name):
    # 채팅방 목록 검색하는 Edit (채팅방이 열려있지 않아도 전송 가능하기 위하여)
    hwndkakao = win32gui.FindWindow(None, "카카오톡")
    hwndkakao_edit1 = win32gui.FindWindowEx( hwndkakao, None, "EVA_ChildWindow", None)
    hwndkakao_edit2_1 = win32gui.FindWindowEx( hwndkakao_edit1, None, "EVA_Window", None)
    hwndkakao_edit2_2 = win32gui.FindWindowEx( hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
    hwndkakao_edit3 = win32gui.FindWindowEx( hwndkakao_edit2_2, None, "Edit", None)

    #Edit에 검색 _ 입력되어있는 텍스트가 있어도 덮어쓰기됨
    win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
    time.sleep(0.1)   # 안정성 위해 필요
    SendReturn(hwndkakao_edit3)
    time.sleep(0.1)

#카카오톡 메세지 보내기
def kakao_sendmessage(kakao_opentalk_name, text):
    open_chatroom(kakao_opentalk_name)  # 채팅방 열기
    kakao_sendtext(kakao_opentalk_name, text)    # 메시지 전송
    kakao_sendtext(kakao_opentalk_name, text[60:80])    # 메시지 전송

#  이미지 관련 ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆



def 검색():
    Saturday = 1164,102,1263,1080 #토요일만 검색 
    
    button = pag.locateCenterOnScreen('./image/01_0. reservation1.png', region = Saturday,confidence=0.9)
    if (button == None) :
        None        
    else :
        Friday = ((button.x)-150, (button.y)-8, (button.x)-100, (button.y+8))
        button_1 = pag.locateCenterOnScreen('./image/01_0. reservation2.png', region = Friday,confidence=0.9) #토요일 찾을 범위 설정      
        
        print("일박",button)
        print("연박",button_1)
        pag.click(button_1,button='left')     
        보안문자_보내기()

#카카오톡 보안문자 캡처 및 전송
def 보안문자_보내기():
    #화면클릭
    pag.click(1800,800)
    time.sleep(0.1)
    #보안문자 이미지 저장
    pag.click(754,1001,button='right')
    time.sleep(0.1)
    pag.click(872,680)
    time.sleep(0.1)
    #카카오톡 선택
    pag.click(3804,83)
    time.sleep(0.1)
    #카카오톡 보안문자 전송
    pag.hotkey('Ctrl','v')
    time.sleep(0.1)
    pag.hotkey('enter')
    time.sleep(0.1)
    #URL 전송
    pag.click(650,53)
    time.sleep(0.1)
    pag.hotkey('ctrl', 'c')
    url = pyperclip.paste()
    kakao_sendmessage("박정철", url)
    #기간
    pag.click(x=907, y=750)
    pag.hotkey('end')
    pag.sleep(0.1)
    #총인원
    pag.click(x=1019, y=747)
    pag.hotkey('end')
    #페이지 선택
    pag.click(1600,800)
    #페이지 아래
    pag.hotkey('end')
    time.sleep(0.1)
    #카카오톡 선택
    pag.click(3804,83)
    time.sleep(0.1)
    보안문자_받기()
    
def 보안문자_받기():
    text1 = pag.locateOnScreen('./image/01_9. security.png', region = (0,0,1920,1680), confidence=0.9) #reservation 100%
    if (text1 == None) :
        보안문자_받기()
    else :
        #보안문자 더블 클릭
        pag.doubleClick(89,285)
        #보안문자 받고 입력 하기 
        time.sleep(0.1)
        #보안문자 복사
        pag.hotkey('ctrl', 'c')
        time.sleep(0.1)
        #보안문자 붙여넣기
        pag.click(x=770, y=195)
        time.sleep(0.1)
        pag.hotkey('ctrl', 'v')
        time.sleep(0.1)
        자동결제()
    

#  자동 일력★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
#정보 입력 기간, 인원
def 결제_page1():
    #다음 클릭
    buttonpostion1 = pag.locateCenterOnScreen('./image/01_1. next.png', region = (0,0,1920,1680), confidence=0.8) #reservation 67%
    pag.click(buttonpostion1.x-30,buttonpostion1.y)
    time.sleep(0.1) #다음 페이지
    결제_page2()
#도착시간 차량설정
def 결제_page2():
    #페이지 선택
    pag.click(1600,800)
    #페이지 아래
    pag.hotkey('end')
    time.sleep(0.2)
    buttonpostion2_1 = pag.locateCenterOnScreen('./image/01_2. payment1.png', region = (0,0,1920,1680), confidence=0.6) #reservation 67%    
    if (buttonpostion2_1 == None) :
        결제_page2()
    else :
        #도착예정시간 선택
        #pag.click(buttonpostion2_1.x,buttonpostion2_1.y)
        pag.click(774,246)
        time.sleep(0.1)
        pag.hotkey('down')
        #페이지 선택
        #pag.click(1600,800)
        #개인정보수집 동의
        buttonpostion2_2 = pag.locateCenterOnScreen('./image/01_2. payment2.png', region = (0,0,1920,1680), confidence=0.6) #reservation 67%    
        pag.click(buttonpostion2_2.x,buttonpostion2_2.y)
        
        #결제 선택
        buttonpostion2_3 = pag.locateCenterOnScreen('./image/01_2. payment3.png', region = (0,0,1920,1680), confidence=0.6) #reservation 67%
        pag.click(buttonpostion2_3.x-30,buttonpostion2_3.y)
        time.sleep(0.2)
        결제_page3()
        
#신용카드결제
def 결제_page3():
    #신용카드결제 
    buttonpostion3_1 = pag.locateCenterOnScreen('./image/01_3. next1.png', region = (0,0,1920,1680), confidence=0.7) 
    if (buttonpostion3_1 == None):
        결제_page3()
    else :        
        pag.click(buttonpostion3_1.x-35,buttonpostion3_1.y) 
        #전체동의
        buttonpostion3_2 = pag.locateCenterOnScreen('./image/01_3. next2.png', region = (0,0,1920,1680), confidence=0.7) 
        #다음
        time.sleep(0.1)
        pag.click(buttonpostion3_2.x+30,buttonpostion3_2.y)
        time.sleep(0.1)
        결제_page4()
        
#카드선택
def 결제_page4():
    #국민 카드 선택
    buttonpostion4_1 = pag.locateCenterOnScreen('./image/01_4. next1.png', region = (0,0,1920,1680), confidence=0.7) 
    if (buttonpostion4_1 == None):
        결제_page4()
    else :
        #국민카드 선택
        time.sleep(0.1)
        pag.click(buttonpostion4_1.x,buttonpostion4_1.y)
        time.sleep(0.1)
        #결제 동의 
        buttonpostion4_2 = pag.locateCenterOnScreen('./image/01_4. next2.png', region = (0,0,1920,1680), confidence=0.7) 
        
        pag.click(buttonpostion4_2.x,buttonpostion4_2.y) 
        #다음
        buttonpostion4_3 = pag.locateCenterOnScreen('./image/01_4. next3.png', region = (0,0,1920,1680), confidence=0.7) 
        time.sleep(0.1)
        pag.click(buttonpostion4_3.x,buttonpostion4_3.y) 
        time.sleep(0.1)
        결제_page5()
        
#앱결제
def 결제_page5():
    buttonpostion5 = pag.locateCenterOnScreen('./image/01_5. payment.png', region = (0,0,1920,1680), confidence=0.7) #reservation 67%
    if (buttonpostion5 == None):
        결제_page5()
    else :
        #앱결제
        pag.click(buttonpostion5.x,buttonpostion5.y)
        결제_page6()

#결제코드보내기       
def 결제_page6():
    button6 = pag.locateCenterOnScreen('./image/01_6. payment.png', region = (0,0,1920,1680), confidence=0.7)
    if (button6 == None):
        결제_page6()
    else :
        #코드보내기
        time.sleep(0.1)
        pag.click(1034,603)
        time.sleep(0.1)
        pag.dragTo(1171,660, 0.2, button='left')
        time.sleep(0.1)
        pag.hotkey('ctrl', 'c')
        결제코드 = pyperclip.paste() 
        kakao_sendmessage("박정철", 결제코드)
        결제_page7()
        
#이메일 확인
def 결제_page7():
    buttonpostion7 = pag.locateCenterOnScreen('./image/01_7. next1.png', region = (0,0,1920,1680), confidence=0.9) #reservation 67%
    if (buttonpostion7 == None):
        결제_page7()
    else :
        #이메일 발송
        buttonpostion7_1 = pag.locateCenterOnScreen('./image/01_7. next2.png', region = (0,0,1920,1680), confidence=0.9) #reservation 67%
        pag.click(buttonpostion7_1.x,buttonpostion7_1.y)
#완료!!!
def 결제_page8():
    buttonpostion8 = pag.locateCenterOnScreen('./image/01_8. next1.png', region = (0,0,1920,1680), confidence=0.9) #reservation 67%
    if (buttonpostion8 == None):
        결제_page8()
    else :
        #이메일 발송
        pag.click(buttonpostion8.x+50,buttonpostion8.y)
        pag.hotkey('enter')
        time.sleep(0.1)   
        pag.hotkey('esc')
        time.sleep(0.1)
        pag.hotkey('enter')
        time.sleep(0.1)
        pag.hotkey('esc')
        
        
def 자동결제():
    결제_page1()


def 수동결제():
    #기간
    pag.click(1600,800)
    pag.hotkey('home')
    pag.sleep(0.3)
    pag.click(x=907, y=750)
    pag.hotkey('pagedown')
    pag.sleep(0.3)
    #총인원
    pag.click(x=1019, y=747)
    pag.hotkey('pagedown')
    #페이지 선택
    pag.click(1600,800)
    #페이지 아래
    pag.hotkey('end')
    time.sleep(0.5)
    결제_page1()

     
def log():
    loggin = pag.locateCenterOnScreen('./image/01_10. loggin.png', region = (1100,0,1250,204), confidence=0.8)
    if (loggin == None):
        None
    else :
        #코드보내기
        pag.click(loggin.x,loggin.y)
        time.sleep(1)
        pag.click(876,442)
        time.sleep(1)
        pag.hotkey('down')
        time.sleep(1)
        pag.hotkey('enter')
        time.sleep(1)
        pag.hotkey('enter')
        time.sleep(1)        
        pag.click(1239,162)
        time.sleep(1)        
        pag.click(1239,162)
        
def log1():
    loggin = pag.locateCenterOnScreen('./image/01_10. loggin.png', region = (1100,0,1250,204), confidence=0.8)
    if (loggin == None):
        None
    else :
        #코드보내기
        pag.click(loggin.x,loggin.y)
        time.sleep(1)
        pag.click(876,442)
        time.sleep(1)
        pag.hotkey('down')
        time.sleep(1)
        pag.hotkey('enter')
        time.sleep(1)
        pag.hotkey('enter')
        time.sleep(1)        
        pag.click(1239,162)
        time.sleep(1)        
        pag.click(1239,162)
        #다음달 선택
        time.sleep(2)
        pag.click(986,429)
        #페이지 선택
        time.sleep(2)
        pag.click(1600,800)



def job():
    while True:
        #페이지 선택
        pag.click(1600,800)
        log()
        pag.hotkey('f5')
        time.sleep(0.3)
        검색()
        pag.hotkey('pagedown')
        time.sleep(0.3)
        검색()
        pag.hotkey('home')
        time.sleep(0.3)
        if keyboard.is_pressed("F4"): # F4 누른게 감지되면
            break

def job1():
    while True:
        #페이지 선택
        pag.click(1600,800)
        log1()
        pag.hotkey('f5')
        time.sleep(0.3)
        검색()
        pag.hotkey('pagedown')
        time.sleep(0.3)
        검색()
        pag.hotkey('home')
        time.sleep(0.3)
        if keyboard.is_pressed("F4"): # F4 누른게 감지되면
            break
################################## GUI 편집 ################################## 

root = Tk()
root.title("울주해양")
root.geometry("290x100+1580+0")
root.wm_attributes("-topmost", 1)

#전송할 카카오톡 이름
def 카카오톡_입력():
    global kakao_opentalk_name
    kakao_opentalk_name = e.get()
    print(kakao_opentalk_name)

lable1=Label(root, text="카카오톡 이름")
lable1.pack()
    
e = Entry(root, width=30)
e.pack()
e.insert(0,"박정철")

btn1 = Button(root, padx=10, pady=5, text="이 번 달", command=job, bg="red", fg="white")
btn1.pack(side=LEFT)

btn2 = Button(root, padx=10, pady=5, text="다 음 달", command=job1, bg="blue", fg="white")
btn2.pack(side=LEFT)

btn3 = Button(root, padx=10, pady=5, text="보안문자", command=보안문자_보내기, bg="green", fg="white")
btn3.pack(side=LEFT)

btn4 = Button(root, padx=10, pady=5, text="자동입력", command=수동결제, bg="black", fg="white")
btn4.pack(side=LEFT)


root.mainloop()