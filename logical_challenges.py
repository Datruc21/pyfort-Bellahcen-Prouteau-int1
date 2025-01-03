"""         PYFORT by Maël and Jalil
THe logical challenge module (done by Jalil), used to challenge the contenders with a game of battleship"""

from random import *
def next_player(n) :
    """Simply used to change the player's turn"""
    if n == 1 :
        return 0
    return 1


def empty_grid() :
    """Creates your different grids for the game"""
    grid = []
    for i in range(3) :
        l = []
        for j in range(3) :
            l.append(" ")
        grid.append(l)
    return grid

def display_grid(grid, message) :
    """Show a grid to the player with a message, no return"""
    print(message)
    print("-------------")
    for i in range(len(grid)) :
        for j in range(len(grid[i])) :
            print("|",grid[i][j],end=" ")
        print("|")
    print("-------------")

def ask_positions() :
    """Ask 2 positions between 1 and 3 and check if the given input is correct """
    a = int(input("Number of the row (between 1 and 3) : "))
    while a>3 or a<1 :
        print("Please enter a number between 1 and 3")
        a = int(input("Number of the row (between 1 and 3) : "))
    b = int(input("Number of the column (between 1 and 3) : "))
    while b > 3 or b < 1:
        print("Please enter a number between 1 and 3")
        b = int(input("Number of the column (between 1 and 3) : "))
    return a,b

def initialize() :
    """Create the player's grid and let him place his boats"""
    grid = empty_grid()
    print("Let's place your first boat : ")
    a,b = ask_positions()
    grid[a-1][b-1] = "B"
    print("Place your second boat : ")
    a, b = ask_positions()
    while grid[a-1][b-1] != " ":
        print("This position is already occupied !")
        a, b = ask_positions()
    grid[a-1][b-1] = "B"
    display_grid(grid, "Here is your grid")
    return grid

def turn(player, player_shots_grid, opponent_grid) :
    """Proceed with either the player's turn or the game master's
    Either way, one will pick 2 integers and shoot at those coordinates
    Verify on the target's grid if it's a hit or a miss"""
    if player == 0 : #player's turn
        display_grid(player_shots_grid,"History of your previous shots:")
        print("Your turn captain !")
        a, b = ask_positions()
        while opponent_grid[a-1][b-1] == "X" or opponent_grid[a-1][b-1] == "." : #To make sure you cannot shoot twice at the same spot
            print("You already shot here !")
            a,b = ask_positions()
        if opponent_grid[a-1][b-1] == "B" :
            player_shots_grid[a-1][b-1] = "X"
            opponent_grid[a - 1][b - 1] = " " # make the ship disappear so you cannot sink infinitely the same ship
            print("Hit and sunk !")
        else :
            player_shots_grid[a - 1][b - 1] = "."
            print("Missed...")
    else :
        print("Game master's turn : ")
        a = randint(0,2)
        b = randint(0,2)
        while player_shots_grid[a][b] == "X" or player_shots_grid[a][b] == "." : #To make sure the game master doesn't do the same shot
            a = randint(0, 2)
            b = randint(0,2)
        print("The game master shot at position {},{}".format(a+1,b+1))
        if opponent_grid[a][b] == "B" :
            print("Hit and sunk !")
            opponent_grid[a][b] = " "
            player_shots_grid[a][b] = "X"
        else :
            player_shots_grid[a][b] = "."
            print("Missed...")
    print()
    next_player(player)

def has_won(player_shots_grid):
    """Verify if one has won, by counting the number of sunk ship"""
    c = 0
    for i in range(3) :
        for j in range(3) :
            if player_shots_grid[i][j] == "X" :
                c += 1
    if c == 2 :
        return True
    return False

def battleship_game() :
    """Coordinates all the functions above to create a complete game of battleship
    Return True if the player wins, False otherwise"""
    print("-----------------------------------------------------",end="")
    print(r"""
__________         __    __  .__                .__    .__        
\______   \_____ _/  |__/  |_|  |   ____   _____|  |__ |__|_____  
 |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___/  |  \|  \____ \ 
 |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   Y  \  |  |_> >
 |______  /(____  /__|  |__| |____/\___  >____  >___|  /__|   __/ 
        \/      \/                     \/     \/     \/   |__|    """)
    print("-----------------------------------------------------")

    Game = True
    print("Each player must place 2 boats on a 3x3 grid.\nBoats are represented by 'B' and missed shots by '.'.\nSunk boats are marked by 'x'.")
    player_grid = initialize()
    player_shot_grid = empty_grid()
    master_grid = empty_grid()
    master_grid[randint(0,2)][randint(0,2)] = "B"
    a = randint(0,2) #Next lines are to make sure that there's two boats at different positions
    b = randint(0, 2)
    while master_grid[a][b] == "B":
        a = randint(0, 2)
        b = randint(0, 2)
    master_grid[a][b] = "B"
    master_shot_grid = empty_grid()
    player = 0
    while Game :
        if player == 0 :
            turn(player,player_shot_grid,master_grid)
            if has_won(player_shot_grid) :
                print("The player won !")
                return True
        else :
            turn(player,master_shot_grid,player_grid)
            if has_won(master_shot_grid) :
                print("You lost to the game master...")
                return False
        player = next_player(player)















