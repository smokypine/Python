# 한국폭염일수(1973 ~ 2022)
# 레퍼런스 : https://data.kma.go.kr/climate/heatWave/selectHeatWaveMixChart.do?pgmNo=674
import csv
import matplotlib.pyplot as plt 
import numpy as np
## 폭염일수
f1 = open('C:/Users/김동현/Desktop/2학년 1학기 파이썬 수업/Python/프로젝트/온실가스_평균기온/폭염일수/한국 평균 폭염일수 1973~2022.csv', encoding='cp949')            # CSV 파일 열어 f에 저장 
Hit = csv.reader(f1)                       # reader() 함수로 읽기
header = next(Hit)                         # 헤더 제거

# 데이터 저장을 위한 리스트 초기화
yeardata = []
hitday = []#폭염일수
avg_Year_Temp = []#연평균기온

#연평균 폭염일수 평균값을 위한 선언
hit_before1990 = 0
hit_1990th = 0
hit_2000th = 0
hit_2010th = 0
hit_2020th = 0

for row in Hit:
    year = int(row[0])
    hit_day = float(row[1])
    avg_Temp = float(row[3])
    yeardata.append(year)
    hitday.append(hit_day)
    avg_Year_Temp.append(avg_Temp)
    if row[0] != "":
        if year >= 1973 and year < 1990:
            hit_before1990 += hit_day
        if year >= 1990 and year < 2000:
            hit_1990th += hit_day
        if year >= 2000 and year < 2010:
            hit_2000th += hit_day
        if year >= 2010 and year < 2020:
            hit_2010th += hit_day
        if year >= 2020:
            hit_2020th += hit_day


hit_before1990 /= 17
hit_1990th /= 10
hit_2000th /= 10
hit_2010th /= 10
hit_2020th /= 3

hit_mean = []# 폭염일 평균값이 든 배열
hit_mean.append(hit_before1990)
hit_mean.append(hit_1990th)
hit_mean.append(hit_2000th)
hit_mean.append(hit_2010th)
hit_mean.append(hit_2020th)


f1.close()

#서브플롯 생성
fig, ax1 = plt.subplots(figsize=(14,6))

#좌측 Y축 설정
ax1.bar(yeardata, hitday, color='lightblue', width=0.8, label='Heatwave Days')#1973~2022년도의 년별 폭염일수 bar그래프
ax1.set_ylabel('Heatwave Days')
ax1.grid(axis='y', linestyle='-', linewidth=0.5, alpha=0.5)
ax1.set_ylim(0, 35)##35까지 늘려주기


#우측에 새로운 y축 설정
ax2 = ax1.twinx()
ax2.plot(yeardata, avg_Year_Temp, color='gold', label='Yearly Average Temperature')
ax2.set_ylabel("Average Temperature(°C)")  # y축 레이블 설정

#일정기준 설정
threshold = 11
ax2.set_ylim(threshold, max(avg_Year_Temp))

##라인 그리기
# 1973~1990까지
line_x1 = [1973,1990]
line_y1 = [hit_mean[0], hit_mean[0]]
ax1.plot(line_x1, line_y1, color='green', linestyle='--')
ax1.text(1978, 9.1, 'Average 7.9', color='green')
print("hit_mean[0] : ", hit_mean[0])

# 1990~2000까지
line_x2 = [1990,2000]
line_y2 = [hit_mean[1], hit_mean[1]]
ax1.plot(line_x2, line_y2, color='brown', linestyle='--')
ax1.text(1991.5, 11.35, 'Average 10.15', color='brown')
print("hit_mean[1] : ", hit_mean[1])

#2000~2010까지
line_x3 = [2000,2010]
line_y3 = [hit_mean[2], hit_mean[2]]
ax1.plot(line_x3, line_y3, color='red', linestyle='--')
ax1.text(2001.5, 10.31, 'Average 9.11', color='red')
print("hit_mean[2] : ", hit_mean[2])

#2010~2020까지
line_x4 = [2010,2020]
line_y4 = [hit_mean[3], hit_mean[3]]
ax1.plot(line_x4, line_y4, color='violet', linestyle='--')
ax1.text(2011.5, 15.69, 'Average 14.49', color='violet')
print("hit_mean[3] : ", hit_mean[3])

plt.xticks(np.arange(1973, 2023, 2), rotation=70)

plt.title("KOR Average Heatwave days Since 1973")  # 제목 설정
plt.legend()
plt.show()

### 한국 전국 폭염일수 데이터
print("yeardata : ", yeardata)##년도
print("hitday : ", hitday)##년도별 폭염일
print("avg_Year_Temp : ", avg_Year_Temp)##년도별 평균온도
print("hit_mean : ", hit_mean)##1990이전 평균 폭염일, 1990년대 평균 폭염일, 2000년대 평균 폭염일, 2010년대 평균 폭염일, 2020년대 평균 폭염일 
