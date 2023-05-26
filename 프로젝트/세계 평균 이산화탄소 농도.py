#서울 평균 열지수
#시작기준을 1970년대로 잡아 2000~ 2004, 2005~2009, 2010~2014, 2015~2019, 2020~2022 의 5~9월 사이의 평균 열지수의 변화를 비교함
#확인 결과 2000년대 전반을 제외하면 대부분 기준점인 1970년대에 비해 열지수가 상승하였으며 2020년대에 가까워질수록 큰 폭으로 상승함.

import csv
import matplotlib.pyplot as plt 
import numpy as np
 
f = open('C:/Users/김동현/Desktop/2학년 1학기 파이썬 수업/Python/프로젝트/온실가스_평균기온/세계 평균 해양 표면 연평균 CO2 데이터_1979~2022.csv', encoding='cp949')            # CSV 파일 열어 f에 저장 
data = csv.reader(f)                       # reader() 함수로 읽기
header = next(data)                        # 헤더를 제거

##yearly_CO2_mean = [0 for x in range()]

year=[]
yearly_CO2_mean=[]
for row in data:
    year.append(row[0])
    yearly_CO2_mean.append(row[1])
 
#plt.xticks(year) 
plt.ylabel("Yearly Mean")
plt.title("Yearly World CO2 Density Mean")

plt.plot( year, yearly_CO2_mean, 'blue', label="CO2",marker='o')
plt.legend()
plt.show()

f.close()                                  # 파일을 닫는다.