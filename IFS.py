import matplotlib.pyplot as plt
import numpy as np
import random
plt.rcParams['figure.figsize'] = (8.0, 4.0) # 设置figure_size尺寸
plt.rcParams['savefig.dpi'] = 3000 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率
# 默认的像素：[6.0,4.0]，分辨率为100，图片尺寸为 600&400
# 指定dpi=200，图片尺寸为 1200*800
# 指定dpi=300，图片尺寸为 1800*1200
# 设置figsize可以在不改变分辨率情况下改变比例

# 迭代次数 * （需输入在命令行中，或者直接赋值） *
trials = 100000

# 每个变换的执行概率
dist = [0.01, 0.85, 0.07, 0.07]
for i in range(1,len(dist)):
    dist[i] += dist[i-1]
    #方便随机
dist = np.array(dist)

# 矩阵值
cx = [[0.00, 0.00, 0.500],
      [0.85, 0.04, 0.075],
      [0.20, -0.26, 0.400],
      [-0.15, 0.28, 0.575]]
cy = [[0.00, 0.16, 0.000],
      [-0.04, 0.85, 0.180],
      [0.23, 0.22, 0.045],
      [0.26, 0.24, -0.086]]
#初始值 (x, y)
x = 0.0
y = 0.0


setx = [0.0]
sety = [0.0]
for t in range(trials):
    # 根据概率分布随机选择变换
    r = np.where(dist>=random.random())[0][0]

    # 迭代
    x0 = cx[r][0] * x + cx[r][1] * y + cx[r][2]
    y0 = cy[r][0] * x + cy[r][1] * y + cy[r][2]
    x = x0
    y = y0
    setx.append(x)
    sety.append(y)


    # 每迭代100次显示1次
    if (t % 10000 == 0):
        # new a figure
        fig = plt.figure()
        ax = fig.gca()

        # set figure information
        ax.set_title("Pixels")
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        # 绘制结果
        # draw the figure, the color is r = read
        figure = ax.scatter(setx, sety, s=1, marker='.')
        plt.show()



