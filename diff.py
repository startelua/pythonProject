import pandas as pd
import numpy as np

df_min = pd.read_csv('/Users/vlad/Downloads/botto2/a_min_31-07_itog.csv', sep=',', engine='python')
df_god = pd.read_csv('/Users/vlad/Downloads/botto2/a_god_31-07_itog.csv', sep=',', engine='python')
df_min1 = pd.read_csv('/Users/vlad/Downloads/botto2/a_min1_31-07_itog.csv', sep=',', engine='python')

df_min['key'] = df_min['oper1'] + '_' + df_min['oper2']
df_min1['key'] = df_min1['oper1'] + '_' + df_min1['oper2']
df_god['key'] = df_god['oper1'] + '_' + df_god['oper2']

merge_df = df_god.merge(df_min, on='key', how='left', indicator=True)
merge_df['counts_y'] = np.where(merge_df['_merge'] == 'left_only', 0, merge_df['counts_y'])
del merge_df['_merge']
merge_df = merge_df.merge(df_min1, on='key', how='left', indicator=True)
merge_df['counts'] = np.where(merge_df['_merge'] == 'left_only', 0, merge_df['counts'])

# merge_df['diff'] = merge_df['counts_x'] - merge_df['counts_y']

result_df = merge_df[['key', 'counts_x', 'counts_y', 'counts']]
result_df.columns = ['relation', 'all', 'min', 'min>1']
print(result_df)



result_df.to_csv('/Users/vlad/Downloads/botto2/a_31-07_itog.csv')

