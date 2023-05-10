import pandas as pd
import requests

def read_f():
  df = pd.read_csv('/Users/vlad/Downloads/1/list_nam.csv',delimiter=',',)

  for i in range(len(df)):
    n_out = str(df.values[i][0])
    df.loc[i,'oper1']=get_ops(n_out)
  #  o2=str(df.values[i][3])
    print(n_out + ' to + o2')
  df_sort=df.sort_values(by=['oper1'])
  print(df_sort)
  df_sort.to_csv('/Users/vlad/Downloads/1/list_.csv')

def get_ops(namber):
    url = "http://num.voxlink.ru/get/"

    querystring = {"num": namber ,"field" :"operator","translit":1}

    payload = ""
    response = requests.request("GET", url, data=payload, params=querystring)
    return response.text

if __name__ == '__main__':
    name_f="min_13-04"
    read_f()