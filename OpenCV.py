from cv2 import threshold
from PIL import Image
from matplotlib import image
import pytesseract
from numpy import binary_repr
import pyautogui as pag
import win32con
import win32api
import win32gui
import keyboard
import time
import pyperclip
import clipboard
from tkinter import *
import cv2
import numpy as np

# try:
#     from PIL import Image 
# except ImportError: 
#     import Image
# import pytesseract 

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' 
# print(pytesseract.image_to_string(Image.open('test.png')))


# def test():
    
#     img = cv2.imread('blook.jpg' , cv2.IMREAD_GRAYSCALE)
#     binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 1)#홀수값 입력
#     cv2.imwrite('blook_binary.jpg', binary)


#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract' 
#     print(pytesseract.image_to_string('test.jpg'))
    
# test()  



img = cv2.imread('blook.jpg' , cv2.IMREAD_GRAYSCALE)

while True:
    block_size = cv2.getTrackbarPos('blook_size', name)
    c = cv2.getTrackbarPos('c', name)
    
    if block_size <= 1:
        block_size = 3
        
    if block_size % 2 == 0:
        block_size += 1
        
    binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, c)
    
   
        
    cv2.imshow(name, binary)
    if cv2.waitKey(1) == ord('q'):
        break




cv2.destroyAllWindows()   


