import pyautogui as pag
import win32con
import win32api
import win32gui
import keyboard
import time
import clipboard
import pyperclip
import glob
import CaptchaCracker as cc

# Target image data size
img_width = 200 #200   #185
img_height = 50 #50   #35
# Target image label length
max_length = 5 #6    #15
# Target image label component
characters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

# Model weight file path
weights_path = "C:/data/model/weights.h5"
# Creating a model application instance
AM = cc.ApplyModel(weights_path, img_width, img_height, max_length, characters)

# Target image path
target_img_path = "C:/data/capture.png"

# Predicted value
pred = AM.predict(target_img_path)
print(pred)
    
