from cgitb import reset
from gettext import find
from tkinter import *
import tkinter
from math import *
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
        
################################## GUI 편집 ################################## 54주6191
window = Tk()
window.title("캠핑장 예약하기")
window.geometry("470x415+1380+156")
window.wm_attributes("-topmost", 1)

#울주에서 예약하기
울주lable1=Label(window, text="해양", width=5, height=2)
울주lable1.grid(row=0, column=0)
#로그
울주log1 = Button(window, width=5, padx=10, pady=5, text="NO.1", command=울주_job, bg="orange", fg="black")
울주log1.grid(row=1, column=0)
울주log2 = Button(window, width=5, padx=10, pady=5, text="NO.2", command=울주_job, bg="orange", fg="black")
울주log2.grid(row=1, column=1)
울주log3 = Button(window, width=5, padx=10, pady=5, text="NO.3", command=울주_job, bg="orange", fg="black")
울주log3.grid(row=1, column=2)
울주log4 = Button(window, width=5, padx=10, pady=5, text="NO.4", command=울주_job, bg="orange", fg="black")
울주log4.grid(row=1, column=3)
#함수
울주btn1 = Button(window, width=5, padx=10, pady=5, text="Saturday", command=울주_토요일, bg="white", fg="black")
울주btn1.grid(row=2, column=0)
울주btn2 = Button(window, width=5, padx=10, pady=5, text="Range", command=울주_범위선택, bg="white", fg="black")
울주btn2.grid(row=2, column=1)
울주btn3 = Button(window, width=5, padx=10, pady=5, text="This(A)", command=울주_job, bg="green", fg="white")
울주btn3.grid(row=2, column=2)
울주btn4 = Button(window, width=5, padx=10, pady=5, text="This(N)", command=울주_job1, bg="green", fg="white")
울주btn4.grid(row=2, column=3)
울주btn5 = Button(window, width=5, padx=10, pady=5, text="Next(A)", command=울주_job2, bg="green", fg="white")
울주btn5.grid(row=2, column=4)

#태화연에서 예약하기
태화연lable1=Label(window, text="태화연", width=5, height=2)
태화연lable1.grid(row=3, column=0)
#로그
태화연log1 = Button(window, width=5, padx=10, pady=5, text="NO.1", command=태화연_log_id1, bg="orange", fg="black")
태화연log1.grid(row=4, column=0)
태화연log2 = Button(window, width=5, padx=10, pady=5, text="NO.2", command=태화연_log_id2, bg="orange", fg="black")
태화연log2.grid(row=4, column=1)
태화연log3 = Button(window, width=5, padx=10, pady=5, text="NO.3", command=태화연_log_id3, bg="orange", fg="black")
태화연log3.grid(row=4, column=2)
태화연log4 = Button(window, width=5, padx=10, pady=5, text="NO.4", command=태화연_log_id4, bg="orange", fg="black")
태화연log4.grid(row=4, column=3)
태화연log5 = Button(window, width=5, padx=10, pady=5, text="NO.5", command=태화연_log_guest, bg="orange", fg="black")
태화연log5.grid(row=4, column=4)
#함수
태화연btn1 = Button(window, width=5, padx=10, pady=5, text="Reset", command=reset, bg="white", fg="black")
태화연btn1.grid(row=5, column=0)
태화연btn2 = Button(window, width=5, padx=10, pady=5, text="Auto", command=태화연_자동입력, bg="white", fg="black")
태화연btn2.grid(row=5, column=1)
태화연btn3 = Button(window, width=5, padx=10, pady=5, text="Day", command=태화연_날짜선택, bg="white", fg="black")
태화연btn3.grid(row=5, column=2)
태화연btn4 = Button(window, width=5, padx=10, pady=5, text="Range", command=태화연_범위선택, bg="white", fg="black")
태화연btn4.grid(row=5, column=3)
태화연btn5 = Button(window, width=5, padx=10, pady=5, text="Start", command=태화연_job, bg="green", fg="white")
태화연btn5.grid(row=5, column=4)

