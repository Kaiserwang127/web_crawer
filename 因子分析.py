# 数据处理
import pandas as pd
import numpy as np

# 绘图
import seaborn as sns
import matplotlib.pyplot as plt
# 因子分析
from factor_analyzer import FactorAnalyzer


df = pd.read_excel('C:/Users/29550/OneDrive/Desktop/量表题数据.xlsx', index_col=0).reset_index(drop=True)
df

df.isnull().sum()
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity

chi_square_value, p_value = calculate_bartlett_sphericity(df)
chi_square_value, p_value

from factor_analyzer.factor_analyzer import calculate_kmo
kmo_all,kmo_model=calculate_kmo(df)
kmo_all
kmo_model


faa = FactorAnalyzer(25,rotation=None)
faa.fit(df)

# 得到特征值ev、特征向量v
ev,v=faa.get_eigenvalues()
print(ev)
print(v)


 # 同样的数据绘制散点图和折线图
plt.scatter(range(1, df.shape[1] + 1), ev)
plt.plot(range(1, df.shape[1] + 1), ev)

# 显示图的标题和xy轴的名字
# 最好使用英文，中文可能乱码
plt.title("Scree Plot")
plt.xlabel("Factors")
plt.ylabel("Eigenvalue")

plt.grid()  # 显示网格
plt.show()  # 显示图形

#选择方式：varimax 方差极大化
#固定公共因子5个

faa_five = FactorAnalyzer(5,rotation="varimax")
faa_five.fit(df)

#公因子方差
faa_five.get_communalities()

#每个变量的公因子方差数据

pd.DataFrame(faa_five.get_communalities(),index=df.columns)

faa_five.get_eigenvalues()
pd.DataFrame(faa_five.get_eigenvalues())

faa_five.loadings_
pd.DataFrame(faa_five.loadings_,index=df.columns)
faa_five.get_factor_variance()

pd.DataFrame(faa_five.get_factor_variance())


#为了更直观地观察每个隐藏变量和哪些特征的关系比较大，进行可视化展示
#为了方便取上面相关系数的绝对值：
df1=pd.DataFrame(np.abs(faa_five.loadings_),index=df.columns)
df1


# 绘图

plt.figure(figsize = (14,14))
ax = sns.heatmap(df1, annot=True, cmap="BuPu")



# 设置y轴字体大小
ax.yaxis.set_tick_params(labelsize=15)
plt.title("Factor Analysis", fontsize="xx-large")

# 设置y轴标签
plt.ylabel("Sepal Width", fontsize="xx-large")
# 显示图片
plt.show()

# 保存图片
# plt.savefig("factorAnalysis.jpg", dpi=500,quality=80,"C:/Users/29550/OneDrive/Desktop/1.jpg")
