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
import time
from Camp_11_울주 import *
from Camp_12_울주_줍줍 import *
from Camp_31_태화연 import *
from Camp_41_대왕암 import *
from Camp_21_신불산 import *
from Camp_51_육부촌 import *
from kakao_01_api import *
from Movie_Factory import *
import cv2
cv2.useOptimized()
True


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
window.geometry("250x190+1660+316")
window.wm_attributes("-topmost", 1)

notebook=tkinter.ttk.Notebook(window, width=460, height=165)
notebook.pack()

frame1=tkinter.Frame(window)
notebook.add(frame1, text="1.임시") 

# #스케쥴 진행
Autobtn1 = Button(frame1, width=5, padx=10, pady=5, text="날짜""선택", command=Movie_Factory_Day, bg="orange", fg="black", font = ("", 7))
Autobtn1.place(x=0, y=10)
Autobtn2 = Button(frame1, width=5, padx=10, pady=5, text="시작", command=Movie_Factory, bg="orange", fg="black", font = ("", 7))
Autobtn2.place(x=50, y=10)

#울주 UI=============================================================================================================== 
frame2=tkinter.Frame(window)
notebook.add(frame2, text="2.해양" )

#울주에서 예약하기
#아이디
울주log1 = Button(frame2, width=5, padx=10, pady=5, text="ID.1", command=울주_log_id1, bg="orange", fg="black", font = ("", 7))
울주log1.place(x=0, y=10)
울주log2 = Button(frame2, width=5, padx=10, pady=5, text="ID.2", command=울주_log_id2, bg="orange", fg="black", font = ("", 7))
울주log2.place(x=50, y=10)
울주log3 = Button(frame2, width=5, padx=10, pady=5, text="ID.3", command=울주_log_id3, bg="orange", fg="black", font = ("", 7))
울주log3.place(x=100, y=10)
울주log4 = Button(frame2, width=5, padx=10, pady=5, text="ID.4", command=울주_log_id4, bg="orange", fg="black", font = ("", 7))
울주log4.place(x=150, y=10)
울주log5 = Button(frame2, width=5, padx=10, pady=5, text="ID.5", command=울주_log_guest, bg="orange", fg="black", font = ("", 7))
울주log5.place(x=200, y=10)

lable1=Label(frame2, text="차량번호", font = ("", 7))
lable1.place(x=0, y=37.5)

entry_울주 = Entry(frame2, width=25, borderwidth=2 , font = ("", 7))
entry_울주.place(x=50, y=37.5)
entry_울주.insert(0,"62소9403",)

def 차량번호():
  차량번호 = entry_울주.get()
  울주_차량번호_입력(차량번호)

울주btn12 = Button(frame2, width=5, padx=10, pady=5, text="차량번호", command=차량번호, bg="yellow", fg="black", font = ("", 7))
울주btn12.place(x=200, y=35)

#함수
울주btn1 = Button(frame2, width=5, padx=10, pady=5, text="Saturday", command=울주_토요일, bg="blue", fg="white", font = ("", 7))
울주btn1.place(x=0, y=59)
울주btn2 = Button(frame2, width=5, padx=10, pady=5, text="Range", command=울주_범위선택, bg="white", fg="black", font = ("", 7))
울주btn2.place(x=50, y=59)
울주btn11 = Button(frame2, width=5, padx=10, pady=5, text="앱결제", command=울주_앱결제, bg="blue", fg="white", font = ("", 7))
울주btn11.place(x=100, y=59)
울주btn21 = Button(frame2, width=5, padx=10, pady=5, text="간편결제", command=울주_간편결제, bg="white", fg="black", font = ("", 7))
울주btn21.place(x=150, y=59)
울주btn31 = Button(frame2, width=5, padx=10, pady=5, text="NH간편결제", command=울주_NH_간편결제, bg="white", fg="black", font = ("", 7))
울주btn31.place(x=200, y=59)


