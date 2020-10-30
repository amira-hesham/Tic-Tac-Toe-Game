from IPython.display import clear_output

def display_board(board):
    print (board[0],'l',board[1],'l',board[2])
    print('------------')
    print (board[3],'l',board[4],'l',board[5])
    print('------------')
    print (board[6],'l',board[7],'l',board[8])
    print('------------')
test_board = ['X','O','X','O','X','O','X','O','X']
display_board(test_board)
def player_input():
  marker=''
  while not  (marker =='X' or marker =='O'):
    marker= input('Choose x or o: ').upper()
          
  if marker == 'X':
    return ('X','O')

  if marker == 'O':
    return ('O','X')
player_input()
def place_marker(board, marker, position):
  board[position]=marker
  return board
place_marker(test_board,'$',8)
display_board(test_board)
def win_check(board, mark):
    
    return ((board[8] == mark and board[7] == mark and board[6] == mark) or 
            (board[5] == mark and board[4] == mark and board[3] == mark) or
            ( board[2] == mark and board[1] == mark and board[0] == mark) or
            ( board[8] == mark and board[4]== mark and board[0] == mark) or
            ( board[6] == mark and board[4]== mark and board[2] == mark) or
            ( board[8]== mark and board[5]== mark and board[2]== mark) or
            ( board[7]== mark and board[4]== mark and board[1]== mark) or
            ( board[6]== mark and board[3]== mark and board[0]== mark))
win_check(test_board,'X')
import random

def choose_first():
  x = random.randint (0,1)
  if x == 0:
     return 'player 1'
  else:
       return 'player 2'
choose_first()
def space_check(board, position):
    
    return board[position]==' ' 
def full_board_check(board):
  return ' ' in board
def player_choice(board):   
    pos=int(input('enter pos '))
    while space_check (board,pos):
      return pos
      break
    else :
      pos=int(input('enter pos '))
def replay():

  a=input('Do you want to play again ( y or n )')
  if a== 'n' :
    return True 
  else:
    return False
print('Welcome to Tic Tac Toe!')


while True:
    # Reset the board
    board = [' ']*9
    # Choose Markers
    mark1,mark2 = player_input()
    # Who Starts First 
    turn = choose_first()
    print(turn + ' will go first.')
    
    # Asking to Start or  End The Game
    while 1:
        if turn == 'Player 1':
            # Player1's turn.
            mark =mark1
            # Display Board 
            display_board(board)
            # Take His Action
            position=player_choice(board)
            board= place_marker(board,mark,position)
            # Did he Win
            if  win_check(board,mark):
                print('Congratulations! You have won the game!')
                break
            else:
                if not full_board_check(board)  :
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
          mark =mark2
            # Display Board 
          display_board(board)
            # Take His Action
          position=player_choice(board)
          board= place_marker(board,mark,position)
            # Did he Win
          if  win_check(board,mark):
            print('Congratulations! You have won the game!')
            break
          else:
            if not full_board_check(board) :
              print('The game is a draw!')
              break
            else:
              turn = 'Player 1'
    # Replay ?
    if replay():
        break
