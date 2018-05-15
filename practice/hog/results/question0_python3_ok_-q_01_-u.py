# -*- coding: utf-8 -*-
# @Time : 2018/5/14 下午6:09
# @Author : ScrewMan
# @Site : 
# @File : result.py.py
# @Software : PyCharm


"""

"""
"""

问题1运行 python3 ok -q 01 -u 结果
=====================================================================
Assignment: Project 1: Hog
OK, version v1.13.11
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 1
(cases remaining: 9)

>>> from hog import *
>>> roll_dice(2, make_test_dice(4, 6, 1))
? 10
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 2
(cases remaining: 8)

>>> from hog import *
>>> roll_dice(3, make_test_dice(4, 6, 1))
? 11
-- Not quite. Try again! --

? 1
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 3
(cases remaining: 7)

>>> from hog import *
>>> roll_dice(4, make_test_dice(2, 2, 3))
? 9
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 4
(cases remaining: 6)

>>> from hog import *
>>> roll_dice(4, make_test_dice(1, 2, 3))
? 1
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 5
(cases remaining: 5)

>>> from hog import *
>>> counted_dice = make_test_dice(4, 1, 2, 6)
>>> roll_dice(3, counted_dice)
? 1
-- OK! --

>>> roll_dice(1, counted_dice)  # Make sure you call dice exactly num_rolls times!
? 4
-- Not quite. Try again! --

? 6
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 6
(cases remaining: 4)

>>> from hog import *
>>> roll_dice(9, make_test_dice(6))
? 54
-- OK! --

>>> roll_dice(7, make_test_dice(2, 2, 2, 2, 2, 2, 1))
? 13
-- Not quite. Try again! --

? 1
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 2 > Case 1
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 2 > Case 2
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Question 1 > Suite 2 > Case 3
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Question 1 unlocked.


"""

