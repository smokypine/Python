###리스트
##['김','이','박','최']
##숫자, int, float, string 전부 다 가능.
lst = [10,20,30,40,50]
str_list = ['하','호']
print(type(lst))
print(lst[0], lst[1], lst[2], lst[3], lst[4])
print(lst[len(lst)-1], lst[len(lst)-2], lst[len(lst)-3], lst[len(lst)-4], lst[len(lst)-5])

#빈 리스트 생성 --> 하나씩 원소를 추가
list1=[]
list1.append("python") #list1.append('')새로운 원소를 추가한다.
list1.append("JAVA")
list1.append("C++")
list1.append("python")
list1.append("python")
list1.append("python")
print(list1)
print("======= for 1 ======")
for i in range(len(list1)):
    print(list1[i])
print("======= for 2 ======")
for i in list1:     # for i in {'python', 'java', 'c++', 'python', 'python', 'python'}과 동일.
    print(i)

print("\n")

#count 와 index
print("======= count와 index ======")
print("count : ", list1.count("python"))##파이썬이 list1 가운데 몇개가 있는지를 출력
print("index : " , list1.index("JAVA"))##자바가 어느 위치에 있는가를 출력


print("\n")

#수정
print("======= 수정 ======")
list1[0] = "AI"
list1[2] = "IOT"
print("list1 : ", list1)

print("\n")

#슬라이싱 [0:5:1] <--- 0부터 시작해서 4까지 1개씩 넘어가라
print("======= 슬라이싱 ======")
list2 = list1[1:5:1] ##['JAVA', 'IOT', 'python', 'python']
print("list1[1:5:1] : ", list2)
list2 = list1[0:5:2] ##['AI', 'IOT', 'python']
print("list1[0:5:2] : ", list2)
list2 = list1[0:len(list1):1] ##['AI', 'JAVA', 'IOT', 'python', 'python', 'python']
print("list1[0:len(list1):1] : ", list2)
list2 = list1[::-1] ##['python', 'python', 'python', 'IOT', 'JAVA', 'AI'] <--- 반대로 출력된다.
print("list1[::-1] : ", list2)

print("\n")

#list1의 일부를 list3에 대입한다.
print("======= list1의 일부를 list3에 대입한다. ======")
list2 = list1[2:6:3]
list3=[1,2,3,4,5,6,7,8,9]
list3[1] = list2
print("list3 : ", list3) ##[1, ['IOT', 'python'], 3, 4, 5, 6, 7, 8, 9]
list3[1:2] = list2
print("list3 : ", list3) ##[1, 'IOT', 'python', 3, 4, 5, 6, 7, 8, 9] 위와 각기 다르게 나옴.

print("\n")

#insert
print("======= insert ======")
food = []
food.append("짜장면")
food.append("샌드위치")
print(food)
food.insert(0,"파스타")
food.insert(2,"짬뽕")
print(food)

print("\n")

#remove
print("======= remove ======")
food.remove("짬뽕")
print(food)

print("\n")

#pop
print("======= pop ======")
print("food :", food)
print("food.pop() :", food.pop()) # food의 마지막 값이 pop됨. 그리고 그 pop된 값은 food 리스트에서 사라진다.
print("food :", food)
print("food.pop(0) :", food.pop(0))
print("food :", food)

print("\n")

#extend 뒤에 붙인다.
print("======= extend ======")
food.append("막국수")
food.append("순대국밥")
print("food :", food)
dessert = ["마카롱", "케익", "홍차", "와플"]
food.extend(dessert)
print("food :", food) ##food : ['짜장면', '막국수', '순대국밥', '마카롱', '케익', '홍차', '와플']
##food_list = food + dessert
##print("food_list :", food_list) food_list : ['짜장면', '막국수', '순대국밥', '마카롱', '케익', '홍차', '와플']

print("\n")

#reverse
print("======= reverse ======") ## 순서를 바꾸어버린다.
print("food :", food)
food.reverse()
print("reverse를 한 food :", food)

print("\n")

#clear
print("======= clear ======")
print("clear 하기 이전 food :", food)
food.clear()
print("clear 한 이후 food :", food)
##del food <---- 메모리에 있던 food 리스트를 삭제한다.

print("\n")

#sort
print("======= sort 정렬 ======")
lst1 = [10, 4, 23, 6, 3, 1, 56, 8, 2]
print("lst1 :", lst1)
print("sorted(lst1)을 한 lst1 :", sorted(lst1)) ##변경이 되긴 하지만 lst1의 값이 변하지는 않는다.
print("lst1 :", lst1)
lst1.sort()
print("sort를 한 뒤의 lst1 :", lst1)

print("\n")


## 리스트 컴프리헨션
## 리스트를 작성하는데 긴 코드가 아니라 짧게 쓰고 싶다.
print("======= 리스트 컴프리헨션 ======")
lst3 = []
for i in range(11) :
    lst3.append(i)
print("lst3 :", lst3)
#리스트 컴프리헨션을 작성하는 법
#리스트 변수명 = [항목 for i in range(11)]
l3 = [i for i in range(0,11,2)] #l3 : [0, 2, 4, 6, 8, 10]
print("l3 :", l3)

#리스트 컴프리헨션으로 0~10까지의 숫자의 제곱을 원소로 가지는 리스트를 작성하라.
#i**2
print("======= 리스트 컴프리헨션으로 0~10까지의 숫자의 제곱을 원소로 가지는 리스트를 작성하라. ======")
lst4 = [i**2 for i in range(0,11)]
print("lst4 :", lst4)
print("======= 리스트 컴프리헨션으로 0~10까지의 숫자의 3배를 원소로 가지는 리스트를 작성하라. ======")
lst4 = [i*3 for i in range(0,11)]
print("lst4 :", lst4)
print("======= 리스트 컴프리헨션으로 'hello' 원소를 10개 가지는 리스트를 작성하라. ======")
lst4 = ['Hello' for i in range(0,11)]
print("lst4 :", lst4)







###튜플
##튜플은 수정이 불가능하다. ---> append, insert, 값 변경이 불가능함.
##('김', '이', '박', '최')





###딕셔너리 {key : value, k1:v1, k2:v2....}
address = {'홍길동':'서울', '김동현':'부천', '박상도':'제주', 'james':'미국'}
print(address['홍길동'])
##print(address['서울']) <--- key값으로만 찾을 수 있다. value값으로는 검색이 불가능하다.