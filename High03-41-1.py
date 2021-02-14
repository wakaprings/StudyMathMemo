import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

# 変数定義
t = sym.Symbol('t')

# 初期座標
pointX = [0,0,t]
pointY = [2,3,0]

tan_alpha = (pointY[0]-pointY[2]) / (pointX[0]-pointX[2])
tan_beta = (pointY[1]-pointY[2]) / (pointX[1]-pointX[2])
# 加法定理(Θ=β-α)
tan_theta = (tan_alpha-tan_beta)/(1+tan_alpha*tan_beta)

#print(sym.simplify(tan_theta))
# 数式の簡略化
#print(sym.simplify(tan_theta))

# tan_thetaをグラフ化する...(1)
x_plot = np.arange(0.01,10,0.01)
y_plot_list = []
for i in x_plot :
    y_plot_list.append(tan_theta.subs(t, i))
y_plot = np.array(y_plot_list)
# (1)をY軸対象にする
x_plot2 = x_plot*(-1)
y_plot_list_2 = []
for i in x_plot2 :
    y_plot_list_2.append(tan_theta.subs(t, i))
y_plot2 = np.array(y_plot_list_2)

plt.figure(figsize=(15.0, 6.0))
plt.plot(x_plot, y_plot, label=str(sym.simplify(tan_theta)), linestyle="-", color='slateblue')
plt.plot(x_plot2, y_plot2, label=str(sym.simplify(tan_theta))+"Y", linestyle="-", color='slateblue')
plt.legend()
plt.savefig('High03-41-1_01.png')
plt.close()
