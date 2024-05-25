#信度检验
# 我们说量表的信度是指量表测量结果的一致性、稳定性、也称为量表的可靠性。
# 如果在相同条件下，运用某量表对某一个概念在不同时间上重复多次进行测量，其测量的结果保持不变，就表明该量表是可信的或具有可靠性。
# 在SPSS中对信度的检验也叫可靠性检验，一般对预调查数据进行，用信度检验Cronbach’s a 系数来衡量，
# 一般认为Cronbach’s a 系数大于等于0.6表面信度检验没有问题。

#引入需要读入文件的pandas库和计算Cronbach’s a 系数的pingouin库，并读入文件
import pandas as pd
import pingouin as pg

from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo


zd_df = pd.read_excel('C:/Users/29550/OneDrive/Desktop/量表题数据.xlsx',header = 0)

#计算Cronbach’s 系数
#Cronbach’s 系数
result = pg.cronbach_alpha(data = zd_df)
print(result)




# 效度检验
# 量表的效度是指量表准确地反映客观事物属性和特征的程度，也称为有效性。
# 市场调查中效度可以理解为调查结果准确地反映调查中所要说明问题的程度。
# 如果一个量表即具有较高的信度，也具有较高的效度，则这个量表就具有较高的内在质量。
# 在检验中，我们通常通过两个方法来衡量效度,分别为为 Bartlett’s球状检验 和 KMO检验


# 一、Bartlett’s球状检验
# 检验总体变量的相关矩阵是否是单位阵；检验各个变量是否各自独立。
# 如果不是单位矩阵，说明原变量之间存在相关性，可以进行因子分析；
# 反之，原变量之间不存在相关性，数据不适合进行主成分分析。
chi_square_value, p_value = calculate_bartlett_sphericity(zd_df)
print("bartlett球状检验参数：\n卡方值为：{}，p值为：{}".format(chi_square_value, p_value))


# 二、KMO检验
# 检验变量间相关性和偏相关性，取值在0~1之间；
# KOM统计量越接近1，变量相关性越强，偏相关性越弱，因子分析效果越好，通常取值从0.6开始进行因子分析
kmo_all, kmo_model = calculate_kmo(zd_df)
print("KMO检验参数：\n", kmo_model)




"""
# 因子分析
# 因子分析是指研究从变量群中提取共性因子的统计技术。
# 最早由英国心理学家C.E.斯皮尔曼提出。他发现学生的各科成绩之间存在着一定的相关性，一科成绩好的学生，往往其他各科成绩也比较好，从而推想是否存在某些潜在的共性因子，或称某些一般智力条件影响着学生的学习成绩。
# 因子分析可在许多变量中找出隐藏的具有代表性的因子。
# 将相同本质的变量归入一个因子，可减少变量的数目，还可检验变量间关系的假设。
# 因子分析的主要目的是用来描述隐藏在一组测量到的变量中的一些更基本的，但又无法直接测量到的隐性变量
# 因子分析有探索性因子分析和证实性因子分析之分。
# 本次是探索性因子分析
# 探索性因子分析不事先假定因子与测度项之间的关系，而让数据“自己说话”。
# 主成分分析和共因子分析是其中的典型方法。
# 验证性因子分析假定因子与测度项的关系是部分知道的，即哪个测度项对应于哪个因子，虽然我们尚且不知道具体的系数。


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_kmo
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
#import scipy.cluster.hierarchy as shc



Load_Matrix = FactorAnalyzer(rotation=None, n_factors=len(zd_df.T), method='principal')
Load_Matrix.fit(zd_df)
f_contribution_var = Load_Matrix.get_factor_variance()
matrices_var = pd.DataFrame()
matrices_var["旋转前特征值"] = f_contribution_var[0]
matrices_var["旋转前方差贡献率"] = f_contribution_var[1]
matrices_var["旋转前方差累计贡献率"] = f_contribution_var[2]
matrices_var

# 同样的数据绘制散点图和折线图
plt.scatter(range(1, zd_df.shape[1] + 1), featValue)
plt.plot(range(1, zd_df.shape[1] + 1), featValue)

plt.title("Scree Plot")
plt.xlabel("Factors")
plt.ylabel("Eigenvalue")

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
plt.grid()  # 显示网格
plt.show()  # 显示图形
"""