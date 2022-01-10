 # 1. 스타트업 기업 목록에 대해 검색 (검색 가능 확인)
 # 2. 만약 기업이 검색 된다면 해당 기업에 대한 크롤링 진행
 # 3. 만약 기업이 검색이 안된다면 넘어가는 것으로 한다.

############## 필요한 패키지 선언 ################

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

##############################################

# 더브이씨 url
url = "https://thevc.kr/"

# Selenium 사용 방법에 대해 설정
# headless Chrome 옵션 설정
options = webdriver.ChromeOptions()
options.headless = False
# Chrome 페이지 중 headless 웹 스크래핑을 차단하는 경우가 있기 때문에 User Agent를 설정 <<자신의 환경에 맞게 변경!!>>
options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")
browser = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)  # chromedriver의 경로를 지정해주어야 한다.

# thevc 로그인
browser.get(url)
# time.sleep(1)
# browser.find_element(By.LINK_TEXT, "로그인/가입").click()
# time.sleep(1)
# browser.find_element(By.ID, "input-email").send_keys("jeonalsrn@gmail.com")
# time.sleep(1)
# browser.find_element(By.ID, "input-password").send_keys("jeon3945!!")
# time.sleep(1)
# browser.find_element(By.XPATH, "//*[@id='layout-wrap']/div[2]/div/div/div[2]/form/button").click()
# time.sleep(1)


# # csv 파일 형태로 스타트업 기업 목록을 작성
# filename = "더브이씨.csv"
# f_w = open(filename, "w", encoding="utf-8-sig", newline="")
# writer = csv.writer(f_w)


# 스타트업 기업 목록 읽어오기
f_r = open('비상장 스타트업 기업 목록.csv', 'r')
reader = csv.reader(f_r)

i = 1
find = False

for line in reader:

    browser.find_element(By.ID, "input-integrated-search").send_keys(line[0])
    time.sleep(2)

    soup = BeautifulSoup(browser.page_source, "lxml")
    search_list = soup.find_all("p", attrs={"class": "vc-typo-ellipsis vc-typo-weight-bold"})
    for search in search_list:
        print(line)
        print(search.get_text().strip())
        result = search.get_text().strip()
        if result == line[0].strip():
            print("check!!")
            find = True

    if find:
        find = False
        browser.find_element(By.CLASS_NAME, "vc-image-box").click()
        time.sleep(1)
        soup = BeautifulSoup(browser.page_source, "lxml")
        Basic_info = soup.find("div", attrs={"class": "vc-block-wrap"}).find_all("div", attrs={
            "class": "vc-flex-container justify-between"})
        for info in Basic_info:
            print(i, ".", info.find("dt"), ":", info.find("dd").get_text())

    else:
        browser.find_element(By.ID, "input-integrated-search").clear()








