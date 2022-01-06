import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액 1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
# new line을 공백으로 처리하는 이유는 계속 개행을 하기 때문이다.
# encoding을 utf8 이 아닌 utf-8-sig 로 쓴 것은 excel문서 상에서 한글이 깨져서 출력되는 경우 바르게 출력 되도록 하기 위함이다.

writer = csv.writer(f)  # csv파일로 만들고자 할 때 사용하는 코드

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
# ["N", "종목명", "현재가", ... ] 이런 식의 리스트 형식으로 구성이 된다.

writer.writerow(title)

for i in range(1, 5):
    res = requests.get(url + str(i))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:   # 의미 없는 line에 대해서 skip을 진행
            continue
        data = [column.get_text().strip() for column in columns]  # 한 줄 for문으로 처리 # strip()함수를 통해서 탭이나 공백들을 제거
        # print(data)
        writer.writerow(data)   # list 형태로 입력 해줘야 한다. # csv 파일에 데이터를 저장할 때 이러한 방식을 사용한다.


