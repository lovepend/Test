from cgitb import reset
from gettext import find
import tkinter
from tkinter import *
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
window.geometry("470x190+1380+156")
window.wm_attributes("-topmost", 1)

notebook=tkinter.ttk.Notebook(window, width=460, height=165)
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
울주log5 = Button(frame2, width=5, padx=10, pady=5, text="NO.5", command=울주_log_guest, bg="orange", fg="black")
울주log5.place(x=240, y=10)
울주log6 = Button(frame2, width=5, padx=10, pady=5, text="말일", command=울주_특정데이, bg="orange", fg="black")
울주log6.place(x=300, y=10)



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
태화연log6 = Button(frame3, width=5, padx=10, pady=5, text="호수뷰", command=태화연_호수뷰, bg="white", fg="black")
태화연log6.place(x=300, y=10)
#날짜
태화연day1 = Button(frame3, width=2, padx=10, pady=5, text="금", command=태화연_Day11, bg="white", fg="black")
태화연day1.place(x=0, y=50)
태화연day2 = Button(frame3, width=2, padx=10, pady=5, text="토", command=태화연_Day12, bg="white", fg="black")
태화연day2.place(x=30, y=50)
태화연day3 = Button(frame3, width=2, padx=10, pady=5, text="금", command=태화연_Day21, bg="white", fg="black")
태화연day3.place(x=60, y=50)
태화연day4 = Button(frame3, width=2, padx=10, pady=5, text="토", command=태화연_Day22, bg="white", fg="black")
태화연day4.place(x=90, y=50)
태화연day5 = Button(frame3, width=2, padx=10, pady=5, text="금", command=태화연_Day31, bg="white", fg="black")
태화연day5.place(x=120, y=50)
태화연day6 = Button(frame3, width=2, padx=10, pady=5, text="토", command=태화연_Day32, bg="white", fg="black")
태화연day6.place(x=150, y=50)
태화연day7 = Button(frame3, width=2, padx=10, pady=5, text="금", command=태화연_Day41, bg="white", fg="black")
태화연day7.place(x=180, y=50)
태화연day8 = Button(frame3, width=2, padx=10, pady=5, text="토", command=태화연_Day42, bg="white", fg="black")
태화연day8.place(x=210, y=50)
태화연day9 = Button(frame3, width=2, padx=10, pady=5, text="금", command=태화연_Day51, bg="white", fg="black")
태화연day9.place(x=240, y=50)
태화연day10 = Button(frame3, width=2, padx=10, pady=5, text="토", command=태화연_Day52, bg="white", fg="black")
태화연day10.place(x=270, y=50)
태화연day11 = Button(frame3, width=5, padx=10, pady=5, text="Day", command=태화연_Day, bg="green", fg="white")
태화연day11.place(x=300, y=50)   
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

def 시간입력():
    신불산_min = entry1.get()
    신불산_sec = entry2.get()
    시간입력_시작(신불산_min,신불산_sec)


lable1=Label(frame4, text="min")
lable1.place(x=310, y=27)
    
entry1 = Entry(frame4, width=5)
entry1.place(x=310, y=8)
entry1.insert(0,"05")

lable2=Label(frame4, text="sec")
lable2.place(x=360, y=27)
    
entry2 = Entry(frame4, width=5)
entry2.place(x=360, y=8)
entry2.insert(0,"00")

신불산time_s = Button(frame4, width=5, padx=5, pady=5, text="초", command=시간입력, bg="orange", fg="black")
신불산time_s.place(x=410, y=10)



#날짜
신불산day1 = Button(frame4, width=2, padx=10, pady=5, text="금", command=신불산_Day11, bg="white", fg="black")
신불산day1.place(x=0, y=50)
신불산day2 = Button(frame4, width=2, padx=10, pady=5, text="토", command=신불산_Day12, bg="white", fg="black")
신불산day2.place(x=30, y=50)
신불산day3 = Button(frame4, width=2, padx=10, pady=5, text="금", command=신불산_Day21, bg="white", fg="black")
신불산day3.place(x=60, y=50)
신불산day4 = Button(frame4, width=2, padx=10, pady=5, text="토", command=신불산_Day22, bg="white", fg="black")
신불산day4.place(x=90, y=50)
신불산day5 = Button(frame4, width=2, padx=10, pady=5, text="금", command=신불산_Day31, bg="white", fg="black")
신불산day5.place(x=120, y=50)
신불산day6 = Button(frame4, width=2, padx=10, pady=5, text="토", command=신불산_Day32, bg="white", fg="black")
신불산day6.place(x=150, y=50)
신불산day7 = Button(frame4, width=2, padx=10, pady=5, text="금", command=신불산_Day41, bg="white", fg="black")
신불산day7.place(x=180, y=50)
신불산day8 = Button(frame4, width=2, padx=10, pady=5, text="토", command=신불산_Day42, bg="white", fg="black")
신불산day8.place(x=210, y=50)
신불산day9 = Button(frame4, width=2, padx=10, pady=5, text="금", command=신불산_Day51, bg="white", fg="black")
신불산day9.place(x=240, y=50)
신불산day10 = Button(frame4, width=2, padx=10, pady=5, text="토", command=신불산_Day52, bg="white", fg="black")
신불산day10.place(x=270, y=50)
신불산day11 = Button(frame4, width=5, padx=10, pady=5, text="Day", command=신불산_Day, bg="green", fg="white")
신불산day11.place(x=300, y=50)
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

