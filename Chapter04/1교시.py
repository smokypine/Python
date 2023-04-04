###제어문
##if문
'''
if 조건 : 
    실행문1
elif 조건 :
    실행문2
else : 
    실행문3
'''
hour = 13
if hour < 12 :
    print("12시가 지나지 않았으니 오전입니다.")
elif hour < 18 :
    print("12시가 지나고 18시가 안 지났으니 오후입니다.")
else :
    print("18시가 지났으니 저녁입니다.")

print("\n")
#장학금을 주는 퀴즈
#score < 200 일 경우 50만원을 줌
#200 <= score < 400 일 경우 100만원
#400 <= score < 500 일 경우1000만원
score_str = input("점수는? : ")
score = int(score_str)
if score < 200 :
    print("점수가 ", score, "이므로 50만원을 획득합니다.")
elif score < 400 :
    print("점수가 ", score, "이므로 100만원을 획득합니다.")
else : 
    ("점수가 ", score, "이므로 1000만원을 획득합니다.")

print("\n")

lunch_str = input("점심을 먹겠습니까? : ")
if lunch_str == 'yes' : 
    menu = input("그렇다면 어디에서 식사를 하시겠습니까? : ")
    if menu == '써브웨이' : 
        print("8호관 1층으로 가십시오.")
    elif menu == '학식' : 
        print("8호관 3층으로 가십시오.")
    else :
        print("그런 가게는 없습니다.")

print("\n")


### 반복문 for
'''
for i in 1,3,4,5,6, 8 :
    print(i)
'''
print("range1")
for i in range(0, 10, 1): ### for(int i; i<10; i++){} 과 동일하다.
    print(i)
print("\n")

print("range2")
sum=0
for i in range(10) : ### 위의 for i in range(0,10,1)과 동일하다.
    sum = sum + i
    #sum += i
    print(i, "번째 sum은 : ", sum)
else:
    print("for문의 조건이 더이상 만족하지 않습니다.")
    print("i가 range(10)을 벗어남.")
    print("for 문이 break나 continue로 종료된 게 아니라 정상종료시에만 실행됩니다.")
print(sum)


