from .items import Item, Bomb, Shovel 

class Player:

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.score = 0
        self.inventory = []
        self.marker = "\U0001f6b6"
        self.grace_period = 0


    def print_status(self, game_grid, number_of_moves):
        """Display the game world, number of moves and number of points collected"""
        print("--------------------------------------")
        print(f"You have {self.score} points.")
        print(f"Currently {number_of_moves} number of moves have been made")
        print(game_grid)

    def have_item(self, type_of_item):
        """Used for checking if type of item is in inventory"""
        for item in self.inventory:
            if isinstance(item, type_of_item):
                return True
        return False

    def remove_item_from_inventory(self, item_type):
        """Remove one item from inventory by its type."""
        for index, item in enumerate(self.inventory):
            if isinstance(item, item_type):
                self.inventory.pop(index) 
                print(f"{item.name} has been used and removed from your inventory.")
        print("No item of this type found in inventory.")
        return None
    
    #--------Abilities--------
    def place_bomb(self, command, g):
        """Places a bomb at player location, the bomb is added to a list of placed bomb to"""
        if command == "b":
            bomb = Bomb("bomb", "\U0001F4A3",self.pos_x, self.pos_y)
            g.set(self.pos_x,self.pos_y, bomb)
            g.active_bombs.append(bomb)
            print("Bomb has been planted,  RUUUUUN!! ")
            return True

    def have_grace(self, action):
        """Passive skill that activates when picking up an item, you gain a imunity to damage for 5 moves"""
        match action:
            case "activate grace":
                self.grace_period = 6
                print("You have picked up an item and you are bleesed with grace, take no damage 5 steps")
            case "update grace":
                if self.grace_period > 0:
                    self.grace_period -= 1
                print(f"You have an active grace, {self.grace_period} more steps")
                if self.grace_period == 0:
                    print("You have no active blessings, pick something up and you shall be blessed")
            case "check grace":
                return self.grace_period > 0

    
    def disarm_trap(self, command, g):
       """Disarm a nearby trap if command is 't'"""
       if command == "t":
        pass

    def show_inventory(self, command):
        """Show inventory if command is 'i'"""
        if command =="i":
            if self.inventory != None:
                for item in self.inventory:
                    print(f"{item.symbol} - {item.name}")
            else:
                print("inventory empty")


    #---------Player movement-------
    def can_move(self, x, y, grid):
        """Check if the player can move to the desired next position"""
        if grid.get(x, y) == "\u25A7 ": # \u25A7 = ▧
            return False
        return True

    # Moves the player, "dx" and "dy" is the diffrence
    def move(self, dx, dy):
        """Move the player\n
        dx = Horizontal movement, from left to right\n
        dy = Vertical movement, from top to bottom"""
        self.pos_x += dx
        self.pos_y += dy

    def direction(self, command, grid):
        """Update the player's direction based on command and handle the interaction with items"""
        dx = 0 
        dy = 0

        if command == "w":
            dy = -1 # (0, dy)
        elif command == "a":
            dx = -1 # (dx, 0)
        elif command == "s":
            dy = 1 # (0, dy)
        elif command == "d":
            dx = 1 # (dx, 0)
        
        if self.can_move(self.pos_x + dx , self.pos_y + dy,grid):  #Check if planned move is possible(no wall)
            maybe_item = grid.get(self.pos_x + dx , self.pos_y + dy)
            self.move(dx, dy)
            if not self.have_grace("check grace"):
                self.score -= 1
            if isinstance(maybe_item, Item):
                #Depending on the item, interact method will handle the specific item diffrently and return bool
                remove_item_from_grid = maybe_item.interact(self)
                if remove_item_from_grid:
                    grid.clear(self.pos_x, self.pos_y)
                    self.have_grace("activate grace")
        else:
            if self.have_item(Shovel):
                Shovel.dig(self,grid, self.pos_x + dx, self.pos_y + dy)
                self.remove_item_from_inventory(Shovel)