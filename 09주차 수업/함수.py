### 함수 ###
# 함수란? input을 주면 output이 나오는 것. y = f(x)

## input 값에 3을 곱하는 함수의 정의
# input = 숫자 -> num1
# output = 숫자 -> output_num
# 이런 기능을 하는 function() -> multi
def multi(num1) : 
    output_num = num1 * 3
    return output_num
# 위에서 정의한 함수를 호출
print("multi(10)의 값 :", multi(10))


## hello라는 이름의 function. input으로는 사람 이름 2개를 입력받음. output으로는 안녕 1번사람, 안녕 2번사람을 함수 내에서 출력
def hello(name1, name2):
    print("안녕",name1,"1번 사람, 안녕",name2,"2번 사람.")
first_name = input("1번 이름을 입력하시오 :")
second_name = input("2번 이름을 입력하시오 :")
hello(first_name, second_name)


# 함수에 기본값이 있는 경우
def hello(name1 ="홍길동", name2 ="임꺽정"):
    print("안녕",name1,"1번 사람, 안녕",name2,"2번 사람.")
hello() # 이렇게 되면 기본값으로 준 홍길동, 임꺽정이 출력된다.
first_name = input("1번 이름을 입력하시오 :")
second_name = input("2번 이름을 입력하시오 :")
hello(first_name, second_name)


## 두 개의 숫자를 입력받아 두 개의 합을 함수 내에서 출력하시오.
def plus(num1, num2) :
    answer = num1 + num2
    print("두 수의 합 :", answer)
plus(100,299) # 이 경우 아래와 같이 input()을 한 것과는 달리 int값으로 인지를 하여 399라는 답이 나온다.
first_num = int(input("첫번째 수를 입력하시오 :"))
second_num = int(input("두번째 수를 입력하시오 :"))
plus(first_num, second_num) # 하지만 input()으로 받았으므로 first_num과 second_num은 모두 char값이다.


