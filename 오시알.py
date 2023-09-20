# import pytesseract
# from PIL import Image

# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# # 이미지 불러오기
# img = Image.open('example.png')


# # OCR 인식
# text = pytesseract.image_to_string(img, lang='eng')

# # 결과 출력
# print(text)


from PIL import Image
import pytesseract
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
img_path = r".\example.png"

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(Image.open(img_path), lang='kor+eng')

print(text)
