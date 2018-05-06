# -*- coding: utf-8 -*-
# @Time : 2018/5/6 下午7:23
# @Author : ScrewMan
# @Site : 
# @File : 03.py
# @Software : PyCharm

# 这里从问题Q7开始
"""Q7"""


def xk(c, d):
    if c == 4:
        return 6
    elif d >= 4:
        return 6 + 7 + c
    else:
        return 25


print(xk(10, 10))
print(xk(10, 6))
print(xk(4, 6))
print(xk(0, 0))


def how_big(x):
    if x > 10:
        print('huge')
    elif x > 5:
        return 'big'
    elif x > 0:
        print('small')
    else:
        print('nothing')


print(how_big(7), len(how_big(7)))
how_big(12)
how_big(1)
how_big(-1)


def so_big(x):
    if x > 10:
        print('huge')
    if x > 5:
        return 'big'
    if x > 0:
        print('small')
    print('nothing')

print('\nso_big\n')
print(so_big(7))
so_big(12)
so_big(1)


def ab(c, d):
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print('foo')

print('\nab\n')
ab(10, 20)


def bake(cake, make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make

print('\nbake\n')
print(bake(0, 29))
print(bake(1, 'mashed potatoes'))


"""Q8"""


def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0 # You can replace this line!

print('\nboth_positive\n')
print(both_positive(-1, 1))
print(both_positive(1, 1))


"""Q9"""


def falling(n, k):
    """Compute the falling factorial of n to depth k.


    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    # result, count = n, 1
    # while count < k:
    #     result, count = result*(n-count), count+1
    # return result

    # 好像没法处理falling(4, 0)， 修改一下

    result, count = 1, 0
    while count < k:
        result, count = result*(n-count), count+1
    return result

    # 可以了

    # 看一下给出的参考代码
    # total, stop = 1, n - k
    # while n > stop:
    #     total, n = total * n, n - 1
    # return total
    # 循环停止条件是n大于某个值---n-k，跟上面我的有点不太同

print('\nfalling\n')
print(falling(6, 3))
print(falling(4, 0))
print(falling(4, 3))
print(falling(4, 1))


"""Q10"""
# 给出猜测的范围，从1开始猜，知道成功


def guess_linear():
    """Guess in increasing order and return the number of guesses."""
    prompt_for_number(LOWER, UPPER)
    num_guesses = 1
    guess = LOWER
    while not is_correct(guess):
        guess += 1
        num_guesses += 1
    return num_guesses

"""Q11"""
# 进阶版猜测，使用二进制搜索算法，二进制搜索算法还是比较简单的


def guess_binary():
    """Return the number of attempted guesses. Implement a faster search
    algorithm that asks the user whether a guess is less than or greater than
    the correct number.

    Hint: If you know the guess is greater than the correct number, then your
    algorithm doesn't need to try numbers that are greater than guess.
    """
    prompt_for_number(LOWER, UPPER)
    num_guesses = 1
    lower, upper = LOWER, UPPER
    guess = (lower + upper) // 2
    while not is_correct(guess):
        if is_too_high(guess):
            upper = guess - 1
        else:
            lower = guess + 1
        guess = (lower + upper) // 2
        num_guesses += 1
    return num_guesses
