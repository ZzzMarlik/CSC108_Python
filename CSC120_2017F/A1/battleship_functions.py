# The following are constants.  A constant is a variable whose value does not
# change. You can use these constants anywhere in this module.
# Do NOT modify or move these constants.

MIN_SHIP_SIZE = 1
MAX_SHIP_SIZE = 10
MAX_BOARD_SIZE = 10
NOT_KNOWN = '-'
EMPTY = '.'
HIT = 'X'
MISS = 'M'

# ===================== Helper Functions =====================

# Here are a few helper functions that we have written and used elsewhere in the
# supplied starter code.  You may make use of these functions in the function(s)
# that you write.

def is_hit(row, col, symbol_board):
    """ (int, int, list of list of str) -> bool

    Return True if and only if symbol_board cell with row position row and
    column position col is not EMPTY.

    >>> board = [[EMPTY, 'b', EMPTY], [EMPTY, 'b', EMPTY],\
                 [EMPTY, EMPTY, EMPTY]]
    >>> is_hit(0, 1, board)
    True
    >>> is_hit(2, 2, board)
    False
    """

    return symbol_board[row][col] != EMPTY


def is_not_unknown(row, col, view_board):
    """ (int, int, list of list of str) -> bool

    Return True if and only if view_board cell with row position row and
    column position col is not NOT_KNOWN.

    >>> board = [['a', NOT_KNOWN], [NOT_KNOWN, 'b']]
    >>> is_not_unknown(1, 1, board)
    True
    >>> is_not_unknown(0, 1, board)
    False
    """

    return view_board[row][col] != NOT_KNOWN


def get_move_from_player():
    """ () -> list of int

    Return a two item list that contains the player's move, or [-1,-1] if
    the player entered a move that cannot be interpreted.
    """

    row = input('Please enter the row: ')
    col = input('Please enter the column: ')

    if row.isdigit() and col.isdigit():
        return [int(row), int(col)]
    else:
        return [-1, -1]


def in_bounds(row, col, board_rows, board_columns):
    """ (int, int, int, int) -> bool

    Return True iff row and col are both between 0 (inclusive) and board_rows or
    board_columns respectively (non-inclusive).

    >>> in_bounds(2, 9, 10, 12)
    True
    >>> in_bounds(2, 9, 9, 8)
    False
    """

    return 0 <= row < board_rows and 0 <= col < board_columns


# ===================================================================
#     Do NOT modify or delete or move ANYTHING above this comment
# ===================================================================

# Add any helper functions that you write below.

def check_direction(lst):
    """ (list of list of int) -> bool

    Return True iff the lst contains all horizontal or vertical ships index.

    >>> check_direction([[0, 0], [0, 1]])
    True
    >>> check_direction([[0, 0], [1, 1]])
    False
    """
    flag1 = True
    flag2 = True
    for i in range(len(lst)):
        if lst[i][0] != lst[0][0]:
            flag1 = False
    for i in range(len(lst)):
        if lst[i][1] != lst[0][1]:
            flag2 = False
    return flag1 or flag2

# ===================== Required Functions =====================

def is_win(lst):
    """ (list of int) -> bool

    Return True if all elements of the list are 0, and False otherwise.

    >>> is_win([0, 0, 0])
    True
    >>> is_win([1, 0])
    False
    """

    for item in lst:
        if item != 0:
            return False
    return True

def get_view_board(num_row, num_col):
    """ (int, int) -> list of list of str

    Return a board with the specified number of rows and columns,
    where each cell of the board contains the NOT_KNOWN symbol.

    >>> get_view_board(2, 1)
    [['-'], ['-']]
    >>> get_view_board(1, 2)
    [['-', '-']]
    """

    acc = []
    for i in range(num_row):
        acc.append([])
        for j in range(num_col):
            acc[i].append(NOT_KNOWN)
    return acc

