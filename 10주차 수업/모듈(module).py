### 모듈(module) ###
# 함수나 변수, 클래스 정의 등의 파이썬 코드가 저장된 소스 파일
# 모듈은 파이썬 프로그램에서 불러와(import) 사용

## 써드 파티 모듈(third party modules)
# 여러 회사나 전문가가 개발해 배포하는 모듈

## 표준 모듈
# 파이썬에 기본적으로 설치된 모듈
# 대표적으로 random이 있으며 math와 statistics, turtle, datetime, sys, os 등 매우 다양
# 표준 모듈의 이름은 sys 모듈의 builtin_module_names 변수에 저장

import math
print(math.fsum([1,2,3])) # <----- fsum([ ])안에 든 숫자들을 전부 더한다.
print(math.gcd(15,25)) # <------ gcd( , ) 안에 든 숫자들의 최대공약수를 구한다.

# math 함수를 선언 안 하고 math모듈 내의 함수를 쓰고 싶을 때
from math import fsum, gcd # <------- math에서 fsum()과 gcd()만 가져온다.
print(gcd(15,27))
print(fsum([1,2,3,4]))



import numpy # 과학 계산을 위한 기본 패키지. 배열과 행렬을 기본으로 수학 연산을 위한 라이브러리 제공
## 넘파이를 설치하였다면 터미널에 pip install numpy 를 입력할 것.
### 만약 could not be resolved Pylance 에러가 난다면 명령 팔레트(Ctrl + Shift + P)를 눌러 Python base를 누를 것. https://12340zszs.tistory.com/106 참조

arrA = numpy.array([1,2,3,4,5])
arrB = numpy.array([6,7,8,9,10])
print(type(numpy.array([1,2,3,4,5,]))) # <class 'numpy.ndarray'>라 나온다.

print(arrA + arrB) # [ 7  9 11 13 15]
print(arrA - arrB) # [-5 -5 -5 -5 -5]
print(arrA * arrB) # [ 6 14 24 36 50]
print(arrA / arrB) # [0.16666667 0.28571429 0.375      0.44444444 0.5       ]

# 별명짓기
import numpy as np # <----- 앞으로 넘파이를 np라 서술하겠다.
arrC = np.array([11,12,13,14,15])
