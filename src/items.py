class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, symbol="?"):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return self.symbol
    
    def pickup(self, player):
        player.inventory.append(self)
        print(f"Picked up an unkown item, maybe i find a use for it later")
    

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

#---------Pickable items------------
class Food(Item):
    def __init__(self, name, symbol, value = 20):
        super().__init__(name, symbol)
        self.value = value

    def pickup(self, player):
        player.score += self.value
        player.inventory.append(self)
        print(f"You found a {self.name}, +{self.value} points.")


class Key(Item):
    """Key to open a locked chest"""
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
    def pickup(self, player):
        player.inventory.append(self)
        print(f"I found i key, it looks like it is used to unlock a chest")

#---------Interactive items----------
class Chest(Item):
    """Locked chest that will need a key to open 
       inside a treasure worth 100 points
    """
    def __init__(self, name, symbol,locked, value = 100):
        super().__init__(name, symbol)
        self.locked = locked
        self.value = value

    def pickup(self, player):
        if player.have_item(Key):#check if player has picked up a key
            print("You use the key and opened the chest")  
            player.score += self.value  
            #remvove key from inventory
        else:
            print("Chest is locked.. better find a key")
        
#----------Dangerous items---------
class Bomb(Item):
    """Currently undergoing changes"""
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
    
    def explode():
        pass

class Trap(Item):
    def __init__(self, name, symbol, armed):
        super().__init__(name, symbol)
        self.armed = armed
    
    def activate():
        pass


pickups = [
        Food("carrot",carrot.strip(), 10), 
        Food("apple",apple.strip(),), 
        Food("strawberry", strawberry.strip()), 
        Food("watermelon", watermelon.strip()), 
        Food("cucumber", cucumber.strip(), 10), 
        Food("meat",meat.strip(), 10) 
        #Eatibles("cherry"), #unicode for cherry does not exist so plan on finding another
    ]

other = [
    Chest("Chest",chest.strip() ,True),
    Key("key",key.strip() )
    ]

#-----------------Place the items---------
def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
    #currently places bomb,chest and key 1 of each
    for item in other:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

