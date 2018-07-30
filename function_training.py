# -*- coding: utf-8 -*-
'''
Created on 2018-07-29

@author: Enzo
'''




'''
编写一个名为 make_shirt()的函数，它接受一个尺码以及要印到 T 恤上的字样。这个函数应打印一个句子，概要地说明 T 恤的尺码和字样。
'''
def make_shirt(size,str):
    print('T恤的尺寸是%d,要打印的字样是%s'%(size,str))

make_shirt(180,'hello world')

'''
编写一个名为 describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。
这个函数应打印一个简单的句子，如 Reykjavik is in Iceland。
给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。
'''
def describe_city(city,country='Iceland'):
    print('%s is in %s'%(city,country))

describe_city('Reykjavik')
describe_city('Reykjavik','Iceland')
describe_city('Beijing','China')

'''
编写一个名为 city_country()的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面这样的字符串：
"长沙, 中国"
至少使用三个城市-国家对调用这个函数，并打印它返回的值
'''
def city_country(city,country):
    results = city + ',' + country
    return results
results = []
results.append(city_country('Beijing','China'))
results.append(city_country('London','England'))
results.append(city_country('Los','America'))
for i in results:
    print(i)

'''
编写一个名为 make_album()的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
'''
dict={}
def make_album(singer,album):
    dict[singer] = album
    return dict
make_album('a',1)
make_album('b',2)
make_album('c',3)
for key in dict.keys():
    print('歌手:%s的专辑为:%s'%(key,dict[key]))


'''
编写一个函数，它接受顾客要在三明治中添加的一系列食材。
这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点的三明治进行概述。
调用这个函数三次，每次都提供不同数量的实参
'''
def cook(*seasonings):
    print('顾客添加的食材有：')
    for seasoning in seasonings:
        print(seasoning)

cook('沙拉','番茄')
cook('生菜')
cook('沙拉','番茄','鸡蛋')

'''
复制前面的程序 user_profile.py，在其中调用 build_profile()来创建有关你的简介；
调用这个函数时，指定你的名和姓，以及三个描述你的键-值对
'''
def build_profile(firstname,lastname,**dict):
    profile={}
    profile['firstname'] = firstname
    profile['lastname'] = lastname
    for key in dict.keys():
        profile[key] = dict[key]
    return profile
print(build_profile('fan','enzo',gender='M',location='Beijing',job='Test'))


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
'''
写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回 
'''
def check_list_len(list):
    if len(list)>2:
        print(list[:2])
        return list[:2]
    else:
        return list

#check_list_len([1,2,3])

'''
定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典。
'''
def check_strindict(dict,str):
    if str in dict.values():
        print('字符串是字典中的值')
    else:
        print('字符串不是字典中的值')
        dict[str] = str
        return dict
dict = {'a':1,'b':2,'c':3}
str = 'd'
#check_strindict(dict,str)


'''
有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''
num = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and i!=k:
                num+=1
                print(i,j,k)
print('一共有%d个互相不同且无重复数字的三位数'%num)


'''
一个足球队在寻找年龄在m岁到n岁的男生or女生（包括m岁和n岁，到底是找男生还是女生，可指定性别）加入。
编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。
'''
m = 12
n = 16
k = 0 #询问次数
num = 0
gender_admit = 'M'
for i in range(1,k+1):
    try:
        gender = input('请输入性别(M表示男，F表示女)：')
        age = int(input('请输入年龄：'))
    except Exception as e:
        print('输入错误：%s'%e)
    if gender.upper() == gender_admit and age in range(m,n+1):
        num+=1
        print('恭喜，你可以加入！')
    else:
        print('Sorry!')
print('符合条件的一共有%d人'%num)