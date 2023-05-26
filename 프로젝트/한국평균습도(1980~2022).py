# 한국평균기온(1970 ~ 2022)
# 레퍼런스 : http://www.climate.go.kr/home/CCS/contents_2021/37_2_past_analysis_etc.php
import csv
import matplotlib.pyplot as plt 
import numpy as np
## 평균습도 1980~2022데이터
f1 = open('C:/Users/김동현/Desktop/2학년 1학기 파이썬 수업/Python/프로젝트/온실가스_평균기온/한국 평균기온,습도,폭염일수,이산화탄소농도(이건 세계기준)_1980~2022.csv', encoding='UTF8')            # CSV 파일 열어 f에 저장 
humidity = csv.reader(f1)                       # reader() 함수로 읽기
header = next(humidity)       

##평균기온
humidity_1980_mean = 0
humidity_1985_mean = 0
humidity_1990_mean = 0
humidity_1995_mean = 0
humidity_2000_mean = 0
humidity_2005_mean = 0
humidity_2010_mean = 0
humidity_2015_mean = 0
humidity_2020_mean = 0

## 상관관계 분석을 위한 1980~2022년의 평균온도, 이산화탄소 농도 리스트 작성. 
everyyear_temp = []##평균기온
everyyear_CO2_mean = []##이산화탄소농도
everyyear_humidity_mean = []##평균습도

for row in humidity:
    year = int(row[0][0:4])
    yearly_humidity_mean = float(row[3])
    ## 상관관계를 구하기 위한 변수들 ---
    yearly_T_mean = float(row[1])
    everyyear_temp.append(yearly_T_mean)
    everyyear_humidity_mean.append(yearly_humidity_mean)
    everyyear_CO2_mean.append(float(row[5]))
    ## --------------------------------
    if row[0] != "":
        if year >= 1980 and year < 1985:
            humidity_1980_mean += yearly_humidity_mean
        if year >= 1985 and year < 1990:
            humidity_1985_mean += yearly_humidity_mean
        if year >= 1990 and year < 1995:
            humidity_1990_mean += yearly_humidity_mean
        if year >= 1995 and year < 2000:
            humidity_1995_mean += yearly_humidity_mean
        if year >= 2000 and year < 2005:
            humidity_2000_mean += yearly_humidity_mean
        if year >= 2005 and year < 2010:
            humidity_2005_mean += yearly_humidity_mean
        if year >= 2010 and year < 2015:
            humidity_2010_mean += yearly_humidity_mean
        if year >= 2015 and year < 2020:
            humidity_2015_mean += yearly_humidity_mean
        if year >= 2020:
            humidity_2020_mean += yearly_humidity_mean

humidity_1980_mean /= 5
humidity_1985_mean /= 5
humidity_1990_mean /= 5
humidity_1995_mean /= 5
humidity_2000_mean /= 5
humidity_2005_mean /= 5
humidity_2010_mean /= 5
humidity_2015_mean /= 5
humidity_2020_mean /= 3

year5_humidity_mean = []
year5_humidity_mean.append(humidity_1980_mean)
year5_humidity_mean.append(humidity_1985_mean)
year5_humidity_mean.append(humidity_1990_mean)
year5_humidity_mean.append(humidity_1995_mean)
year5_humidity_mean.append(humidity_2000_mean)
year5_humidity_mean.append(humidity_2005_mean)
year5_humidity_mean.append(humidity_2010_mean)
year5_humidity_mean.append(humidity_2015_mean)
year5_humidity_mean.append(humidity_2020_mean)

f1.close()
year5 = ["1980", "1985", "1990", "1995", "2000", "2005", "2010", "2015", "2020"] 


x=[x for x in range(len(year5))]
plt.plot(x, year5_humidity_mean, 'r--', label="Humidity")

plt.bar(range(len(year5)), year5_humidity_mean, width=0.70)
plt.ylim(bottom=60)
 
plt.title("KOR Average Humidity Since 1980th")   # 제목을 설정한다. 
plt.ylabel("Average humidity(%)")         # y축에 레이블를 붙인다. 
 
# y축에 틱을 붙인다. 
plt.xticks(range(len(year5)), year5) 
plt.legend()
plt.show()

## 상관관계 확인
correlation = np.corrcoef(everyyear_temp, everyyear_CO2_mean)
print("평균기온과 이산화탄소 농도의 상관관계 : ", correlation) ## 꽤나 높은 상관관계

correlation = np.corrcoef(everyyear_humidity_mean, everyyear_CO2_mean)
print("평균습도와 이산화탄소 농도의 상관관계 : ", correlation) ## 중간정도의 상관관계