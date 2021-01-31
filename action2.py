import pandas as pd
import numpy as np
from pandas import Series, DataFrame

data = {'chinese': [68, 95, 98, 90, 80],
        'math': [65, 76, 86, 88, 90],
        'english': [30, 98, 88, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['zhangfei', 'guanyu', 'liubei',
                             'dianwei', 'xuchu'], columns=['chinese', 'math', 'english'])
df2.rename(columns={'chinese':'语文', 'math':'数学', 'english':'英语'}, inplace=True)
df2_describe = df2.describe().drop(index=['count', '25%', '50%', '75%'])
print('平均成绩、最大成绩、最小成绩、标准差，如下所示:')
print(df2_describe)
print('\n')
df2['总分'] = df2.apply(lambda x: x.sum(), axis=1)
df2_rank = df2.sort_values('总分', ascending=False)
df2_rank['rank'] = range(1, len(df2_rank)+1)
print('各个学生的成绩排名如下：')
print(df2_rank)


