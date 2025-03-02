class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, symbol="?"):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return self.symbol
    
    def interact(self):
        """Default, can be overidden by subclasses"""
        print("You stumble upon something not knowing what to do, you scratch your head")


#---------------Unicode emojis--------#
strawberry = "\U0001F353"
watermelon = "\U0001F349"
cucumber = "\U0001F952"
meat = "\U0001F356"
apple = "\U0001F34E"
carrot = "\U0001F955"

key = "\U0001F511"
bomb = "\U0001F4A3"
chest = "\U0001F9F0"
trap = "\U0001FAA4 "
shovel = "\U0001F944"
fire = "\U0001F525"


#---------Pickable items------------
class Food(Item):
    def __init__(self, name, symbol, value = 20):
        super().__init__(name, symbol)
        self.value = value

    def interact(self, player):
        return self.pickup(player)
        
    def pickup(self, player):
        player.score += self.value
        player.inventory.append(self)
        print(f"You found a {self.name}, + {self.value} points.")
        return True


class Key(Item):
    """Key to open a locked chest"""
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
    
    def interact(self, player):
        return self.pickup(player)
        
    def pickup(self, player):
        player.inventory.append(self)
        print(f"I found a {self.name}, it looks like it is used to unlock a chest")
        return True


class Shovel(Item):
    def __init__(self, name, symbol="?"):
        super().__init__(name, symbol)
    
    def interact(self, player):
        return self.pickup(player)
    
    def pickup(self, player):
        player.inventory.append(self)
        print(f"I found a {self.name}, i should be able to remove a wall piece now")
        return True

    def dig(self,grid, x, y):
        grid.clear(x, y)
        print("You've used the shovel to remove a wall")
        return True
    

#---------Interactive items----------
class Chest(Item):
    """Locked chest that will need a key to open 
       inside a treasure worth 100 points
    """
    def __init__(self, name, symbol, value = 100):
        super().__init__(name, symbol)
        self.value = value

    def interact(self, player):
        return self.unlock(player)

    def unlock(self, player):
        if player.have_item(Key):#check if player has picked up a key
            print("You use the key and opened the chest")  
            player.score += self.value
            player.remove_item_from_inventory(Key)
            return True
        else:
            print("Chest is locked.. better find a key")
            return False
        

#----------Dangerous items---------
class Bomb(Item):
    """Bomb is placed by player and it will explode after 3 player moves"""
    def __init__(self, name, symbol, x, y, countdown = 4):
        super().__init__(name, symbol)
        self.countdown = countdown
        self.pos_x = x
        self.pos_y = y

    def interact(self, player):
        return False
    
    def tick(self, grid):
        """Each Move player makes, the bomb will tick and then explode"""
        self.countdown -= 1
        if self.countdown <= 0:
            self.explode(grid)
            return True
        return False
    
    def explode(self, grid):
        """This is called when coutndown reaches 0 it sets the area ablaze"""
        print("Bomb has exploded")
        explosion_radius = grid.get_surrounding_cordinates(self.pos_x, self.pos_y)
        explosion_radius.append((self.pos_x,self.pos_y))# added here to also set the center position ablaze
        for x, y in explosion_radius:
            grid.set(x,y, fire)
    

class Trap(Item):

    def __init__(self, name, symbol, num_of_activations=3):
        super().__init__(name, symbol)
        self.num_of_activations = num_of_activations

    def interact(self, player):
        if self.num_of_activations > 0:
            return self.activate(player)
        
    def activate(self, player):
        player.score -= 10
        self.num_of_activations -= 1
        if self.num_of_activations == 0:
            return True # Removes Trap from grid
        return False# Keeps the Trap on the grid

    
pickups = [
        Food("Carrot",carrot, 10), 
        Food("Apple",apple,), 
        Food("Strawberry", strawberry), 
        Food("Watermelon", watermelon), 
        Food("Cucumber", cucumber, 10), 
        Food("Meat",meat, 10) 
    ]

other = [
    Chest("Chest",chest),
    Chest("Chest",chest),
    Key("Key",key),
    Key("Key",key),
    Trap("Trap",trap),
    Shovel("Shovel", shovel)
    ]


#-----------------Place the items---------
def place_item(grid, item):
    while True:
        # Randomize a position until we find a position that is empty
        x = grid.get_random_x()
        y = grid.get_random_y()
        if grid.is_empty(x, y):
            grid.set(x, y, item)
            break 
    
def randomize(grid):
    for item in pickups:
        place_item(grid, item)

    for item in other:
        place_item(grid, item)

def fertile_soil(grid, num_moves):
    """Spawns a new item of type food when number of moves is 25,50,75 and so on"""
    if num_moves % 25 == 0:
        item = grid.random_one_item(pickups)
        place_item(grid, item)




    
