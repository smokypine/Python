### Lamda 함수 작성하기
## map, filter 사용할줄 알아야

# 입력 숫자 1개 받고
# 출력으로 숫자 +1 을 하는 함수
def addone(num):
    return num + 1
print(addone(10)) # 11이 출력된다. 그럼 이걸 람다함수로 바꿔보자.

#lambda 입력값 : return값
print((lambda num : num+1)(10)) # 위 addone(10)함수와 동일하게 11이 출력된다.


#1. 숫자 2개를 입력받아 합을 return하는 함수를 만들어라
a = int(input("숫자 1을 입력하시오 :"))
b = int(input("숫자 2를 입력하시오 :"))
print((lambda num1, num2 : num1+num2)(a,b))
def sum1(n1, n2):
    return n1+n2

#2. 숫자 2개를 입력받아서 a,b입력, a%b를 출력하라.
c = int(input("n1을 입력하시오 :"))
d = int(input("n2를 입력하시오 :"))
print((lambda n1,n2 : n1%n2)(c,d))
def cal(n1, n2) :
    return n1%n2

#3. map을 활용하여
list1 = [20,22,23,24,25,26] #을 [21, 23, 24, 25, 26, 27]로 바꾸고 싶다면?
# list(map(lambda function, 입력값 리스트))
aftermap = list(map(lambda num : num+1, list1))
print(aftermap)

#4. map을 이용하여 리스트 2개의 합을 구하는 것과 리스트 2개의 나머지를 구하는 것을 해보자.
list1 = [20,22,23,24,25,26]
list2 = [2, 3, 5, 2, 1, 6]
summap = list(map(lambda n1,n2 : n1+n2, list1,list2))
print("두 리스트의 합", summap)
calmap = list(map(lambda n1,n2 : n1%n2, list1,list2))
print("두 리스트의 나머지", calmap)

#5. map을 이용하여 리스트 2개의 합을 튜플로 작성해보자.
list1 = [20,22,23,24,25,26]
list2 = [2, 3, 5, 2, 1, 6]
summapTuple = tuple(map(lambda n1,n2 : n1+n2, list1,list2))
print("두 리스트의 합을 튜플로 :", summapTuple)

#6. filter을 사용하여 리스트 [1, -2, 3, -5, 8, 3]에서 음수를 전부 제거해 보자
#filter(function, list)
allpluslist = list(filter(lambda x : x>0, [1, -2, 3, -5, 8, 3]))
print("음수를 전부 제거한 리스트 :", allpluslist)
 #lambda x : x>0 은 0보다 큰 것만 출력시키는 것.

