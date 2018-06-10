""" Optional problems for Lab 3 """

from lab03 import *

## Higher order functions

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    """
    cycle函数的作用很明显，根据n返回循环调用f1 f2 f3的结果
    提示用到了内嵌函数：
        内嵌函数也返回一个函数 类似这样 f1(f3(f2(f1(x))))
        
    有点迷茫
    
    做完下面的题回来做
   
    """
    def which_func(n):
        if n % 3 == 0:
            return lambda x: x
        elif n % 3 == 1:
            return f1(lambda x:x)
        elif n % 3 == 2:
            return f2(lambda x:x)
        elif n % 3 == 3:
            return f3(lambda x:x)

    def inner(n):
        func = which_func(n)
        return inner(n-1)
    return inner

## Lambda expressions

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda x: y * 10 + x
    while x > 0:
        x, y = x//10, f(x % 10)
    return y == n

## More recursion practice

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    if n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"

def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    """应该返回的结果  对 n 到 1 分别求 odd_term or even_term
        结束条件是 n==1 是返回 odd_term(1)
    """
    if n == 1:
        return odd_term(1)
    if n % 2 == 0:
        return even_term(n) + interleaved_sum(n-1, odd_term, even_term)
    else:
        return odd_term(n) + interleaved_sum(n-1, odd_term, even_term)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    """先来一版 一般的实现"""
    n = str(n)
    i, count = 0, 0
    while i <= len(n)-2:
        for a in n[i+1:]:
            count = count + 1 if int(a) == 10-int(n[i]) else count
        i += 1
    return count





"""
cycle
is_prime
还有一个画程序内存图的
"""
