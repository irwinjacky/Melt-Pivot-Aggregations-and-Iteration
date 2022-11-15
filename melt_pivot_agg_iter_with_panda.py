# %%
print('Melt, Pivot, Aggregations, and Iteration.')

import pandas as pd
import numpy as np
#importing data
data = pd.read_csv('breast-cancer.data')
data.columns = ['class', 'age', 'menopause', 'tumor_size', 'inv_nodes', 'node_caps', 'deg_malig', 'breast', 'breast_quad', 'irradiat']

# %%
#working on Melt
print('Melt')
#create data frame
df = pd.DataFrame(data)
print(df.columns)
#print(df)
#melt
df_melt = pd.melt(df, id_vars = ['inv_nodes'], value_vars = ['tumor_size'], value_name = 'tumor size')
print(df_melt)

# %%
#pivot
print('pivot')
print(data.columns)
#pivot data
df_pivot = data.pivot(columns = 'irradiat', values = 'tumor_size')
print(df_pivot)

# %%
#Aggregations
print('Aggregations')

#aggregation max and min of data
df_aggregation = data.aggregate({'age': ['max', 'min'],
    'tumor_size': ['max', 'min'],
    'inv_nodes': ['max', 'min'],
    'deg_malig': ['max']})

print(df_aggregation)

# %%
#Iteration
print('Iteration')

#iteration

df = pd.DataFrame(np.random.randn(4,3),columns = ['age','tumor_size','deg_malig'])
for row_index,row in df.iterrows():
   print (row_index,row)

# %%
#Groupby
print('Groupby')

#group data by tumor size
df_groupby1 = data.groupby('tumor_size').sum()
print(df_groupby1[:10])

#groupby inv_nodes
df_groupby2 = data.groupby('inv_nodes').sum()
print(df_groupby2)

#groupby age
df_groupby3 = data.groupby('age').sum()
print(df_groupby3)

# %%



