# hello.py
def helloWorld() : 
    print("helloData.py에 있습니다.")

helloWorld()

if __name__ == "__main__" : 
    print("__name__ : ", __name__)
else :
    print("hello.py __name__ : ", __name__) # 모듈(module).py에서 hello.py 의 print("__name__ : ", __name__)는 __name__ :  hello 가 출력된다.


