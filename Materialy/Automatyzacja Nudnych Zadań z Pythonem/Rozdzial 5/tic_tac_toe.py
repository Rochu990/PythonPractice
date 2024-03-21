
the_board = {'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ',
             'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
             'low-L' : ' ', 'low-M' : ' ', 'low-R' : ' '}

def print_Board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    

print_Board(the_board)

turn = 'X'
for i in range(9):
    print_Board(the_board)
    print('Ruch gracza ' + turn + '. W którym polu stawiasz znak?')
    move = input()
    the_board[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'

print_Board(the_board)