""" Lab 04 Optional Questions """
import itertools
from lab04 import *


# Q6
def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"
    """接受list返回list
    使用递归
    如果元素是list需要调用自己，返回l
    
    flat=lambda L: sum(map(flat,L),[]) if isinstance(L,list) else [L]

    """
    li = []
    for item in lst:
        if type(item) == list:
            li.extend(flatten(item))
        else:
            li.append(item)
    return li


# Q7
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    """集合直接能够进行交集，并集，差集，补集的运算 两个set的并集 | 或者 union
    & 是交集
    - 是差集
    ^ 是补集
    """
    return list(set(lst1) | set(lst2))


# if __name__ == '__main__':
#     a, b = [1, 2], [2, 3, 4]
#     a = set(a)
#     b = set(b)
#     c = a | b
#     print(c)
######################
### Connect N Game ###
######################

def create_row(size):
    """Returns a single, empty row with the given size. Each empty spot is
    represented by the string '-'.

    >>> create_row(5)
    ['-', '-', '-', '-', '-']
    """
    "*** YOUR CODE HERE ***"
    # lst = []
    # for i in range(size):
    #     lst += ['-']
    # return lst
    return ['-' for i in range(size)]


def create_board(rows, columns):
    """Returns a board with the given dimensions.

    >>> create_board(3, 5)
    [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-']]
    """
    "*** YOUR CODE HERE ***"
    return [create_row(columns) for i in range(rows)]


def replace_elem(lst, index, elem):
    """Create and return a new list whose elements are the same as those in
    LST except at index INDEX, which should contain element ELEM instead.

    >>> old = [1, 2, 3, 4, 5, 6, 7]
    >>> new = replace_elem(old, 2, 8)
    >>> new
    [1, 2, 8, 4, 5, 6, 7]
    >>> new is old   # check that replace_elem outputs a new list
    False
    """
    assert index >= 0 and index < len(lst), 'Index is out of bounds'
    "*** YOUR CODE HERE ***"
    """注意到 old 不是 new所以需要产生一个副本，方式可以是使用list()方法，也可以使用切片"""
    lst = list(lst)  # lst = lst[:]
    lst[index] = elem
    return lst


def get_piece(board, row, column):
    """Returns the piece at location (row, column) in the board.

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> board = put_piece(board, rows, 0, 'X')[1] # Puts piece "X" in column 0 of board and updates board
    >>> board = put_piece(board, rows, 0, 'O')[1] # Puts piece "O" in column 0 of board and updates board
    >>> get_piece(board, 1, 0)
    'X'
    >>> get_piece(board, 1, 1)
    '-'
    """
    "*** YOUR CODE HERE ***"
    return board[row][column]


def put_piece(board, max_rows, column, player):
    """Puts PLAYER's piece in the bottommost empty spot in the given column of
    the board. Returns a tuple of two elements:

        1. The index of the row the piece ends up in, or -1 if the column
           is full.
        2. The new board

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> row, new_board = put_piece(board, rows, 0, 'X')
    >>> row
    1
    >>> row, new_board = put_piece(new_board, rows, 0, 'O')
    >>> row
    0
    >>> row, new_board = put_piece(new_board, rows, 0, 'X')
    >>> row
    -1
    """
    "*** YOUR CODE HERE ***"
    """
    1 找到最后不为空的行，返回上一行的索引
    2 如果不是-1就更新上一行的值
    3 返回tuple
    """
    blank_idx = -1
    for idx, val in enumerate(board):
        if val[column] in ['X', 'O']:
            blank_idx = idx - 1
            break
        else:
            blank_idx = idx
    if blank_idx != -1:
        board[blank_idx][column] = player
    return (blank_idx, board)


# if __name__ == '__main__':
#     rows, columns = 2, 2
#     board = create_board(rows, columns)
#     row, new_board = put_piece(board, rows, 0, 'X')
#     row, new_board = put_piece(new_board, rows, 0, 'O')
#     row, new_board = put_piece(new_board, rows, 0, 'X')

def make_move(board, max_rows, max_cols, col, player):
    """Put player's piece in column COL of the board, if it is a valid move.
    Return a tuple of two values:

        1. If the move is valid, make_move returns the index of the row the
           piece is placed in. Otherwise, it returns -1.
        2. The updated board

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> row, board = make_move(board, rows, columns, 0, 'X')
    >>> row
    1
    >>> get_piece(board, 1, 0)
    'X'
    >>> row, board = make_move(board, rows, columns, 0, 'O')
    >>> row
    0
    >>> row, board = make_move(board, rows, columns, 0, 'X')
    >>> row
    -1
    >>> row, board = make_move(board, rows, columns, -4, '0')
    >>> row
    -1
    """
    "*** YOUR CODE HERE ***"
    """与 put_piece 的区别 是 COL可能是无效的"""
    if max_cols <= col or col < 0:
        return (-1, board)
    else:
        return put_piece(board, max_rows, col, player)