#함수
신불산btn1 = Button(frame4, width=5, padx=10, pady=5, text="Time 0.1", command=신불산_time_controll_01, bg="white", fg="black")
신불산btn1.place(x=0, y=130)
신불산btn2 = Button(frame4, width=5, padx=10, pady=5, text="Time 0.2", command=신불산_time_controll_02, bg="white", fg="black")
신불산btn2.place(x=60, y=130)
신불산btn3 = Button(frame4, width=5, padx=10, pady=5, text="Time 0.3", command=신불산_time_controll_03, bg="white", fg="black")
신불산btn3.place(x=120, y=130)
신불산btn4 = Button(frame4, width=5, padx=10, pady=5, text="Time 0.5", command=신불산_time_controll_05, bg="white", fg="black")
신불산btn4.place(x=180, y=130)
신불산btn5 = Button(frame4, width=5, padx=10, pady=5, text="Time 0.7", command=신불산_time_controll_07, bg="white", fg="black")
신불산btn5.place(x=240, y=130)
신불산btn5 = Button(frame4, width=5, padx=10, pady=5, text="Time 0.9", command=신불산_time_controll_09, bg="white", fg="black")
신불산btn5.place(x=300, y=130)
신불산btn5 = Button(frame4, width=5, padx=10, pady=5, text="Time 0.1", command=신불산_time_controll_10, bg="white", fg="black")
신불산btn5.place(x=360, y=130)


#대왕암 UI===============================================================================================================
frame5=tkinter.Frame(window)
notebook.add(frame5, text="★대왕암★")

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

#테스트 UI===============================================================================================================
frame6=tkinter.Frame(window)
notebook.add(frame6, text="★테스트★")

#로그
테스트log1 = Button(frame6, width=5, padx=10, pady=5, text="NO.1", command="테스트_Log_Id1", bg="orange", fg="black")
테스트log1.place(x=0, y=10)
테스트log2 = Button(frame6, width=5, padx=10, pady=5, text="NO.2", command="테스트_Log_Id2", bg="orange", fg="black")
테스트log2.place(x=60, y=10)
테스트log3 = Button(frame6, width=5, padx=10, pady=5, text="NO.3", command="테스트_Log_Id2", bg="orange", fg="black")
테스트log3.place(x=120, y=10)
테스트log4 = Button(frame6, width=5, padx=10, pady=5, text="NO.4", command="테스트_Log_Id2", bg="orange", fg="black")
테스트log4.place(x=180, y=10)
#날짜
테스트btn1 = Button(frame6, width=5, padx=10, pady=5, text="Day1", command="테스트_Log_Id2", bg="white", fg="black")
테스트btn1.place(x=0, y=50)
테스트btn2 = Button(frame6, width=5, padx=10, pady=5, text="Day2", command="테스트_Log_Id2", bg="white", fg="black")
테스트btn2.place(x=60, y=50)
테스트btn3 = Button(frame6, width=5, padx=10, pady=5, text="Day3", command="테스트_Log_Id2", bg="white", fg="black")
테스트btn3.place(x=120, y=50)
테스트btn4 = Button(frame6, width=5, padx=10, pady=5, text="Day4", command="테스트_Log_Id2", bg="white", fg="black")
테스트btn4.place(x=180, y=50)
테스트btn5 = Button(frame6, width=5, padx=10, pady=5, text="Day", command="테스트_Log_Id2", bg="white", fg="black")
테스트btn5.place(x=240, y=50)
#함수
테스트btn1 = Button(frame6, width=5, padx=10, pady=5, text="Reset", command="테스트_Log_Id2", bg="white", fg="black")
테스트btn1.place(x=0, y=90)
테스트btn2 = Button(frame6, width=5, padx=10, pady=5, text="Auto", command="테스트_Log_Id2", bg="white", fg="black")
테스트btn2.place(x=60, y=90)
테스트btn3 = Button(frame6, width=5, padx=10, pady=5, text="Cursor", command="테스트_Log_Id2", bg="white", fg="black")
테스트btn3.place(x=120, y=90)
테스트btn4 = Button(frame6, width=5, padx=10, pady=5, text="Range", command="테스트_Log_Id2", bg="white", fg="black")
테스트btn4.place(x=180, y=90)
테스트btn5 = Button(frame6, width=5, padx=10, pady=5, text="Start", command="테스트_Log_Id2", bg="white", fg="black")
테스트btn5.place(x=240, y=90)
테스트btn6 = Button(frame6, width=5, padx=10, pady=5, text="Karavan", command="테스트_Log_Id2", bg="green", fg="white")
테스트btn6.place(x=300, y=90)
테스트btn7 = Button(frame6, width=5, padx=10, pady=5, text="Start(A)", command="테스트_Log_Id2", bg="green", fg="white")
테스트btn7.place(x=360, y=90)

window.mainloop()