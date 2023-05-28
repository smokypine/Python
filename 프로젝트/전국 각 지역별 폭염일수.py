# 한국폭염일수(1973 ~ 2022)
# 레퍼런스 : https://data.kma.go.kr/climate/heatWave/selectHeatWaveMixChart.do?pgmNo=674
import csv
import matplotlib.pyplot as plt 
import numpy as np
## 폭염일수
f1 = open('C:/Users/김동현/Desktop/2학년 1학기 파이썬 수업/Python/프로젝트/온실가스_평균기온/폭염일수/전국 각 지역별 폭염일수 1973~2022.csv', encoding='cp949')            # CSV 파일 열어 f에 저장 
Hit = csv.reader(f1)                       # reader() 함수로 읽기
header = next(Hit)                         # 헤더 제거

# 데이터 저장을 위한 리스트 초기화
yeardata = []
hitday_00 = []#서울
hitday_01 = []#부산
hitday_02 = []#대구
hitday_03 = []#인천
hitday_04 = []#광주
hitday_05 = []#대전
hitday_06 = []#울산
hitday_07 = []#세종
hitday_08 = []#경기도
hitday_09 = []#강원도
hitday_10 = []#충청북도
hitday_11 = []#충청남도
hitday_12 = []#전라북도
hitday_13 = []#전라남도
hitday_14 = []#경상북도
hitday_15 = []#경상남도
hitday_16 = []#제주특별자치도

for row in Hit:
    year = int(row[0])
    hit_day = float(row[1])
    avg_Temp = float(row[3])
    yeardata.append(year)
    hitday_01.append(hit_day)
    hitday_02.append(hit_day)
    hitday_03.append(hit_day)
    hitday_04.append(hit_day)
    hitday_05.append(hit_day)
    hitday_06.append(hit_day)
    hitday_08.append(hit_day)
    hitday_09.append(hit_day)
    hitday_10.append(hit_day)
    hitday_11.append(hit_day)
    hitday_12.append(hit_day)
    hitday_13.append(hit_day)
    hitday_14.append(hit_day)
    hitday_15.append(hit_day)
    hitday_16.append(hit_day)
    if year >= 2019:
        hitday_07.append(hit_day)

print(yeardata)        
print("00 : ", hitday_01)
print("01 : ", hitday_01)
print("02 : ", hitday_02)
print("03 : ", hitday_03)
print("04 : ", hitday_04)
print("05 : ", hitday_05)
print("06 : ", hitday_06)
print("07 : ", hitday_07)
print("08 : ", hitday_08)
print("09 : ", hitday_09)
print("10 : ", hitday_10)
print("11 : ", hitday_11)
print("12 : ", hitday_12)
print("13 : ", hitday_13)
print("14 : ", hitday_14)
print("15 : ", hitday_15)
print("16 : ", hitday_16)

