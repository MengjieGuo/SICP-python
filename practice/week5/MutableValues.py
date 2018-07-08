# -*- coding: utf-8 -*-
# @Time : 2018/7/8 下午7:14
# @Author : ScrewMan
# @Site : 
# @File : MutableValues.py
# @Software : PyCharm


"""

1、is 和 == 的区别
    is 指的是是否是同一个对象
    == 值连个对象的值是否相同

    如果is为True，那么 ==一定为True

2、默认参数值是函数值的一部分，不是由调用生成的
>>> def f(s=[]):
... s.append(3)
... return len(s)
...
>>> f()
1
>>> f()
2
>>> f()
3

这里的s指向同一个对象
"""