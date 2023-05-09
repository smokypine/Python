##### 0328.py

i = 3
i,j,k = 3,5,"hello"
print(i,j,k) 

### 이렇게 쓸 수도 있다.
_mem2 = 2 

print("\n")

### 다양한 대입연산자
a, b = 100, 5
a+=b
print("a += b : ", a)
a, b = 100, 5
a-=b
print("a -= b : ", a)
a, b = 100, 5
a *=b
print("a *= b : ", a)
# 나머지 구하기
a, b = 100, 5
a%=b
print("a %= b : " ,a)
# 몫 구하기
a, b = 100, 5
a//=b
print("a //= b : ", a)

print("\n")

### 사용자로부터 입력을 받는 함수
name = input("이름은 무엇입니까? : ")
print("제 이름은", name,"입니다.")

year2Class = input("2학년 몇 반 인가요? : ")
print("저는", year2Class, "반 입니다.")
print(type(year2Class)) #input 타입으로 입력된 값은 파이썬에선 무조건 String 값으로 저장된다.

print("\n")

# 다른 자료형을 int로 바꾸는 방법
int()
# 다른 자료형을 float로 바꾸는 방법
float()
# 다른 자료형을 String으로 바꾸는 방법
str()

age = input("나이는 어떻게 되니? : ")
print("저는",age,"살 입니다.")
print(type(age))
print("우리 아빠는 저보다 30살 많은 ", int(age)+30,"살 이에요.") #입력된 age가 str 값이므로 int()함수를 이용해 int값으로 바꿔준다.

a=10
print("a는", type(a), "타입입니다.")
str_A=str(a)
print("str_A는", type(str_A), "타입입니다")

print("\n")

### 함수 input()과 int() 활용방법
planet = input("원하는 행성은? : ")
strRadius = input(planet + "의 반지름은? : ")
radius = int(strRadius)

length = 2 * 3.14 * radius
print(planet, "의 반지름은 : ", radius, "이다.")
print(planet, "의 둘레길이는 : ", length, "이다.")