from cgitb import reset
from gettext import find
from tkinter import *
import tkinter
from math import *
from turtle import bgcolor, color, width
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
from 육부촌 import *
from kakao_api import *
from Test import *


def schedule_job():
    schedule.every().day.at("08:45:00").do(신불산_자동) 
    schedule.every().day.at("09:45:00").do(태화연_자동) 
    schedule.every().day.at("10:55:00").do(대왕암_자동) 
    schedule.every().day.at("13:45:00").do(신불산_자동) 
    schedule.every().day.at("15:45:00").do(태화연_자동) 
    schedule.every().day.at("14:55:00").do(대왕암_자동) 
    while True:
        schedule.run_pending()

################################## GUI 편집 ################################## 54주6191
window = Tk()
window.title("캠핑장 예약하기")
window.geometry("470x150+1380+156")
window.wm_attributes("-topmost", 1)

notebook=tkinter.ttk.Notebook(window, width=460, height=125)
notebook.pack()

frame1=tkinter.Frame(window)
notebook.add(frame1, text="★Auto" )

#스케쥴 진행
Autobtn1 = Button(frame1, width=5, padx=10, pady=5, text="스케쥴러", command=schedule_job, bg="orange", fg="black")
Autobtn1.place(x=0, y=10)
Autobtn1 = Button(frame1, width=5, padx=10, pady=5, text="육부촌", command=육부촌_Start, bg="orange", fg="black")
Autobtn1.place(x=60, y=10)

###################
frame2=tkinter.Frame(window)
notebook.add(frame2, text="★울주해양" )

#울주에서 예약하기
#로그
울주log1 = Button(frame2, width=5, padx=10, pady=5, text="NO.1", command=울주_log_id1, bg="orange", fg="black")
울주log1.place(x=0, y=10)
울주log2 = Button(frame2, width=5, padx=10, pady=5, text="NO.2", command=울주_log_id2, bg="orange", fg="black")
울주log2.place(x=60, y=10)
울주log3 = Button(frame2, width=5, padx=10, pady=5, text="NO.3", command=울주_log_id3, bg="orange", fg="black")
울주log3.place(x=120, y=10)
울주log4 = Button(frame2, width=5, padx=10, pady=5, text="NO.4", command=울주_log_id4, bg="orange", fg="black")
울주log4.place(x=180, y=10)
#함수
울주btn1 = Button(frame2, width=5, padx=10, pady=5, text="Saturday", command=울주_토요일, bg="white", fg="black")
울주btn1.place(x=0, y=50)

울주btn2 = Button(frame2, width=5, padx=10, pady=5, text="Range", command=울주_범위선택, bg="white", fg="black")
울주btn2.place(x=60, y=50)
울주btn3 = Button(frame2, width=5, padx=10, pady=5, text="This(A)", command=울주_This_A, bg="green", fg="white")
울주btn3.place(x=120, y=50)
울주btn4 = Button(frame2, width=5, padx=10, pady=5, text="This(N)", command=울주_This_N, bg="green", fg="white")
울주btn4.place(x=180, y=50)
울주btn5 = Button(frame2, width=5, padx=10, pady=5, text="Next(A)", command=울주_Next_A, bg="green", fg="white")
울주btn5.place(x=240, y=50)
울주btn5 = Button(frame2, width=5, padx=10, pady=5, text="Next(N)", command=울주_Next_N, bg="green", fg="white")
울주btn5.place(x=300, y=50)
울주btn6 = Button(frame2, width=5, padx=10, pady=5, text="Auto", command=울주_자동, bg="green", fg="white")
울주btn6.place(x=360, y=50)


frame3=tkinter.Frame(window)
notebook.add(frame3, text="★태화연★")

