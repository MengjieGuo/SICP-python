# -*- coding: utf-8 -*-
# @Time : 2018/6/12 下午10:54
# @Author : ScrewMan
# @Site : 
# @File : full.py
# @Software : PyCharm


# @trace1
# def triple(x):
#  return 3 * x
#
# # is identical to
#
# def triple(x):
#  return 3 * x
# triple = trace1(triple)


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
看了下ppt，发现并不难
"""

"""2"""
def bar(f):
    print(f)

    def g(x):
        print(f)
        return f(x - 1)

    return g

f = 4


def a(x):
    """lambda x: x + f"""
    print(x)
    print(f)
    xx = f
    return x+f
print(bar(a)(2))

"""
关于最后的 f(x-1) f实际上是 lambda x: x + f
那么 在x+f中 参数x是 2-1=1 那么f是？是bar的参数f还是全局的f？
经过反复的验证，f是全局的f

是否可以这样理解
最后的f(x-1)函数调用是 a(x-1)，但是a函数并非bar函数 或 g函数的内函数，所以无法访问其内部变量f（这里的内部变量f是函数）
此时会搜索全局变量f，此时f=4
"""

"""3"""
def dream1(f):
    kick = lambda x: mind()
    def dream2(secret):
        mind = f(secret)
        kick(2)
    return dream2
inception = lambda secret: lambda: secret
real = dream1(inception)(42)

# def a(x):
#     return x
# x = 1
#
# b = lambda y: y + x
# if __name__ == '__main__':
#     print(a(b)(2))  # got 3, 说明最后的 x(2)调用中， y+x: y=2 x=1 ,x是全局的变量x。


# def ab(g):
#     return g
#
# g = 2
#
#
# def guo(x):
#     print(x)
#     print(g)
#     return x + g
#
# print(ab(guo))
# print(ab(guo)(2))
#
# # 测试inner function中使用父函数的形参
#
#
# def ab(x):
#     print(x)
#
#     def b(x):
#         print(x)
#         return x
#     return b
# ab(1)(2)
