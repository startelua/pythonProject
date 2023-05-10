# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import requests

def read_f(name):
  df = pd.read_csv('/Users/vlad/Downloads/botto2/'+name+'.csv',delimiter=';',)

  for i in range(len(df)):
    n_out = str(df.values[i][2])
    df.loc[i,'oper1']=get_ops(n_out)
    df.loc[i,'oper2']=get_ops(df.values[i][3])
  #  o2=str(df.values[i][3])
    print(n_out + ' to + o2')
  df_sort=df.sort_values(by=['oper1'])
  print(df_sort)
  df_sort.to_csv('/Users/vlad/Downloads/botto2/'+name+'_.csv')

  aggr_df = df.groupby(['oper1', 'oper2']).size().reset_index(name='counts')
  aggr_df = aggr_df.sort_index(axis=1, ascending=True)
  aggr_df.to_csv('/Users/vlad/Downloads/botto2/'+name+'_itog.csv')


def get_ops(namber):
    url = "http://num.voxlink.ru/get/"

    querystring = {"num": namber ,"field" :"operator","translit":1}

    payload = ""
    response = requests.request("GET", url, data=payload, params=querystring)
    return response.text



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name_f="min_13-04"
    read_f(name_f)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
