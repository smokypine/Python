#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# LAB 11-2 삼각함수의 기본인 사인 그래프 그리기, 288쪽
#
import math
import matplotlib.pyplot as plt

x = []
y = []
z = []

for angle in range(360):
    x.append(angle)
    z.append(math.cos(math.radians(angle)))
    y.append(math.sin(math.radians(angle)))

plt.plot(x, y)
plt.plot(x, z, 'r-')
plt.title("SINE & COSINE WAVE")
plt.show()