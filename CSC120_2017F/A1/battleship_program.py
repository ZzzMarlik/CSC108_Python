import random
import os
import battleship_functions as bf

HUMAN_PLAYER = 'You'
NEXT_TURN_MESSAGE = 'Now playing:'
TURN_END_MESSAGE = 'End of turn:'

# ========= Some functions that are called to play the game follow. ======
# ========= You may find it helpful to read and understand all of   ======
# ========= the code below these lines.  Do NOT change any of it!   ======

def display_boards(view_board, symbol_board, player_name, turn_message):
    """ (list of list of str, list of list of str, str, str) -> NoneType

    Precondition: Both view_board and symbol_board contain at least one
    non empty row.

    Display the view_board and the symbol_board belonging to player player_name,
    preceded by a message that includes turn_message.
    """

    print('\n--------------------------')
    print(turn_message, player_name)
    print('--------------------------\n')
    print('view board                 symbol board')
    print()
    gap_between_boards = ' ' * (28 - len(view_board))

    # Display the column numbers
    print(' ', end='')
    for col in range(len(view_board[0])):
        print(col, end='')
    print(gap_between_boards + ' ', end='')
    for col in range(len(view_board[0])):
        print(col, end='')
    print()

    # Display row numbers and cell contents.
    for row in range(len(view_board)):
        print(row, end='')
        for col in range(len(view_board[0])):
            print(view_board[row][col], end='')
        print(gap_between_boards + str(row), end='')
        for col in range(len(symbol_board[0])):
            print(symbol_board[row][col], end='')
        print()

    print()
    print(' ' + bf.HIT + ' means hit.                Upper-case means hit.')
    print(' ' + bf.MISS + ' means miss.')


def get_ship_labels(game_file):
    """ (file open for reading) -> list of str

    Return the ship labels that are found in game_file, a file that is open
    for reading.
    """

    return game_file.readline().split()


def get_ship_sizes(game_file):
    """ (file open for reading) -> list of int

    Return the ship sizes that are found in game_file, a file that is open
    for reading.
    """

    ship_sizes = game_file.readline().split()
    for i in range(len(ship_sizes)):
        ship_sizes[i] = int(ship_sizes[i])

    return ship_sizes


def get_symbol_board(game_file):
    """ (file open for reading) -> list of list of str

    Return the symbol board that is found in game_file, a file that is open
    for reading.
    """

    board = []

    for line in game_file:
        line = line.strip()
        sublist = []
        for char in line:
            sublist.append(char)
        board.append(sublist)

    return board


def get_valid_filename(msg):
    """ (str) -> str

    Prompt the user, using msg, to type the name of a file. This file should
    exist in the same directory as the python file being executed. If a file
    with the given name does not exist, keep re-prompting until the user gives
    a valid filename.  Return the name of that file.
    """

    filename = input(msg)
    while not os.path.exists(filename):
        print('That file does not exist.')
        filename = input(msg)

    return filename


def place_ship(row1, col1, row2, col2, symbol_board, ship_symbol):
    """ (int, int, int, int, list of list of str, str) -> NoneType

    Preconditions:
    - len(ship_symbol) == 1
    - Cell (row1, col1) comes before cell (row2, col2) in the symbol_board
    and both sets of coordinates are valid for this symbol_board.

    Place the ship ship_symbol on the symbol_board from (row1, col1) to
    (row2, col2), inclusive.

    >>> board = [[bf.EMPTY, bf.EMPTY, bf.EMPTY], \
    [bf.EMPTY, bf.EMPTY, bf.EMPTY], [bf.EMPTY, bf.EMPTY, bf.EMPTY]]
    >>> place_ship(0, 0, 1, 0, board, 'd')
    >>> board
    [['d', '.', '.'], ['d', '.', '.'], ['.', '.', '.']]
    >>> place_ship(2, 1, 2, 2, board, 'z')
    >>> board
    [['d', '.', '.'], ['d', '.', '.'], ['.', 'z', 'z']]
    """

    if row1 == row2:
        # place the ship horizontally
        for col in range(col1, col2 + 1):
            symbol_board[row1][col] = ship_symbol
    elif col1 == col2:
        # place the ship vertically
        for row in range(row1, row2 + 1):
            symbol_board[row][col1] = ship_symbol


def print_sunk_message(ship_size, ship_label):
    """ (int, str) -> NoneType

    Print a message telling player that a ship_size ship with ship_label
    has been sunk.
    """

    print('The size {0} {1} ship has been sunk!'.format(ship_size, ship_label))