def print_board(board, max_rows, max_cols):
    """Prints the board. Row 0 is at the top, and column 0 at the far left.

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> print_board(board, rows, columns)
    - -
    - -
    >>> new_board = make_move(board, rows, columns, 0, 'X')[1]
    >>> print_board(new_board, rows, columns)
    - -
    X -
    """
    "*** YOUR CODE HERE ***"
    for m in board:
        st = ''
        for n in m:
            st += n + ' '
        print(st[:-1])


        # if __name__ == '__main__':
        #     rows, columns = 2, 2
        #     board = create_board(rows, columns)
        #     print_board(board, rows, columns)
        # new_board = make_move(board, rows, columns, 0, 'X')[1]
        # print_board(new_board, rows, columns)


def check_win_row(board, max_rows, max_cols, num_connect, row, player):
    """ Returns True if the given player has a horizontal win
    in the given row, and otherwise False.

    >>> rows, columns, num_connect = 4, 4, 2
    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 0, 'O')[1]
    >>> check_win_row(board, rows, columns, num_connect, 3, 'O')
    False
    >>> board = make_move(board, rows, columns, 2, 'X')[1]
    >>> board = make_move(board, rows, columns, 0, 'O')[1]
    >>> check_win_row(board, rows, columns, num_connect, 3, 'X')
    False
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> check_win_row(board, rows, columns, num_connect, 3, 'X')
    True
    >>> check_win_row(board, rows, columns, 4, 3, 'X')    # A win depends on the value of num_connect
    False
    >>> check_win_row(board, rows, columns, num_connect, 3, 'O')   # We only detect wins for the given player
    False
    """
    "*** YOUR CODE HERE ***"
    """检查第row行有num_connect个player连着就返回True，否则返回False"""
    flag = 0
    for a in board[row]:
        flag = flag + 1 if a == player else 0
        if flag == num_connect:
            return True
    return False

    # tmp_count = [(k, len(list(v))) for k, v in itertools.groupby(board[row])]
    # print(tmp_count)
    # for a in tmp_count:
    #     if a[0] == player:
    #         if a[1] >= num_connect:
    #             return True
    # return False


#
# if __name__ == '__main__':
#     rows, columns, num_connect = 4, 4, 2
#     board = create_board(rows, columns)
#     board = make_move(board, rows, columns, 0, 'X')[1]
#     board = make_move(board, rows, columns, 0, 'O')[1]
#     check_win_row(board, rows, columns, num_connect, 3, 'O')
#     board = make_move(board, rows, columns, 2, 'X')[1]

def check_win_column(board, max_rows, max_cols, num_connect, col, player):
    """ Returns True if the given player has a vertical win in the given column,
    and otherwise False.

    >>> rows, columns, num_connect = 5, 5, 2
    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> check_win_column(board, rows, columns, num_connect, 0, 'X')
    False
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> check_win_column(board, rows, columns, num_connect, 1, 'O')
    False
    >>> board = make_move(board, rows, columns, 2, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> check_win_column(board, rows, columns, num_connect, 1, 'O')
    True
    >>> check_win_column(board, rows, columns, 4, 1, 'O')
    False
    >>> check_win_column(board, rows, columns, num_connect, 1, 'X')
    False
    """
    "*** YOUR CODE HERE ***"
    flag = 0
    for a in board:
        flag = flag + 1 if a[col] == player else 0
        if flag == num_connect:
            return True
    return False


# if __name__ == '__main__':
#     rows, columns, num_connect = 5, 5, 2
#     board = create_board(rows, columns)
#     board = make_move(board, rows, columns, 0, 'X')[1]
#     board = make_move(board, rows, columns, 1, 'O')[1]
#     check_win_column(board, rows, columns, num_connect, 0, 'X')
#
#     board = make_move(board, rows, columns, 1, 'X')[1]
#     board = make_move(board, rows, columns, 1, 'O')[1]
#     check_win_column(board, rows, columns, num_connect, 1, 'O')
#
#     board = make_move(board, rows, columns, 2, 'X')[1]
#     board = make_move(board, rows, columns, 1, 'O')[1]
#     check_win_column(board, rows, columns, num_connect, 1, 'O')

