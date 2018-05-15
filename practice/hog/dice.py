"""Functions that simulate dice rolls.

A dice function takes no arguments and returns a number from 1 to n
(inclusive), where n is the number of sides on the dice.

Types of dice:

 -  Dice can be fair, meaning that they produce each possible outcome with equal
    probability. Examples: four_sided, six_sided

 -  For testing functions that use dice, deterministic test dice always cycle
    through a fixed sequence of values that are passed as arguments to the
    make_test_dice function.
"""

from random import randint


def make_fair_dice(sides):
    """Return a die that returns 1 to SIDES with equal chance."""
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'

    def dice():
        return randint(1, sides)

    return dice


four_sided = make_fair_dice(4)
six_sided = make_fair_dice(6)


def make_test_dice(*outcomes):
    """Return a die that cycles deterministically through OUTCOMES.

    >>> dice = make_test_dice(1, 2, 3)
    >>> dice()
    1
    >>> dice()
    2
    >>> dice()
    3
    >>> dice()
    1
    >>> dice()
    2

    This function uses Python syntax/techniques not yet covered in this course.
    The best way to understand it is by reading the documentation and examples.

    这里提到了一个 关键字 nonlocal
        这个关键字的作用：在函数内部使用函数外部（且非全局变量）的变量
        在这里就是告诉python解释器 dice() 中的 index 是 make_test_dice()中定义的index
        这样向index赋值时，就是向外层index赋值

    同样的还有 global 关键字：在函数内使用全局的变量
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1

    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]

    return dice

# if __name__ == '__main__':
#     dice = make_test_dice(1, 2, 3)
#     print(1)
#     dice()
#     print(4)
#     dice()
#     print(2)
#     dice()


"""
测试结果
=====================================================================
Assignment: Project 1: Hog
OK, version v1.13.11
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 0 > Suite 1 > Case 1
(cases remaining: 2)

>>> from hog import *
>>> test_dice = make_test_dice(4, 1, 2)
>>> test_dice()
? 4
-- OK! --

>>> test_dice() # Second call
? 1
-- OK! --

>>> test_dice() # Third call
? 2
-- OK! --

>>> test_dice() # Fourth call
? 4
-- OK! --

---------------------------------------------------------------------
Question 0 > Suite 2 > Case 1
(cases remaining: 1)

Q: Which of the following is the correct way to "roll" a fair, six-sided die?
Choose the number of the correct choice:
0) six_sided
1) make_test_dice(6)
2) six_sided()
3) make_fair_dice(6)
? 2
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 0 unlocked.
"""