def update_after_hit(row, col, symbol_board, ships, sizes, hits_list):
    """ (int, int, list of list of str, list of str, list of int, list of int)
          -> NoneType

    Modify symbol_board and hits_list to account for a hit of the cell
    with row position row and column position col. Report a sunk ship.
    """

    ship_index = ships.index(symbol_board[row][col])
    hits_list[ship_index] = hits_list[ship_index] - 1

    if hits_list[ship_index] == 0:
        print_sunk_message(sizes[ship_index], ships[ship_index])

    symbol_board[row][col] = symbol_board[row][col].upper()


def verify_game_parameters(board, ships, sizes):
    """ (list of list of str, list of str, list of int) -> bool

    Return True if and only if board is rectangular with at least one cell,
    at most bf.MAX_BOARD_SIZE cells per row and at most bf.MAX_BOARD_SIZE rows,
    the number of ship labels is the same as the number of ship sizes,
    there is at least one ship, all ships have a valid size, and all ships
    have a valid, unique label.

    >>> board = [['.', 'b', '.'], ['.', 'b', '.'], ['a', 'a', 'a']]
    >>> ships = ['a', 'b']
    >>> sizes = [3, 2]
    >>> verify_game_parameters(board, ships, sizes)
    True
    >>> board = []
    >>> ships = ['a', 'd', 'h', 'i', 'n']
    >>> sizes = [1, 1, 1, 2, 1]
    >>> verify_game_parameters(board, ships, sizes)
    False
    """

    # Confirm that the board has a valid number of rows.
    if len(board) == 0 or len(board) > bf.MAX_BOARD_SIZE:
        return False

    # Confirm that the board has a valid number of columns.
    if len(board[0]) == 0 or len(board[0]) > bf.MAX_BOARD_SIZE:
        return False

    # Confirm that all rows have the same number of columns.
    num_columns = len(board[0])
    for row in range(len(board)):
        if len(board[row]) != num_columns:
            return False

    # Confirm that number of ships is the same as the number of ship sizes.
    if len(ships) != len(sizes):
        return False

    # Confirm that the ships and sizes lists are not empty.
    if len(ships) == 0:
        return False

    # Confirm that each ship has a valid size.
    for i in range(len(sizes)):
        if sizes[i] < bf.MIN_SHIP_SIZE or sizes[i] > bf.MAX_SHIP_SIZE:
            return False

    # Confirm that each ship has a valid unique label.
    for i in range(len(ships)):
        if len(ships[i]) > 1:
            return False
        else:
            for j in range(len(ships)):
                if i != j and ships[i] == ships[j]:
                    return False

    return True


def make_computer_symbol_board(board_rows, board_columns, ships, sizes):
    """ (int, int, list of str, list of int) -> list of list of str

    Return a new board_rows by board_columns symbol board with the ship symbols
    in ships and ship sizes in sizes placed randomly on the symbol board,
    horizontally or vertically, and the rest of the cells bf.EMPTY.
    """

    # make a board_rows by board_columns board that is entirely bf.EMPTY
    board = []
    for row in range(board_rows):
        board.append([])
        for column in range(board_columns):
            board[row].append(bf.EMPTY)

    for index in range(len(ships) - 1, -1, -1):
        # get the ship symbol and its size
        placed = False
        ship = ships[index]
        ship_size = sizes[index]

        while not placed:

            # randomly generate a location at which to place the ship
            start_row = random.randint(0, board_rows - 1)
            start_col = random.randint(0, board_columns - 1)

            # randomly determine whether to place horizontally or vertically
            direction = random.randint(0, 1)

            if direction == 0:
                # calculate the (row, col) coordinates for horizontal placement
                end_row = start_row
                end_col = start_col + ship_size - 1
            elif direction == 1:
                # calculate the (row, col) coordinates for vertical placement
                end_row = start_row + ship_size - 1
                end_col = start_col

            # If the start and end locations are within the bounds of the board
            # and the cells are not occupied, place the ship.
            if (bf.in_bounds(start_row, start_col, board_rows,
	                     board_columns) and \
                bf.in_bounds(end_row, end_col, board_rows, board_columns) \
                and not bf.is_occupied(start_row, start_col, end_row, end_col,
                                    board)):
                place_ship(start_row, start_col, end_row, end_col, board, ship)
                placed = True

    return board


