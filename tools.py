import random

def create_board(size):
    matrix_close = [[" X" for x in range(size)] for x in range(size)]
    total_cells = size * size
    # # Vérifie que le nombre total de cases est pair
    # if total_cells % 2 != 0:
    #     raise ValueError("La taille doit permettre un nombre pair de cases.")
    numbers = list(range(1, total_cells // 2 + 1)) * 2
    random.shuffle(numbers)
    matrix_open = [numbers[i * size:(i + 1) * size] for i in range(size)]
    return matrix_close, matrix_open



def valid_input(state, x, y):
    valid = True
    size = state["size"]
    for i in range(2):
        if x[i] < 0 or x[i] >= size:
            valid = False
        if y[i] < 0 or y[i] >= size:
            valid = False
    return valid



def print_board(matrix):
    size = len(matrix)
    print("\n  === Memory Game Board ===\n")
    print("      " + "  ".join(f"{i:2}" for i in range(size)))

    print("    +" + "----" * size + "+")
    for i, row in enumerate(matrix):
        row_str = "  ".join(f"{val:2}" for val in row)
        print(f"{i:2}  | {row_str} |")
    print("    +" + "----" * size + "+\n")

