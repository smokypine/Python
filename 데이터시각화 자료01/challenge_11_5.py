#
# 따라하며 배우는 파이썬과 데이터과학(생능출판사 2020)
# 11.12 겹쳐진 히스토그램도 그리자 : 다중 히스토그램, 295쪽
#
import matplotlib.pyplot as plt

n_bins = 5

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.hist(x, n_bins, histtype='bar', color='blue', alpha=0.3)

plt.show()