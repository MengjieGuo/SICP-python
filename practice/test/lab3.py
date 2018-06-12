# -*- coding: utf-8 -*-
# @Time : 2018/6/10 下午3:07
# @Author : ScrewMan
# @Site : 
# @File : lab3.py
# @Software : PyCharm

def a(x, y):
    print("x or y")
    print(x, y)
    return x or y

def b():
    print('welcome to')
    return 'hello'

def c():
    print('cs61a')
    return 'world'
if __name__ == '__main__':
    # aa = print('y')
    # print(aa)
    # c = a(print("x"), print("y"))
    # print(type(c))
    # print(c)
    str_a = '1'
    print(b(), c())

"""
print()函数返回None
"""