울주btn3 = Button(frame2, width=5, padx=10, pady=5, text="This(A)", command=울주_This_A, bg="green", fg="white", font = ("", 7))
울주btn3.place(x=0, y=83)
울주btn4 = Button(frame2, width=5, padx=10, pady=5, text="This(N)", command=울주_This_N, bg="white", fg="black", font = ("", 7))
울주btn4.place(x=50, y=83)
울주btn5 = Button(frame2, width=5, padx=10, pady=5, text="Next(A)", command=울주_Next_A, bg="white", fg="black", font = ("", 7))
울주btn5.place(x=100, y=83)
울주btn5 = Button(frame2, width=5, padx=10, pady=5, text="Next(N)", command=울주_Next_N, bg="white", fg="black", font = ("", 7))
울주btn5.place(x=150, y=83)
울주btn6 = Button(frame2, width=5, padx=10, pady=5, text="울주줍줍", command=울주줍줍_새로고침, bg="green", fg="white", font = ("", 7))
울주btn6.place(x=200, y=83)

#신불산 UI===============================================================================================================
frame3=tkinter.Frame(window)
notebook.add(frame3, text="3.신불")

#로그
신불산log1 = Button(frame3, width=5, padx=10, pady=5, text="ID.1", command=신불산_Log_Id1, bg="orange", fg="black", font = ("", 7))
신불산log1.place(x=0, y=10)
신불산log2 = Button(frame3, width=5, padx=10, pady=5, text="ID.2", command=신불산_Log_Id2, bg="orange", fg="black", font = ("", 7))
신불산log2.place(x=50, y=10)
신불산log3 = Button(frame3, width=5, padx=10, pady=5, text="ID.3", command=신불산_Log_Id3, bg="orange", fg="black", font = ("", 7))
신불산log3.place(x=100, y=10)
신불산log4 = Button(frame3, width=5, padx=10, pady=5, text="ID.4", command=신불산_Log_Id4, bg="orange", fg="black", font = ("", 7))
신불산log4.place(x=150, y=10)
신불산log5 = Button(frame3, width=5, padx=10, pady=5, text="ID.G", command=신불산_Log_Guest, bg="orange", fg="black", font = ("", 7))
신불산log5.place(x=200, y=10)

lable1=Label(frame3, text="분", font = ("", 7))
lable1.place(x=25, y=110)
    
entry1 = Entry(frame3, width=10, font = ("", 7))
entry1.place(x=50, y=110)
entry1.insert(0,"58")

lable2=Label(frame3, text="초", font = ("", 7))
lable2.place(x=125, y=110)
    
entry2 = Entry(frame3, width=10, font = ("", 7))
entry2.place(x=150, y=110)
entry2.insert(0,"00")

def 시간_실시간():
    신불산_min = entry1.get()
    신불산_sec = entry2.get()
    #시간입력_시작(신불산_hour,신불산_min,신불산_sec)
    print(신불산_min,신불산_sec)
    시간입력_실시간(신불산_min,신불산_sec)

def 시간_줍기():
    신불산_min = entry1.get()
    신불산_sec = entry2.get()
    #시간입력_시작1(신불산_hour,신불산_min,신불산_sec)
    print(신불산_min,신불산_sec)
    시간입력_줍기(신불산_min,신불산_sec)

def 시간_줍기1():
    신불산_min = entry1.get()
    신불산_sec = entry2.get()
    #시간입력_시작(신불산_hour,신불산_min,신불산_sec)
    print(신불산_min,신불산_sec)
    시간입력_줍기1(신불산_min,신불산_sec)

# 신불산time_s = Button(frame3, width=5, padx=5, pady=5, text="시작", command=시간입력, bg="orange", fg="black", font = ("", 7))
# 신불산time_s.place(x=400, y=10)


#함수
신불산btn1 = Button(frame3, width=5, padx=10, pady=5, text="0.1", command=신불산_time_controll_01, bg="white", fg="black", font = ("", 7))
신불산btn1.place(x=0, y=35)
신불산btn2 = Button(frame3, width=5, padx=10, pady=5, text="0.2", command=신불산_time_controll_02, bg="white", fg="black", font = ("", 7))
신불산btn2.place(x=50, y=35)
신불산btn3 = Button(frame3, width=5, padx=10, pady=5, text="첫번째", command=신불산_range1, bg="white", fg="black", font = ("", 7))
신불산btn3.place(x=100, y=35)
신불산btn4 = Button(frame3, width=5, padx=10, pady=5, text="두번째", command=신불산_range2, bg="white", fg="black", font = ("", 7))
신불산btn4.place(x=150, y=35)
신불산btn5 = Button(frame3, width=5, padx=10, pady=5, text="세번째", command=신불산_range3, bg="white", fg="black", font = ("", 7))
신불산btn5.place(x=200, y=35)

