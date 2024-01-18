import requests
from bs4 import BeautifulSoup
import datetime

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%8B%9C%EA%B3%84'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

time_str = soup.find('span', {'class': 'time_text'}).text
now = datetime.datetime.strptime(time_str, '%Y.%m.%d. %H:%M:%S')

print(now)