# 한국폭염일수(1973 ~ 2022)
# 레퍼런스 : https://data.kma.go.kr/climate/heatWave/selectHeatWaveMixChart.do?pgmNo=674
import csv
import matplotlib.pyplot as plt 
import numpy as np
## 폭염일수
f1 = open('C:/Users/김동현/Desktop/2학년 1학기 파이썬 수업/Python/프로젝트/온실가스_평균기온/연도별(2011~2022) 온열질환 응급실감시체계 운영 결과.csv', encoding='UTF8')            # CSV 파일 열어 f에 저장 
Hit = csv.reader(f1)                       # reader() 함수로 읽기
header = next(Hit)                         # 헤더 제거

# 데이터 저장을 위한 리스트 초기화
yeardata = []
hit_illness_00 = []#서울
hit_illness_01 = []#부산
hit_illness_02 = []#대구
hit_illness_03 = []#인천
hit_illness_04 = []#광주
hit_illness_05 = []#대전
hit_illness_06 = []#울산
hit_illness_07 = []#세종
hit_illness_08 = []#경기도
hit_illness_09 = []#강원도
hit_illness_10 = []#충청북도
hit_illness_11 = []#충청남도
hit_illness_12 = []#전라북도
hit_illness_13 = []#전라남도
hit_illness_14 = []#경상북도
hit_illness_15 = []#경상남도
hit_illness_16 = []#제주특별자치도

for row in Hit:
    year = int(row[0])
    hit_day_00 = int(row[2])
    hit_day_01 = int(row[3])
    hit_day_02 = int(row[4])
    hit_day_03 = int(row[5])
    hit_day_04 = int(row[6])
    hit_day_05 = int(row[7])
    hit_day_06 = int(row[8])
    hit_day_07 = int(row[9])
    hit_day_08 = int(row[10])
    hit_day_09 = int(row[11])
    hit_day_10 = int(row[12])
    hit_day_11 = int(row[13])
    hit_day_12 = int(row[14])
    hit_day_13 = int(row[15])
    hit_day_14 = int(row[16])
    hit_day_15 = int(row[17])
    hit_day_16 = int(row[18])
    yeardata.append(year)

    hit_illness_00.append(hit_day_00)
    hit_illness_01.append(hit_day_01)
    hit_illness_02.append(hit_day_02)
    hit_illness_03.append(hit_day_03)
    hit_illness_04.append(hit_day_04)
    hit_illness_05.append(hit_day_05)
    hit_illness_06.append(hit_day_06)
    hit_illness_08.append(hit_day_08)
    hit_illness_09.append(hit_day_09)
    hit_illness_10.append(hit_day_10)
    hit_illness_11.append(hit_day_11)
    hit_illness_12.append(hit_day_12)
    hit_illness_13.append(hit_day_13)
    hit_illness_14.append(hit_day_14)
    hit_illness_15.append(hit_day_15)
    hit_illness_16.append(hit_day_16)
    if year >= 2014:
        hit_illness_07.append(hit_day_07)

print("년도 : ", yeardata)
print("서울 : ", hit_illness_00)
print("부산 : ", hit_illness_01)
print("대구 : ", hit_illness_02)
print("인천 : ", hit_illness_03)
print("광주 : ", hit_illness_04)
print("대전 : ", hit_illness_05)
print("울산 : ", hit_illness_06)
print("세종 : ", hit_illness_07)
print("경기 : ", hit_illness_08)
print("강원 : ", hit_illness_09)
print("충북 : ", hit_illness_10)
print("충남 : ", hit_illness_11)
print("전북 : ", hit_illness_12)
print("전남 : ", hit_illness_13)
print("경북 : ", hit_illness_14)
print("경남 : ", hit_illness_15)
print("제주 : ", hit_illness_16)