#날짜
신불산day1 = Button(frame3, width=2, padx=5, pady=5, text="1F", command=신불산_Day11, bg="white", fg="black", font = ("", 7))
신불산day1.place(x=0, y=59)
신불산day2 = Button(frame3, width=2, padx=5, pady=5, text="1S", command=신불산_Day12, bg="white", fg="black", font = ("", 7))
신불산day2.place(x=25, y=59)
신불산day3 = Button(frame3, width=2, padx=5, pady=5, text="2F", command=신불산_Day21, bg="white", fg="black", font = ("", 7))
신불산day3.place(x=50, y=59)
신불산day4 = Button(frame3, width=2, padx=5, pady=5, text="2S", command=신불산_Day22, bg="white", fg="black", font = ("", 7))
신불산day4.place(x=75, y=59)
신불산day5 = Button(frame3, width=2, padx=5, pady=5, text="3F", command=신불산_Day31, bg="white", fg="black", font = ("", 7))
신불산day5.place(x=100, y=59)
신불산day6 = Button(frame3, width=2, padx=5, pady=5, text="3S", command=신불산_Day32, bg="white", fg="black", font = ("", 7))
신불산day6.place(x=125, y=59)
신불산day7 = Button(frame3, width=2, padx=5, pady=5, text="4F", command=신불산_Day41, bg="white", fg="black", font = ("", 7))
신불산day7.place(x=150, y=59)
신불산day8 = Button(frame3, width=2, padx=5, pady=5, text="4S", command=신불산_Day42, bg="white", fg="black", font = ("", 7))
신불산day8.place(x=175, y=59)
신불산day9 = Button(frame3, width=5, padx=10, pady=5, text="Day", command=신불산_Day, bg="blue", fg="white", font = ("", 7))
신불산day9.place(x=200, y=59)


#함수
신불산btn1 = Button(frame3, width=5, padx=10, pady=5, text="Reset", command=신불산_Reset, bg="white", fg="black", font = ("", 7))
신불산btn1.place(x=0, y=83)
신불산btn2 = Button(frame3, width=5, padx=10, pady=5, text="자동입력", command=신불산_자동입력, bg="blue", fg="white", font = ("", 7))
신불산btn2.place(x=50, y=83)
신불산btn3 = Button(frame3, width=5, padx=10, pady=5, text="실시간", command=시간_실시간, bg="white", fg="black", font = ("", 7))
신불산btn3.place(x=100, y=83)
신불산btn4 = Button(frame3, width=5, padx=10, pady=5, text="줍기", command=시간_줍기, bg="green", fg="white", font = ("", 7))
신불산btn4.place(x=150, y=83)
신불산btn5 = Button(frame3, width=5, padx=10, pady=5, text="줍기_V1", command=시간_줍기1, bg="green", fg="white", font = ("", 7))
신불산btn5.place(x=200, y=83)


신불산btn99 = Button(frame3, width=5, padx=10, pady=5, text="동기화", command=시간_동기화, bg="blue", fg="white", font = ("", 7))
신불산btn99.place(x=0, y=130)

#중구 UI===============================================================================================================
frame4=tkinter.Frame(window)
notebook.add(frame4, text="4.중구")

#로그
태화연log1 = Button(frame4, width=5, padx=10, pady=5, text="ID.1", command=태화연_Log_Id1, bg="orange", fg="black", font = ("", 7))
태화연log1.place(x=0, y=10)
태화연log2 = Button(frame4, width=5, padx=10, pady=5, text="ID.2", command=태화연_Log_Id2, bg="orange", fg="black", font = ("", 7))
태화연log2.place(x=50, y=10)
태화연log3 = Button(frame4, width=5, padx=10, pady=5, text="ID.3", command=태화연_Log_Id3, bg="orange", fg="black", font = ("", 7))
태화연log3.place(x=100, y=10)
태화연log4 = Button(frame4, width=5, padx=10, pady=5, text="ID.4", command=태화연_Log_Id4, bg="orange", fg="black", font = ("", 7))
태화연log4.place(x=150, y=10)
태화연log5 = Button(frame4, width=5, padx=10, pady=5, text="ID.5", command=태화연_Log_Guest, bg="orange", fg="black", font = ("", 7))
태화연log5.place(x=200, y=10)


