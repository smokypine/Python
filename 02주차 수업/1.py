#1.py
#동양미래대
#파이썬 프로그래밍
''' 
이것은
여러줄로 이루어진
주석입니다.
'''
print("hello world!!")
print("it is good to see you")
print("python" + "만세")
print("Python!!!"*3)
print(type(11))
print("hello world" * 5,0)

print(1,2,-5,3.14,2.71828)
print('hi','phthon')

print('23000원은','50000원 ?개','1000원 ?개')
print('5000원',23000//5000,'개')
print('1000원',(23000%5000)//1000,'개')

#eval() function : 표현식(수식) 문자열 실행 - 모든 실행 가능한 파이썬 문장의 문자열을 실행
print(eval('3 + 15 / 2'))
print(eval('4 * 3 % 5'))
print(eval('3 * -2 **3'))
print(eval('"java" * 3'))

print(1 + 62 -3 * 52)
print(eval('1 + 62 -3 * 52'))
print(256 * 553 -152)
print(eval('256 * 553 -152'))
print(162353290930 % 539253 + 162353290930 // 539253)
print(eval('162353290930 % 539253 + 162353290930 // 539253'))

allMoney = 80000
m50000 = 0
m10000 = 0
m5000 = 0
m1000 = 0
exchange = 0
print("78000인데 어떻게 할까요?")
m50000 = 78000 // 50000
exchange = 78000 % 50000
print("5만원권은 " ,m50000 , "장입니다.")
m10000 = exchange // 10000
exchange = exchange % 10000
print("10000원권은 " , m10000 , "장입니다.")
m5000 = exchange // 5000
exchange = exchange % 5000
m1000 = exchange // 1000
print("5000원권은 " , m5000 , "장입니다.")
print("1000 : " , m1000 , "장입니다.")
print("낸 금액은 ",allMoney,"이므로 ",allMoney-78000,"원을 거슬러 받아야 합니다.")



