from .grid import Grid
from .player import Player
from . import items
from datetime import datetime

def log_highscore(player_name, num_of_moves, score, filename = "game_results.txt"):
    """logs highscore after game has ended: example of how it is written\n
   
       11:48:40 - player1 - Number of moves: 35 - Total highscore: 158\n
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    text = f"{current_time} - {player_name} - Number of moves: {num_of_moves} - Total highscore: {score}\n"
    with open(filename, "a") as file:
        file.write(text)
    print(f"Game results have been saved to {filename}")

#----------Create player, game grid and items----------
player = Player(17, 6)#Start x and y pos for player
g = Grid()#Create game grid
g.set_player(player)#Place player on the grid
g.make_walls()#Create grid walls
items.randomize(g)#Randomly place items on the grid

command = "h"
num_of_moves = 0

# Loop until the user presses Q or X.
while not command.casefold() in ["q", "x"]:
    player.print_status(g,num_of_moves)
    num_of_moves += 1

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    player.direction(command,g)
    player.have_grace("update grace")
    player.show_inventory(command)
    player.place_bomb(command,g)
    g.update_bombs()
    player.disarm_trap(command,g)
    
    items.fertile_soil(g, num_of_moves)
    
 
print("Thank you for playing!")
log_highscore("player1", num_of_moves, player.score)