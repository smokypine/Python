'''
while 조건 :
    수행문
'''
i=10
while i>5:
    print(i, "는 5보다 큽니다.")
    i-=1
print("\n")
#n = 1부터 5까지 찍어보는 프로그램.
#결과물로 1 2 3 4 5 나오도록.
i=1
while i<=5 : 
    print(i, end=' ') #줄바꿈이 아니라 ' '으로 
    i+=1
else:
    print("while이 잘 끝남. 현재 i의 값은 ", i, "입니다.\n")

#놀이기구 탑승
#4명 탑승 가능, 5명은 안됨.
#키 150이상 사람만 탑승 가능.
count = 0
while count<4 :
    height = input("키가 어떻게 되십니까? : ")
    height_int = int(height)
    if height_int >= 150 :
        print("탑승 가능합니다.")
        count = count + 1   
    else :
        print("키가 150미만이기에 탑승이 불가능합니다.")
    print("현재 총 ", count, "명 탑승 중입니다.")   
else :
    print("승객 4명 탑승 완료. 놀이기구가 출발합니다.\n")


#continue, break 키워드. 반복문 안에서 사용됨.
#반복문 중간에 반복을 끊고 실행을 종료하는 것.
#주로 if문 안쪽에서 사용됨.

#input으로 입력을 받는데 무한 반복 중이다. 하지만 exit이란 값을 받으면 입력받는 것을 종료한다.
#apple을 받으면 print("이 단어를 입력하였습니다 : ", write)를 출력하지 않는다.
while True :
    write = input("단어를 넣으시오 : ")
    if write == "exit" : 
        print("exit을 입력하였으므로 반복문을 종료합니다.")
        break
    else :
        if write == 'apple' :
            continue
        print("이 단어를 입력하였습니다 : ", write) #apple을 입력하여 continue가 동작하였을 경우엔 출력이 되지 않음.
    print("아직 while 반복문 안에 있습니다.")
print("while문이 종료되었습니다.")