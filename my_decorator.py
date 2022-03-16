# -*- coding: utf-8 -*-
'''
Created on 2022-03-16

@author: Enzo
'''

import time

def run_time(func):
    #函数运行时长
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print('%s spend: %.4f s'%(func.__name__,end_time-start_time))
        return result
    return inner

if __name__ == '__main__':
    pass
