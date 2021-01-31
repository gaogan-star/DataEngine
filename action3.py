import pandas as pd
import numpy as np
from pandas import Series, DataFrame

df = pd.read_csv(r'D:\11_Bigdata\黑马数据大赛培训\day1\car_complain.csv')
df1 = df.brand.value_counts()                                   # 统计品牌
df2 = df.drop_duplicates(['car_model'])                         # 统计车型数量之前，删除重复车型
df3 = df2.brand.value_counts()                                  # 统计车各品牌车型数
df_merge = pd.concat([df1, df3], axis=1, sort=True)             # 将品牌及车型重组一个dataframe
column_names = df_merge.columns.values
column_names[1] = 'car'
df_merge.columns = column_names                                 # 修改重复列名
# print(df_merge.loc[['吉利汽车']])
df_merge.eval('ratio = brand/car', inplace=True)                # 计算品牌投诉量与车型的比值
df_merge = df_merge.sort_values('ratio', ascending=False)       # 排序
print('平均车型投诉最多的品牌是：')
print(df_merge.index[0])                                        # 打印最多的平均车型投诉最多的品牌
