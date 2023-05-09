l1 = ["파이썬", "DB프로그래밍", "JAVA", "웹프론트엔드", "IOT"] # 수강과목
l2 = [101, 102, 103, 104, 105] # 강의실
# dictionary로 만든다.
d1 = dict(zip(l1, l2))

# for문 혹은 while문을 돌린다. quit이 들어올 때까지.
while True:
    # input()으로 강의명 입력
    c = input("강의명을 입력하시오 : ")
    if c =="quit":
        print("quit을 입력했으니 종료합니다.")
        break
    else :        
        if c in d1.keys() :
            # 강의실을 알려준다.
            print(d1[c])
        else :
            print("잘못 입력하였습니다. 다시 입력하십시오.")
            continue
