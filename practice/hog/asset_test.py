# -*- coding: utf-8 -*-
# @Time : 2018/5/9 下午8:09
# @Author : ScrewMan
# @Site : 
# @File : asset_test.py
# @Software : PyCharm

"""
在开发一个程序时候，与其让它运行时崩溃，不如在它出现错误条件时就崩溃（返回错误）。这时候断言assert 就显得非常有用。

assert的语法格式：

assert expression
1
它的等价语句为：

if not expression:
    raise AssertionError
"""

if __name__ == '__main__':
    a_str = 'a_str'
    b_int = 2
    assert type(a_str) == str
    # assert type(b_int) == str , 'b_int must be str'
    assert len(a_str) > 0, 'You must supply outcomes to make_test_dice'