#로그
태화연log1 = Button(frame3, width=5, padx=10, pady=5, text="NO.1", command=태화연_Log_Id1, bg="orange", fg="black")
태화연log1.place(x=0, y=10)
태화연log2 = Button(frame3, width=5, padx=10, pady=5, text="NO.2", command=태화연_Log_Id2, bg="orange", fg="black")
태화연log2.place(x=60, y=10)
태화연log3 = Button(frame3, width=5, padx=10, pady=5, text="NO.3", command=태화연_Log_Id3, bg="orange", fg="black")
태화연log3.place(x=120, y=10)
태화연log4 = Button(frame3, width=5, padx=10, pady=5, text="NO.4", command=태화연_Log_Id4, bg="orange", fg="black")
태화연log4.place(x=180, y=10)
태화연log5 = Button(frame3, width=5, padx=10, pady=5, text="NO.5", command=태화연_Log_Guest, bg="orange", fg="black")
태화연log5.place(x=240, y=10)
#날짜
태화연btn1 = Button(frame3, width=5, padx=10, pady=5, text="Day1", command=태화연_Day1, bg="white", fg="black")
태화연btn1.place(x=0, y=50)
태화연btn2 = Button(frame3, width=5, padx=10, pady=5, text="Day2", command=태화연_Day2, bg="white", fg="black")
태화연btn2.place(x=60, y=50)
태화연btn3 = Button(frame3, width=5, padx=10, pady=5, text="Day3", command=태화연_Day3, bg="white", fg="black")
태화연btn3.place(x=120, y=50)
태화연btn4 = Button(frame3, width=5, padx=10, pady=5, text="Day4", command=태화연_Day4, bg="white", fg="black")
태화연btn4.place(x=180, y=50)
태화연btn5 = Button(frame3, width=5, padx=10, pady=5, text="Day", command=태화연_Day, bg="green", fg="white")
태화연btn5.place(x=240, y=50)
#함수
태화연btn1 = Button(frame3, width=5, padx=10, pady=5, text="Reset", command=태화연_Reset, bg="white", fg="black")
태화연btn1.place(x=0, y=90)
태화연btn2 = Button(frame3, width=5, padx=10, pady=5, text="Auto", command=태화연_자동입력, bg="white", fg="black")
태화연btn2.place(x=60, y=90)
태화연btn3 = Button(frame3, width=5, padx=10, pady=5, text="Range", command=태화연_범위선택, bg="white", fg="black")
태화연btn3.place(x=120, y=90)
태화연btn4 = Button(frame3, width=5, padx=10, pady=5, text="Start", command=태화연_Start, bg="white", fg="black")
태화연btn4.place(x=180, y=90)
태화연btn5 = Button(frame3, width=5, padx=10, pady=5, text="Start(A)", command=태화연_자동, bg="green", fg="white")
태화연btn5.place(x=240, y=90)
태화연btn5 = Button(frame3, width=5, padx=10, pady=5, text="Enter", command=태화연_자동, bg="green", fg="white")
태화연btn5.place(x=300, y=90)

#신불산 UI===============================================================================================================
frame4=tkinter.Frame(window)
notebook.add(frame4, text="★신불산★")

#로그
신불산log1 = Button(frame4, width=5, padx=10, pady=5, text="NO.1", command=신불산_Log_Id1, bg="orange", fg="black")
신불산log1.place(x=0, y=10)
신불산log2 = Button(frame4, width=5, padx=10, pady=5, text="NO.2", command=신불산_Log_Id2, bg="orange", fg="black")
신불산log2.place(x=60, y=10)
신불산log3 = Button(frame4, width=5, padx=10, pady=5, text="NO.3", command=신불산_Log_Id3, bg="orange", fg="black")
신불산log3.place(x=120, y=10)
신불산log4 = Button(frame4, width=5, padx=10, pady=5, text="NO.4", command=신불산_Log_Id4, bg="orange", fg="black")
신불산log4.place(x=180, y=10)
신불산log5 = Button(frame4, width=5, padx=10, pady=5, text="NO.G", command=신불산_Log_Guest, bg="orange", fg="black")
신불산log5.place(x=240, y=10)
#날짜
신불산day1 = Button(frame4, width=5, padx=10, pady=5, text="Day1", command=신불산_Day1, bg="white", fg="black")
신불산day1.place(x=0, y=50)
신불산day2 = Button(frame4, width=5, padx=10, pady=5, text="Day2", command=신불산_Day2, bg="white", fg="black")
신불산day2.place(x=60, y=50)
신불산day3 = Button(frame4, width=5, padx=10, pady=5, text="Day3", command=신불산_Day3, bg="white", fg="black")
신불산day3.place(x=120, y=50)
신불산day4 = Button(frame4, width=5, padx=10, pady=5, text="Day4", command=신불산_Day4, bg="white", fg="black")
신불산day4.place(x=180, y=50)
신불산day5 = Button(frame4, width=5, padx=10, pady=5, text="Day", command=신불산_Day, bg="green", fg="white")
신불산day5.place(x=240, y=50)
#함수
신불산btn1 = Button(frame4, width=5, padx=10, pady=5, text="Reset", command=신불산_Reset, bg="white", fg="black")
신불산btn1.place(x=0, y=90)
신불산btn2 = Button(frame4, width=5, padx=10, pady=5, text="Auto", command=신불산_자동입력, bg="white", fg="black")
신불산btn2.place(x=60, y=90)
신불산btn3 = Button(frame4, width=5, padx=10, pady=5, text="Range", command=신불산_범위선택, bg="white", fg="black")
신불산btn3.place(x=120, y=90)
신불산btn4 = Button(frame4, width=5, padx=10, pady=5, text="Start", command=신불산_Start, bg="white", fg="black")
신불산btn4.place(x=180, y=90)
신불산btn5 = Button(frame4, width=5, padx=10, pady=5, text="Start(A)", command=신불산_자동, bg="green", fg="white")
신불산btn5.place(x=240, y=90)

