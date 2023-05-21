#서울 평균 최고기온
#
import csv
import matplotlib.pyplot as plt 
 
f = open('C:/Users/김동현/Desktop/2학년 1학기 파이썬 수업/Python/프로젝트/서울(2019~2022).csv', encoding='UTF8')            # CSV 파일 열어 f에 저장 
data = csv.reader(f)                       # reader() 함수로 읽기
header = next(data)                        # 헤더를 제거

monthly_temp = [ 0 for x in range(5) ]    # 매달 풍속을 담을 리스트
days_counted = [ 0 for x in range(5) ]    # 각 달마다 측정된 일수
maxTemp2019 = [ 0 for x in range(5) ]
maxTemp2019_dayscount=[ 0 for x in range(5) ]
maxTemp2020 = [ 0 for x in range(5) ]
maxTemp2020_dayscount=[ 0 for x in range(5) ]
maxTemp2021 = [ 0 for x in range(5) ]
maxTemp2021_dayscount=[ 0 for x in range(5) ]
maxTemp2022 = [ 0 for x in range(5) ]
maxTemp2022_dayscount=[ 0 for x in range(5) ]
maxT2019=[]
maxT2020=[]
maxT2021=[]
maxT2022=[]
for row in data: 
    month = int(row[0][5:7])               # 0번 열에서 달 정보 추출
    year=int(row[0][0:4])
    ##if row[4] !=  '' :                     # 풍속 데이터 존재하는지 확인
    ##    temp = float(row[4])               # 풍속을 얻어 온다.
    ##    monthly_temp[month-5] += temp      # 해당 달에 풍속 데이터 추가
    ##    days_counted[month-5] += 1         # 해당 달의 일수를 증가

    if row[4] != '':
        maxtmp = float(row[4])
        if year == 2019:           
            maxTemp2019[month-5] += maxtmp
            maxTemp2019_dayscount[month-5] += 1 
            maxT2019.append(maxtmp) 
        if year == 2020:
            maxTemp2020[month-5] += maxtmp
            maxTemp2020_dayscount[month-5] += 1  
            maxT2020.append(maxtmp) 
        if year == 2021:
            maxTemp2021[month-5] += maxtmp
            maxTemp2021_dayscount[month-5] += 1
            maxT2021.append(maxtmp)   
        if year == 2022:
            maxTemp2022[month-5] += maxtmp
            maxTemp2022_dayscount[month-5] += 1 
            maxT2022.append(maxtmp)  

for i in range(5) :
    ##monthly_temp[i] /= days_counted[i]   # 일수로 나누어 월평균 구하기
    maxTemp2019[i] /= maxTemp2019_dayscount[i]   # 일수로 나누어 월평균 구하기
    maxTemp2020[i] /= maxTemp2020_dayscount[i]   # 일수로 나누어 월평균 구하기
    maxTemp2021[i] /= maxTemp2021_dayscount[i]   # 일수로 나누어 월평균 구하기
    maxTemp2022[i] /= maxTemp2022_dayscount[i]   # 일수로 나누어 월평균 구하기
      
print(monthly_temp)
##plt.plot(monthly_temp, 'blue', label="Avg")
#plt.xticks(range(0,5), ["May", "June", "July", "August", "September"]) 
plt.ylabel("Avg Temperature(°C)")
plt.title("2019 Seoul Meen Temperture")

#plt.plot(maxTemp2019, 'red', label="2019")
#plt.plot(maxTemp2020, 'green', label="2020")
#plt.plot(maxTemp2021, 'blue', label="2021")
#plt.plot(maxTemp2022, 'pink', label="2022")
#plt.legend()


plt.hist(maxT2019,10,alpha=0.4)
plt.hist(maxT2020,10,alpha=0.4)
plt.hist(maxT2021,10,alpha=0.4)
plt.hist(maxT2022,10,alpha=0.4)

 
 
plt.show()
f.close()                                  # 파일을 닫는다.
