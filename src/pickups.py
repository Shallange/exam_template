
class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=20, symbol="?"):#\U0001F353
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


pickups = [
        Item("carrot",10), 
        Item("apple"), 
        Item("strawberry",20,"\U0001F353"), 
        Item("cherry"), 
        Item("watermelon"), 
        Item("radish", 10), 
        Item("cucumber", 10), 
        Item("meatball", 10)
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

