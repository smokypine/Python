#서울 평균기온. 시작기준을 1970년대로 잡아 2000~ 2004, 2005~2009, 2010~2014, 2015~2019, 2020~2022 의 5~9월 사이의 평균온도의 변화를 비교함
#확인 결과 1970년대에 비해 온도가 전반적으로 상승되었음을 확인할 수 있음.

import csv
import matplotlib.pyplot as plt 
import numpy as np
 
f = open('C:/Users/김동현/Desktop/2학년 1학기 파이썬 수업/Python/프로젝트/열지수/서울 열지수(1973~2022 5월~9월).csv', encoding='cp949')            # CSV 파일 열어 f에 저장 
data = csv.reader(f)                       # reader() 함수로 읽기
header = next(data)                        # 헤더를 제거

monthly_hit = [ 0 for x in range(5) ]    # 5~9월간 매달 열지수를 담을 리스트
days_counted = [ 0 for x in range(5) ]    # 각 달마다 측정된 일수

temp1970th = [ 0 for x in range(5) ]
temp1970th_dayscount=[ 0 for x in range(5) ]
temp2000th_fh = [ 0 for x in range(5) ]##2000년대 전반
temp2000th_fh_dayscount=[ 0 for x in range(5) ]
temp2000th_sh = [ 0 for x in range(5) ]##2000년대 후반
temp2000th_sh_dayscount=[ 0 for x in range(5) ]
temp2010th_fh = [ 0 for x in range(5) ]##2010년대 전반
temp2010th_fh_dayscount=[ 0 for x in range(5) ]
temp2010th_sh = [ 0 for x in range(5) ]##2010년대 후반
temp2010th_sh_dayscount=[ 0 for x in range(5) ]
temp2020th = [ 0 for x in range(5) ]
temp2020th_dayscount=[ 0 for x in range(5) ]

for row in data: 
    month = int(row[0][4:6])               # 0번 열에서 달 정보 추출
    year=int(row[0][0:4])               ## 년도별로 구분하는 방법

    if row[4] != '':
        hit = float(row[1])
        if year >= 1973 and year < 1980:           
            temp1970th[month-5] += hit
            temp1970th_dayscount[month-5] += 1  
        if year >= 2000 and year< 2005:           
            temp2000th_fh[month-5] += hit
            temp2000th_fh_dayscount[month-5] += 1 
        if year >= 2005 and year< 2010:           
            temp2000th_sh[month-5] += hit
            temp2000th_sh_dayscount[month-5] += 1 
        if year >= 2010 and year < 2015:           
            temp2010th_fh[month-5] += hit
            temp2010th_fh_dayscount[month-5] += 1   
        if year >= 2015 and year < 2020:           
            temp2010th_sh[month-5] += hit
            temp2010th_sh_dayscount[month-5] += 1   
        if year >= 2020:           
            temp2020th[month-5] += hit
            temp2020th_dayscount[month-5] += 1   


for i in range(5) :
    temp1970th[i] /= temp1970th_dayscount[i]   # 일수로 나누어 월평균 구하기
    temp2000th_fh[i] /= temp2000th_fh_dayscount[i]   # 일수로 나누어 월평균 구하기
    temp2000th_sh[i] /= temp2000th_sh_dayscount[i]   # 일수로 나누어 월평균 구하기
    temp2010th_fh[i] /= temp2010th_fh_dayscount[i]   # 일수로 나누어 월평균 구하기
    temp2010th_sh[i] /= temp2010th_sh_dayscount[i]   # 일수로 나누어 월평균 구하기
    temp2020th[i] /= temp2020th_dayscount[i]   # 일수로 나누어 월평균 구하기

      
print(monthly_hit)
plt.xticks(range(0,5), ["May", "June", "July", "August", "September"]) 
plt.ylabel("Temperture Index")
plt.title("Seoul Temperture Index")

plt.plot(temp1970th, 'blue', label="1970th",marker='o')
plt.plot(temp2000th_fh, 'brown', label="2000th first half",marker='o')
plt.plot(temp2000th_sh, 'magenta', label="2000th second half",marker='o')
plt.plot(temp2010th_fh, 'green', label="2010th first half",marker='o')
plt.plot(temp2010th_sh, 'orange', label="2010th second half",marker='o')
plt.plot(temp2020th, 'red', label="2020th",marker='o')
plt.legend()
plt.show()

f.close()                                  # 파일을 닫는다.