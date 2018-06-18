# -*- coding: utf-8 -*-
# @Time : 2018/6/18 下午2:53
# @Author : ScrewMan
# @Site : 
# @File : ExamPrep02_Recursion&lambdaFunction.py
# @Software : PyCharm
"""
1. Express Yourself (Fa14 MT1 Q3a))
A k-bonacci sequence starts with K-1 zeros and then a one. Each subsequent element
is the sum of the previous K elements. The 2-bonacci sequence is the standard
Fibonacci sequence. The 3-bonacci and 4-bonacci sequences each start with the following
ten elements:
n: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...
kbonacci(n, 2): 0, 1, 1, 2, 3, 5, 8, 13, 21, 35, ...
kbonacci(n, 3): 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, ...
kbonacci(n, 4): 0, 0, 0, 1, 1, 2, 4, 8, 15, 29, ...
Fill in the blanks of the implementation of kbonacci below, a function that takes
non-negative integer n and positive integer k and returns element n of a k-bonacci
sequence.
"""


def kbonacci(n, k):
    """Return element N of a K-bonacci sequence.
    if n=7, k=4 then total（7） =   total(6) + total(5) + total(4) + total(3)
    >>> kbonacci(3, 4)
    1
    >>> kbonacci(9, 4)
    29
    >>> kbonacci(4, 2)
    3
    >>> kbonacci(8, 2)
    21
    """
    if n < k - 1:
        return 0
    elif n == k - 1:
        return 1
    else:
        total = 0
        i = n - k  # 如果使用while循环，total的值应该是前k个数的和
        while i < n:
            total = total + kbonacci(i, k)
            i = i + 1
        return total


"""
2. Combine, Reverse, and Remove (Fa14 MT1 Q3b)
Fill in the blanks of the following functions defined together in the same file. Assume
that all arguments to all of these functions are positive integers that do not contain
any zero digits. For example, 1001 contains zero digits (not allowed), but 1221 does
not (allowed). You may assume that reverse is correct when implementing remove.
"""


def combine(left, right):
    """Return all of LEFT's digits followed by all of RIGHT's
    digits."""
    factor = 1
    while factor <= right:
        factor = factor * 10
    return left * factor + right


def reverse(n):
    """Return the digits of N in reverse.
    >>> reverse(122543)
    345221
    """
    if n < 10:
        return n
    else:
        return combine(n % 10, reverse(n // 10))  # 注意/和//的区别，一个返回float，一个是取整数部分。例如 10/3=3.3333333 10//3=3


def remove(n, digit):
    """Return all digits of N that are not DIGIT, for DIGIT
    less than 10.
    >>> remove(243132, 3)
    2412
    >>> remove(remove(243132, 1), 2)
    433
    """
    removed = 0
    while n != 0:
        a, n = n % 10, n // 10
        if a != digit:
            removed = removed * 10 + a
    return reverse(removed)  # 为什么会用到反转函数？因为removed就是反过来的，例如 remove(34132, 3) removed=214


"""
3. You Complete Me (Sp15 Midterm 1 Q3d)
Implement the memory function, which takes a number x and a single-argument function
f. It returns a function with a peculiar behavior that you must discover from the
doctests. You may only use names and call expressions in your solution. You may not
write numbers or use features of Python not yet covered in the course.
"""
square = lambda x: x * x
double = lambda x: 2 * x


def memory(x, f):
    """Return a higher-order function that prints its
    memories.
    >>> f = memory(3, lambda x: x)
    >>> f = f(square)
    3
    >>> f = f(double)
    9
    >>> f = f(print)
    6
    >>> f = f(square)
    3
    None
    """

    def g(h):
        print(f(x))
        return memory(x, h)

    return g


# if __name__ == '__main__':
#     f = memory(3, lambda x: x)
#     f = f(square)
#     f = f(double)
#     f = f(print)
#     f = f(square)

"""
4. You Complete Me (Sp15 Midterm 1 Q3b)
Add parentheses and single-digit integers in the blanks below so that the expression
on the second line evaluates to 2015. You may only add parentheses and single-digit
integers. You may leave some blanks empty.
"""
lamb = lambda lamb: lambda: lamb + lamb
# print(lamb(1000)() + (lambda b, c: b() * b() - c)(lamb(2), 1))


# Environment Diagrams

def mouse(n):
    if n >= 10:
        squeak = n // 100
        n = frog(squeak) + n % 10
    return n


def frog(croak):
    if croak == 0:
        return 1
    else:
        return 10 * mouse(croak + 1)


# print(mouse(357))  # 47

# What would python display
from operator import add
avengers = 6


def vision(avengers):
    print(avengers)
    return avengers + 1


def hawkeye(thor, hulk):
    love = lambda black_widow: add(black_widow, hulk)
    return thor(love)


def hammer(worthy, stone):
    if worthy(stone) < stone:
        return stone
    elif worthy(stone) > stone:
        return -stone
    return 0


capt = lambda iron_man: iron_man(avengers)


def guo(a, b):
    """
    >>> guo(2, 3)
    8
    """
    return 1