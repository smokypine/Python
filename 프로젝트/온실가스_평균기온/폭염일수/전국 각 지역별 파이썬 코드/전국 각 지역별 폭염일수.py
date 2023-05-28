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
City = []
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

hit_before1990 = []
hit_1990th = []
hit_2000th = []
hit_2010th = []
hit_2020th = []

for row in Hit:
    year = int(row[0])
    hit_day_00 = float(row[2])
    hit_day_01 = float(row[3])
    hit_day_02 = float(row[4])
    hit_day_03 = float(row[5])
    hit_day_04 = float(row[6])
    hit_day_05 = float(row[7])
    hit_day_06 = float(row[8])
    hit_day_07 = float(row[9])
    hit_day_08 = float(row[10])
    hit_day_09 = float(row[11])
    hit_day_10 = float(row[12])
    hit_day_11 = float(row[13])
    hit_day_12 = float(row[14])
    hit_day_13 = float(row[15])
    hit_day_14 = float(row[16])
    hit_day_15 = float(row[17])
    hit_day_16 = float(row[18])
    yeardata.append(year)



    hitday_00.append(hit_day_00)
    hitday_01.append(hit_day_01)
    hitday_02.append(hit_day_02)
    hitday_03.append(hit_day_03)
    hitday_04.append(hit_day_04)
    hitday_05.append(hit_day_05)
    hitday_06.append(hit_day_06)
    hitday_08.append(hit_day_08)
    hitday_09.append(hit_day_09)
    hitday_10.append(hit_day_10)
    hitday_11.append(hit_day_11)
    hitday_12.append(hit_day_12)
    hitday_13.append(hit_day_13)
    hitday_14.append(hit_day_14)
    hitday_15.append(hit_day_15)
    hitday_16.append(hit_day_16)
    if year >= 2019:
        hitday_07.append(hit_day_07)

print("년도 : ", yeardata)
print("서울 : ", hitday_00)
print("부산 : ", hitday_01)
print("대구 : ", hitday_02)
print("인천 : ", hitday_03)
print("광주 : ", hitday_04)
print("대전 : ", hitday_05)
print("울산 : ", hitday_06)
print("세종 : ", hitday_07)
print("경기 : ", hitday_08)
print("강원 : ", hitday_09)
print("충북 : ", hitday_10)
print("충남 : ", hitday_11)
print("전북 : ", hitday_12)
print("전남 : ", hitday_13)
print("경북 : ", hitday_14)
print("경남 : ", hitday_15)
print("제주 : ", hitday_16)