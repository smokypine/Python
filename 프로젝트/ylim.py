import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.exp(x)

# 서브플롯 생성
fig, ax1 = plt.subplots()

# 좌측 y축 설정
ax1.plot(x, y1, color='blue')
ax1.set_xlabel('X')
ax1.set_ylabel('Y1', color='blue')
ax1.tick_params(axis='y', colors='blue')

# 우측 y축 설정
ax2 = ax1.twinx()
ax2.plot(x, y2, color='red')
ax2.set_ylabel('Y2', color='red')
ax2.tick_params(axis='y', colors='red')

# 그래프 출력
plt.show()


