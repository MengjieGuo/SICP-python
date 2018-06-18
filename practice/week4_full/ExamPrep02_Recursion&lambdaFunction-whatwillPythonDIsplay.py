# -*- coding: utf-8 -*-
# @Time : 2018/6/18 下午2:53
# @Author : ScrewMan
# @Site : 
# @File : ExamPrep02_Recursion&lambdaFunction.py
# @Software : PyCharm

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


if __name__ == '__main__':
    """
    capt(vision) # 6
    
    print(print(1), vision(2)) # 1 2 None 3
    
    hawkeye(hammer, 3) # 会报错，thor(love) 调用只有一个参数，而hammer(love) 会报错
    
    hawkeye(capt, 3) # 9 
    
    hammer(lambda ultron: ultron, -1) # 0
    
    hammer(vision, avengers) # 6 6 -6
    """
    # capt(vision)
    # print(print(1), vision(2))
    # hawkeye(hammer, 3)
    # print(hawkeye(capt, 3))
    # print(hammer(lambda ultron: ultron, -1))
    # print(hammer(vision, avengers))
