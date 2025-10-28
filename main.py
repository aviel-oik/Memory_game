import game
from game import coord_input
import tools

def play(size):
    state = game.init_game(size)
    tools.print_board(state["board_close"])
    win = False
    while not win:
        a,b = coord_input(state)
        game.play_round(state,a,b)
        win = game.is_win(state)




def main():
    size = int(input("Enter the size (even number) of the game: "))
    play(size)



if __name__ == "__main__":
    main()
