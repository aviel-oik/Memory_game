import time
import tools
import copy

def init_game(size):
    board_close,board_open = tools.create_board(size)
    state = {"board_close" : board_close, "board_open" : board_open, "size" : size, "open_card" : [], "tries" : 0}
    return state



def coord_input(state):
    valid = False
    while not valid:
        a = input("enter the coordinates of the first map in the form of x,y :")
        try:
            x1 = int(a[0])
            y1 = int(a[2])
        except ValueError:
            print("invalid coordinates")
            valid = False
            continue
        b = input("enter the coordinates of the second map in the form of x,y :")
        try:
            x2 = int(b[0])
            y2 = int(b[2])
        except ValueError:
            print("invalid coordinates")
            valid = False
            continue
        valid = valid_round(state, [x1,x2], [y1,y2])
    return [x1,y1],[x2,y2]



def valid_round(state, x, y):
    valid = True
    valid = tools.valid_input(state, x, y)
    if x in state["open_card"] or y in state["open_card"]:
        valid = False
        print("card already open")
    return valid



def play_round(state, x, y):
    state["tries"] += 1
    tmp_board = copy.deepcopy(state["board_close"])
    tmp_board[x[0]][x[1]] = state["board_open"][x[0]][x[1]]
    tmp_board[y[0]][y[1]] = state["board_open"][y[0]][y[1]]
    tools.print_board(tmp_board)
    time.sleep(2)
    if state["board_open"][x[0]][x[1]] == state["board_open"][y[0]][y[1]]:
        state["board_close"][x[0]][x[1]] = state["board_open"][x[0]][x[1]]
        state["board_close"][y[0]][y[1]] = state["board_open"][y[0]][y[1]]
        state["open_card"].append([x[0], x[1]])
        state["open_card"].append([y[0], y[1]])
    tools.print_board(state["board_close"])



def is_win(state):
    win = True
    board = state["board_close"]
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == " X":
                win = False
    if win:
        print(f"\nCongratulations!!!\nYou won after {state["tries"]} tries.")
    return win







