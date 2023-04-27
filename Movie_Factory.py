from gettext import find
from re import A
from tkinter import *
from turtle import goto
from kakao_01_api import *
from urllib3 import encode_multipart_formdata
import pyautogui as pag
import webbrowser
import win32con
import win32api
import win32gui
import keyboard
import pyperclip
import clipboard
import schedule
import requests
import time
import json
import datetime
import sys

def Movie_Factory_Day():
  while True:
    if keyboard.is_pressed("F2"):
      global Movie_Factory_day1
      Movie_Factory_day1  = pag.position()
      print(Movie_Factory_day1)
      time.sleep(0.5)
      break   
  while True:  
    if keyboard.is_pressed("F2"):
      global Movie_Factory_day2
      Movie_Factory_day2  = pag.position()
      print(Movie_Factory_day2)
      time.sleep(0.5)
      break  
  while True: 
    if keyboard.is_pressed("F2"):
      global Movie_Factory_day3
      Movie_Factory_day3  = pag.position()
      print(Movie_Factory_day3)
      time.sleep(0.5)
      break  
  while True: 
    if keyboard.is_pressed("F2"):
      global Movie_Factory_day4
      Movie_Factory_day4 = pag.position()
      print(Movie_Factory_day4)
      time.sleep(0.5)
      break   
  print("끝")

def Movie_Factory():
  #첫날
  pag.click(Movie_Factory_day1)
  time.sleep(0.5)
  #첫타임 선택
  button = pag.locateCenterOnScreen("./image/91. MovieFactory/02. MovieFactory.png",  confidence=0.9) 
  time.sleep(0.5)
  pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
  Movie_Factory_Serch()
  #두번째 날
  pag.click(Movie_Factory_day2)
  time.sleep(0.5)  
  #두번째 타임 선택
  button = pag.locateCenterOnScreen("./image/91. MovieFactory/02. MovieFactory.png",  confidence=0.9) 
  time.sleep(0.5)
  pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
  Movie_Factory_Serch()

def Movie_Factory_Serch():
  button = pag.locateCenterOnScreen("./image/91. MovieFactory/01. MovieFactory.png",  confidence=0.9) 
  if (button == None) :
    None   
    print("없음")   
  else : 
    pag.click(button.x,button.y, button='left', clicks=1, interval=0.1)
    print("있음")   
    refresh_token()
    kakao_message_you("Movie_Factory")
