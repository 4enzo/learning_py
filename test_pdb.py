# -*- coding: utf-8 -*-
'''
Created on 2018-08-06

@author: Enzo
'''

def get_average(a,b):
    results = a+b
    print('results=%d'%results)
    return results

a = 100
b = 200
c = a+b
ret = get_average(a,b)
print(ret)

''' 
python -m pdb xxx.py

l ----list:显示代码
n ----next:向下执行一行代码
c ----continue:继续执行代码
b ----break:添加断点
clear ----:删除断点
p ----print 打印一个变量的值
s ----step:进入到一个函数
a ----args:打印所有的参数
q ----quit:退出调试 
r ----return快速执行到函数的最后一行

'''