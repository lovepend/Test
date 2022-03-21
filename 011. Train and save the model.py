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


# Training image data path
train_img_path_list = glob.glob("C:/data/sample/*.png")

# Training image data size
img_width = 200 #200 #180
img_height = 50 #50 #35

# Creating an instance that creates a model
CM = cc.CreateModel(train_img_path_list, img_width, img_height)

# Performing model training
model = CM.train_model(epochs=100) #100

# Saving the weights learned by the model to a file
model.save_weights("C:/data/model/weights.h5")