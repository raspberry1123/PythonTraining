# -*- coding: utf-8 -*-
'''
Created on 2012/03/05

@author: kou
'''






# 基本的な使い方
for i in ('a' , 'b' , 'c'):
    print i,

print

# シーケンスなら、in句の後ろに持ってくることができる
for i in [5,4,3,2,1]:
    print i,
    
print

# 文字列もシーケンスなので、in句の後ろに持ってくることができる。
for i in "Hello World":
    print i,
    
print

# range関数でリストを生成し、in句の後ろに持ってくることも可能。
for i in range(1 , 10):
    print i,
# enumerateメソッドを利用すると、インデックスと要素が同時に取り出せる。
# enumerateメソッドは、ジェネレータと呼ばれる類のメソッドである。
for idx , ele in enumerate(['あ' , 'い' , 'う' , 'え' , 'お']):
    print idx , ele


myfile = open('myfile.txt' , 'r')

# ファイルオブジェクトはイテレータプロトコルをサポートしているので、in句の後ろに持ってくることができる。
for line in myfile:
    print line.rstrip()

