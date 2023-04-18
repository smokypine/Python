### zip()
# list, tuple이 여러개 -> 하나의 튜플의 조합으로 된 리스트로 변환
l1 = ['1조', '2조', '3조']
YA = ['홍', '박', '김']
YB = ['최', '한', 'James']

z = zip(l1, YA, YB)
print("z의 클래스 : ", type(z))
print(z) # <-------- z의 메모리 주소값
print(list(z)) # <-------- list로 변경

print(tuple(zip(l1, YA, YB))) # <-------- 튜플로 변경


## 예제
l2 = ['한식', '양식', '중식', '분식']
l3 = ['전주식당', '닥터로빈', '홍콩반점', '토마토']
l4 = ['제육볶음', '리조또', '짬뽕', '김밥']

tmenu = list(zip(l2,l3,l4))
print(tmenu) # <------ [('한식', '전주식당', '제육볶음'), ('양식', '닥터로빈', '리조또'), ('중식', '홍콩반점', '짬뽕'), ('분식', '토마토', '김밥')] 과 같이 함게 묶여서 나온다.
for i in tmenu:
    print(i[0], i[1], i[2])

## 
tmenu = list(zip('ABCD', l2, l3, l4))
for i in tmenu:
    print(i[0], i[1], i[2], i[3])

## dictionary로 바꾸기
print(dict(zip(l2, l3)))
print(dict(zip(l2, zip(l3,l4)))) # <---------- l3과 l4를 zip으로 묶어 value로 만들었다.

print(dict(zip('1234',l3)))
print(list(enumerate(l3))) # <---------------- enumerate() 함수를 이용해 0,1,2,3.... 과 같은 숫자를 l3의 리스트의 각 아이템과 페어로 준다.
print(dict(enumerate(l3))) # <---------------- enumerate() 함수를 이용해 0,1,2,3.... 과 같은 숫자를 key값으로 준다.


## 다음과 같이 list의 아이템 갯수가 각기 다른 경우 zip()을 하면
l2 = ['한식', '양식', '중식']
l3 = ['전주식당', '닥터로빈', '홍콩반점', '토마토']
l4 = ['제육볶음', '리조또']
tmenu = list(zip(l2,l3,l4))
print(tmenu) # <--------- [('한식', '전주식당', '제육볶음'), ('양식', '닥터로빈', '리조또')] 와 같이 가장 작은 list를 기준으로 잡힌다.



