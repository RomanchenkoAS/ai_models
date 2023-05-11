"""
Tic Tac Toe AI Player
"""

from random import seed, randint
import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_num = 0
    o_num = 0

    for row in board:
        for cell in row:
            if cell == X:
                x_num += 1
            if cell == O:
                o_num += 1

    if x_num == o_num:
        return X
    elif x_num > o_num:
        return O
    else:
        raise Exception('Invalid board')


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = deepcopy(board)

    # Whose turn is it
    move = player(board_copy)

    # Make a move
    if board_copy[action[0]][action[1]] == EMPTY:
        board_copy[action[0]][action[1]] = move
    else:
        raise Exception("Invalid move")

    return board_copy


def winner(b):
    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError
    players = X, O

    for p in players:
        # Diagonals
        if ((b[0][0] == p and b[1][1] == p and b[2][2] == p) or
                (b[2][0] == p and b[1][1] == p and b[0][2] == p)):
            return p

        for i in range(3):
            # Rows
            if (b[i][0] == p and b[i][1] == p and b[i][2] == p):
                return p
            # Columns
            if (b[0][i] == p and b[1][i] == p and b[2][i] == p):
                return p

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    The game is over when either someone has won, or all the cells are filled
    """
    # True if there is a winner | False if no one has won
    has_winner = bool(winner(board))
    # True if there are empty cells | False if board filled 
    has_empty_cells = False
    for row in board:
        for cell in row:
            if cell == EMPTY:
                has_empty_cells = True
    
    # Someone has won OR no empty cells left
    return has_winner or not has_empty_cells


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def display(board):
    """
    Display current board in debug purposes
    """
    
    print("-----")
    for row in board:
        for cell in row:
            print(cell, "\t", end="")
        print()
    print("-----")


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        # Game is over, no moves left
        return None

    def max_value(board):
        if terminal(board):
            r = utility(board)
            return r

        v = -10

        for action in actions(board):
            v = max(v, min_value(result(board, action)))

        return v

    def min_value(board):
        if terminal(board):
            r = utility(board)
            return r

        v = 10

        for action in actions(board):
            v = min(v, max_value(result(board, action)))

        return v

    # Get possible board outcomes
    states = []
    for action in list(actions(board)):
        states.append((action, result(board, action)))
        
    # Initialize the random number generator
    seed()
    
    if player(board) == X:
        # Need to find maximum value out of the opponent possible moves 
        outcomes = []

        for move, state in states:
            outcomes.append((move, min_value(state)))
        
        good_outcomes = [(move) for (move, outcome) in outcomes if outcome > 0]

        if good_outcomes:
            # If there are any winning moves, pick one by random
            return good_outcomes[randint(0, len(good_outcomes) - 1)]
        else:
            # If not - we will settle for a draw
            good_outcomes = [(move)
                             for (move, outcome) in outcomes if outcome == 0]
            if good_outcomes:
                return good_outcomes[randint(0, len(good_outcomes) - 1)]
            else:
                # well then - anything will do
                return outcomes[0][0]

    elif player(board) == O:
        # Need to find minimum value out of the opponent possible moves
        outcomes = []

        for move, state in states:
            outcomes.append((move, max_value(state)))
            
        good_outcomes = [(move) for (move, outcome) in outcomes if outcome < 0]

        if good_outcomes:
            # If there are any winning moves, pick one by random
            return good_outcomes[randint(0, len(good_outcomes) - 1)]
        else:
            # If not - we will settle for a draw
            good_outcomes = [(move)
                             for (move, outcome) in outcomes if outcome == 0]
            if good_outcomes:
                return good_outcomes[randint(0, len(good_outcomes) - 1)]
            else:
                # well then - anything will do
                return outcomes[0][0]

    else:
        raise Exception("Invalid player distribution")


def main():
    # A simple test case
    
    board = [[X, EMPTY, EMPTY],
             [EMPTY, O, EMPTY],
             [X, EMPTY, EMPTY]]

    print("initial")
    display(board)

    print("Current move: ", player(board))

    result = minimax(board)
    print("result of calculation")
    print(result)

if __name__ == "__main__":
    main()
