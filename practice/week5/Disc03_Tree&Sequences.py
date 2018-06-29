# -*- coding: utf-8 -*-
# @Time : 2018/6/28 下午7:37
# @Author : ScrewMan
# @Site : 
# @File : Disc03_Tree&Sequences.py
# @Software : PyCharm

# 1.2 What would Python display?


def a_1_2():
    """
    >>> a = [3, 1, 4, 2, 5, 3]
    >>> a[1::2]
    [1, 2, 3]
    >>> a[:]
    [3, 1, 4, 2, 5, 3]
    >>> a[4:2]
    []
    >>> a[1:-2]
    [1, 4, 2]
    >>> a[::-1]
    [3, 5, 2, 4, 1, 3]
    """


# 2.1 What would Python display?


def a_2_1():
    """
    >>> [i + 1 for i in [1, 2, 3, 4, 5] if i % 2 == 0]
    [3, 5]
    >>> [i * i - i for i in [5, -1, 3, -1, 3] if i > 2]
    [20, 6, 6]
    >>> [[y * 2 for y in [x, x + 1]] for x in [1, 2, 3, 4]]
    [[2, 4], [4, 6], [6, 8], [8, 10]]
    """


# THere will be tree

# Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_leaf(tree):
    return not branches(tree)


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

# 3.1 Write a function that returns the largest number in a tree.


def tree_max(t):
    """Return the max of a tree."""
