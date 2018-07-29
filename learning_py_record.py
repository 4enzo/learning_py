# -*- coding: utf-8 -*-
'''
Created on 2018-07-22

@author: Enzo
'''


# == is
# is是比较两个引用是否指向了同一个对象（引用比较）
# == 是比较两个对象是否相等

a = [1,2,3]
b = [1,2,3]
c = a

a == b
# True

a is b
# False

a == c
# True

a is c
# True


"""
私有化
xx:公有变量
_xx:单前置下划线，私有化属性和方法，from module import *禁止导入，类对象和之类可以访问
__xx:双前置下划线，避免与之类中的属性命名冲突，无法在外部直接访问，（名字重名所以访问不到）
__xx__:双前后下划线，用户名字空间的魔法对象或属性，例如：__init__,__不要自己发明这样的名字
xx__:单后置下划线，用于避免与python关键字的冲突
"""

# @ property

class Test(object):
    def __init__(self):
        self.__num = 100  # 私有变量

# 正常情况下，操作私有变量需要使用set get函数，但这显得繁琐
# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self,number):
        if isinstance(number,int):
            self.__num = number
        else:
            print('The number is not a int')

t = Test()
t.num = 20
print(t.num)