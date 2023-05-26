#세계 온실가스 증가지수
#시작기준을 1980년대(이산화탄소/메탄), 2000년대(아산화질소, 육불화황)로 각각 잡아 10년, 5년 단위로 평균값을 구해 온실가스의 증가여부를 파악함.
#온실가스는 지구온난화의 주범. <- 당연히 폭염의 이유 증가 가운데 하나.
#단위
#이산화탄소(ppm - part per million) : 100만분의 1
#메탄, 아산화질소(ppb - part per billion) : 10억분의 1
#육불화황(ppt - part per trillion) : 1조 분의 1
# 레퍼런스 : https://gml.noaa.gov/ccgg/trends/

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
# 지구온난화의 1/4만큼의 책임이 있는 것으로 분석되는 온실가스.
# 이산화탄소에 비해 28배 더 심한 온난화를 일으킴. 지구온난화의 2번째 주범
# 아산화질소와 동일하게 가축사육에서 주로 배출됨.(가축의 트림, 방귀가 주 발생원인)
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


## 아산화질소 데이터
# 이산화탄소보다 온실 효과를 유발하는 힘이 256배나 강하다.
# 지구온난화를 일으키는 원인으로서의 입지는 3번째.(1등 : 이산화탄소, 2등 : 메탄)
# 메탄과 동일하게 가축사육에서 주로 배출됨.(가축의 분뇨가 주 발생원인)
f3 = open('C:/Users/김동현/Desktop/2학년 1학기 파이썬 수업/Python/프로젝트/온실가스_평균기온/세계 평균 해양 표면 연평균 아산화질소 데이터_2001~2022.csv', encoding='cp949')            # CSV 파일 열어 f에 저장 
N2O = csv.reader(f3)                       # reader() 함수로 읽기
header = next(N2O)                        # 헤더를 제거

N2O_2000_mean = 0
N2O_2005_mean = 0
N2O_2010_mean = 0
N2O_2015_mean = 0
N2O_2020_mean = 0

for row in N2O:
    year = int(row[0])
    yearly_N2O_mean = float(row[1])
    if row[0] != "":
        if year >= 2001 and year < 2005:
            N2O_2000_mean += yearly_N2O_mean
        if year >= 2005 and year < 2010:
            N2O_2005_mean += yearly_N2O_mean
        if year >= 2010 and year < 2015:
            N2O_2010_mean += yearly_N2O_mean
        if year >= 2015 and year < 2020:
            N2O_2015_mean += yearly_N2O_mean
        if year >= 2020:
            N2O_2020_mean += yearly_N2O_mean

N2O_2000_mean /= 4
N2O_2005_mean /= 5
N2O_2010_mean /= 5
N2O_2015_mean /= 5
N2O_2020_mean /= 3

year10_N2O_mean = []
year10_N2O_mean.append(N2O_2000_mean)
year10_N2O_mean.append(N2O_2005_mean)
year10_N2O_mean.append(N2O_2010_mean)
year10_N2O_mean.append(N2O_2015_mean)
year10_N2O_mean.append(N2O_2020_mean)


## 육불화황
# 절대수치는 낮아도 이산화탄소에 비해 지구온난화 지수가 2만 3500배 높은 온실가스. 
# 대기중에 한 번 배출되면 최대 3200년간 존재하며 불활성, 무색, 무취, 무독성, 난연성으로 500˚C 이상의 열에서도 분해되지 않는 특성을 가져
# 전력기기 분야에서 지속적으로 사용/배출이 되고 있음.
f4 = open('C:/Users/김동현/Desktop/2학년 1학기 파이썬 수업/Python/프로젝트/온실가스_평균기온/세계 평균 해양 표면 연평균 육불화황 데이터.csv', encoding='cp949')            # CSV 파일 열어 f에 저장 
SF6 = csv.reader(f4)                       # reader() 함수로 읽기
header = next(SF6)                        # 헤더를 제거

SF6_2000_mean = 0
SF6_2005_mean = 0
SF6_2010_mean = 0
SF6_2015_mean = 0
SF6_2020_mean = 0

for row in SF6:
    year = int(row[0])
    yearly_SF6_mean = float(row[1])
    if row[0] != "":
        if year >= 1998 and year < 2005:
            SF6_2000_mean += yearly_SF6_mean
        if year >= 2005 and year < 2010:
            SF6_2005_mean += yearly_SF6_mean
        if year >= 2010 and year < 2015:
            SF6_2010_mean += yearly_SF6_mean
        if year >= 2015 and year < 2020:
            SF6_2015_mean += yearly_SF6_mean
        if year >= 2020:
            SF6_2020_mean += yearly_SF6_mean

SF6_2000_mean /= 7
SF6_2005_mean /= 5
SF6_2010_mean /= 5
SF6_2015_mean /= 5
SF6_2020_mean /= 3

year10_SF6_mean = []
year10_SF6_mean.append(SF6_2000_mean)
year10_SF6_mean.append(SF6_2005_mean)
year10_SF6_mean.append(SF6_2010_mean)
year10_SF6_mean.append(SF6_2015_mean)
year10_SF6_mean.append(SF6_2020_mean)


year10_1 = ["1980th", "1990th", "2000th", "2010th", "2020th"]
year10_2 = ["2000th", "2005th", "2010th", "2015th", "2020th"]

f1.close()    
f2.close()
f3.close()
f4.close()# 파일을 닫는다.

# 갯수가 2 x 2개, 크기가 (10, 8) 인치 
fig, ax = plt.subplots(2, 2, figsize=(12, 9)) 
fig.suptitle("Yearly World GREEN GAS Density Mean")
 
ax[0, 0].plot(year10_1, year10_CO2_mean, 'red', label="CO2", marker='o')
ax[0, 0].set_title("CO2")
#plt.setp(ax[0,0], xlabel='From 1980th ~ 2020th')
plt.setp(ax[0,0], ylabel='CO2 10 Year Cycle Increase(ppm)')

ax[0, 1].plot(year10_1, year10_CH4_mean, 'blue', label="CH4", marker='o')
ax[0, 1].set_title("CH4")
#plt.setp(ax[0,1], xlabel='x axis label')
plt.setp(ax[0,1], ylabel='CH4 10 Year Cycle Increase(ppb)')

ax[1, 0].plot(year10_2, year10_N2O_mean, 'green', label="N2O", marker='o')
ax[1, 0].set_title("N2O")
#plt.setp(ax[0,1], xlabel='x axis label')
plt.setp(ax[1,0], ylabel='N2O 5 Year Cycle Increase(ppb)')

ax[1, 1].plot(year10_2, year10_SF6_mean, 'black', label="N2O", marker='o')
ax[1, 1].set_title("SF6")
#plt.setp(ax[0,1], xlabel='x axis label')
plt.setp(ax[1,1], ylabel='SF6 5 Year Cycle Increase(ppt)')

plt.show()
