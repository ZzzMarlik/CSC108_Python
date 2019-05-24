import builtins

# Check for use of functions print and input.

our_print = print

def disable_print(*args):
    raise Exception("You must not call print anywhere except make_move!")

def disable_input(*args):
    raise Exception("You must not call input anywhere except make_move!")

builtins.print = disable_print
builtins.input = disable_input



import battleship_functions as bf

def is_board(lst):
    """ (object) -> bool
    
    Return True iff lst is a list of list of str.
    
    >>> is_board([['a', 'b', 'c']])
    True
    """
    
    if not isinstance(lst, list):
        return False
        
    for element in lst:
        if not isinstance(element, list):
            return False
        for s in element:
            if not isinstance(s, str):
                return False
    return True
    

# Get the initial value of the constants
constants_before = [1, 10, '-', '.', 'X', 'M']

# Type check battleship_functions.is_win
result = bf.is_win([1, 2, 3])
assert isinstance(result, bool), \
       '''bf.is_win should return a bool, but returned {0}
       .'''.format(type(result))

# Type check battleship_functions.get_view_board
result = bf.get_view_board(5, 6)
assert is_board(result), \
       '''bf.get_view_board should return a list of list of str!'''

# Type check battleship_functions.is_occupied
symbol_board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
# Updated on Nov. 6th @ 5:35pm. Orig call showed a diagonal ship.
# result = bf.is_occupied(0, 0, 1, 1, symbol_board)
result = bf.is_occupied(0, 0, 0, 1, symbol_board)
assert isinstance(result, bool), \
       '''bf.is_occupied should return a bool, but returned {0}
       .'''.format(type(result))

# Type check battleship_functions.update_view_board
view_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
symbol_board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
result = bf.update_view_board(0, 0, view_board, symbol_board)
assert result is None, \
       '''bf.update_view_board should return None, but returned {0}
       .'''.format(type(result))

# Type check battleship_functions.get_moves_info
view_board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
result = bf.get_moves_info(view_board)
assert isinstance(result, list) and all(isinstance(item, int) \
                                        for item in result), \
       '''bf.get_moves_info should return a list of int!'''

# Type check battleship_functions.verify_symbol_board
symbol_board = [['a', 'a', 'a'], ['b', 'b', '.'], ['.', '.', '.']]
ships = ['a', 'b']
sizes = [3, 2]
result = bf.verify_symbol_board(symbol_board, ships, sizes)
assert isinstance(result, bool), \
       '''bf.verify_symbol_board should return a bool, but returned {0}
       .'''.format(type(result))


# Get the final values of the constants
constants_after = [bf.MIN_SHIP_SIZE, bf.MAX_SHIP_SIZE, bf.NOT_KNOWN, bf.EMPTY, 
                   bf.HIT, bf.MISS]


# Check whether the constants are unchanged.
assert constants_before == constants_after, \
       '''Your function(s) modified the value of one or more constants.
       Edit your code so that the values of the constants are not 
       changed by your functions.'''
    
    

our_print("""

The type checker passed.

This means that your functions in battleship_functions.py:
- are named correctly,
- take the correct number of arguments, and
- return the correct types.  

This does NOT mean that the functions are correct!

Be sure to thoroughly test your functions yourself before submitting.

Warning: the typechecker did not check make_move, because that function 
requires user input and produces output. """)

