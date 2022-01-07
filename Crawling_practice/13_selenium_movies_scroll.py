from selenium import webdriver
browser = webdriver.Chrome("D:\ChromeDV\chromedriver.exe")
browser.maximize_window()

url = "https://play.google.com/store/movies/category/MOVIE"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)")  # 1920 x 1080
# browser.execute_script("window.scrollTo(0, 2080)")  # 1920 x 1080

#  화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2  # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내리기
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    else:
        prev_height = curr_height

print("스크롤 완료")

############################################################################################################################################

from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class": ["ULeU3b neq64b", "TjRVLb"]})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class": "hP61id"}).get_text() # 여러 개의 class를 받을 수 있다.
    print(title)
    