from .grid import Grid
from .player import Player
from . import items


#----------Skapa player, spelplanen och items----------
player = Player(17, 6)# start x and y pos for player
g = Grid()#skapa spelplanen
g.set_player(player)# placera player på spelplanen
g.make_walls()#skapa spelplanets väggar
items.randomize(g)#random placering av items på spelplanen


command = "t"
num_of_moves = 0

# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    num_of_moves += 1
    player.print_status(g,num_of_moves)
    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]
    items.fertile_soil(g, num_of_moves)
    player.direction(command,g)
    player.show_inventory(command)
    player.place_bomb(command,g)
    player.disarm_trap(command,g)
    
 
print("Thank you for playing!")
