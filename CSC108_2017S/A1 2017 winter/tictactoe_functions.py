EMPTY = '-'


def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.3, 0.5, 2)
    True
    >>> is_between(0, 2, 3)
    False
    """
    return min_value <= value <= max_value


def game_board_full(game_board):
    """ (str) -> bool

    Return True if and only if the game_borad doesn't contains empty cell.

    >>> game_board_full('X-OX')
    False
    >>> game_board_full('XOOX')
    True
    """
    return not (EMPTY in game_board)


def get_board_size(game_board):
    """ (str) -> int

    Precondition: the length of the paramater is a perfect square.

    Return the length of each side of the given game_board.

    >>> get_board_size('X-OX')
    2
    >>> get_board_size('XOX-OXOX-')
    3
    """
    return int(len(game_board) ** 0.5)


def make_empty_board(size):
    """ (int) -> str

    Precondition: 1 <= size <= 9

    Return a string for storing information about a tic-tac-toe game board
    whose size is given by the parameter.

    >>> make_empty_board(2)
    '----'
    >>> make_empty_board(3)
    '---------'
    """
    return EMPTY * (size ** 2)


def get_str_index(row_index, col_index, size):
    """ (int, int, int) -> int

    Precondition: 1 <= row_inded, col_index, size <= 9

    Return the index of the cell in the string representation of the game board
    corresponding to the given row_index and col_index and game board size.

    >>> get_str_index(2, 3, 4)
    6
    >>> get_str_index(9, 9, 9)
    80
    """
    return (row_index - 1) * size + (col_index - 1)


def make_move(symbol, row_index, col_index, game_board):
    """(str, int, int, str) -> str

    Return the tic-tac-toe game board that results when the given symbol is
    placed at the given cell position formed by row_index and col_index in the
    given tic-tac-toe game board.

    >>> make_move('X', 1, 1, '-OX-OXOX-')
    'XOX-OXOX-'
    >>> make_move('O', 2, 3, '---------')
    '-----O---'
    """
    i = get_str_index(row_index, col_index, get_board_size(game_board))
    return game_board[:i] + symbol + game_board[i + 1:]


def extract_line(game_board, direction, number):
    """ (str, str, int) -> str

    Return one line from the game_board by given direction and numbe.

    >>> extract_line('ABCD', 'down', 2)
    'BD'
    >>> extract_line('ABCD', 'across', 2)
    'CD'
    >>> extract_line('A', 'down_diagonal', 2)
    'A'
    >>> extract_line('A', 'up_diagonal', 2)
    'A'
    """
    s = get_board_size(game_board)
    if direction == 'down' and number <= s:
        d = get_str_index(1, number, s)
        return game_board[d:d + s * (s - 1) + 1:s]
    if direction == 'across' and number <= s:
        d = get_str_index(number, 1, s)
        return game_board[d:d + s]
    if direction == 'down_diagonal':
        return game_board[0:s ** 2:s + 1]
    if direction == 'up_diagonal':
        if s == 1:
            return game_board
        else:
            i = get_str_index(s, 1, s)
            e = get_str_index(1, s, s)
            return game_board[i:e - 1:1 - s]