def is_occupied(row_1, col_1, row_2, col_2, symbol_board):
    """ (int, int, int, int, list of list of str) -> bool

    Return True if the path from the first row and column cell to the second
    row and column cell, including those two cells, is not completely empty,
    and return False otherwise.

    >>> is_occupied(0, 0, 0, 1, [['.', '.', '.'], ['.', 'x', '.']])
    False
    >>> is_occupied(0, 1, 1, 1, [['.', '.', '.'], ['.', 'x', '.']])
    True
    """
    if row_1 == row_2:
        if col_1 > col_2:
            i = 0
            while i <= col_1 - col_2:
                if symbol_board[row_1][col_2 + i] != EMPTY:
                    return True
                i += 1
            return False
        else:
            i = 0
            while i <= col_2 - col_1:
                if symbol_board[row_1][col_1 + i] != EMPTY:
                    return True
                i += 1
            return False
    if col_1 == col_2:
        size = abs(row_1 - row_2)
        if row_1 > row_2:
            for i in range(size + 1):
                if symbol_board[row_2 + i][col_1] != EMPTY:
                    return True
            return False
        else:
            for i in range(size + 1):
                if symbol_board[row_1 + i][col_1] != EMPTY:
                    return True
            return False

def update_view_board(row, col, view_board, symbol_board):
    """(int, int, list of list of str, list of list of str) -> NoneType

    Set the element of that cell in the view board to HIT or MISS using
    the corresponding cell from the symbol board.

    >>> view_board = [[NOT_KNOWN], [NOT_KNOWN]]
    >>> symbol_board = [[EMPTY], ['a']]
    >>> update_view_board(0, 0, view_board, symbol_board)
    >>> view_board
    [['M'], ['-']]
    >>> update_view_board(1, 0, view_board, symbol_board)
    >>> view_board
    [['M'], ['X']]
    """

    if symbol_board[row][col] != EMPTY:
        view_board[row][col] = HIT
    else:
        view_board[row][col] = MISS

def get_moves_info(view_board):
    """ (list of list of str) -> list of int

    Return a 3-element list that contains the number of moves made so far
    in the board, the number of moves that were successful, and the number of
    unsuccessful moves.

    >>> get_moves_info([['-'],['-']])
    [0, 0, 0]
    >>> get_moves_info([['M'],['X']])
    [2, 1, 1]
    """
    num_moves = 0
    num_hits = 0
    num_miss = 0
    for i in range(len(view_board)):
        for j in range(len(view_board[i])):
            if view_board[i][j] != NOT_KNOWN:
                num_moves += 1
                if view_board[i][j] == HIT:
                    num_hits += 1
                if view_board[i][j] == MISS:
                    num_miss += 1
    return [num_moves, num_hits, num_miss]

# For make_move(), we have given you the required function header and docstring,
# and have supplied suggestions for reading moves and printing an error message.
# Complete the function body.

def make_move(view_board):
    """ (list of list of str) -> list of int

    Return a list containing a valid row and column for view_board.
    """
    acc = get_move_from_player()
    while not in_bounds(acc[0], acc[1], len(view_board), len(view_board[0]))\
            or view_board[acc[0]][acc[1]] != NOT_KNOWN:
        print('Invalid move!')
        acc = get_move_from_player()
    return acc


# Complete the other required functions before completing verify_symbol_board().
# For verify_symbol_board(), we have given you the header, the start of the
# docstring, and a function body that always returns True.  This will allow you
# to play the game with valid game boards.  You need to complete the docstring
# and replace the given function body with a correct function body, so that
# invalid symbol boards are detected.

def verify_symbol_board(board, ships, sizes):
    """ (list of list of str, list of str, list of int) -> bool

    Preconditions: len(ships) == len(sizes) and len(ships) > 0,
                    board != [] and each row in board has length len(board[0]).
                    Each ship in ships has a valid unique label and
                    a valid size in sizes.

    Return True if the potential symbol board is a valid symbol board.

    >>> board = [['a', 'a'], ['.', '.'], ['.', 'b']]
    >>> ships = ['a', 'b']
    >>> sizes = [2, 1]
    >>> verify_symbol_board(board, ships, sizes)
    True
    >>> board = [['a', '.'], ['.', 'a'], ['.', 'b']]
    >>> verify_symbol_board(board, ships, sizes)
    False
    """
    record = {}
    for i in range(len(board)): #collect info from the given board
        for j in range(len(board[i])):
            if board[i][j] != EMPTY:
                if board[i][j] in ships: # check for invalid ship
                    if board[i][j] in record:
                        record[board[i][j]].append([i, j])
                    else:
                        record[board[i][j]] = [[i, j]]
                else:
                    return False
    for key in record:
        if len(record[key]) != sizes[ships.index(key)]: # check for the nums of ships
            return False
        else:
            if not check_direction(record[key]): # check directions of ships' placements
                return False
    for item in ships: # extra check for the nums of ships
        if item not in record:
            return False
    return True
