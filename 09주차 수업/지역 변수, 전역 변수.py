### 지역 변수, 전역 변수 ###
num = 100 #전역 변수 global variable
def addone() :
    num = 10
    print("addone() :", num + 1)
    print("addone()의 num :", num)
    num = num * 8 + 200
    return num
result = addone()
print("전역변수 num :", num) # 즉 함수 안에서의 변수와 그렇지 않은 변수는 변수명이 같다고 하더라도 둘 다 다른 변수이다.
print("addone()의 결과값 :", result)


## 내부 function에서 num을 수정하지 않는다면 전역변수 num값을 그대로 사용할 수 있다.
def addone1() :
    print("addone1() 내부의 num :", num)
    print("addone1() + 1 :", num+1)
addone1()
print("전역번수 num의 값 :", num) # 함수를 벗어나면 바뀐 num값은 초기화된다.


## 내부 function에서도 전역변수를 사용하면서 수정을 하여 function()이 끝난 뒤에도 반영을 하고 싶다.
def addone2() :
    global num # num이 전역변수라는 의미. 제일 위에서 선언한 num = 100과 커넥팅이 되어 변수에 새로운 값 대입 가능.
    num = 200
    num = num + 1
addone2()
print("addone2() 함수 선언 이후 전역변수 num의 값 :", num) # <---- num = 201이 반영됨.




### 인자의 갯수가 여러개인 경우 ###
# EX) print()
# print(1,2,3,4,5,6,7,8)
def hello(*names) : # *values : object <------- * 이 중요. * 은 인자를 여러개로 쓸 수 있게 해준다.
    for i in names :
        print("hello", i)
hello("홍길동","김길동","박길동","장길동")


# 몇 개의 숫자를 받던 상관없이 그 숫자들의 합을 구하여라.
def plus(*numbers) :
    result = 0
    for num in numbers :
        result = result + num
    return result
print("합 : ", plus(5,21,7,19,31))
list1 = [2,4,8,3,15,31,78,12]
print("list1의 합 :", plus(*list1)) # <---------- 리스트의 값을 가져올 때도 *를 붙이면 가능하다.


# dictionary = {key1 : value1, key2 : value2}
# 이 경우는 ** 를 한다.
coffee = {"아메리카노" : 2000, "카페라떼" : 3000, "홍차" : 2500}
def print_menu(**key_value) :
    for key in key_value :
        print(key , key_value[key],"원")

print_menu(**coffee)
print_menu(핫도그 = 2000, 스폰케이크 = 3000, 튀김 = 2000, 순대 = 4000) # 딕셔너리는 이런 방식으로 쓸 수도 있다.


# 인자가 여러개일 경우 복합
def func1(*num, **menu) : 
    #num들의 합
    result = 0
    for n in num :
        result = result + n
    print(result)
    #menu를 출력하라
    for key in menu :
        print(key, menu[key])

func1(*list1, **coffee)
func1(4,2,65,4,26,7,1, 삼겹살 = 15000, 갈비살 = 18000, 항정살 = 20000, 돼지껍데기 = 5000)