import requests

# google에 user agent string이라고 입력하면 내 desktop의 user agent를 확인 할 수 있다.

url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("navernews_politics.html", "w", encoding="utf8") as f:
    f.write(res.text)
