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



#### 자동차의 등록번호와 생산년도, 배기량으로 구성된 딕셔너리가 있다.
carDict = {'H1':('2017', '3000'), 
           'K3':('2022','2000'), 
           'H4':('2020','3200'), 
           'D2':('2020','1500'), 
           'H2':('2022','3000'), 
           'K3':('2022','2700')} ## <----------- key값이 앞의 'K3'과 동일하므로 'K3':('2022','2700')만 딕셔너리에 남는다.
'''이를 다음과 같은 형식으로 출력하는 코드를 만드시오
[실행결과]
H1 ('2017','3000')
K3 ('2022', '2700') 
H4 ('2020', '3200')
D2 ('2020', '1500')
H2 ('2022', '3000')'''

print(carDict.items()) # dict_items([('H1', ('2017', '3000')), ('K3', ('2022', '2700')), ('H4', ('2020', '3200')), ('D2', ('2020', '1500')), ('H2', ('2022', '3000'))])
for item in carDict.items():
    print(item)
## 정답
for key in carDict.keys():
    print(key, carDict[key])
# 이 2개 중 하나를 쓰면 된다.
for key, value in carDict.items():
    print(key, value)

## sub1) 생산년도로 구성된 각 요소가 int 형인 yearList 리스트를 생성하고 출력하는 코드를 만드시오
# [실행결과] : [2017, 2022, 2020, 2020, 2022]
yearList = []
print(carDict.values()) # carDict 딕셔너리의 value값을 출력.
for value in carDict.values():
    print("year:", value[0], "배기량 :", value[1])
    yearList.append(int(value[0])) # int값으로 치환.
print(yearList)

## sub2) 생산년도를 입력받아 해당 년도에 생성된 자동차가 몇대인지 출력하는 코드를 작성하시오(for 문을 쓰지 말고 한번만 실행하고 종료한다.)
# [실행결과]
# 생산년도를 입력하세요 : 2020
# 2020의 등록 차는 2대입니다.
year = input("생산년도를 입력하세요 : ")
print(year,"의 등록 차는 ", yearList.count(int(year)), "대입니다.")
#for문을 사용
count = 0
for value in carDict.values() :
    if year==value[0]:
        count = count + 1
print(year,"의 등록 차는 ", count, "대입니다.")



##### 스포츠 구기종목 문제
#두개의 List를 zip로 묶어서 딕셔너리로 나타낸 후 사용자로부터 종목이름을 입력받아서 그에 맞는 인원수를 출력하라.
sport = ['축구', '야구', '농구', '배구']
num = [11, 9, 5, 6]
''' 
1) while문을 돌려서 할 것. => while 1:
2) quit을 만나면 종료할 것.
3) 다른 종목이 들어오면 "몰라요 다시 입력 받을 것."
4) continue, break를 활용할 것. 
'''
dictionary = dict(zip(sport, num)) # dict(zip(list1, list2))를 통해 리스트 2개를 연결해 딕셔너리로 만들 수 있다. list1이 key가 되고 list2가 value가 된다.
print(dictionary)
while 1:
    i = input("궁금한 종목 이름을 입력하세요. 올바른 종목을 입력하면 인원수를 알려줍니다. : ")
    if i in dictionary.keys():
        #인원수 출력
        print("인원수:", dictionary[i],"명")
    elif i == 'quit':
        break
    else :
        print("몰라요 다시 입력해 주세요.")
        continue
    print("김동현 님은 지금 ", i, "에 대한 정보를 서치하셨습니다.")
# 만약 list로 zip을 묶었다면
List1= list(zip(sport, num)) # [('축구', 11), ('야구', 9), ('농구', 5), ('배구', 6)]