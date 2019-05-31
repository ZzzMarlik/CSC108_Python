"""The student written functions for the Connect-N game.
"""

# Do not change these constants!
EMPTY = '-'
DOWN = 'down'
ACROSS = 'across'
DOWN_RIGHT = 'down_right'
DOWN_LEFT = 'down_left'
MAX_BOARD_SIZE = 9


def between(value: int, min_value: int, max_value: int) -> bool:
    """Return True if and only if value is between min_value and
    max_value, inclusive.

    Precondition: min_value <= max_value

    >>> between(1, 0, 2)
    True
    >>> between(0, 2, 3)
    False
    """
    return min_value <= value <= max_value
# Implement the rest of the required functions here.

def game_board_full(board: str) -> bool:
    """Return True if and only if all of the cells in the game
    board have been chosen.
    
    >>> game_board_full('abcd')
    True
    >>> game_board_full('abc-')
    False
    """
    return EMPTY not in board

def get_board_size(board: str) -> int:
    """Return the length of each side of the given game board.
    
    >>> get_board_size('abcd')
    2
    >>> get_board_size('---------')
    3
    """
    return int(len(board)**(1/2))

def create_empty_board(size: int) -> str:
    """Return a string for storing information about a game board
    whose size is given by the parameter.
    
    >>> create_empty_board(2)
    '----'
    >>> create_empty_board(3)
    '---------'
    """
    return EMPTY * (size ** 2)
    
def get_str_index(row: int, col: int, size: int) -> int:
    """Return the index in the string representation of the game board
    corresponding to the given row and column indices.
    
    >>> get_str_index(2, 1, 2)
    2
    >>> get_str_index(3, 3, 4)
    10
    """
    return (row - 1) * size + (col - 1)

def make_move(char: str, row: int, col: int, board: str) -> str:
    """Return the game board that results when the given symbol is
    placed at the given cell position in the given game board.
    
    >>> make_move('A', 1, 1, '----')
    'A---'
    >>> make_move('B', 2, 2, 'A---')
    'A--B'
    """
    size = get_board_size(board)
    index = get_str_index(row, col, size)
    return board[:index] + char + board[index + 1:]

def get_increment(direction: str, size: int) -> int:
    """Return the difference between the str indices of two adjacent cells
    on a line that goes in the direction specified by the first parameter.
    
    >>> get_increment(DOWN, 3)
    3
    >>> get_increment(ACROSS, 3)
    1
    >>> get_increment(DOWN_RIGHT, 3)
    4
    >>> get_increment(DOWN_LEFT, 3)
    2
    """
    if direction == DOWN:
        return size
    elif direction == ACROSS:
        return 1
    elif direction == DOWN_RIGHT:
        return size + 1
    else:
        return size - 1

def get_last_index(row: int, col: int, direction: str, size: int) -> int:
    """Return the str index of the last cell in a line that begins at the
    specified location and goes in the specified direction all the way to
    the game board boundary, on a game board of the specified size.
    
    >>> get_last_index(1, 1, DOWN, 2)
    2
    >>> get_last_index(1, 1, ACROSS, 2)
    1
    >>> get_last_index(1, 1, DOWN_RIGHT, 2)
    3
    >>> get_last_index(1, 1, DOWN_LEFT, 2)
    0
    """
    if direction == DOWN:
        return get_str_index(size, col, size)
    elif direction == ACROSS:
        return get_str_index(row, size, size)
    elif direction == DOWN_RIGHT:
        if row == 1:
            return get_str_index(size - col + 1, size, size)
        else:
            return get_str_index(size, size - row + 1, size)
    else:
        return get_str_index(col, row, size)
        
if __name__ == '__main__':
    import doctest

    # Uncomment this line to run the examples in your docstrings.
    doctest.testmod()
