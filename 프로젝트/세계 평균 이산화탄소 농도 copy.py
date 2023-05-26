#서울 평균 열지수
#시작기준을 1970년대로 잡아 2000~ 2004, 2005~2009, 2010~2014, 2015~2019, 2020~2022 의 5~9월 사이의 평균 열지수의 변화를 비교함
#확인 결과 2000년대 전반을 제외하면 대부분 기준점인 1970년대에 비해 열지수가 상승하였으며 2020년대에 가까워질수록 큰 폭으로 상승함.

import csv
import matplotlib.pyplot as plt 
import numpy as np
## 이산화탄소 데이터
f1 = open('C:/Users/김동현/Desktop/2학년 1학기 파이썬 수업/Python/프로젝트/온실가스_평균기온/세계 평균 해양 표면 연평균 CO2 데이터_1979~2022.csv', encoding='cp949')            # CSV 파일 열어 f에 저장 
CO2 = csv.reader(f1)                       # reader() 함수로 읽기
header = next(CO2)                        # 헤더를 제거

CO2_1980_mean = 0
CO2_1990_mean = 0
CO2_2000_mean = 0
CO2_2010_mean = 0
CO2_2020_mean = 0

for row in CO2:
    year_CO2 = int(row[0])
    yearly_CO2_mean = float(row[1])
    if row[0] != "":
        if year_CO2 >= 1979 and year_CO2 < 1990:
            CO2_1980_mean += yearly_CO2_mean
        if year_CO2 >= 1990 and year_CO2 < 2000:
            CO2_1990_mean += yearly_CO2_mean
        if year_CO2 >= 2000 and year_CO2 < 2010:
            CO2_2000_mean += yearly_CO2_mean
        if year_CO2 >= 2010 and year_CO2 < 2020:
            CO2_2010_mean += yearly_CO2_mean
        if year_CO2 >= 2020:
            CO2_2020_mean += yearly_CO2_mean

CO2_1980_mean /= 11
CO2_1990_mean /= 10
CO2_2000_mean /= 10
CO2_2010_mean /= 10
CO2_2020_mean /= 3

year10_CO2_mean = []
year10_CO2_mean.append(CO2_1980_mean)
year10_CO2_mean.append(CO2_1990_mean)
year10_CO2_mean.append(CO2_2000_mean)
year10_CO2_mean.append(CO2_2010_mean)
year10_CO2_mean.append(CO2_2020_mean)


## 메탄 데이터
f2 = open('C:/Users/김동현/Desktop/2학년 1학기 파이썬 수업/Python/프로젝트/온실가스_평균기온/세계 평균 해양 표면 연평균 메탄 데이터 1984~2022.csv', encoding='cp949')            # CSV 파일 열어 f에 저장 
CH4 = csv.reader(f2)                       # reader() 함수로 읽기
header = next(CH4)                        # 헤더를 제거

CH4_1980_mean = 0
CH4_1990_mean = 0
CH4_2000_mean = 0
CH4_2010_mean = 0
CH4_2020_mean = 0

for row in CH4:
    year = int(row[0])
    yearly_CH4_mean = float(row[1])
    if row[0] != "":
        if year >= 1984 and year < 1990:
            CH4_1980_mean += yearly_CH4_mean
        if year >= 1990 and year < 2000:
            CH4_1990_mean += yearly_CH4_mean
        if year >= 2000 and year < 2010:
            CH4_2000_mean += yearly_CH4_mean
        if year >= 2010 and year < 2020:
            CH4_2010_mean += yearly_CH4_mean
        if year >= 2020:
            CH4_2020_mean += yearly_CH4_mean

CH4_1980_mean /= 6
CH4_1990_mean /= 10
CH4_2000_mean /= 10
CH4_2010_mean /= 10
CH4_2020_mean /= 3

year10_CH4_mean = []
year10_CH4_mean.append(CH4_1980_mean)
year10_CH4_mean.append(CH4_1990_mean)
year10_CH4_mean.append(CH4_2000_mean)
year10_CH4_mean.append(CH4_2010_mean)
year10_CH4_mean.append(CH4_2020_mean)

year10 = ["1980", "1990", "2000", "2010", "2020"]


#plt.xticks(range(0,5), ["1980th", "1990th", "2000th", "2010th", "2020th"]) 
#plt.ylabel("Yearly Mean")
#plt.title("Yearly World GREEN GAS Density Mean")

#plt.plot( year10_CO2_mean, 'blue', label="CO2",marker='o')
#plt.plot( year10_CH4_mean, 'red', label="CH4",marker='o')
#plt.legend()
#plt.show()

f1.close()    
f2.close()                              # 파일을 닫는다.

# 갯수가 2 x 2개, 크기가 (5, 5) 인치 
fig, ax = plt.subplots(2, 2, figsize=(10, 8)) 
fig.suptitle("Yearly World GREEN GAS Density Mean")
 
ax[0, 0].plot(year10, year10_CO2_mean, 'blue', label="CO2", marker='o')
ax[0, 0].set_title("CO2")

ax[0, 1].plot(year10, year10_CH4_mean, 'red', label="CH4", marker='o')
ax[0, 1].set_title("CH4")


plt.setp(ax[0,0], xlabel='x axis label')
plt.setp(ax[0,0], ylabel='x axis label')
plt.setp(ax[0,1], xlabel='x axis label')
plt.setp(ax[0,1], ylabel='x axis label')



plt.show()
