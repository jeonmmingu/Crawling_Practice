from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()   # 창 최대화

url = "http://flight.naver.com"
browser.get(url)    # 해당 url로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일, 28일 선택
browser.find_elements_by_link_text("27")[0].click()     # [0] -> 이번 달
browser.find_elements_by_link_text("28")[0].click()     # [0] -> 이번 달

# 제주도 선택
browser.find_element_by_xpath().click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 브라우저가 10초동안 대기하는데 언제까지 대기하냐면 해당 x-path가 나올 때 까지 대기하는 것을 원칙으로
# 하고 만약 그 동안 찾지 못한다면 실패 한 것으로 간주하여 에러 코드를 출력하고 프로그램을 종료한다.
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "#x-path")))
finally:
    browser.quit()

# 첫번째 결과 출력
elem = browser.find_element_by_xpath()