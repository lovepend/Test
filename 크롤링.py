import requests

url = 'https://example.com'
response = requests.get(url)

# 웹 페이지 내용 출력
print(response.text)



from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')

# 원하는 데이터 추출
data = soup.find('div', {'class': 'content'})