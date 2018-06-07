HW_SOURCE_FILE = 'hw03.py'

#############
# Questions #
#############

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'has_seven',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if '7' in str(k):
        return True
    return False

def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    # i = 1
    # result = 0
    # while i <= n:
    #     result += term(i)
    #     i += 1
    s = term(n)
    if n == 1:
        return s
    s += summation(n-1, term)
    return s
    "*** YOUR CODE HERE ***"

def square(x):
    return x * x

def identity(x):
    return x

triple = lambda x: 3 * x

increment = lambda x: x + 1

add = lambda x, y: x + y

mul = lambda x, y: x * y

def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence and base.
    The terms to be combined are term(1), term(2), ..., term(n).  combiner is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)   # 2 * 1^2 * 2^2 * 3^2
    72
    """
    "*** YOUR CODE HERE ***"
    """
    使用递归思想
        先求 add(base, 剩余n-1和)
        再求 add(base, add(base, 剩余其他n-2和))
        
        像这样的
        combiner(base, accumulate(combiner, term(n), n-1, term))
        计算是从n开始知道1为止
        if n <= 1:
            return combiner(base, term(1)) 
        
    """
    """
    i = 1
    result = base
    while i <= n:
        result = combiner(result, term(i))
        i += 1
    return result
    """
    """
    重写
    """
    if n == 0:
        return combiner(base, term(0))
    if n == 1:
        return combiner(base, term(1))
    return accumulate(combiner, combiner(base, term(n)), n-1, term)
"""
add(0, add(5, add(4, add(3, add(2, 1))))))
"""
if __name__ == '__main__':
    print(accumulate(add, 0, 5, identity))

def summation_using_accumulate(n, term):
    """Returns the sum of term(1) + ... + term(n). The implementation
    uses accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'summation_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'product_using_accumulate',
    ...       ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    return accumulate(mul, 1, n, term)


def filtered_accumulate(combiner, base, pred, n, term):
    """Return the result of combining the terms in a sequence of N terms
    that satisfy the predicate pred. combiner is a two-argument function.
    If v1, v2, ..., vk are the values in term(1), term(2), ..., term(N)
    that satisfy pred, then the result is
         base combiner v1 combiner v2 ... combiner vk
    (treating combiner as if it were a binary operator, like +). The
    implementation uses accumulate.

    >>> filtered_accumulate(add, 0, lambda x: True, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> filtered_accumulate(add, 11, lambda x: False, 5, identity) # 11
    11
    >>> filtered_accumulate(add, 0, odd, 5, identity)   # 0 + 1 + 3 + 5
    9
    >>> filtered_accumulate(mul, 1, greater_than_5, 5, square)  # 1 * 9 * 16 * 25
    3600
    >>> # Do not use while/for loops or recursion
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'filtered_accumulate',
    ...       ['While', 'For', 'Recursion'])
    True
    """
    def combine_if(x, y):
        "*** YOUR CODE HERE ***应该是对参数y进行处理，看是否满足filtered_accumulate的参数pred"
        if pred(y):
            return combiner(x, y)
        else:
            return x
    return accumulate(combine_if, base, n, term)

def odd(x):
    return x % 2 == 1

def greater_than_5(x):
    return x > 5

def make_repeater(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5)
    5
    """
    "*** YOUR CODE HERE ***"
    """
    if a = make_repeater(increments, 1) return increment(x), if call a(5) will get 5+1
    if a = make_repeater(increments, 2) return increment(increment(x)), will get (5+1)+1
    递归是要有边界条件的
    递归结束的条件是n达到某个值，在这里是1
    如果返回 increment(increment) 也就是 f(f)是会报错的，这里需要里面的f是一个可以接收参数的函数。。。
    一开始只使用compose无法满足条件所以这里想到使用 compose1 返回的就是可以接收一个参数的函数
    
    结束条件是 compose(f, f) , 这里是2次调用，所以结束的n要变大
    
    最后一个测试用例没有通过，n为0，所以需要加入判断条件，如果n=0则返回参数，这。。。要不仿照compose1再写一个
    """
    if n == 0:
        return return_x()
    if n <= 2:
        return compose1(f, f)
    return compose1(f, make_repeater(f, n-1))

    """
    如果使用accumulate 和 compose1 实现单行的return
    
    回顾下 accumulate 的作用，有个操作函数f, 有个base，有个n，有个函数g，对1到n分别求g(x), 然后对所有的结果求f(x, y)
    """


def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def return_x():
    def h(x):
        return x
    return h

###################
# Extra Questions #
###################

quine = """
"*** YOUR CODE HERE ***"
"""

def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"

def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"

three = successor(two)

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"

def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"

def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"

def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"

# if __name__ == '__main__':
#     # a = accumulate(mul, 1, 4, square)
#     # a = accumulate(mul, 1, 6, triple)
#     # add_three = make_repeater(increment, 3)
#     # print(add_three(5))
#     a = make_repeater(increment, 2)
#     print(a(5))

    """
    test  make_repeater
    # b = increment(increment(1))
    # print(b)
    # a = square
    # c = square(a)
    # print(c('x'))
    # 现在的思路，是错误的。
    """

