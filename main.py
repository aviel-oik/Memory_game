import game
from game import coord_input

def play(size):
    state = game.init_game(size)
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
