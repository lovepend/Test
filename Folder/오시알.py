# import pytesseract
# from PIL import Image

# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# # 이미지 불러오기
# img = Image.open('example.png') 


# # OCR 인식
# text = pytesseract.image_to_string(img, lang='eng')

# # 결과 출력
# print(text)







from easyocr import Reader
import cv2
import requests
import numpy as np
from PIL import ImageFont, ImageDraw, Image


#clipboard.paste('captcha.png')
#
#im1 = pag.screenshot('captcha.png',clipboard.paste)
#100%
#im1 =  pag.screenshot('captcha.png', region=(700,245,220,80))

#50%
#im1 =  pag.screenshot('captcha.png', region=(832,787,81,23))
#im1 =  pag.screenshot('captcha.png', region=(0,0,1920,1080))

#pag.screenshot('sample.png')

# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# img_path = r".\example.png"

# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# text = pytesseract.image_to_string(Image.open(img_path), lang='kor+eng')

# print(text)


### tesseract ###
# import pytesseract
# import cv2
# import os

# dir = r"C:\Users\LinkTech\Documents\Visual Studio Code\Test\\"

import easyocr
import cv2

# import torch torch.cuda.get_device_name(0) torch.cuda.is_available() print(torch.__version__)

file = r"C:\Users\LinkTech\Documents\Visual Studio Code\Test\captcha.png"
#reader = easyocr.Reader(['en'], gpu=True)
reader = easyocr.Reader(['ko', 'en'], gpu=True, model_storage_directory= 'korean_g2.pth')
img = cv2.imread(file)
#img = cv2.imread(im1)
text = reader.readtext(img, detail=0)
print(text)



### easyorc ###
# import easyocr
# import os
# import cv2

# dir = r"C:\Users\LinkTech\Documents\Visual Studio Code\Test\\"
# reader = easyocr.Reader(['ko'], gpu=False)

# for i in os.listdir(dir):
#     j = 0
#     img = cv2.imread(dir+i)
#     text = reader.readtext(img, detail=0, allowlist="0123456789")
#     print(i +" => " +text[j])
#     j += 1