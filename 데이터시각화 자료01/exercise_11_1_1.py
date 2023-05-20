#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 심화문제 풀이, 302쪽
#
import matplotlib.pyplot as plt

x = [x for x in range(7, 13)]
y = [456, 492, 578, 599, 670, 854]

plt.plot(x, y)
plt.xlabel('Month')      
plt.ylabel('User')

plt.show()