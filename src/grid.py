import random

class Grid:
    """Represents the game grid"""
    width = 36
    height = 14
    empty = ". "  #Symbol for an empty cell (space is needed)
    wall = "\u25A7 " #Symbol for an impassable wall "\u25A7" == ▧ in unicode (space needed in string)

    def __init__(self):
        """Skapa ett objekt av klassen Grid"""
        # The game grid is stored as a list of list, We use list comprehension to set the "empty" symbol for each cell.
        self.active_bombs = [] # list of placed bombs on grid by player
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]
        

    #------Place the player on the grid---------
    def set_player(self, player):
        self.player = player


    #------Methods for item manipulation on the grid-----
    def get(self, x, y):
        """Retrieve what is at a certain position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Change whats at a certain position"""
        self.data[y][x] = value

    def clear(self, x, y):
        """Remove item from a position"""
        self.set(x, y, self.empty)

    def update_bombs(self):
        """Check  each bomb in the list to see if they have exploded and remove them from the list of active bombs"""
        for bomb in self.active_bombs:
            if bomb.tick(self):
                self.active_bombs.remove(bomb)
    
    def get_surrounding_cordinates(self, x, y):
        """Returns the adjesent cordinates to the object position"""
        cordinates = [
            (-1, -1),(0, -1),(1, -1),# Upper row: NW,N,NE
            (-1, 0),(1, 0), # Middle row: W, E 
            (-1, 1),(0, 1),(1, 1) # Lower row: SW,S,WE
        ]
        cordinates_adjesent_to_object = []
        for dx, dy in cordinates:
            adj_x = x + dx
            adj_y = y + dy
            cordinates_adjesent_to_object.append((adj_x, adj_y))
        return cordinates_adjesent_to_object

    #-------------Print the game grid---------------
    def __str__(self):
        """Enables printing the grid with the print() function"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += self.player.marker
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs
    

    #-----------Create walls around the entire grid--------------
    def make_walls(self):
        """Create walls around the entire game grid"""
        for i in range(self.height):
            self.set(0, i, self.wall)
            if i < 4:
                self.set(23, i, self.wall)
                self.set(14, i, self.wall)
            if i > 8:
                self.set(10, i, self.wall)
                self.set(18, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)
            

    #---------Methods for placing items------------
    def get_random_x(self):
        """Randomly generate a x-coordinate on the grid"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Randomly generate a Y-coordinate on the grid"""
        return random.randint(0, self.height-1)

    def is_empty(self, x, y):
        """Returns True if a specific cell is empty"""
        return self.get(x, y) == self.empty
    
    def random_one_item(self,items):
        """Used for fertilizied soil, to spawn one random type of food"""
        spawn_new_item = random.choice(items)
        return spawn_new_item

