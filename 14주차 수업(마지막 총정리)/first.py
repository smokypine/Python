### 딕셔너리 관련 중간고사 문제
dic = {'a':10, 'b':20, 'c':30, 'd':40}
keyList = dic.keys()
valueList=dic.values()
print(keyList)
print(valueList)
## 답
# print(keyList) : dict_keys(['a', 'b', 'c', 'd'])
# print(valueList) : dict_values([10, 20, 30, 40])
# 딕셔너리에서는 dic[key] = key값에 대응되는 value이 나온다. 예를 들어 dic['a'] = 10이다.


members = {'홍':'111', '박':'222', '정':'333'}
members['최'] = '555' # key중 '최'가 없으므로 '최':'555'가 members에 새롭게 추가된다.
members.update({'강':'666'}) # key중 '강'이 없으므로 '강':'666'이 members에 새롭게 추가된다.
members['김'] = '777'# key중 '김'이 없으므로 '김':'777'이 members에 새롭게 추가된다.
members.update({'최':'888'}) # members 중에 '최'가 key값에 있으므로 value값이 기존의 '555'에서 '888'로 바뀐다.
members['최'] = '111'# members 중에 '최'가 key값에 있으므로 value값이 기존의 '888'에서 '111'로 바뀐다.
print(members.pop('홍')) # dict.pop(key)는 해당 key값의 value값을 출력하고 딕셔너리에서 해당 key와 value를 없앤다.
print(members)
## 답
# print(members.pop('홍')) : 111
# print(members) : {'박': '222', '정': '333', '최': '111', '강': '666', '김': '777'}
# 즉 dict.update(key:value) 와 dict[key]=value 는 동일하다.


# 자동차의 등록번호와 생산년도, 배기량으로 구성된 딕셔너리가 있다.
carDict = {'H1':('2017', '3000'), 
           'K3':('2022','2000'), 
           'H4':('2020','3200'), 
           'D2':('2020','1500'), 
           'H2':('2022','3000'), 
           'K3':('2022','2700')}
# 이를 다음과 같은 형식으로 출력하는 코드를 만드시오
# [실행결과]
# H1 ('2017','3000')
# K3 ('2022', '2700')
# H4 ('2020', '3200')
# D2 ('2020', '1500')
# H2 ('2022', '3000')
print(carDict.items()) # dict_items([('H1', ('2017', '3000')), ('K3', ('2022', '2700')), ('H4', ('2020', '3200')), ('D2', ('2020', '1500')), ('H2', ('2022', '3000'))])
for item in carDict.items():
    print(item)
## 정답
for key in carDict.keys():
    print(key, carDict[key])
# 이 2개 중 하나를 쓰면 된다.
for key, value in carDict.items():
    print(key, value)

## 생산년도로 구성된 각 요소가 int 형인 yearList 리스트를 생성하고 출력하는 코드를 만드시오
# [실행결과] : [2017, 2022, 2020, 2020, 2022]
yearList = []
print(carDict.values()) # carDict 딕셔너리의 value값을 출력.
for value in carDict.values():
    print("year:", value[0], "배기량 :", value[1])
    yearList.append(int(value[0])) # int값으로 치환.
print(yearList)

##  생산년도를 입력받아 해당 년도에 생성된 자동차가 몇대인지 출력하는 코드를 작성하시오(for 문을 쓰지 말고 한번만 실행하고 종료한다.)
# [실행결과]
# 생산년도를 입력하세요 : 2020
# 2020의 등록 차는 2대입니다.
car=0
year = input("생산년도를 입력하세요 : ")
while 
print(year,"의 등록 차는 ",car,"대입니다.")