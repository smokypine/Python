# Python Selenium 설치하기
   # - 웹 자동화를 위한 library(Chrome에서만 작동)
# pip install selenium
# pip install webdriver_manager 

# selenium import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# webdriver_manager import
from webdriver_manager.chrome import ChromeDriverManager

# time import <-------- 실행된 창이 유지되는 시간을 규정하기 위한 옵션
import time

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 크롬 드라이버 최신 버전 설정
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.naver.com") # naver가 켯다가 꺼짐
time.sleep(1) # 켜진 naver 창을 1초동안 유지시키고 끔

# 네이버 창의 뉴스를 키고 싶다면? F12-> 뉴스 우클릭 -> 검사 -> 개발자 도구에서 선택된 부분을 우클릭 Copy -> Copy full XPath 선택
# /html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a  <------- 네이버의 뉴스 버튼
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(1)

# 부동산 정보 확인하기
driver.get("https://m.land.naver.com/search")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").click() #서치로 가서 검색창을 클릭했다.
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input").send_keys("우성꿈동산") #검색창에 우성꿈동산을 입력한다.
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]/i").click() #우성꿈동산을 검색한다.
rentprice = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]/dd").text #3억을 띄운다.
print(rentprice)


### for문을 통한 주식 정보 확인하기
## Top 종목의 종목 이름 10개를 가져오고 싶다
driver.get("https://finance.naver.com/")
time.sleep(1)
# 규칙을 확인한다.
# /html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/th/a <----- tr[1]
# /html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[2]/th/a <----- tr[2]
# /html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[3]/th/a <----- tr[3] 과 같이 규칙성을 확인할 수 있다.

# for문을 써 보자!
lst1 = []
for i in range(10):
    subject1 = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/th/a").text # {i}만 바꾸는 방식
    lst1.append(subject1) # lst 배열에 subject값을 넣어준다.
print(lst1)

## 그렇다면 Top 종목의 주가를 가져와보자. 방법은 위와 거의 동일하다.
# 규칙은 다음과 같다.
# /html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[1] <--- tr[1]
# /html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[2]/td[1] <--- tr[2]
# /html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[3]/td[1] <--- tr[3] 과 같은 규칙이 확인 가능하다.

#for 문을 써 보자!
lst2 = []
for i in range(10):
    subject2 = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[1]").text # {i}만 바꾸는 방식
    lst2.append(subject2) # lst 배열에 subject값을 넣어준다.
print(lst2)

# 가격변동 액수
lst3 = []
for i in range(10):
    subject3 = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[2]").text # {i}만 바꾸는 방식
    lst3.append(subject3) # lst 배열에 subject값을 넣어준다.
print(lst3)

# 가격변동 비율
lst4 = []
for i in range(10):
    subject4 = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i+1}]/td[3]").text # {i}만 바꾸는 방식
    lst4.append(subject4) # lst 배열에 subject값을 넣어준다.
print(lst4)

print("종목명  주가  가격변동액  변동비율\t")
### 결과확인용 코드
for i in range(10):
    print("종목명 :", lst1[i]," 주가 :",lst2[i]," 가격변동액 :",lst3[i]," 변동비율 :",lst4[i])