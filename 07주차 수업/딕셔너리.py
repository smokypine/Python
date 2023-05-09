### 딕셔너리 {key : value, k1:v1, k2:v2....}
## 키(key) : 벨류(value) 의 조합이다.
address = {'홍길동':'서울', '김동현':'부천', '박상도':'제주', 'james':'미국'}
print("address['홍길동']의 value : ", address['홍길동'])
## print(address['서울']) <--- key값으로만 찾을 수 있다. value값으로는 검색이 불가능하다.

d1 = {1001 : "홍길동", 1002 : "김동현", 1003 : "고민정", 1004 : "박찬욱"}
print("type(d1) : ", type(d1))
print("d1[1001] : ", d1[1001])
## print(d1[0]) <------- 에러가 난다. 딕셔너리는 key값인 1001, 1002, 1003, 1004만 검색이 가능하다.




### 딕셔너리의 추가.
## 강좌에 대한 딕셔너리를 만들고 싶다.
d2 = dict() ## 새로운 딕셔너리의 추가
d2 = {} ## 새로운 딕셔너리의 추가
d2['강좌명'] = '파이썬'
d2['개설 요일'] = '화요일'
d2['개설년도'] = 2003
d2['수강생'] = ['김동현', '배용준', '정찬성'] ## 딕셔너리의 value로 리스트를 추가할 수 있다.
print("딕셔너리 d2 : ", d2)
print("d2['수강생'] : ", d2['수강생'])
print("len(d2) : ", len(d2)) ## 이 경우 key의 개수를 리턴해주는 것.



## 문제 1.
# 딕셔너리 key : value <---- 1:1월, 2:2월, 3:3월..... 12:12월
# for문을 돌려서 각각의 value값을 찍어라.
month = {1:'1월', 2:'2월', 3:'3월', 4:'4월', 5:'5월', 6:'6월', 7:'7월', 8:'8월', 9:'9월', 10:'10월', 11:'11월', 12:'12월'}
num = 1
for i in range(1, 13, 1):
    print("month의 key값", num, "의 value는 : ", month[i])
    num = num + 1



### 딕셔너리 메소드
# 딕셔너리의 key를 리턴하라.,
print("month.keys() : ", month.keys())
# 딕셔너리의 value를 리턴하라
print("month.values() : ", month.values())
# 딕셔너리의 키와 벨류를 함게 리턴하라.
print("month.items() : ", month.items())
# 딕셔너리의 입력된 key값에 해당하는 value값을 변경한다. .update({key : value})
month.update({1 : 'January'}) # <-------------- 기존에 있던 key라면 value를 수정한다.
month.update({13 : '13월??'}) # <-------------- key가 기존에 없던 값이라면 딕셔너리의 마지막 부분에 추가된다.
print(month)
# pop(key) 괄호 안에 넣은 key값을 제거.
print("month.pop(1) : ", month.pop(1))
# 맨 마지막 item을 제거
print("month.popitem() : ", month.popitem())




##문제 2. 딕셔너리의 메소드를 활용하여 문제1을 수정하라.
# month.keys() 활용 - 1
for i in month.keys():
    print(month[i])

# month.keys() 활용 - 2 ******
for i in month: ### 위의 month.keys()와 동일하게 month안에 있는 key들이 리턴이 된다.
    print(month[i])

# month.values() 활용
for i in month.values() :
    print("value : ", i)

# month.items() 활용 - 1 <----------- key와 value 둘을 함게 가져오고 싶을 때
for i in month.items():
    print(i[1])
    print("key : value : ", i)

# month.items() 활용 - 2 <----------- key와 value 둘을 함게 가져오고 싶을 때
print("month 딕셔너리의 key : value")
for i, j in month.items() : ## i엔 key값을 할당하고 j엔 value값을 할당한다.
    print(i,":", j)



###### 딕셔너리 - 튜플 - 리스트 변환
# tuple - 변경불가, 수정X
# tuple -> list 유자차 추가 -> tuple 변경
# list -> tuple
# tuple (1,2,3,4), list ['김동현', '박민수', '강병화', '남궁누리'] => dictionary
seql = ['아메리카노','핫초코','카페라떼','아이스티']
seqt = tuple(seql) # <---------- 리스트를 튜플로 수정
print(type(seqt))
print("seqt :", seqt)

seql2 = list(seqt) # <----------- 튜플을 리스트로 수정
print(type(seql2))
print("seql2 :", seql2)

seqd = dict(enumerate(seql)) # <------------- enumerate() 메소드를 이용해 seql의 각 아이템에 숫자 0, 1, 2... 를 조합하여 딕셔너리로 만든다.
print(type(seqd))
print("seqd :", seqd)