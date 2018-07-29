# -*- coding: utf-8 -*-
'''
Created on 2018-07-29

@author: Enzo
'''


'''
定义一个函数，成绩作为参数传入。
如果成绩小于60，则输出不及格。
如果成绩在60到80之间，则输出良好；
如果成绩高于80分，则输出优秀，
如果成绩不在0-100之间，则输出 成绩输入错误
'''

def score():
    try:
        score = float(input('Please input the socre:'))
    except Exception as e:
        print('Error! the Exception is %s'%e)
    if score >= 0 and score < 60:
        print('Sorry, You should not pass!')
    elif score >= 60 and score < 80:
        print('Good! nice work')
    elif score>=80 and score <= 100:
        print('perfect!')
    else:
        print('Sorry! The score should be 0~100')
# score()

'''
用python函数实现如下:
随机产生一个数，让用户来猜，猜中结束，若猜错，则提示用户猜大或猜小。
'''
import random

rand_num = random.randint(0,10)
# 定义flag，为True时一直循环猜数字，当猜正确后置为False跳出循环
guess_flag = False
num = 0
while guess_flag:
    num += 1
    guess_num = int(input('请输入你猜的数字：'))
    if rand_num == guess_num:
        print('回答正确！第%d次猜测成功！'%num)
        guess_flag = False
    elif rand_num > guess_num:
        print('猜小了！请继续')
    else:
        print('猜大了，请继续')


'''
写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5
'''

def calc_len(data):
    if len(data)>5:
        print('传入对象的长度大于5，实际长度为%d'%len(data))
    else:
        print('传入对象的长度小于5，实际长度为%d'%len(data))

test_str = 'abc'
test_list = ['a','b','c','d','e']
test_tuple = ('a','b','c','d','e','f','1',2,['a','b'])
# calc_len(test_str)
# calc_len(test_list)
# calc_len(test_tuple)

'''
写函数，将姓名、性别，城市作为参数，并且性别默认为f(女)。
如果城市是在长沙并且性别为女，则输出姓名、性别、城市，并返回True,否则返回False
'''

def city(name,city,gender='f'):

    if city == '长沙' and gender.upper() == 'F':
        print('姓名：%s\t性别：%s\t城市：%s\t'%(name,gender,city))
        return True
    else:
        return False

#city('lily','长沙')
#city('lily','长沙','M')
#city('lily','长沙','F')