def main_single_player():
    """ () -> NoneType

    A single player game with no opponent.  This may be used for the purpose
    of testing our functions.
    """

    filename = get_valid_filename('Game filename: ')
    game_file = open(filename)
    ships = get_ship_labels(game_file)
    sizes = get_ship_sizes(game_file)
    symbol_board = get_symbol_board(game_file)
    if ( not verify_game_parameters(symbol_board, ships, sizes) or
         not bf.verify_symbol_board(symbol_board, ships, sizes)):
        print('The supplied game is not valid.  Game exiting.')
        return
    view_board = bf.get_view_board(len(symbol_board), len(symbol_board[0]))
    display_boards(view_board, symbol_board, HUMAN_PLAYER, NEXT_TURN_MESSAGE)

    hits_list = sizes[:]

    while not bf.is_win(hits_list):

        print()
        print('Take a turn.')
        [row, col] = bf.make_move(view_board)

        print()
        if bf.is_hit(row, col, symbol_board):
            print('You hit a ship!')
            update_after_hit(row, col, symbol_board, ships, sizes, hits_list)
        else:
            print('You missed!')

        bf.update_view_board(row, col, view_board, symbol_board)
        display_boards(view_board, symbol_board, HUMAN_PLAYER,
                       NEXT_TURN_MESSAGE)

    print()
    moves_info = bf.get_moves_info(view_board)
    print('You won in', moves_info[0:1], 'move(s) with', moves_info[1:2],
          'hit(s) and', moves_info[2:3], 'miss(es)!')


def make_computer_move(view_board):
    """ (list of list of str) -> list of int

    Return the randomly generated row and column of the computer's next move.
    """

    board_rows = len(view_board)
    board_columns = len(view_board[0])

    row = random.randint(0, board_rows - 1)
    col = random.randint(0, board_columns - 1)

    while bf.is_not_unknown(row, col, view_board):
        row = random.randint(0, board_rows - 1)
        col = random.randint(0, board_columns - 1)

    return [row, col]


def main_versus_computer():
    """ () -> NoneType

    Play the game with a single player vs. the computer.
    """

    filename = get_valid_filename('Game filename: ')
    game_file = open(filename)
    ships = get_ship_labels(game_file)
    sizes = get_ship_sizes(game_file)
    symbol_board_player = get_symbol_board(game_file)
    if ( not verify_game_parameters(symbol_board_player, ships, sizes) or
         not bf.verify_symbol_board(symbol_board_player, ships, sizes)):
        print('The supplied game is not valid.  Game exiting.')
        return
    board_rows = len(symbol_board_player)
    board_columns = len(symbol_board_player[0])
    view_board_player = bf.get_view_board(board_rows, board_columns)
    hits_player = sizes[:]

    symbol_board_computer = make_computer_symbol_board(board_rows,
                                                       board_columns, ships,
                                                       sizes)
    view_board_computer = bf.get_view_board(board_rows, board_columns)
    hits_computer = sizes[:]

    player_turn = True

    while not bf.is_win(hits_player) and not bf.is_win(hits_computer):

        print('\n\n')
        print(':' * 40)
        print()
        if player_turn:
            player_name = HUMAN_PLAYER
            opponent_symbol_board = symbol_board_computer
            symbol_board = symbol_board_player
            view_board = view_board_player
            display_boards(view_board, symbol_board, player_name,
                           NEXT_TURN_MESSAGE)
            print('\nIt is your turn!')
            [row, col] = bf.make_move(view_board)
            hits_list = hits_player
        else:
            player_name = 'Computer'
            opponent_symbol_board = symbol_board_player
            view_board = view_board_computer
            symbol_board = symbol_board_computer
            display_boards(view_board, symbol_board, player_name,
                           NEXT_TURN_MESSAGE)
            [row, col] = make_computer_move(view_board)
            hits_list = hits_computer

        print()
        if bf.is_hit(row, col, opponent_symbol_board):
            print(player_name, 'hit a ship!')
            update_after_hit(row, col, opponent_symbol_board, ships, sizes,
	                     hits_list)
        else:
            print(player_name, 'missed!')
        print()

        bf.update_view_board(row, col, view_board, opponent_symbol_board)
        display_boards(view_board, symbol_board, player_name, TURN_END_MESSAGE)
        input('\nPress enter.\n')
        player_turn = not player_turn

    print()
    if bf.is_win(hits_player):
        moves_info = bf.get_moves_info(view_board_player)
        print('You won in', moves_info[0:1], 'move(s) with', moves_info[1:2],
	      'hit(s) and', moves_info[2:3], 'miss(es)!')
    else:
        moves_info = bf.get_moves_info(view_board_computer)
        print('The computer won in', moves_info[0:1], 'move(s) with',
	      moves_info[1:2], 'hit(s) and', moves_info[2:3], 'miss(es)!')


if __name__ == '__main__':

    prompt = 'Enter s for single-player mode or c to play against the computer:'
    game_mode = input(prompt + ' ')

    if game_mode == 's':
        main_single_player()
    elif game_mode == 'c':
        main_versus_computer()
    else:
        print('Error! You entered an invalid option:', game_mode)