#장소
태화연location1 = Button(frame4, width=5, padx=10, pady=5, text="태화연", command=중구_태화연, bg="white", fg="black", font = ("", 7))
태화연location1.place(x=0, y=35)
태화연location2 = Button(frame4, width=5, padx=10, pady=5, text="황방산", command=중구_황방산, bg="white", fg="black", font = ("", 7))
태화연location2.place(x=50, y=35)
태화연location3 = Button(frame4, width=5, padx=10, pady=5, text="별뜨락", command=중구_별뜨락, bg="white", fg="black", font = ("", 7))
태화연location3.place(x=100, y=35)
태화연location4 = Button(frame4, width=5, padx=10, pady=5, text="입화산", command=중구_입화산, bg="white", fg="black", font = ("", 7))
태화연location4.place(x=150, y=35)

#차량번호
lable1=Label(frame4, text="차량번호", font = ("", 7))
lable1.place(x=0, y=110.5)

entry_중구 = Entry(frame4, width=10, font = ("", 7))
entry_중구.place(x=50, y=110.5)
entry_중구.insert(50,"62소9403")

def 중구_차량번호():
  차량번호 = entry_중구.get()
  중구_차량번호_입력(차량번호)

중구btn25 = Button(frame4, width=5, padx=10, pady=5, text="차량번호", command=중구_차량번호, bg="yellow", fg="black", font = ("", 7))
중구btn25.place(x=200, y=35)

#날짜
태화연day1 = Button(frame4, width=2, padx=5, pady=5, text="1F", command=태화연_Day11, bg="white", fg="black", font = ("", 7))
태화연day1.place(x=0, y=59)
태화연day2 = Button(frame4, width=2, padx=5, pady=5, text="1S", command=태화연_Day12, bg="white", fg="black", font = ("", 7))
태화연day2.place(x=25, y=59)
태화연day3 = Button(frame4, width=2, padx=5, pady=5, text="2F", command=태화연_Day21, bg="white", fg="black", font = ("", 7))
태화연day3.place(x=50, y=59)
태화연day4 = Button(frame4, width=2, padx=5, pady=5, text="2S", command=태화연_Day22, bg="white", fg="black", font = ("", 7))
태화연day4.place(x=75, y=59)
태화연day5 = Button(frame4, width=2, padx=5, pady=5, text="3F", command=태화연_Day31, bg="white", fg="black", font = ("", 7))
태화연day5.place(x=100, y=59)
태화연day6 = Button(frame4, width=2, padx=5, pady=5, text="3S", command=태화연_Day32, bg="white", fg="black", font = ("", 7))
태화연day6.place(x=125, y=59)
태화연day7 = Button(frame4, width=2, padx=5, pady=5, text="4F", command=태화연_Day41, bg="white", fg="black", font = ("", 7))
태화연day7.place(x=150, y=59)
태화연day8 = Button(frame4, width=2, padx=5, pady=5, text="4S", command=태화연_Day42, bg="white", fg="black", font = ("", 7))
태화연day8.place(x=175, y=59)
태화연day9 = Button(frame4, width=5, padx=10, pady=5, text="Day", command=태화연_Day, bg="blue", fg="white", font = ("", 7))
태화연day9.place(x=200, y=59)   
#함수
태화연btn1 = Button(frame4, width=5, padx=10, pady=5, text="Reset", command=태화연_Reset, bg="white", fg="black", font = ("", 7))
태화연btn1.place(x=0, y=83)
태화연btn2 = Button(frame4, width=5, padx=10, pady=5, text="자동실행", command=중구_자동입력, bg="blue", fg="white", font = ("", 7))
태화연btn2.place(x=50, y=83)
태화연btn3 = Button(frame4, width=5, padx=10, pady=5, text="Range", command=태화연_범위선택, bg="white", fg="black", font = ("", 7))
태화연btn3.place(x=100, y=83)
태화연btn4 = Button(frame4, width=5, padx=10, pady=5, text="Start", command=태화연_Start, bg="green", fg="white", font = ("", 7))
태화연btn4.place(x=150, y=83)
태화연btn5 = Button(frame4, width=5, padx=10, pady=5, text="Start(A)", command=태화연_JubJub, bg="white", fg="black", font = ("", 7))
태화연btn5.place(x=200, y=83)

