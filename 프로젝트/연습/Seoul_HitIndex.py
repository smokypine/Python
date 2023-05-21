#서울 열지수

#
import csv
import matplotlib.pyplot as plt 
 
f = open('C:/Users/김동현/Desktop/2학년 1학기 파이썬 수업/Python/프로젝트/서울(2019~2022).csv', encoding='UTF8')            # CSV 파일 열어 f에 저장 
data = csv.reader(f)                       # reader() 함수로 읽기
header = next(data)                        # 헤더를 제거

monthly_temp = [ 0 for x in range(5) ]    # 매달 풍속을 담을 리스트
days_counted = [ 0 for x in range(5) ]    # 각 달마다 측정된 일수

HitIndex2019 = [ 0 for x in range(5) ]
HitIndex2019_dayscount=[ 0 for x in range(5) ]
HitIndex2020 = [ 0 for x in range(5) ]
HitIndex2020_dayscount=[ 0 for x in range(5) ]
HitIndex2021 = [ 0 for x in range(5) ]
HitIndex2021_dayscount=[ 0 for x in range(5) ]
HitIndex2022 = [ 0 for x in range(5) ]
HitIndex2022_dayscount=[ 0 for x in range(5) ]

for row in data: 
    month = int(row[0][5:7])               # 0번 열에서 달 정보 추출
    year=int(row[0][0:4])               ## 년도별로 구분하는 방법
    ##if row[4] !=  '' :                     # 풍속 데이터 존재하는지 확인
    ##    temp = float(row[4])               # 풍속을 얻어 온다.
    ##    monthly_temp[month-5] += temp      # 해당 달에 풍속 데이터 추가
    ##    days_counted[month-5] += 1         # 해당 달의 일수를 증가

    if row[4] != '':
        maxtmp = float(row[12])
        if year == 2019:           
            HitIndex2019[month-5] += maxtmp
            HitIndex2019_dayscount[month-5] += 1  
        if year == 2020:
            HitIndex2020[month-5] += maxtmp
            HitIndex2020_dayscount[month-5] += 1  
        if year == 2021:
            HitIndex2021[month-5] += maxtmp
            HitIndex2021_dayscount[month-5] += 1  
        if year == 2022:
            HitIndex2022[month-5] += maxtmp
            HitIndex2022_dayscount[month-5] += 1  

for i in range(5) :
    ##monthly_temp[i] /= days_counted[i]   # 일수로 나누어 월평균 구하기
    HitIndex2019[i] /= HitIndex2019_dayscount[i]   # 일수로 나누어 월평균 구하기
    HitIndex2020[i] /= HitIndex2020_dayscount[i]   # 일수로 나누어 월평균 구하기
    HitIndex2021[i] /= HitIndex2021_dayscount[i]   # 일수로 나누어 월평균 구하기
    HitIndex2022[i] /= HitIndex2022_dayscount[i]   # 일수로 나누어 월평균 구하기
      
print(monthly_temp)
##plt.plot(monthly_temp, 'blue', label="Avg")
plt.xticks(range(0,5), ["May", "June", "July", "August", "September"]) 
plt.ylabel("Avg Temperature(°C)")
plt.title("2019 Seoul Hit Index")

plt.plot(HitIndex2019, 'red', label="2019",marker='o')
plt.plot(HitIndex2020, 'green', label="2020",marker='^')
plt.plot(HitIndex2021, 'blue', label="2021",marker='*')
plt.plot(HitIndex2022, 'pink', label="2022",marker='o')
plt.legend()
plt.show()

f.close()                                  # 파일을 닫는다.