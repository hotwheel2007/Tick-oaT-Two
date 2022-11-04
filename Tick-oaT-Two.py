# Tick-oaT-Two
# Idea by Oats Jenkins
# Brought to python by hw2007

from termcolor import colored

board = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]
peices = [" ", colored("–", "green", attrs = ["bold"]), colored("|", "green", attrs = ["bold"]), colored("+", "green", attrs = ["bold", "dark"])]
row_letters = ["a", "b", "c"]
win_conditions = ["012", "345", "678", "036", "147", "258", "048", "246"]
player = 1
move = 0
peice_color = "green"
peice_attrs = ["bold"]
info_color = "yellow"

print("")
print(colored("==== Tick-oaT-Two ====", info_color))
print(colored("Idea by: Oats Jenkins", info_color))
print(colored("Programmed by: hw2007", info_color))
print("")

def reset():
    global board
    global player

    board = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]
    player = 1


def draw_board():
    print(colored("    1   2   3", "white", attrs = ["dark"]))
    print(colored("  –––––––––––––", "white", attrs = ["dark"]))

    print(colored("a | ", "white", attrs = ["dark"]) + peices[board[0]] + colored(" | ", "white", attrs = ["dark"])
    + peices[board[1]] + colored(" | ", "white", attrs = ["dark"]) + peices[board[2]]
    + colored(" | ", "white", attrs = ["dark"]))

    print(colored("  –––––––––––––", "white", attrs = ["dark"]))

    print(colored("b | ", "white", attrs = ["dark"]) + peices[board[3]] + colored(" | ", "white", attrs = ["dark"])
    + peices[board[4]] + colored(" | ", "white", attrs = ["dark"]) + peices[board[5]]
    + colored(" | ", "white", attrs = ["dark"]))

    print(colored("  –––––––––––––", "white", attrs = ["dark"]))

    print(colored("c | ", "white", attrs = ["dark"]) + peices[board[6]] + colored(" | ", "white", attrs = ["dark"])
    + peices[board[7]] + colored(" | ", "white", attrs = ["dark"]) + peices[board[8]]
    + colored(" | ", "white", attrs = ["dark"]))

    print(colored("  –––––––––––––", "white", attrs = ["dark"]))


def place_piece(player, pos):
    try:
        position = ((row_letters.index(pos[0]) * 3) + int(pos[1])) - 1
        if board[position] == player or int(pos[1]) > 3:
            print(colored("Invalid placement!", "red", attrs = ["bold"]))
            return(False)
        else:
            if board[position] + player < 4:
                board[position] += player
                return(True)
            else:
                print(colored("Invalid placement!", "red", attrs = ["bold"]))
                return(False)

    except:
        print(colored("Invalid placement!", "red", attrs = ["bold"]))
        return(False)


def win():
    for condition in win_conditions:
        conditions_met = [0, 0, 0]

        for i in range(0, 3):
            if board[int(condition[i])] == 3:
                conditions_met[i] = 1

        if conditions_met == [1, 1, 1]:
            return(True)

    return(False)


while True:
    print("")
    print("")
    print("")
    draw_board()
    print("")

    print("Player " + str(player) + ": Where would you like to place your piece?")
    move = input(colored("> ", "white", attrs = ["dark"]))


    if place_piece(player, move):
        if win():
            print("")
            print("")
            print("")
            draw_board()
            print("")

            print(colored("PLAYER " + str(player) + " WINS!", "green", attrs = ["bold", "reverse"]))
            print("Would you like to play again? (y/n)")
            play_again = input(colored("> ", "white", attrs = ["dark"]))
            if play_again == "y": reset()
            else: exit()
        else:
            if player == 1: player = 2
            else: player = 1
