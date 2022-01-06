from selenium import webdriver
import time

# browser = webdriver.Chrome("/usr/local/bin/chromedriver")
browser = webdriver.Chrome()

# 1. 네이버 이동
browser.get("http://naver.com/")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("honest479")
browser.find_element_by_id("pw").send_keys("rjqnrtjs6cjr!")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(2)   # 로딩 시간을 기다리거나 하는 경우에 사용

# 5. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit()  # 크롬의 모든 탭 종료


