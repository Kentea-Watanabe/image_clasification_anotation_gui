# jsonファイルのラベルをcsvファイルに変換する

# coding:utf-8

import json

#Pandasをインポート
import pandas as pd
from pandas.io.json import json_normalize

#変換したいJSONファイルを読み込む
df = pd.read_json('result.json', orient='index')
df = df.reset_index()
df.columns=['img_path', 'label']
print(df)

# read_jsonした結果だとネストしたjsonを展開できないのでnormalizeで展開させる
# df_json = json_normalize(df['data'])
# print(df_json)
df.to_csv("out.csv", encoding='utf-8')
