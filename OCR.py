from tkinter import *
from Folder.kakao_01_api import *
import pyautogui as pag
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
import cv2
import easyocr
import cv2
import multiprocessing as mp
import threading
from PIL import Image
reader = easyocr.Reader(['en'], gpu=True)

input_image_path = '제목 없음1.png'  # 확대할 스크린샷 파일 경로
output_image_path = '제목 없음.png'  # 저장할 파일 경로

# 이미지 열기
image = Image.open(input_image_path)

# 이미지 크기 가져오기
width, height = image.size

# 이미지 2배 확대
enlarged_image = image.resize((width * 4, height * 4))

# 확대된 이미지 저장
enlarged_image.save(output_image_path)

print(f"이미지가 {output_image_path}에 저장되었습니다.")

file = r"제목 없음.png"
# reader = easyocr.Reader(['en'], gpu=True)
img = cv2.imread(file)
text = reader.readtext(img, detail=0)
print(text)
input_text = str(text)
input_text1 = input_text[2:8]   
print(input_text1) 
pyperclip.copy(input_text1)
