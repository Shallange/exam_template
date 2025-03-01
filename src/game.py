from .grid import Grid
from .player import Player
from . import items


#----------Create player, game grid and items----------
player = Player(17, 6)#Start x and y pos for player
g = Grid()#Create game grid
g.set_player(player)#Place player on the grid
g.make_walls()#Create grid walls
items.randomize(g)#Randomly place items on the grid


command = "t"
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
#append to txt fil  "player , date , number of moves ,  high score "