def check_win(board, max_rows, max_cols, num_connect, row, col, player):
    """Returns True if the given player has any kind of win after placing a
    piece at (row, col), and False otherwise.

    >>> rows, columns, num_connect = 2, 2, 2
    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'O')
    False
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'X')
    True

    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 0, 'O')[1]
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> check_win(board, rows, columns, num_connect, 1, 0, 'X')
    True
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'X')
    False

    >>> board = create_board(rows, columns)
    >>> board = make_move(board, rows, columns, 0, 'X')[1]
    >>> board = make_move(board, rows, columns, 1, 'O')[1]
    >>> board = make_move(board, rows, columns, 1, 'X')[1]
    >>> check_win(board, rows, columns, num_connect, 0, 0, 'X')
    False
    >>> check_win(board, rows, columns, num_connect, 1, 0, 'X')
    True
    """
    diagonal_win = check_win_diagonal(board, max_rows, max_cols, num_connect,
                                      row, col, player)
    "*** YOUR CODE HERE ***"
    if diagonal_win:
        return True
    else:
        row_win = check_win_row(board, max_rows, max_cols, num_connect, row, player)
        if row_win:
            return True
        else:
            col_win = check_win_column(board, max_rows, max_cols, num_connect, col, player)
            if col_win:
                return True
    return False


###############################################################
### Functions for reference when solving the other problems ###
###############################################################

def check_win_diagonal(board, max_rows, max_cols, num_connect, row, col, player):
    """ Returns True if the given player has a diagonal win passing the spot
    (row, column), and False otherwise.
    """
    # Find top left of diagonal passing through the newly placed piece.
    adjacent = 0
    row_top_left, col_top_left = row, col
    while row_top_left > 0 and col_top_left > 0:
        row_top_left -= 1
        col_top_left -= 1

    # Loop through top left to bottom right diagonal and check for win.
    while row_top_left < max_rows and col_top_left < max_cols:
        piece = get_piece(board, row_top_left, col_top_left)
        if piece == player:
            adjacent += 1
        else:
            adjacent = 0
        if adjacent >= num_connect:
            return True
        row_top_left += 1
        col_top_left += 1

    # Find top right of diagonal passing through the newly placed piece.
    adjacent = 0
    row_top_right, col_top_right = row, col
    while row_top_right > 0 and col_top_right < max_cols - 1:
        row_top_right -= 1
        col_top_right += 1

    # Loop through top right to bottom left diagonal and check for win.
    while row_top_right < max_rows and col_top_right >= 0:
        piece = get_piece(board, row_top_right, col_top_right)
        if piece == player:
            adjacent += 1
        else:
            adjacent = 0
        if adjacent >= num_connect:
            return True
        row_top_right += 1
        col_top_right -= 1

    return False


#####################################################################################
### You do not need to read or understand the following code for this assignment. ###
#####################################################################################

import sys


def other(player):
    """ Returns the given player's opponent.
    """
    if player == 'X':
        return 'O'
    return 'X'


def play(board, max_rows, max_cols, num_connect):
    max_turns = max_rows * max_cols
    playing = True
    print("Player 'X' starts")
    who = 'X'
    turns = 0

    while True:
        turns += 1
        if turns > max_turns:
            print("No more moves. It's a tie!")
            sys.exit()

        while True:
            try:
                col_index = int(input('Which column, player {}? '.format(who)))
            except ValueError as e:
                print('Invalid input. Please try again.')
                continue

            row_index, board = make_move(board, max_rows, max_cols, col_index, who)

            if row_index != -1:
                break

            print("Oops, you can't put a piece there")

        print_board(board, max_rows, max_cols)

        if check_win(board, max_rows, max_cols, num_connect, row_index, col_index, who):
            print("Player {} wins!".format(who))
            sys.exit()

        who = other(who)


def start_game():
    # Get all parameters for the game from user.
    while True:
        # Get num_connect from user.
        while True:
            try:
                num_connect = int(input('How many to connect (e.g. 4 for Connect 4)? '))
            except ValueError as e:
                print('Invalid input. Please try again.')
                continue
            break

        # Get number of rows for board from user.
        while True:
            try:
                max_rows = int(input('How many rows? '))
            except ValueError as e:
                print('Invalid input. Please try again.')
                continue
            break

        # Get number of columns for board from user.
        while True:
            try:
                max_cols = int(input('How many columns? '))
            except ValueError as e:
                print('Invalid input. Please try again.')
                continue
            break

        if max_rows >= num_connect or max_cols >= num_connect:
            break
        print("Invalid dimensions for connect {0}. Please try again.".format(num_connect))

    board = create_board(max_rows, max_cols)
    play(board, max_rows, max_cols, num_connect)
