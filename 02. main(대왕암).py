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

#대왕암 Test 2022.03.17 #Viewer Size 80% #화면 맨아래로 통일

################################## 카카오톡 ################################## 

# 채팅방에 메시지 전송
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
            "text":"Hello, world! 대왕암",
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
            "text":"태화연 확인",
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
    #날짜 클릭
    pag.click(week)
    time.sleep(0.2)
    #검색
    button = pag.locateCenterOnScreen("./image/02._1. reservation.png", region = find_range, confidence=0.85) 
    if (button == None) :
        None      
    else :
        print(button)
        time.sleep(0.2) 
        pag.moveTo(button.x,button.y)
        time.sleep(0.1) 
        pag.click(button.x,button.y, button='left', clicks=5, interval=0.1)
        확인()
        
def 확인() : 
    button1 = pag.locateCenterOnScreen('./image/03._2. next.png', region = (640,88,1198,390),confidence=0.8)   
    print(button1)
    if (button1 == None) :
        확인()      
    else :
        time.sleep(0.2) 
        pag.moveTo(button1.x,button1.y)
        time.sleep(0.1) 
        pag.click(button1.x,button1.y, button='left', clicks=5, interval=0.1)
        kakao_message_me()
        time.sleep(500)

################################## GUI 편집 ################################## 

root = Tk()
root.title("태화연")
root.geometry("430x100+1980+0")
root.wm_attributes("-topmost", 1)

#전송할 카카오톡 이름
def 카카오톡_입력():
    global kakao_opentalk_name
    kakao_opentalk_name = e.get()
    print(kakao_opentalk_name)

lable1=Label(root, text="카카오톡 이름")
lable1.pack()

#버튼 기능
# 541, 590, 645, 699, 755 
def 테스트():
    global week
    week = 717,646 
    
def 금요일():
    global week
    week = 785,646

def 토요일():
    global week
    week = 851,646

def 호수뷰():
    global find_range
    find_range = (1250,527,1391,922)

def 전체():
    global find_range
    find_range = (1250,527,1391,922)

def job():
    while True:
        검색()
        pag.click(1381,638)
        time.sleep(1)
        검색()
        pag.click(1381,583)
        time.sleep(1)
        if keyboard.is_pressed("F4"): # F4 누른게 감지되면
            break

#  이미지 관련 ☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆


                   
e = Entry(root, width=30)
e.pack()
e.insert(0,"박정철")

btn = Button(root, padx=10, pady=5, text="테 스 트", command=테스트, bg="green", fg="white")
btn.pack(side=LEFT)
btn1 = Button(root, padx=10, pady=5, text="금 요 일", command=금요일, bg="green", fg="white")
btn1.pack(side=LEFT)
btn2 = Button(root, padx=10, pady=5, text="토 요 일", command=토요일, bg="green", fg="white")
btn2.pack(side=LEFT)
btn3 = Button(root, padx=10, pady=5, text="호 수 뷰", command=호수뷰, bg="blue", fg="white")
btn3.pack(side=LEFT)
btn4 = Button(root, padx=10, pady=5, text="전    체", command=전체, bg="blue", fg="white")
btn4.pack(side=LEFT)
btn5 = Button(root, padx=10, pady=5, text="태 화 연", command=job, bg="red", fg="white")
btn5.pack(side=LEFT)

root.mainloop()