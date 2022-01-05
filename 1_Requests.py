import requests
# URL을 불러오는 부분
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")

res.raise_for_status() # 응답코드가 200 (정상적으로 작동) 이 아니라면 에러코드를 출력하고 프로그램을 종료

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
