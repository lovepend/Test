from PIL import Image

# 이미지 파일 경로
input_image_path = 'captcha1.png'  # 확대할 스크린샷 파일 경로
output_image_path = 'captcha.png'  # 저장할 파일 경로

# 이미지 열기
image = Image.open(input_image_path)

# 이미지 크기 가져오기
width, height = image.size

# 이미지 2배 확대
enlarged_image = image.resize((width * 2, height * 2))

# 확대된 이미지 저장
enlarged_image.save(output_image_path)

print(f"이미지가 {output_image_path}에 저장되었습니다.")