# -*- coding: utf-8 -*-
# @Time : 2018/6/14 下午10:02
# @Author : ScrewMan
# @Site : 
# @File : higherOrderFunction.py
# @Software : PyCharm
from practice.hw02.hw02 import square


def mystery(f, x):
    """
    >>> from operator import add, mul
    >>> a = mystery(add, 3)
    >>> a(4) # add(3, 4)
    7
    >>> a(12)
    15
    >>> b = mystery(mul, 5)
    >>> b(7) # mul(5, 7)
    35
    >>> b(1)
    5
    >>> c = mystery(lambda x, y: x * x + y, 4)
    >>> c(5)
    21
    >>> c(7)
    23
    >>> foo = mystery(lambda a, b: a(b), lambda c: 5 + square(c))
    >>> foo(-2)
    9
    """
    return lambda y: f(x, y)


# 2. What would Python display?
# >>> foo = mystery(lambda a, b: a(b), lambda c: 5 + square(c))
# >>> foo(-2)
#
# >>> 9

def fox_says(start, middle, end, num):
    """
    >>> fox_says('wa', 'pa', 'pow', 3)
    'wa-pa-pa-pa-pow'
    >>> fox_says('fraka', 'kaka', 'kow', 4)
    'fraka-kaka-kaka-kaka-kaka-kow'
    """

    def repeat(k):
        if k == 1:
            return middle
        return middle + "-" + repeat(k - 1)

    return start + '-' + repeat(num) + '-' + end


"""
1、最后一次调用没有参数
2、总共调用了3次函数
"""
print((lambda x: lambda y: lambda: x * x)(3)(lambda z: z * z)())


def combine(n, f, result):
    """
    Combine the digits in non-negative integer n using f.
    >>> from operator import  mul, add
    >>> combine(3, mul, 2) # mul(3, 2)
    6
    >>> combine(43, mul, 2) # mul(4, mul(3, 2))
    24
    >>> combine(6502, add, 3) # add(6, add(5, add(0, add(2, 3)
    16
    >>> combine(239, pow, 0) # pow(2, pow(3, pow(9, 0))))
    8
    """
    if n == 0:
        return result
    else:
        return combine(n // 10, f, f(n % 10, result))

# 2. James wants to print this week’s discussion handouts for all the students in CS
# 61A. However, both printers are broken! The first printer only prints multiples of n
# pages, and the second printer only prints multiples of m pages. Help James figure out
# whether or not it’s possible to print exactly total number of handouts!
def has_sum(total, n, m):
    """
    >>> has_sum(1, 3, 5)
    False
    >>> has_sum(5, 3, 5) # 0 * 3 + 1 * 5 = 5
    True
    >>> has_sum(11, 3, 5) # 2 * 3 + 1 * 5 = 11
    True
    """
    if ____________________________________________________:
        return ____________________________________
    elif __________________________________________________:
        return ____________________________________
    return ________________________________________________

# 3. The next day, the printers break down even more! Each time they are used, the first
# printer prints a random x copies 50 ≤ x ≤ 60, and the second printer prints a random
# y copies 130 ≤ y ≤ 140. James also relaxes his expectations: he’s satisfied as long
# as there’s at least lower copies so there are enough for everyone, but no more than
# upper copies to prevent waste.
def sum_range(lower, upper):
    """
    >>> sum_range(45, 60) # Printer 1 prints within this range
    True
    >>> sum_range(40, 55) # Printer 1 can print a number 56-60
    False
    >>> sum_range(170, 201) # Printer 1 + 2 will print between
    180 and 200 copies total
    True
    """
    def copies(pmin, pmax):
        if ________________________________________________:
            return ____________________________________
        elif ______________________________________________:
            return ____________________________________
        return ____________________________________________
    return copies(0, 0)