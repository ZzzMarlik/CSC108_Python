"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles_small.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if puzzle is the same as view.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    """
    # put the function body here
    return puzzle == view

def game_over(puzzle: str, view: str, selection: str) -> bool:
    """Return True if puzzle is the same as view or the selection is QUIT.

    >>> game_over('banana', 'banana', 'C')
    True
    >>> game_over('apple', 'a^^le', 'Q')
    True
    """
    return (puzzle == view) or (selection == QUIT)

def bonus_letter(puzzle: str, view: str, letter: str) -> bool:
    """Return True if and only if the letter appears in the puzzle
    but not in its view.

    >>> bonus_letter('banana', 'banana', 'a')
    False
    >>> bonus_letter('apple', 'a^^le', 'p')
    True
    """
    return (letter in puzzle) and (letter not in view)

def update_letter_view(puzzle: str, view: str, index: int, guess: str) -> str:
    """Return a single character string representing the next view
    of the character at the given index.

    >>> update_letter_view('apple', 'a^^l^', 2, 'x')
    '^'
    >>> update_letter_view('apple', 'a^^l^', 2, 'p')
    'p'
    """
    if puzzle[index] == guess:
        return puzzle[index]
    else:
        return view[index]

def calculate_score(current_score: int, occurrences: int, option: str) -> int:
    """ Return the new score by adding CONSONANT_POINTS per occurrence of the
    letter to the current score if the letter is a consonant, or by deducting
    the VOWEL_PRICE from the score if the letter is a vowel.

    >>> calculate_score(4, 2, 'C')
    6
    >>> calculate_score(4, 1, 'V')
    3
    """
    if option == CONSONANT:
        return current_score + (occurrences * CONSONANT_POINTS)
    if option == VOWEL:
        return current_score - VOWEL_PRICE

def next_player(current_player: str, occureences: int) -> str:
    """Return the next player depends on the number of occurrences in the
    puzzle of the letter last chosen by the current player.

    >>> next_player(PLAYER_ONE, 2)
    "Player One"
    >>> next_player(PLAYER_ONE, 0)
    "Player Two"
    """
    if occureences > 0:
        return current_player
    else:
        if current_player == PLAYER_ONE:
            return PLAYER_TWO
        else:
            return PLAYER_ONE
