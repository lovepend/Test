from gettext import find
import pyautogui as pag
import win32con
import win32api
import win32gui
import keyboard
import time
import pyperclip
from tkinter import *
import requests
import json
#import clipboard
#import schedule

#신불산 Test 2022.03.21 #Viewer Size 67%

################################## 카카오톡 ################################## 

# 채팅방에 메시지 전송

# 카카오톡 메시지 API
def refresh_token():
    url = "https://kauth.kakao.com/oauth/token"
    #url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

    data = {
        "grant_type": "refresh_token",
        "client_id": "ddcfd4509dc2ec690ebb764199ff2247",
        #"refresh_token": "{refresh_token}"
        "refresh_token": "CsrbYjjznXydtF3QoSHWF8a9nfjBYQ_oZ0BAxwo9c-wAAAF_mkcY_Q"
    }
    response = requests.post(url, data=data)
    tokens = response.json()

    # kakao_code.json 파일 저장
    with open("kakao_token.json", "w") as fp:
        json.dump(tokens, fp)
        
def kakao_message_me():

    #2.
    with open("kakao_token.json","r") as fp:
        tokens = json.load(fp)

    url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

    # kapi.kakao.com/v2/api/talk/memo/default/send 

    headers={
        "Authorization" : "Bearer " + tokens["access_token"]
    }

    data={
        "template_object": json.dumps({
            "object_type":"text",
            "text":"Hello, world! 신불산",
            "link":{
                "web_url":"www.naver.com"
            }
        })
    }

    response = requests.post(url, headers=headers, data=data)
    response.status_code
    
def kakao_message_you():
        
    with open("kakao_token.json","r") as fp:
        tokens = json.load(fp)
    # print(tokens)
    # print(tokens["access_token"])

    friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

    # GET /v1/api/talk/friends HTTP/1.1
    # Host: kapi.kakao.com
    # Authorization: Bearer {ACCESS_TOKEN}

    headers={"Authorization" : "Bearer " + tokens["access_token"]}

    result = json.loads(requests.get(friend_url, headers=headers).text)

    print(type(result))
    print("=============================================")
    print(result)
    print("=============================================")
    friends_list = result.get("elements")
    print(friends_list)
    # print(type(friends_list))
    print("=============================================")
    print(friends_list[0].get("uuid"))
    friend_id = friends_list[0].get("uuid")
    print(friend_id)


    send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"

    data={
        'receiver_uuids': '["{}"]'.format(friend_id),
        "template_object": json.dumps({
            "object_type":"text",
            "text":"신불산 확인",
            "link":{
                "web_url":"www.daum.net",
                "web_url":"www.naver.com"
            },
            "button_title": "바로 확인"
        })
    }

    response = requests.post(send_url, headers=headers, data=data)
    response.status_code

################################## 기능 편집 ################################## 

def 검색():
    print()
    button = pag.locateCenterOnScreen("./image/04._1. reservation.png", region = find_range, confidence=0.85) 
    if (button == None) :
        None      
    else :
        print(button)
        time.sleep(0.2) 
        pag.moveTo(button.x,button.y)
        time.sleep(0.1) 
        pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
        확인()
        
def 확인() : 
    button1 = pag.locateCenterOnScreen('./image/04._2. next.png', region = (510,100,1324,333), confidence=0.8)   
    print(button1)
    if (button1 == None) :
        확인()      
    else :
        time.sleep(0.2)
        pag.click(1222,282)
        #time.sleep(0.2) 
        #pag.moveTo(button1.x,button1.y)
        #time.sleep(0.1) 
        #pag.click(button1.x,button1.y, button='right', clicks=1, interval=0.1)
        refresh_token()
        kakao_message_you()
        time.sleep(500)

################################## GUI 편집 ################################## 

root = Tk()
root.title("신불산")
root.geometry("460x100+1390+0")
root.wm_attributes("-topmost", 1)

#전송할 카카오톡 이름
def 카카오톡_입력():
    global kakao_opentalk_name
    kakao_opentalk_name = e.get()
    print(kakao_opentalk_name)

e = Entry(root, width=30)
e.pack()
e.insert(0,"박정철")

lable1=Label(root, text="카카오톡 이름")
lable1.pack()

lable1=Label(root, text="날짜선택 -> 범위선택 -> 작업시작(지정은 F4)")
lable1.pack()

#버튼 기능
def 날짜선택():
    while True:
        if keyboard.is_pressed("F4"): 
            global day 
            day  = pag.position()
            print(day)
            time.sleep(0.5)
            break         
        
def 금요일():
    global week
    week = 1342,114

def 토요일():
    global week
    week = 1390,114

def 범위선택():
    while True:
        if keyboard.is_pressed("F4"): 
            global find_range1 
            find_range1  = pag.position()
            print(find_range1)
            time.sleep(0.5)
            break  
    while True:
        if keyboard.is_pressed("F4"): 
            global find_range2 
            find_range2  = pag.position()
            print(find_range2)
            time.sleep(0.5)
            break  
        
    global find_range
    find_range = (find_range1.x,find_range1.y,find_range2.x,find_range2.y)

def 전체():
    global find_range
    find_range = (630,474,1419,1079)

def job():
    while True:
        #날짜 클릭
        pag.click(day)
        time.sleep(0.2)
        #검색
        검색()
        if keyboard.is_pressed("F4"): # F4 누른게 감지되면
            break

#  이미지 관련 ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆

btn0 = Button(root, padx=10, pady=5, text="날짜선택", command=날짜선택, bg="green", fg="white")
btn0.pack(side=LEFT)
btn1 = Button(root, padx=10, pady=5, text="날짜선택", command=날짜선택, bg="green", fg="white")
btn1.pack(side=LEFT)
btn2 = Button(root, padx=10, pady=5, text="날짜선택", command=날짜선택, bg="green", fg="white")
btn2.pack(side=LEFT)
btn3 = Button(root, padx=10, pady=5, text="범위선택", command=범위선택, bg="blue", fg="white")
btn3.pack(side=LEFT)
btn4 = Button(root, padx=10, pady=5, text="범위선택", command=범위선택, bg="blue", fg="white")
btn4.pack(side=LEFT)
btn5 = Button(root, padx=10, pady=5, text="작업시작", command=job, bg="red", fg="white")
btn5.pack(side=LEFT)

root.mainloop()