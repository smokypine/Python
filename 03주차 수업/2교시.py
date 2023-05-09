##### ppt 8장 문자열 다루기

### 문자열의 길이 반환 : 함수 len()
var = "python"
print("var : ", var)
# 오름차순
print("var의 length는 : ", len(var))
print(var[0],var[1],var[2],var[3],var[4],var[5])
# 내림차순
print(var[-1],var[-2],var[-3],var[-4],var[-5],var[-6]) # 즉 var[0]과 var[-6]은 동일하다.
# 문자열을 표현하는 다른 방법
print("PYTHON"[0], "PYTHON"[1], "PYTHON"[2], "PYTHON"[3], "PYTHON"[4], "PYTHON"[5])
print("PYTHON"[-1], "PYTHON"[-2], "PYTHON"[-3], "PYTHON"[-4], "PYTHON"[-5], "PYTHON"[-6])

print("\n")

### 문자열에서 일부만 떼는 것. 부분 문자열의 참조 방식.
# 첨자의 양수
var1 = "APPLE"
print(var1[0:3])
print(var1[2:5])
print(var1[0:len(var1)])
print("JAVASCRIPT"[0:len("JAVASCRIPT")])
# 첨자의 음수
print(var1[-6:-1])
print(var1[-6:-3])
print(var1[-len(var1):-1])
# 첨자의 양수와 음수를 혼합하여 사용
print(var1[1:-3])
print(var1[3:-1])
# start와 end를 비우면 '처음부터' '끝까지'를 의미
print(var1[:3])
print(var1[3:])
print(var1[:]) # 앞뒤를 비워두면 문자열 전체를 반환

print("\n")

### 슬라이싱으로 문자열의 부분 문자열 참조
str = "Monty Python"
print(len(str))
print(str[0:5], str[6:], str[6:12])
print(str[-12:-7], str[-6:], str[-6:0]) #str[-6:0]과 같이 start 첨자가 end 첨자보다 문자열 범위 내에서 왼쪽에 위치하지 않을 때 공백문자열이 반환된다.