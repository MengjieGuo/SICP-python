""" Lab 3: Recursion and Midterm Review """

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    """
    求a b 的最大公约数
    
    根据欧几里得对最大公约数的描述：
        如果较小的能够被较大的整除，那么较小的就是最大公约数
        或者定理：两个整数的最大公约数等于其中较小的那个数和两数相除余数的最大公约数。最大公约数（Greatest Common Divisor）缩写为GCD
    所以如果要求a b的最大公约数，求 b 和 a%b 的最大公约数就可以了。
    结束条件是 当余数为0时，除数就是最大公约数。
    """
    if a % b == 0:
        return b
    if a > b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)

b = 0

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
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
    """需要打印出n的变化过程，结果以n==1结尾，所以计算新的n然后调用自己直到n==1
        实在想不出如何返回 计算步数的方式，所以引用了一个全局变量b
    """
    global b
    print(n)
    b += 1
    if n == 1:
        return b
    n = n//2 if n % 2 == 0 else n*3+1
    return hailstone(n)