#대왕암에서 예약하기
대왕암lable1=Label(window, text="대왕암", width=5, height=2)
대왕암lable1.grid(row=6, column=0)
#로그
대왕암log1 = Button(window, width=5, padx=10, pady=5, text="NO.1", command=대왕암_log_id1, bg="orange", fg="black")
대왕암log1.grid(row=7, column=0)
대왕암log2 = Button(window, width=5, padx=10, pady=5, text="NO.2", command=대왕암_log_id2, bg="orange", fg="black")
대왕암log2.grid(row=7, column=1)
대왕암log3 = Button(window, width=5, padx=10, pady=5, text="NO.3", command=대왕암_log_id3, bg="orange", fg="black")
대왕암log3.grid(row=7, column=2)
대왕암log4 = Button(window, width=5, padx=10, pady=5, text="NO.4", command=대왕암_log_id4, bg="orange", fg="black")
대왕암log4.grid(row=7, column=3)
#함수
대왕암btn1 = Button(window, width=5, padx=10, pady=5, text="Reset", command=reset, bg="white", fg="black")
대왕암btn1.grid(row=8, column=0)
대왕암btn2 = Button(window, width=5, padx=10, pady=5, text="Auto", command=대왕암_자동입력, bg="white", fg="black")
대왕암btn2.grid(row=8, column=1)
대왕암btn3 = Button(window, width=5, padx=10, pady=5, text="Day", command=대왕암_날짜선택, bg="white", fg="black")
대왕암btn3.grid(row=8, column=2)
대왕암btn4 = Button(window, width=5, padx=10, pady=5, text="Cursor", command=대왕암_커서선택, bg="white", fg="black")
대왕암btn4.grid(row=8, column=3)
대왕암btn5 = Button(window, width=5, padx=10, pady=5, text="Range", command=대왕암_범위선택, bg="white", fg="black")
대왕암btn5.grid(row=8, column=4)
대왕암btn6 = Button(window, width=5, padx=10, pady=5, text="Karavan", command=대왕암_카라반, bg="green", fg="white")
대왕암btn6.grid(row=8, column=5)
대왕암btn7 = Button(window, width=5, padx=10, pady=5, text="Start", command=대왕암_오토, bg="green", fg="white")
대왕암btn7.grid(row=8, column=6)

#신불산에서 예약하기
신불산lable1=Label(window, text="신불산", width=5, height=2)
신불산lable1.grid(row=9, column=0)
#로그
신불산log1 = Button(window, width=5, padx=10, pady=5, text="NO.1", command=신불산_log_id1, bg="orange", fg="black")
신불산log1.grid(row=10, column=0)
신불산log2 = Button(window, width=5, padx=10, pady=5, text="NO.2", command=신불산_log_id2, bg="orange", fg="black")
신불산log2.grid(row=10, column=1)
신불산log3 = Button(window, width=5, padx=10, pady=5, text="NO.3", command=신불산_log_id3, bg="orange", fg="black")
신불산log3.grid(row=10, column=2)
신불산log4 = Button(window, width=5, padx=10, pady=5, text="NO.4", command=신불산_log_id4, bg="orange", fg="black")
신불산log4.grid(row=10, column=3)
신불산log5 = Button(window, width=5, padx=10, pady=5, text="NO.4", command=태화연_log_guest, bg="orange", fg="black")
신불산log5.grid(row=10, column=4)
#함수
신불산btn1 = Button(window, width=5, padx=10, pady=5, text="Reset", command=reset, bg="white", fg="black")
신불산btn1.grid(row=11, column=0)
신불산btn2 = Button(window, width=5, padx=10, pady=5, text="Auto", command=신불산_자동입력, bg="white", fg="black")
신불산btn2.grid(row=11, column=1)
신불산btn3 = Button(window, width=5, padx=10, pady=5, text="Day", command=신불산_날짜선택, bg="white", fg="black")
신불산btn3.grid(row=11, column=2)
신불산btn4 = Button(window, width=5, padx=10, pady=5, text="Range", command=신불산_범위선택, bg="white", fg="black")
신불산btn4.grid(row=11, column=3)
신불산btn5 = Button(window, width=5, padx=10, pady=5, text="Start", command=신불산_job, bg="green", fg="white")
신불산btn5.grid(row=11, column=4)


window.mainloop()