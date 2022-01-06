import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=28&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
res = requests.get(url, headers=headers)

res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class": re.compile("^search-product")})

for item in items:

    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
    if ad_badge:
        print("\n", "  <광고상품 제외합니다.>", "\n")
        continue

    name = item.find("div", attrs={"class": "name"}).get_text() # 제품명
    # 애플 제품 제외
    if "Apple" in name:
        print("\n", " <Apple 상품 제외합니다.>", "\n")
        continue

    price = item.find("strong", attrs={"class": "price-value"}).get_text() # 가격

    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    star = item.find("em", attrs={"class": "rating"}) # 평점
    if star:
        star = star.get_text()
    else:
        print("  <평점 없는 상품은 제외합니다.>")
        continue

    num_star = item.find("span", attrs={"class": "rating-total-count"}) # 평점 수
    if num_star:
        num_star = num_star.get_text()
        num_star = num_star[1:-1]
    else:
        print("  <평점 수 없는 상품은 제외합니다.>")
        continue

    if float(star) >= 4.5 and int(num_star) >= 100:
        print(name)
        print(price)
        print(star)
        print(num_star)


