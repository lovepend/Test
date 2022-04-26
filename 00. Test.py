from xml.etree.ElementPath import xpath_tokenizer_re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui as pag



driver = webdriver.Chrome()
driver.get("https://www.junggu.ulsan.kr/camping/index.do")
options = Options()

#지정한 user-agent로 설정합니다.
user_agent = "Mozilla/5.0 (Linux; Android 9; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Mobile Safari/537.36"
options.add_argument('user-agent=' + user_agent)

#options.add_argument('headless') #headless모드 브라우저가 뜨지 않고 실행됩니다.
#options.add_argument('--window-size= x, y') #실행되는 브라우저 크기를 지정할 수 있습니다.
options.add_argument('--start-maximized') #브라우저가 최대화된 상태로 실행됩니다.
#options.add_argument('--start-fullscreen') #브라우저가 풀스크린 모드(F11)로 실행됩니다.
#options.add_argument('--blink-settings=imagesEnabled=false') #브라우저에서 이미지 로딩을 하지 않습니다.
#options.add_argument('--mute-audio') #브라우저에 음소거 옵션을 적용합니다.
#options.add_argument('incognito') #시크릿 모드의 브라우저가 실행됩니다.

#####첫 시작화면#####
팝업1 = "/html/body/div/div[2]/div[2]/div[2]/label/input"
팝업2 = "/html/body/div/div[2]/div[1]/div[2]/label/input"

driver.find_element_by_xpath(팝업1).click()
driver.find_element_by_xpath(팝업2).click()

#####로그인#####
로그인 = "/html/body/div/header/div[3]/div[4]/div[1]/ul/li[1]/a"
driver.find_element_by_xpath(로그인).click()

이메일 = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div/div[1]/input"
driver.find_element_by_xpath(이메일).send_keys("lovepend@nate.com")

패스워드 = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div/div[2]/input"
driver.find_element_by_xpath(패스워드).send_keys("*Qkqh4fkdgo")

로그인 = "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/form/div/div[3]/button"
driver.find_element_by_xpath(로그인).click()

#####캠핑장 선택#####
태화연캠핑장 = "/html/body/div/div[1]/div[1]/div[2]/div/ul/li[1]/div[2]/span[3]/a"
driver.find_element_by_xpath(태화연캠핑장).click()

차량번호 = "/html/body/div[1]/div[1]/div[2]/div[2]/form/div[2]/div[1]/div/ul/li[5]/div[2]/input"
driver.find_element_by_xpath(차량번호).send_keys("62소6403")

이용준수사항 = "/html/body/div[1]/div[1]/div[2]/div[2]/form/div[2]/div[2]/div/div[2]/input"
driver.find_element_by_xpath(이용준수사항).click()

입실정원준수사항 = "/html/body/div[1]/div[1]/div[2]/div[2]/form/div[2]/div[3]/div/div[2]/input"
driver.find_element_by_xpath(입실정원준수사항).click()

취소및환불규정 = "/html/body/div[1]/div[1]/div[2]/div[2]/form/div[2]/div[4]/div/div[2]/input"
driver.find_element_by_xpath(취소및환불규정).click()

개인정보수집이용동의 = "/html/body/div[1]/div[1]/div[2]/div[2]/form/div[2]/div[5]/div/div[2]/input[1]"
driver.find_element_by_xpath(개인정보수집이용동의).click()


이용날짜1 = "/html/body/div[1]/div[1]/div[2]/div[2]/form/div[1]/div[1]/div[4]/div[1]/input"
driver.find_element_by_xpath(이용날짜1).click()
이용날짜2 = "/html/body/div[2]/div/div/select[2]"
driver.find_element_by_xpath(이용날짜2).click()
#월 선택
이용날짜3 = "/html/body/div[2]/div/div/select[2]/option[2]"
driver.find_element_by_xpath(이용날짜3).click()
#날짜 선택

#/html/body/div[2]/table/tbody/tr[1]/td[1]/a   td[7]으로 감
#/html/body/div[2]/table/tbody/tr[2]/td[1]/a   td[7]으로 감
이용날짜4 = "/html/body/div[2]/table/tbody/tr[5]/td[2]/a"
driver.find_element_by_xpath(이용날짜4).click()

time.sleep(1)