#ㅇ
태화연log6 = Button(frame4, width=5, padx=10, pady=5, text="호수뷰", command=태화연_호수뷰, bg="white", fg="black", font = ("", 7))
태화연log6.place(x=100, y=107)
태화연log7 = Button(frame4, width=5, padx=10, pady=5, text="2_3층", command=태화연_2_3층, bg="white", fg="black", font = ("", 7))
태화연log7.place(x=150, y=107)


#대왕암 UI===============================================================================================================
frame5=tkinter.Frame(window)
notebook.add(frame5, text="5.동구")

#로그
대왕암log1 = Button(frame5, width=5, padx=10, pady=5, text="NO.1", command=대왕암_Log_Id1, bg="orange", fg="black", font = ("", 7))
대왕암log1.place(x=0, y=10)
대왕암log2 = Button(frame5, width=5, padx=10, pady=5, text="NO.2", command=대왕암_Log_Id2, bg="orange", fg="black", font = ("", 7))
대왕암log2.place(x=50, y=10)
대왕암log3 = Button(frame5, width=5, padx=10, pady=5, text="NO.3", command=대왕암_Log_Id3, bg="orange", fg="black", font = ("", 7))
대왕암log3.place(x=100, y=10)
대왕암log4 = Button(frame5, width=5, padx=10, pady=5, text="NO.4", command=대왕암_Log_Id4, bg="orange", fg="black", font = ("", 7))
대왕암log4.place(x=150, y=10)
#날짜
대왕암btn1 = Button(frame5, width=5, padx=10, pady=5, text="Day1", command=대왕암_Day1, bg="white", fg="black", font = ("", 7))
대왕암btn1.place(x=0, y=35)
대왕암btn2 = Button(frame5, width=5, padx=10, pady=5, text="Day2", command=대왕암_Day2, bg="white", fg="black", font = ("", 7))
대왕암btn2.place(x=50, y=35)
대왕암btn3 = Button(frame5, width=5, padx=10, pady=5, text="Day3", command=대왕암_Day3, bg="white", fg="black", font = ("", 7))
대왕암btn3.place(x=100, y=35)
대왕암btn4 = Button(frame5, width=5, padx=10, pady=5, text="Day4", command=대왕암_Day4, bg="white", fg="black", font = ("", 7))
대왕암btn4.place(x=150, y=35)
대왕암btn5 = Button(frame5, width=5, padx=10, pady=5, text="Day", command=대왕암_Day, bg="blue", fg="white", font = ("", 7))
대왕암btn5.place(x=200, y=35)
#함수
대왕암btn1 = Button(frame5, width=5, padx=10, pady=5, text="Reset", command=대왕암_Reset, bg="white", fg="black", font = ("", 7))
대왕암btn1.place(x=0, y=59)
대왕암btn2 = Button(frame5, width=5, padx=10, pady=5, text="Auto", command=대왕암_자동입력, bg="blue", fg="white", font = ("", 7))
대왕암btn2.place(x=50, y=59)
대왕암btn3 = Button(frame5, width=5, padx=10, pady=5, text="Cursor", command=대왕암_커서선택, bg="white", fg="black", font = ("", 7))
대왕암btn3.place(x=100, y=59)
대왕암btn4 = Button(frame5, width=5, padx=10, pady=5, text="Range", command=대왕암_범위선택, bg="white", fg="black", font = ("", 7))
대왕암btn4.place(x=150, y=59)
대왕암btn5 = Button(frame5, width=5, padx=10, pady=5, text="Start", command=대왕암_Start, bg="green", fg="white", font = ("", 7))
대왕암btn5.place(x=200, y=59)
대왕암btn6 = Button(frame5, width=5, padx=10, pady=5, text="Karavan", command=대왕암_Karavan, bg="green", fg="white", font = ("", 7))
대왕암btn6.place(x=0, y=83)

