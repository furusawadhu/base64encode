import sys
import csv
import base64
import subprocess

#ファイルパスの取得
args = sys.argv
filename = args[1]

#csvファイルを開く
f = open(filename,'r',encoding='utf-8')
csv_data = csv.reader(f)

row3_list = []

#csv内の3列目の値をbase64にエンコードしてリストに格納する
for row in csv_data:
    value=row[2]
    base64_value = base64.b64encode(value.encode()).decode()
    row3_list.append(base64_value)

f.close()

#row3_listの一番最初の要素（列名）を取り除く
row3_list.pop(0)

#リストの内容をテキストファイルに書き出して開く
with open('base64encoded_data.text','w') as f:
    for d in row3_list:
        f.write(d+"\n")
subprocess.Popen(["start", "", r"base64encoded_data.text"], shell=True)