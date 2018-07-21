# -*- coding: utf-8 -*-
'''
Created on 2018-07-21

@author: Enzo
'''

class Person(object):
    """人的类"""
    def __init__(self,name):
        super(Person,self).__init__()
        self.name = name
        self.gun = None #保存枪的对象引用
        self.hp = 100 #血量

    def anzhuang_zidan(self,dan_jia,zi_dan):
        """把子弹装到弹夹中"""
        #弹夹.保存子弹
        dan_jia.baocun_zidan(zi_dan)

    def anzhuang_danjia(self,gun,dan_jia):
        """把弹夹安装到枪中"""
        #枪.保存弹夹
        gun.baocun_danjia(dan_jia)

    def naqiang(self,gun):
        self.gun = gun

    def kou_ban_ji(self,enemy):
        """枪发射射击敌人"""
        #枪.开火（敌人）
        self.gun.fire(enemy)
    def diaoxue(self,shashangli):
        """掉血"""
        self.hp-= shashangli

    def __str__(self):
        if self.hp > 0:
            if self.gun:
                return '%s的血量是%d,他有枪，%s'%(self.name,self.hp,self.gun)
            else:
                return '%s的血量是%d,他没有枪'%(self.name,self.hp)
        else:
            return '%s已挂'%self.name


class Gun(object):
    """枪类"""
    def __init__(self,name):
        super(Gun, self).__init__()
        self.name = name
        self.danjia = None #用来记录弹夹对象的引用

    def __str__(self):
        if self.danjia:
            return '枪的信息为%s,%s'%(self.name,self.danjia)
        else:
            return '枪的信息为%s,没有弹夹'%self.name

    def baocun_danjia(self,dan_jia):
        """用一个属性来保存这个弹夹对象的引用"""
        self.danjia = dan_jia

    def fire(self,enemy):
        """枪从弹夹中获取一发子弹，然后让这法子弹去击中敌人"""
        #弹夹.弹出一发子弹（）
        zidan_tmp = self.danjia.tanchu_zidan()
        if zidan_tmp:
            zidan_tmp.shoot(enemy)
        else:
            print('弹夹没有子弹了')


class Danjia(object):
    """弹夹类"""
    def __init__(self,max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num #用来记录弹夹的容量
        self.zidan_list = [] #用来记录所有子弹的引用
    def __str__(self):
        return '子弹的信息是：%d/%d'%(len(self.zidan_list),self.max_num)

    def baocun_zidan(self,zi_dan):
        """将子弹保存"""
        self.zidan_list.append(zi_dan)

    def tanchu_zidan(self):
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None

class Zidan(object):
    """子弹类"""
    def __init__(self,shashangli):
        super(Zidan, self).__init__()
        self.shashangli = shashangli
    def shoot(self,enemy):
        """让敌人掉血"""
        #敌人.掉血
        enemy.diaoxue(self.shashangli)



def main():
    """用来控制整个程序的流程"""
    #1. 创建老王对象
    laowang = Person('老王')

    #2. 创建一个枪对象
    ak47 = Gun('AK47')


    #3. 创建一个子弹夹对象
    dan_jia = Danjia(20)

    #4. 创建一些子弹
    zi_dan = Zidan(10)


    #5. 老王把子弹安装到弹夹中
    #laowang.安装子弹到弹夹中
    for i in range(15):

        laowang.anzhuang_zidan(dan_jia,zi_dan)

    #6. 老王把弹夹安装到枪中
    #老王.安装弹夹到枪中
    laowang.anzhuang_danjia(ak47,dan_jia)

    #7.测试
    #测试弹夹信息
    #print(dan_jia)
    #测试枪的信息
    #print(ak47)
    #8.老王拿枪
    #laowang.拿枪
    laowang.naqiang(ak47)
    #测试
    print(laowang)
    #9. 创建敌人
    enemy = Person('敌人')
    print(enemy)
    #10. 老王开枪
    #laowang.扣扳机（敌人）
    for i in range(12):
        laowang.kou_ban_ji(enemy)
        print(enemy)
        print(laowang)




if __name__ == '__main__':
    main()