from cgitb import reset
from gettext import find
from tkinter import *
import pyautogui as pag
import win32con
import win32api
import win32gui
import keyboard
import clipboard
import pyperclip
import requests
import schedule
import json
import time
from 울주 import *
from 태화연 import *
from 대왕암 import *
from 신불산 import *
from kakao_api import *


        
################################## GUI 편집 ################################## 
root = Tk()
root.title("캠핑장 예약하기")
root.geometry("470x300+1380+0")
root.wm_attributes("-topmost", 1)

#울주에서 예약하기
울주lable1=Label(root, text="울주해양", width=30, height=2)
울주lable1.grid(row=0, columnspan=3)
울주btn1 = Button(root, padx=10, pady=5, text="이번달달", command=울주_job, bg="green", fg="white")
울주btn1.grid(row=1, column=0)
울주btn2 = Button(root, padx=10, pady=5, text="다음달달", command=울주_job1, bg="green", fg="white")
울주btn2.grid(row=1, column=1)
울주btn3 = Button(root, padx=10, pady=5, text="다음달순", command=울주_job2, bg="green", fg="white")
울주btn3.grid(row=1, column=2)
울주btn4 = Button(root, padx=10, pady=5, text="토요고정", command=울주_토요일, bg="white", fg="black")
울주btn4.grid(row=1, column=3)
울주btn5 = Button(root, padx=10, pady=5, text="범위선택", command=울주_범위선택, bg="white", fg="black")
울주btn5.grid(row=1, column=4)

#태화연에서 예약하기
태화연lable1=Label(root, text="태 화 연", width=30, height=2)
태화연lable1.grid(row=2, columnspan=3)
태화연btn1 = Button(root, padx=10, pady=5, text="초기셋팅", command=reset, bg="orange", fg="black")
태화연btn1.grid(row=3, column=0)
태화연btn2 = Button(root, padx=10, pady=5, text="날짜선택", command=태화연_날짜선택, bg="white", fg="black")
태화연btn2.grid(row=3, column=1)
태화연btn3 = Button(root, padx=10, pady=5, text="자동입력", command=태화연_자동입력, bg="white", fg="black")
태화연btn3.grid(row=3, column=2)
태화연btn4 = Button(root, padx=10, pady=5, text="범위선택", command=태화연_범위선택, bg="white", fg="black")
태화연btn4.grid(row=3, column=3)
태화연btn5 = Button(root, padx=10, pady=5, text="작업시작", command=태화연_job, bg="green", fg="white")
태화연btn5.grid(row=3, column=4)

#대왕암에서 예약하기
대왕암lable1=Label(root, text="대 왕 암", width=30, height=2)
대왕암lable1.grid(row=4, columnspan=3)
대왕암btn1 = Button(root, padx=10, pady=5, text="초기셋팅", command=reset, bg="orange", fg="black")
대왕암btn1.grid(row=5, column=0)
대왕암btn2 = Button(root, padx=10, pady=5, text="날짜선택", command=대왕암_날짜선택, bg="white", fg="black")
대왕암btn2.grid(row=5, column=1)
대왕암btn3 = Button(root, padx=10, pady=5, text="커서선택", command=대왕암_커서선택, bg="white", fg="black")
대왕암btn3.grid(row=5, column=2)
대왕암btn4 = Button(root, padx=10, pady=5, text="범위선택", command=대왕암_범위선택, bg="white", fg="black")
대왕암btn4.grid(row=5, column=3)
대왕암btn5 = Button(root, padx=10, pady=5, text="대왕카라", command=대왕암_카라반, bg="green", fg="white")
대왕암btn5.grid(row=5, column=4)
대왕암btn6 = Button(root, padx=10, pady=5, text="대왕오토", command=대왕암_오토, bg="green", fg="white")
대왕암btn6.grid(row=5, column=5)

#신불산에서 예약하기
신불산lable1=Label(root, text="신 불 산", width=30, height=2)
신불산lable1.grid(row=6, columnspan=3)
신불산btn1 = Button(root, padx=10, pady=5, text="초기셋팅", command=reset, bg="orange", fg="black")
신불산btn1.grid(row=7, column=0)
신불산btn2 = Button(root, padx=10, pady=5, text="날짜선택", command=신불산_날짜선택, bg="white", fg="black")
신불산btn2.grid(row=7, column=1)
신불산btn3 = Button(root, padx=10, pady=5, text="범위선택", command=신불산_범위선택, bg="white", fg="black")
신불산btn3.grid(row=7, column=2)
신불산btn4 = Button(root, padx=10, pady=5, text="신불산고", command=신불산_job, bg="green", fg="white")
신불산btn4.grid(row=7, column=3)


root.mainloop()