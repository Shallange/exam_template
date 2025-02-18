from .grid import Grid
from .player import Player
from . import pickups


#----------Skapa player, spelplanen och items----------
player = Player(17, 6)# start x and y pos for player
g = Grid()#skapa spelplanen
g.set_player(player)# placera player på spelplanen
g.make_walls()#skapa spelplanets väggar
pickups.randomize(g)#random placering av items på spelplanen


command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    player.print_status(g)
    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    if command == "d" and player.can_move(1, 0, g):  # move right
        # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
        maybe_item = g.get(player.pos_x + 1, player.pos_y)
        player.move(1, 0)

        if isinstance(maybe_item, pickups.Item):
            # we found something
            player.score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