#lable1=Label(frame4, width=5, padx=10, pady=5, text="i 입력")
#lable1.place(x=330, y=0)


#대왕암 UI===============================================================================================================
frame5=tkinter.Frame(window)
notebook.insert(2, frame5, text="★대왕암★")

#로그
대왕암log1 = Button(frame5, width=5, padx=10, pady=5, text="NO.1", command=대왕암_Log_Id1, bg="orange", fg="black")
대왕암log1.place(x=0, y=10)
대왕암log2 = Button(frame5, width=5, padx=10, pady=5, text="NO.2", command=대왕암_Log_Id2, bg="orange", fg="black")
대왕암log2.place(x=60, y=10)
대왕암log3 = Button(frame5, width=5, padx=10, pady=5, text="NO.3", command=대왕암_Log_Id3, bg="orange", fg="black")
대왕암log3.place(x=120, y=10)
대왕암log4 = Button(frame5, width=5, padx=10, pady=5, text="NO.4", command=대왕암_Log_Id4, bg="orange", fg="black")
대왕암log4.place(x=180, y=10)
#날짜
대왕암btn1 = Button(frame5, width=5, padx=10, pady=5, text="Day1", command=대왕암_Day1, bg="white", fg="black")
대왕암btn1.place(x=0, y=50)
대왕암btn2 = Button(frame5, width=5, padx=10, pady=5, text="Day2", command=대왕암_Day2, bg="white", fg="black")
대왕암btn2.place(x=60, y=50)
대왕암btn3 = Button(frame5, width=5, padx=10, pady=5, text="Day3", command=대왕암_Day3, bg="white", fg="black")
대왕암btn3.place(x=120, y=50)
대왕암btn4 = Button(frame5, width=5, padx=10, pady=5, text="Day4", command=대왕암_Day4, bg="white", fg="black")
대왕암btn4.place(x=180, y=50)
대왕암btn5 = Button(frame5, width=5, padx=10, pady=5, text="Day", command=대왕암_Day, bg="white", fg="black")
대왕암btn5.place(x=240, y=50)
#함수
대왕암btn1 = Button(frame5, width=5, padx=10, pady=5, text="Reset", command=대왕암_Reset, bg="white", fg="black")
대왕암btn1.place(x=0, y=90)
대왕암btn2 = Button(frame5, width=5, padx=10, pady=5, text="Auto", command=대왕암_자동입력, bg="white", fg="black")
대왕암btn2.place(x=60, y=90)
대왕암btn3 = Button(frame5, width=5, padx=10, pady=5, text="Cursor", command=대왕암_커서선택, bg="white", fg="black")
대왕암btn3.place(x=120, y=90)
대왕암btn4 = Button(frame5, width=5, padx=10, pady=5, text="Range", command=대왕암_범위선택, bg="white", fg="black")
대왕암btn4.place(x=180, y=90)
대왕암btn5 = Button(frame5, width=5, padx=10, pady=5, text="Start", command=대왕암_Start, bg="white", fg="black")
대왕암btn5.place(x=240, y=90)
대왕암btn6 = Button(frame5, width=5, padx=10, pady=5, text="Karavan", command=대왕암_Karavan, bg="green", fg="white")
대왕암btn6.place(x=300, y=90)
대왕암btn7 = Button(frame5, width=5, padx=10, pady=5, text="Start(A)", command=대왕암_자동, bg="green", fg="white")
대왕암btn7.place(x=360, y=90)

window.mainloop()