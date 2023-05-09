
#.replace("a", "b") : a 문자열을 b 문자열로 대체하다.
str = "파이썬은 하하하 호호호 히히히 피피피 파이썬은 파이썬은 파이썬은"
newstr = str.replace("파이썬", "자바")
print("str : ", str)
print("newstr : ", newstr)

#.count("asd") : 
print("str.count('파이썬') : ", str.count("파이썬"))

#'**'.join : 각 char 사이사이마다 '**'이 들어간다.
print('->'.join(str))

#.find("파이썬") : 해당 스트링에서 "파이썬"이 몇번째로 나오는가를 확인한다.
print(str.find("파"))
print(str.find("이"))
print(str.find("썬"))
print(str.find("파이썬"))
print(str.find("이썬"))
print(str.find("자바"))

print("\n")

#.index("파이썬") : 해당 스트링에서 "파이썬"이 몇번째로 나오는가를 확인한다.
print(str.index("파"))
print(str.index("이"))
print(str.index("썬"))
print(str.index("파이썬"))
print(str.index("이썬"))
#print(str.index("자바")) <- find()와는 달리 에러가 난다.

print("\n")

# aaa.split() : 쪼개는 함수
print(str.split()) #split()의 내부가 공백일 경우 띄어쓰기 되는 것으로 짤라서 출력해달라.
print(str.split("파이썬"))

newnewstr = "파이썬은,하하하,호호호,히히히,피피피,파이썬은,파이썬은,파이썬은"
print(newnewstr.split(","))

print("\n")

# '{}+{}={}'.format(a,b,a+b) : 문자와 숫자를 함께 쓰고 싶을 경우 사용
print('{}+{}={}'.format(2,3,5))
a,b=5,10
print('{}+{}={}'.format(a,b,a+b))
print('{0}+{1}={2}'.format(4,3,7))
print('{0}+{2}={1}'.format(4,3,7))
c,d=5.000,10.000
print('{}+{}={}'.format(c,d,c+d))
print('{0:d}+{1:f}={2:d},{3:s}'.format(a,b,a+b,"ㅎㅎㅎ")) #첫번째숫자는 정수로, 두번째 숫자는 실수로, 세번째 숫자는 정수로, 네번째 문자열은 string으로

print("\n")

#boolean
value = False #True #
print(type(value))
print(int(value)) ##<- False를 int로 바꾸면 0이 된다.

print(bool(1))
print(bool(0))
print(bool(1.34)) #0을 제외한 다른 모든 int값은 True값을 출력한다.
print(bool(-3.24)) #0을 제외한 다른 모든 int값은 True값을 출력한다.
print(bool("만나서반갑습니다.")) #''(공백)을 제외한 다른 모든 STRING값은 True값을 출력한다.
print(bool(5>6))