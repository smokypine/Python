# hello.py
def helloWorld() : 
    print("Hello World!!!")

print("오늘은 모듈을 처음 배운 날입니다.")
print("오늘의 기온은 23도입니다.")
helloWorld()

if __name__ == "__main__" : 
    print("__name__ : ", __name__)
else :
    print("hello.py __name__ : ", __name__) # 모듈(module).py에서 hello.py 의 print("__name__ : ", __name__)는 __name__ :  hello 가 출력된다.


