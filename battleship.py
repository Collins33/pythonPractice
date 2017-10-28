board=[]
for x in range(5):
  board.append(["O"]*5)

def print_board(board_in):
  for x in range(0,len(board_in)):
    print board_in[x]
  return board_in


print_board(board)
