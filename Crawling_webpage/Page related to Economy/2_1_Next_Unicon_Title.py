# a = 9401/20
# b = 20*470
# 총 471번의 더 보기를 누른 후 title 정보를 가져 와야 한다.
# Selenium + BeautifulSoup 사용

############## 필요한 패키지 선언 ################

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

##############################################

# 넥스트 유니콘 url
url = "https://www.nextunicorn.kr/companies"

# Selenium 사용 방법에 대해 설정
# headless Chrome 옵션 설정
# options = webdriver.ChromeOptions()
# options.headless = False    # 넥스트 유니콘에서 chrome headless에 대해 차단하기 때문에 False로 지정 후 클롤링 하는 방식을 사용하였다.
# Chrome 페이지 중 headless 웹 스크래핑을 차단하는 경우가 있기 때문에 User Agent를 설정 <<자신의 환경에 맞게 변경!!>>
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
browser = webdriver.Chrome("D:\ChromeDV\chromedriver.exe")  # chromedriver의 경로를 지정해주어야 한다.

# 넥스트 유니콘 로그인 (더보기 로딩 시간: 2초, 로그인 시 로그인이 풀리는 것을 방지하기 위해 3초 sleep 설정)
browser.get(url)
browser.maximize_window()
time.sleep(3)
browser.find_element_by_link_text("로그인").click()
time.sleep(3)
browser.find_element_by_id("email").send_keys("honest479@naver.com")
time.sleep(3)
browser.find_element_by_xpath("//*[@id='modal-wrapper']/div/div[1]/input[2]").send_keys("jeon3945!!")
time.sleep(3)
browser.find_element_by_xpath("//*[@id='modal-wrapper']/div/button").click()
time.sleep(3)
browser.get(url)

# 더보기를 끝까지 돌린다.
for i in range(1, 472):     # 로딩 시간 때문에 1416초 정도 걸린다. = 24분 정도 소요
    time.sleep(1)
    browser.find_element_by_xpath("//*[@id='modal-wrapper']/div[2]/div[2]/div/button").click()

time.sleep(15)

# csv 파일 형태로 스타트업 기업 목록을 작성
filename = "기업명.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

filename_url = "url.csv"
f_url = open(filename_url, "w", encoding="utf-8-sig", newline="")
writer_url = csv.writer(f_url)

# 해당 페이지에 존재하는 기업 명에 대한 자료들을 web_Scrapping.

soup = BeautifulSoup(browser.page_source, "lxml")
box_list = soup.find("div", attrs={"class": "sc-1rekng9-0 la-DThV"}).find_all("a")

for box in box_list:
    title = [box.find("div", attrs={"class": "sc-1b61jus-2 bKZGff"}).get_text()]
    url = ["https://www.nextunicorn.kr" + box["href"]]
    writer.writerow(title)
    writer_url.writerow(url)

browser.quit()
