######################################## 주의 사항 ###############################################

# 아래 두 항목에 대해서 검색 후 환경에 맞게 설정 !!
# "User-Agent" 를 환경에 맞게 다시 설정.(Google에 user agent string 검색)
# "chromedriver" 경로를 환경에 맞게 다시 설정.(윈도우 : cmd, 맥 : terminal 에서 chromedriver의 경로 탐색)

################################################################################################

#################################### 필요한 패키지 선언 ############################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests
import csv

###############################################################################################
print("크롤링 중...")
######################################## 시가총액 ################################################

# 네이버 금융 - 시가총액
url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

# csv 파일로 저장.
filename = "시가총액.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)


# title을 list의 형태로 저장.
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
writer.writerow(title)  # 첫 번째 줄에 title을 저장


# 1 페이지부터 끝 페이지 까지 차례대로 전부 저장.
curr_page = 1
while True:
    # print("page :", curr_page)
    res = requests.get(url + str(curr_page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    prev_on = soup.find("table", attrs={"class": "Nnavi"}).find("td", attrs={"class": "on"}).get_text().strip()
    prev_on = int(prev_on)
    # print(prev_on)
    if not prev_on == curr_page:
        break

    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:   # 의미 없는 line에 대해서 skip을 진행
            continue
        data = [column.get_text().strip() for column in columns]  # 한 줄 for문으로 처리 # strip()함수를 통해서 탭이나 공백들을 제거
        writer.writerow(data)   # list 형태로 입력 해줘야 한다. # csv 파일에 데이터를 저장할 때 이러한 방식을 사용한다.
        # print(data)
    curr_page += 1
################################################################################################
print("시가총액 완료")

######################################## ETF ###################################################

def naver_finance_crawling(title):
    elem = browser.find_element(By.LINK_TEXT, title)
    elem.click()

    time.sleep(3)

    # csv 파일로 저장.
    if title == "국내 업종/테마":     # 파일명에 '/'가 포함되면 경로로 인식하기 때문에 제대로 코드가 작동을 하지 않는다.
        filename = 'EFT - 국내 업종,테마.csv'
    else:
        filename = 'EFT - ' + title + '.csv'
    f = open(filename, "w", encoding="utf-8-sig", newline="")
    writer = csv.writer(f)

    # title을 list의 형태로 저장.
    title_name = ["종목명", "현재가", "전일비", "등락률", "NAV", "3개월수익률", "거래량", "거래대금(백만)", "시가총액(억)"]
    writer.writerow(title_name)  # 첫 번째 줄에 title을 저장

    # 해당 페이지의 데이터 불러오기
    soup = BeautifulSoup(browser.page_source, "lxml")
    data_rows = soup.find("table", attrs={"class": "type_1 type_etf"}).find("tbody").find_all("tr")

    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:  # 의미 없는 line에 대해서 skip을 진행
            continue
        data = [column.get_text().strip() for column in columns]  # 한 줄 for문으로 처리 # strip()함수를 통해서 탭이나 공백들을 제거
        writer.writerow(data)  # list 형태로 입력 해줘야 한다. # csv 파일에 데이터를 저장할 때 이러한 방식을 사용한다.

    print(title, " 완료!")
    f.close()

################################################################################################

# 네이버 금융 - Etf
url = "https://finance.naver.com/sise/etf.naver"

# Selenium 사용 방법에 대해 설정
# headless Chrome 방식으로 Selenium 사용
options = webdriver.ChromeOptions()
options.headless = True
# Chrome 페이지 중 headless 웹 스크래핑을 차단하는 경우가 있기 때문에 User Agent를 설정 <<자신의 환경에 맞게 변경!!>>
options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36")
browser = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)  # chromedriver의 경로를 지정해주어야 한다.

# 크롬 브라우저 열기 (해당 url에 맞게)
browser.get(url)

naver_finance_crawling('국내 시장지수')
naver_finance_crawling('국내 업종/테마')
naver_finance_crawling('국내 파생')
naver_finance_crawling('해외 주식')
naver_finance_crawling('원자재')
naver_finance_crawling('채권')
naver_finance_crawling('기타')

################################################################################################
print("크롤링 완료!")