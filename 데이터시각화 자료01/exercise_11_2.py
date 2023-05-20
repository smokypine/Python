#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 심화문제 풀이, 302쪽
#
import math
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, (2 * np.pi) * 6, 360)
y = []
z = []

for angle in x:
    y.append(angle * math.sin(angle))
    z.append(20 * math.cos(angle))
    
plt.plot(x, y, 'r-')
plt.plot(x, z, 'b--')
plt.show()