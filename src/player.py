from .items import Item, Bomb 

class Player:

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.score = 0
        self.inventory = []
        self.marker = "\U0001f6b6"


    def print_status(self, game_grid, number_of_moves):
        """Visa spelvärlden och antal poäng."""
        print("--------------------------------------")
        print(f"You have {self.score} points.")
        print(f"Currently {number_of_moves} number of moves have been made")
        print(game_grid)

    def have_item(self, type_of_item):
        """used for checking if type of item is in inventory"""
        for item in self.inventory:
            #checks if the current item is an instance of the type_of_item class
            if isinstance(item, type_of_item):
                return True
        return False


    #--------Abilities--------
    def place_bomb(self, command, g):
        if command == "b":
            bomb = Bomb("bomb", "\U0001F4A3")
            g.set(self.pos_x,self.pos_y, bomb)
            print("Bomb has been planted,  RUUUUUN!! ")

    def have_grace(self):
        pass 
    
    def disarm_trap(self, command, g):
       #if command == "t" 
        pass


    def show_inventory(self, command):
        if command =="i":
            if self.inventory != None:
                for item in self.inventory:
                    print(f"{item.symbol} - {item.name}")
            else:
                print("inventory empty")


    #---------Player movement-------
    def can_move(self, x, y, grid):
        if grid.get(x, y) == "\u25A7 ": # \u25A7 = ▧
            return False
        return True

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def direction(self, command, grid):
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
                maybe_item.interact(self)#Depending on the item, interact method will handle the specific item diffrently
                grid.clear(self.pos_x, self.pos_y)