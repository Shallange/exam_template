
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
    

class Eatibles(Item):
    def __init__(self, name, symbol, value = 20):
        super().__init__(name, symbol)
        self.value = value

    def pickup(self, player):
        player.score += self.value
        player.inventory.append(self)
        print(f"You found a {self.name}, +{self.value} points.")

class Chest(Item):
    """Locked chest that will need a key to open 
       inside a treasure worth 100 points
    """
    def __init__(self, name, symbol,locked):
        super().__init__(name, symbol)
        self.locked = locked

class Key(Item):
    """Key to open a locked chest"""
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
        
class Bomb(Item):
    """Currently undergoing changes"""
    def __init__(self, name, symbol):
        super().__init__(name, symbol)


#Testing with the diffrent classes
other = [
    Chest("Chest", "\U0001F9F0",True),
    Bomb("bomb", "\U0001F4A3"),
    Key("key", "\U0001F511")
    ]

pickups = [
        Eatibles("carrot","\U0001F955", 10), 
        Eatibles("apple","\U0001F34E"), 
        Eatibles("strawberry", "\U0001F353"), 
        Eatibles("watermelon","\U0001F349"), 
        Eatibles("cucumber","\U0001F952", 10), 
        Eatibles("meat","\U0001F356", 10) 
        #Eatibles("cherry"), #unicode for cherry does not exist so plan on finding another
    ]


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

