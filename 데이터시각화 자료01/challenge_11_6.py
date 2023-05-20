#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 11.14 여러 개의 상자 차트 그리기, 298쪽
#
import numpy as np
import matplotlib.pyplot as plt

data1 = np.random.randn(100, 10)
print(data1)
plt.boxplot(data1)

plt.show()
