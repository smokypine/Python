#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 심화문제 풀이, 303쪽
#
import math
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(0, 50, 30)
y = np.random.randint(0, 50, 30)
print(len(x))    
plt.scatter(x, y)
plt.show()
