#################################### 필요한 패키지 선언 ############################################

from bs4 import BeautifulSoup
from datetime import datetime
import requests
import pandas as pd
import re

#################################################################################################



#################################### 크롤링 결과 값 저장 ############################################

title_text = []
date_text = []
result = {}

#################################################################################################



#################################### 크롤링 함수 ############################################

def crawler(maxpage, query, sort, s_date, e_date):
    s_from = s_date.replace(".", "")
    e_to = e_date.replace(".", "")
    maxpage_t = (int(maxpage) - 1) * 10 + 1  # 11= 2페이지 21=3페이지 31=4페이지  ...81=9페이지 , 91=10페이지, 101=11페이지
    page = 1

    # 400 페이지까지만 제공함.
    while page <= 4001:
        # 네이버 기사형태 지정
        url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort=" + sort + "&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'lxml')

        # 제목 추출
        atags = soup.select('ul.list_news > li.bx > div.news_wrap.api_ani_send > div > a')
        for atag in atags:
            title_text.append(atag.text)  # 제목

        # 날짜 추출
        date_lists = soup.select('ul.list_news > li.bx > div.news_wrap.api_ani_send > div > div > div > span')
        for date_list in date_lists:
            # 가끔 이상한 info가 껴있는 경우가 있음.
            if len(date_list) != 1:
                continue
            date_text.append(date_list.text)

        # 모든 리스트를 딕셔너리 형태로 저장
        # id= date , document = title , label 은 일단 3으로 고정(의미 없는 값)
        result = {"id": date_text, "document": title_text, "label": '3'}

        df = pd.DataFrame(result)  # df로 변환

        page += 10

        # print(df)

        # 인덱스 없애기
        df.to_csv(f'{query}_title.csv', sep=',', index=False, encoding="utf-8-sig")

        if (df['id'][len(df) - 1] == '2021.06.17.'):
            return

        # 400페이지만 제공하므로 시작 날짜를 마지막에 크롤링한 것으로 바꾸고 다시 크롤링
        if (page == 4001 and df['id'][len(df) - 1] != '2021.06.17.'):
            s_date = (df['id'][len(df) - 1])
            crawler(maxpage, query, sort, s_date, e_date)

########################################################################################



#################################### 필요한 정보 검색 ############################################

# url 인자 설정
maxpage = "100000"
query = ["에이비엘바이오", "삼천당제약", "안트로젠", "압타바이오", "유바이오로직스", "보령제약"]    # 검색 목록
sort = "2"  #관련도순=0  최신순=1  오래된순=2
s_date = "2017.06.01"  # 시작 날짜 입력
e_date = "2021.06.17"  # 마지막 날짜 입력

for i in query:
    crawler(maxpage, i, sort, s_date, e_date)
    print(i, " 크롤링 완료!")

##############################################################################################
