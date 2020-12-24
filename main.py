# -----Global Variables -----

# Game board
board = ["-", "-", "-","-", "-", "-", "-", "-", "-"]


# If game is still going
game_still_going = True

# who won? or tie?
winner = None

# whoes turn is it
current_player = "X"


# Display a game
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])


# Play a game tic tac toe
def play_game():

  # Display initial board
  display_board()

  # while the game is still going
  while game_still_going:

    # handle a single turn of an arbitrary player
    handle_turn(current_player)

    # check if the game has ended
    check_if_game_over()

    # flip to the other player
    flip_player()

    # The game has ended 
    if winner == "X" or winner == "0":
      print(winner + " won.")
    elif winner == None:
      print("Tie.")


# handle a single turn of an arbitrary player
def handle_turn(player):

  print(player + "'s turn.'")
  position = input("Choose a position from 1-9: ")


  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")

    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  board[position] = player

  display_board()


def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():

  # Set up global veriables
  global winner

  # check rows T/F
  row_winner = check_rows()
  # check compile T/F
  column_winner = check_columns()
  # check diagonals T/F
  diagnals_winner = check_diagnals()

  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagnals_winner:
    winner = diagnals_winner
  else:
    winner = None
  return

  return

def check_rows():
  # Set up global variables
  global game_still_going
  # check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # if any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner (X or 0)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_columns():
  # Set up global variables
  global game_still_going
  # check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # if any columns does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner (X or 0)
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return

def check_diagnals():
  # Set up global variables
  global game_still_going
  # check if any of the diagnals have all the same value (and is not empty)
  diagnal_1 = board[0] == board[4] == board[8] != "-"
  diagnal_2 = board[6] == board[4] == board[2] != "-"
  # if any diagnals does have a match, flag that there is a win
  if diagnal_1 or diagnal_2:
    game_still_going = False
  # Return the winner (X or 0)
  if diagnal_1:
    return board[0]
  elif diagnal_2:
    return board[6]
  return 


def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
  return


def flip_player():
  # gobal variables we next
  global current_player
  # if the current player was A, then change it to B
  if current_player == "X":
    current_player = "0"
  # if the current_player was A, then change it to B
  elif current_player == "0":
    current_player = "X"
  return
  

play_game()







# define board
# display(print) board
# play game
# handle turn
# check win
  # check rows
  # check columns
  # check diagrams
# check tie
# flip player