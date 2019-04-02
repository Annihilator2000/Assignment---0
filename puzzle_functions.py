""" Where's That Word? functions. """

# The constant describing the valid directions. These should be used
# in functions get_factor and check_guess.
UP = 'up'
DOWN = 'down'
FORWARD = 'forward'
BACKWARD = 'backward'

# The constants describing the multiplicative factor for finding a
# word in a particular direction.  This should be used in get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

# The constant describing the threshold for scoring. This should be
# used in get_points.
THRESHOLD = 5
BONUS = 12

# The constants describing two players and the result of the
# game. These should be used as return values in get_current_player
# and get_winner.
P1 = 'player one'
P2 = 'player two'
P1_WINS = 'player one wins'
P2_WINS = 'player two wins'
TIE = 'tie game'

# The constant describing which puzzle to play. Replace the 'puzzle1.txt' with
# any other puzzle file (e.g., 'puzzle2.txt') to play a different game.
PUZZLE_FILE = 'puzzle1.txt'


# Helper functions.  Do not modify these, although you are welcome to
# call them.

def get_column(puzzle: str, col_num: int) -> str: 
    """Return column col_num of puzzle.

    Precondition: 0 <= col_num < number of columns in puzzle

    >>> get_column('abcd\nefgh\nijkl\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def get_row_length(puzzle: str) -> int: 
    """Return the length of a row in puzzle.
    """

    return len(puzzle.split('\n')[0])


def contains(text1: str, text2: str) -> bool: 
    """Return whether text2 appears anywhere in text1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return text2 in text1


# Implement the required functions below.
def get_current_player(player_one_turn: bool) -> str: 
    """Return 'player one' if player_one_turn is True; otherwise, return
    'player two'.

    >>> get_current_player(True)
    'player one'
    >>> get_current_player(False)
    'player two'
    """

    if player_one_turn is True:
        return P1
    else:
        return P2

    
    # Complete this function.
def get_winner(player_one_score: int, player_two_score: int) -> str: 
    """Return 'player one wins' or 'player two wins' based on whose
    score is highest;otherwise returns 'tie game' if score
    of both the players is equal.

    >>> get_winner(24, 48)
    'player two wins'
    >>> get_winner(36, 20)
    'player one wins'
    >>> get_winner(20, 20)
    'tie game'
    """

    if player_one_score > player_two_score:
        return P1_WINS
    elif player_two_score > player_one_score:
        return P2_WINS
    else:
        return TIE


def reverse(string: str) -> str: 
    """Return a reversed copy of string entered.

    >>>reverse(buffalo)
    'olaffub'
    """

    return string[::-1]


def get_row(puzzle: str, row_num: int) -> str: 
    """Return the letters in the row corresponding
    to the row number, excluding the newline
    character.

    Precondition: 0 <= row_num < number of rows in puzzle

    >>>get_row('abcd\nefgh\nijkl\n', 1)
    'efgh'
    """
    
    return (puzzle.split('\n')[row_num])


def get_factor(direction: str) -> int: 
    """Return the multiplicative factor associated
    with the input direction.

    >>>get_factor('up')
    4
    >>>get_factor('down')
    2
    """

    if direction == UP:
        return UP_FACTOR
    elif direction == DOWN:
        return DOWN_FACTOR
    elif direction == FORWARD:
        return FORWARD_FACTOR
    else:
        return BACKWARD_FACTOR


def get_points(direction: str, num_words_left: int) -> int:   
    """ Return the points that would be earned if a word is
    guessed correctly in a particular direction.

    >>>get_points('up', 2)
    32
    >>>get_points('down',1)
    30
    """

    factor = get_factor(direction)
    if num_words_left >= THRESHOLD:
        return THRESHOLD * factor
    elif THRESHOLD > num_words_left > 1:
        return (2 * THRESHOLD - num_words_left) * factor
    else:
        return (2 * THRESHOLD - num_words_left) * factor + BONUS


def check_guess(puzzle: str, direction: str, guessed_word: str, \
                location_num: int, num_words_left: int) -> int: 
    """Return the points earned for a word guessed correctly
    in the puzzle at a particular location(row or column) and
    in a particular direction;otherwise returns the integer
    0.

    >>>check_guess('abcd\nefgh\nijkl\n', 'forward', 'bcd', 0, 5)
    5
    >>>check_guess('abcd\nefgh\nijkl\n', 'forward', 'bcd', 2, 5)
    0
    >>>check_guess('abcd\nefgh\nijkl\n', 'backward', 'bcd', 0, 5)
    0
    """

    if direction == DOWN: 
        if contains(get_column(puzzle, location_num), guessed_word) is True:
            return get_points(direction, num_words_left)
        else:
            return 0
    elif direction == UP: 
        if contains(get_column(puzzle, location_num), \
                    reverse(guessed_word)) is True:
            return get_points(direction, num_words_left)
        else:
            return 0
    elif direction == FORWARD:
        if contains(get_row(puzzle, location_num), guessed_word) is True:
            return get_points(direction, num_words_left)
        else:
            return 0
    else:
        if contains(get_row(puzzle, location_num), \
                    reverse(guessed_word)) is True:
            return get_points(direction, num_words_left)
        else:
            return 0
    
