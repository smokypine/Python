## 라이브러리 뷰티플 솝(BeautifulSoup)
# 터미널에 pip install beautifulsoup4 입력. 
# 만약 Requirement already satisfied 와 같은 에러가 난다면 하단의 인터프리터를 python(base) 로 수정하라.
from bs4 import BeautifulSoup 

# 터미널에 pip install requests 를 입력.
import requests ## http 요청 처리 library

headers = {
    "User-Agent": "동양미래대학교"
}
# 뉴스 크롤링
webpage = requests.get("https://n.news.naver.com/mnews/article/001/0013943781")
# webpage = requests.get("https://n.news.naver.com/mnews/article/001/0013943781", headers=headers) 둘 중 하나 에러나지 않는 것을 선택.
print(webpage)

# 페이지의 html 받아오기
soup = BeautifulSoup(webpage.content, "html.parser")
print(soup)

# 페이지의 기사 받아오기
# 먼저 해당 페이지의 개발자도구를 클릭(F12)
# Ctrl + Shift + C 를 누르고 크롤링 하고 싶은 곳을 클릭.
news = soup.select_one("#dic_area").get_text().strip()
print(news)