### 문자 사이의 간격을 step로 조정 가능
var = "Hello World"

# str[start:end:step] <- 문자 사이의 간격을 step로 조정, step을 생략하면 1
print(var[0:11:1])
print(var[0:11:2])

# str[:] == str[::] == str[::1] <- 전체 문자열 반환
print(var[::])

# 간격인 step은 음수도 가능 <- start는 end보다 오른쪽에 위치한 첨자여야 함
print(var[-7:-1:1])
print(var[-11:-1:1])

# str[::-1] 은 역순 문자열 반환
print(var[::-1])
print(var[11::-1])
print(var[::-2])

print("\n")

print("abcdefg"+"\b"+"hijk") # \b는 삭제한다.
print("abcdefg"+"\v"+"hijk") # \v는 tab를 누른 효과와 동일하다.

print("\n")

### String 메소드
# 메소드 str.replace(a,b) : 문자열 str에서 a가 나타나는 모든 부분을 b로 바꾸는 메소드
str_var = "hahahaha"
sstr_var = str_var.replace("h","f")
print(str_var)
print(sstr_var)

str_var1 = "안녕하세요 파이썬 수업중입니다. 파이썬 파이썬 파이썬 파이썬 파이썬 조아"
sstr_var1 = str_var1.replace("파이썬","JAVA")
ssstr_var1 = str_var1.replace("파이썬","JAVA", 3) # 파이썬을 JAVA로 3번만 바꾼다.
print(str_var1)
print(sstr_var1)
print(ssstr_var1)


### 문제
# 실수를 입력받음
# 102.345
#1+0+2+3+4+5
#sum을 출력하라
num = input("여섯자리 실수를 입력하세요 : ")
num1=num.replace(".","")

answer = int(num1[0]) + int(num1[1]) + int(num1[2]) + int(num1[3]) + int(num1[4]) + int(num1[5])
print(answer)