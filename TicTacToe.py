import random

# get players' names
player = {}
player['a'] = input('Player A, what is your name?  ')
player['b'] = input('Player B, what is your name?  ')

# print welcome message
print()
print("Hello {a} and {b}!  I hope you're ready to have some fun!!!".format(**player))
print()
print("{a} you will be X's".format(**player))
print("{b} you will be O's".format(**player))
print()
print('To make a move, type in the column and row for the spot your want.')
print('For example "a1" for column a and row 1')
print()

# select who goes first
whos_turn = random.choice(['a', 'b'])
print('Randomly selected, {} will go first'.format(player[whos_turn]))
print()
if whos_turn == "a":
    whos_turn_mark = 'X'
else:
    whos_turn_mark = 'O'

# initializations
table_vals = {'a1': ' ', 'a2': ' ', 'a3': ' ', 'b1': ' ', 'b2': ' ', 'b3': ' ', 'c1': ' ', 'c2': ' ', 'c3': ' '}
winner = None
moves = []
ways_to_win = [['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
               ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],
               ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']]


def print_board():
    # print whole board
    print('    a   b   c')
    print()
    print('1   {a1} | {b1} | {c1}'.format(**table_vals))
    print('    ' + chr(8212) + '   ' + chr(8212) + '   ' + chr(8212))
    print('2   {a2} | {b2} | {c2}'.format(**table_vals))
    print('    ' + chr(8212) + '   ' + chr(8212) + '   ' + chr(8212))
    print('3   {a3} | {b3} | {c3}'.format(**table_vals))
    print()



def move_valid(move):
    # check proper syntax, letter then number
    if move[0] < move[1]:
        print('Move must be in form letter then number.  For example "a3"')
        return False

    # make sure move is in range
    if move[0] > 'c' or move[1] > '3':
        print('Move is out of range. Please select again my friend.')
        return False

    # check to see if spot has already been taken
    if move in moves:
        print('That spot is already taken.  Please select again.')
        return False

    return True


def winner_check():
    for x in ways_to_win:

        line_check = ''

        for y in x:
            line_check += table_vals[y]
        if line_check == 'XXX':
            return 'a'
        elif line_check == 'OOO':
            return 'b'
    else:
        return None


def switch_player_mark(whos_turn, whos_turn_mark):
    if whos_turn == 'a':
        whos_turn = 'b'
    else:
        whos_turn = "a"

    if whos_turn_mark == "X":
        whos_turn_mark = "O"
    else:
        whos_turn_mark = "X"

    return whos_turn, whos_turn_mark


while winner == None:

    print_board()
    move = input('{0} please place your {1}.  Location: '.format(player[whos_turn], whos_turn_mark))
    move = move.lower()
    print()

    if move_valid(move):
        moves.append(move)
        table_vals[move] = whos_turn_mark

        # check to see if we have a winner
        winner = winner_check()
        if winner == 'a' or winner == 'b':
            break
    else:
        continue

    whos_turn, whos_turn_mark = switch_player_mark(whos_turn, whos_turn_mark)

print("and the winner is....{w}".format(w = player[winner]))