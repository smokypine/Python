### 람다함수(lambda function()) ###
## 목적은 function을 짧게 만드는데, 이름짓기가 귀찮다. ""실행문이 하나밖에 없다!!!"" ------> 한줄짜리 function으로 만든다.
def addone(x):
    return x + 1
print(addone(1))

#위의 함수를 다음과 같이 바꾼다.
#lambda parameter_name : parameter로 실행하는 문
lambda x : x + 1
print((lambda x : x+1)(1)) # <-------------- 이것과 위의 addone(x) 함수가 동일하다.

# num1값과 num2값을 입력하여 num1+num2값을 출력하는 lambda함수
print((lambda num1,num2 : num1+num2)(100, 200))


### map 과 filter ###
## 기존의 특정 list가 존재할 때
list1 = [1,2,3,4,5,6]
# addone() 을 하여
#list2 = [2,3,4,5,6,7] 로 만드는 것. <------------ 이럴 때 map을 쓴다.
print("list1 :", list1)
## map(함수, input 리스트) <---- 입력한 리스트를 함수를 적용시켜 새로운 리스트를 만들어라.
map(addone, list1)
list2 = list(map(lambda x : x+1, list1))
print("list2 :", list2)


list1 = [1,2,3,4,5,6]
list2 = [2,3,4,5,6,7]
# 위의 두 리스트를 더해 result = [3,5,7,9,11,13] 를 만들어라.
result = list(map(lambda x,y : x+y, list1,list2))
print("result :", result)