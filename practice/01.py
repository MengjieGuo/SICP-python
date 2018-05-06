# -*- coding: utf-8 -*-
# @Time : 2018/5/4 下午4:45
# @Author : ScrewMan
# @Site : 
# @File : 01.py
# @Software : PyCharm


from operator import add, sub

import cmath


def a_plus_abs_b_guo(a, b):
    """Return a+abs(b), but without calling abs.

    Question 1
    python3 -m doctest 01.py

    1、很明显，f是一个函数
    2、这个f接受2个参数
    3、是否有这样的函数，当b<0时，返回a-b---sub(a, b); 是否有函数当b>0时，返回a+b---add(a, b)

    >>> a_plus_abs_b_guo(2, 3)
    5
    >>> a_plus_abs_b_guo(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


def two_of_three_guo(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    Question 2
    1、先求出3个参数中最大的两个---没有类似函数
    2、求出最小的参数---min()函数可以
    3、一行代码完成求x^2+y^2---a^2+b^2+c^2-min(a, b, c)^2

    注意：平方符号^，在python中是 **2---所以a^2 就是a**2

    >>> two_of_three_guo(1, 2, 3)
    13
    >>> two_of_three_guo(5, 3, 1)
    34
    >>> two_of_three_guo(10, 2, 8)
    164
    >>> two_of_three_guo(5, 5, 5)
    50
    """
    return a ** 2 + b ** 2 + c ** 2 - min(a, b, c) ** 2


def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return max(a * a + b * b, a * a + c * c, b * b + c * c)


def largest_factor_guo(n):
    """Return the largest factor of n that is smaller than n.

    返回小于n的n的最大因子。---除了自己，最大的因数
    1、从1开始的循环---1到根号下n 或者 n/2 + 1
    2、使用while循环的话--- count=根号下n，从1开始，count+=1
    3、根据提示 提示：要检查是否b整除a，则可以使用表达式a % b == 0，这可以理解为，“分割的其余部分a通过b为0。”
        如果a整除b，那么b就是n的因子。---从1开始没法直接返回最大的因数b
    4、倒着计数，从根号下n开始，第一个满足a%b==0的就是n的最大因数



    >>> largest_factor_guo(15) # factors are 1, 3, 5
    5
    >>> largest_factor_guo(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor_guo(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    # count = cmath.sqrt(n)  # 求出n的平方根---还需要求接近平方根的最大整数   count = n//2+1 应该也是可以的
    count = n - 1
    while count >= 1:  # 1也是
        if n % count == 0:  # 如果满足a%b==0，那么这个b就是最大的因数？
            return count
        count -= 1


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    factor = n - 1
    while factor > 0:
        if n % factor == 0:
            return factor
        factor -= 1

#
# """Question 4 根据描述，是在第一个参数同时为true时，一个返回1，另一个不返回1"""
#
#
# def if_function(condition, true_result, false_result):
#     """Return true_result if condition is a true value, and
#     false_result otherwise.
#
#     1、很明显的，当condition=True，返回
#
#     >>> if_function(True, 2, 3)
#     2
#     >>> if_function(False, 2, 3)
#     3
#     >>> if_function(3==2, 3+2, 3-2)
#     1
#     >>> if_function(3>2, 3+2, 3-2)
#     5
#     """
#     if condition:
#         return true_result
#     else:
#         return false_result
#
#         def with_if_statement():
#             """
#             >>> with_if_statement()
#             1
#             """
#             if c():
#                 return t()
#             else:
#                 return f()
#
#
# def with_if_function():
#     return if_function(c(), t(), f())
#
#
# def c():
#     "*** YOUR CODE HERE ***"
#
#
# def t():
#     "*** YOUR CODE HERE ***"
#
#
# def f():
#     "*** YOUR CODE HERE ***"


"""Question 5 """


def hailstone_guo(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone_guo(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"

    count = 1
    while n > 1:
        count += 1
        print(int(n))
        if n % 2 == 0:
            n = n / 2  # n//2是整数，如果是小数，或得到整数部分
        else:
            n = n * 3 + 1
    print(int(n))
    # print(count)
    return count

if __name__ == '__main__':
    """"""
    # hailstone_guo(10)