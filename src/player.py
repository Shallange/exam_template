from .pickups import Item # For checking instance of Maybeitem

class Player:
    marker = "@"#Spelarens ikon på spelplanen

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.score = 0
        self.inventory = []


    def show_inventory(self,command):
        if command =="i":
            if self.inventory != None:
                for item in self.inventory:
                    print(f"{item.symbol} - {item.name}")
            else:
                print("inventory empty")

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy


    def can_move(self, x, y, grid):
        if grid.get(x, y) == "\u25A0": # \u25A0 = ■
            return False
        return True

    def direction(self, command,grid):
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
            self.score -= 1
            if isinstance(maybe_item, Item):
            #we found something
                maybe_item.pickup(self)#Depending on the item, Pickupmetod will handle the specific item diffrently
                grid.set(self.pos_x, self.pos_y, grid.empty)
                grid.clear(self.pos_x, self.pos_y)


    def print_status(self, game_grid):
        """Visa spelvärlden och antal poäng."""
        print("--------------------------------------")
        print(f"You have {self.score} points.")
        print(game_grid)
