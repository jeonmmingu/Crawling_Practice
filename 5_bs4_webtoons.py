import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

# soup 객체 안에 해당 페이지를 parsing 해서 전부 다 가져오도록 하는 코드이다.
soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class": "title"})
# a element의 class 속성이 title 인 모든 element를 반환
for cartoon in cartoons:
    print(cartoon.get_text())

