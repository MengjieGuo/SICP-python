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
    """Define a tree"""
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)


def label(tree):
    """Define label"""
    return tree[0]


def branches(tree):
    """Define branches"""
    return tree[1:]


def is_leaf(tree):
    """Define leaf"""
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
    """Return the max of a tree.
    >>> tree_max([5, [7, [3]]])
    7
    >>> tree_max([10, [7, [3]]])
    10
    >>> tree_max([1, [7, [3, [16]]]])
    16
    """
    """示例有个求所有leaf组成的list
        按照递归的思想，求tree的最大值就是求 跟节点 和 每个 branches 的最大值。（此时每个branches都是各自tree的最大值）

    """
    if is_leaf(t):
        return label(t)
    else:
        return max(label(t), max([tree_max(b) for b in branches(t)]))


# 3.2 Write a function that returns the height of a tree. Recall that the height of
# a tree is the length of the longest path from the root to a leaf.


# def height(t):
#     """Return the height of a tree"""
#     if is_leaf(t):
#         return 1
#     else:
#         return max([height(t)+1 for b in branches(t)])


# 3.3 Write a function that takes in a tree and squares every value. It should
# return a new tree. You can assume that every item is a number.

def square_tree(t):
    """Return a tree with the square of every element in t
    >>> square_tree([1, [7, [3, [16]]]])
    [1, [49, [9, [256]]]]
    """
    """示例有求所有leaf+1，然后生成新tree。这里需要将每个子树的根节点也求square"""

    if is_leaf(t):
        return tree(label(t) ** 2)
    else:
        bs = [square_tree(b) for b in branches(t)]
        return tree(label(t) ** 2, bs)


# 3.4 Write a function that takes in a tree and a value x and returns a list containing
# the nodes along the path required to get from the root of the tree to
# a node containing x.
# If x is not present in the tree, return None. Assume that the entries of the
# tree are unique.
# For the following tree, find path(t, 5) should return [2, 7, 6, 5]

# def find_path(tree, x):
#     """
#     >>> find_path(t, 5)
#     [2, 7, 6, 5]
#     >>> find_path(t, 10) # returns None
#     """
#     if is_leaf(tree):
#         return [label(tree)] if label(tree) == x else None
#     return [label(tree)] if label(tree) == x else [label(tree)] + [find_path(b, x) for b in branches(tree)]

# 3.5 Write a function that takes in a tree and a depth k and returns a new tree
# that contains only the first k levels of the original tree.
# For example, if t is the tree shown in the previous question, then prune(t,
# 2) should return the following tree.
# def prune(t, k):
#     """"""