대왕암btn7 = Button(frame5, width=5, padx=10, pady=5, text="Start(A)", command=대왕암_자동, bg="white", fg="black", font = ("", 7))
대왕암btn7.place(x=50, y=83)

#육부촌 UI===============================================================================================================
frame6=tkinter.Frame(window)
notebook.add(frame6, text="6.육부")

#로그
육부촌log1 = Button(frame6, width=5, padx=10, pady=5, text="Day1", command=육부촌_Day1, bg="orange", fg="black", font = ("", 7))
육부촌log1.place(x=0, y=10)
육부촌log2 = Button(frame6, width=5, padx=10, pady=5, text="Day2", command=육부촌_Day2, bg="orange", fg="black", font = ("", 7))
육부촌log2.place(x=50, y=10)
육부촌log3 = Button(frame6, width=5, padx=10, pady=5, text="Day3", command=육부촌_Day3, bg="orange", fg="black", font = ("", 7))
육부촌log3.place(x=100, y=10)
육부촌log4 = Button(frame6, width=5, padx=10, pady=5, text="Day4", command=육부촌_Day4, bg="orange", fg="black", font = ("", 7))
육부촌log4.place(x=150, y=10)
육부촌log5 = Button(frame6, width=5, padx=10, pady=5, text="Day_Cho", command=육부촌_Day, bg="orange", fg="black", font = ("", 7))
육부촌log5.place(x=200, y=10)
#날짜
육부촌btn1 = Button(frame6, width=5, padx=10, pady=5, text="Hold", command="육부촌_Log_Id2", bg="white", fg="black", font = ("", 7))
육부촌btn1.place(x=0, y=35)
육부촌btn2 = Button(frame6, width=5, padx=10, pady=5, text="Hold", command="육부촌_Log_Id2", bg="white", fg="black", font = ("", 7))
육부촌btn2.place(x=50, y=35)
육부촌btn3 = Button(frame6, width=5, padx=10, pady=5, text="Hold", command="육부촌_Log_Id2", bg="white", fg="black", font = ("", 7))
육부촌btn3.place(x=100, y=35)
육부촌btn4 = Button(frame6, width=5, padx=10, pady=5, text="Hold", command="육부촌_Log_Id2", bg="white", fg="black", font = ("", 7))
육부촌btn4.place(x=150, y=35)
육부촌btn5 = Button(frame6, width=5, padx=10, pady=5, text="Hold", command="육부촌_Log_Id2", bg="white", fg="black", font = ("", 7))
육부촌btn5.place(x=200, y=35)
#함수
육부촌btn1 = Button(frame6, width=5, padx=10, pady=5, text="Reset", command="육부촌_Log_Id2", bg="white", fg="black", font = ("", 7))
육부촌btn1.place(x=0, y=59)
육부촌btn2 = Button(frame6, width=5, padx=10, pady=5, text="Auto", command="육부촌_Log_Id2", bg="white", fg="black", font = ("", 7))
육부촌btn2.place(x=50, y=59)
육부촌btn3 = Button(frame6, width=5, padx=10, pady=5, text="Cursor", command="육부촌_Log_Id2", bg="white", fg="black", font = ("", 7))
육부촌btn3.place(x=100, y=59)
육부촌btn4 = Button(frame6, width=5, padx=10, pady=5, text="Range", command=육부촌_범위선택, bg="white", fg="black", font = ("", 7))
육부촌btn4.place(x=150, y=59)
육부촌btn5 = Button(frame6, width=5, padx=10, pady=5, text="줍줍", command=육부촌_Start1, bg="white", fg="black", font = ("", 7))
육부촌btn5.place(x=200, y=59)
육부촌btn6 = Button(frame6, width=5, padx=10, pady=5, text="Karavan", command="육부촌_Log_Id2", bg="green", fg="white", font = ("", 7))
육부촌btn6.place(x=0, y=83)
육부촌btn7 = Button(frame6, width=5, padx=10, pady=5, text="Start(A)", command=육부촌_Start, bg="green", fg="white", font = ("", 7))
육부촌btn7.place(x=50, y=83)

window.mainloop()