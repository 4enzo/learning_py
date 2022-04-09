# -*- coding: utf-8 -*-
'''
Created on 2022-03-16

@author: Enzo
'''

import time
import functools

def run_time(func):
    "函数运行时长"
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('%s spend: %.4f s'%(func.__name__,end_time-start_time))
        return result
    return inner

#@property
class Test(object):
    def __init__(self):
        self.__num = 100
    #@property可以把一个方法装饰成一个属性来使用
    #正常情况下，操作私有变量需要使用set get函数，但这显得繁琐
    # 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@xxx.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self,number):
        if isinstance(number,int):
            self.__num = number
        else:
            print('The number is not a int')


class Foo(object):
    name = 'test'
    def __init__(self):
        pass

    #通常情况下，类中定义的方法默认都是实例方法
    #self实例方法的调用离不开实例,需要把实例自己传给函数
    def normal_func(self):
        "实例方法"
        print('This is normal_func')

    #@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样
    #如果方法内部没有操作实例属性的操作，仅仅包含一些工具性的操作，建议使用静态方法，比如格式化时间输出
    @staticmethod
    def static_func():
        "静态方法"
        print('This is static_func')

    #@classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码
    #如果需要对类属性，即静态变量进行限制性操作，则建议使用类方法
    @classmethod
    def class_func(cls):
        "类方法"
        print('This is class_func')


if __name__ == '__main__':
    #实例方法需要实例，只能：类名().方法名()调用
    Foo().normal_func()

    #类名.方法名()
    #也可以类名().方法名(),但不建议
    Foo.static_func()

    #类名.方法名()
    #也可以类名().方法名(),但不建议
    Foo.class_func()
