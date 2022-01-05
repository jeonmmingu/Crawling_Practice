import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

# soup 객체 안에 해당 페이지를 parsing 해서 전부 다 가져오도록 하는 코드이다.
soup = BeautifulSoup(res.text, "lxml")

# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 첫 번째로 발견되는 a element를 출력
# print(soup.a.attrs) # a element의 속성 정보를 출력
# print(soup.a["href"]) # a element의 href 속성 '값'을 출력

# print(soup.find("a", attrs={"class": "Nbtn_upload"})) # class = "Nbtn_upload" 인 a element 를 찾아달라는 의미
# print(soup.find(attrs={"class": "Nbtn_upload"})) # class = "Nbtn_upload"인 어떤 element를 찾아달라는 의미이다.

# print(soup.find("li", attrs={"class": "rank01"}))
# rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling  # 줄 바꿈이 존재할 수 있기 때문에 2번 써야하는 경우가 있다.
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.get_text())

# print(rank1.find_next_siblings("li"))


