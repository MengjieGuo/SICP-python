# -*- coding: utf-8 -*-
# @Time : 2018/6/12 下午10:54
# @Author : ScrewMan
# @Site : 
# @File : full.py
# @Software : PyCharm


@trace1
def triple(x):
 return 3 * x

# is identical to

def triple(x):
 return 3 * x
triple = trace1(triple)


"""

"""


def delay(arg):
    print('delayed')

    def g():
        return arg

    return g
"""
>>> delay(delay)()(6)()
>>> print(delay(print)()(4))
"""


def horse(mask):
 horse = mask
 def mask(horse):
    return horse
 return horse(mask)
mask = lambda horse: horse(2)
horse(mask)

"""
这是什么？
"""
