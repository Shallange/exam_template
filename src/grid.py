import random

class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    width = 36
    height = 14
    empty = ". "  # Tecken för en tom ruta (space is needed)
    wall = "\u25A7 " #Tecken för en ogenomtränglig vägg  "\u25A7" == ▧ in unicode (space needed in string)

    def __init__(self):
        """Skapa ett objekt av klassen Grid"""
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.active_bombs = [] # list of placed bombs on grid by player
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]
        
    #------placera spelaren på spelplanen---------
    def set_player(self, player):
        self.player = player

    #-----------metoder för item på spelplanen
    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def update_bombs(self):
        """For each bomb in list of bombs check if they have exoloded and remove from list if so"""
        for bomb in self.active_bombs:
            if bomb.tick():
                self.clear(bomb.pos_x, bomb.pos_y)
                self.active_bombs.remove(bomb)
        

    #-------------printa ut spelplanen---------------
    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
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
    

    #-----------Skapa spelplanens väggar--------------
    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""
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
            

    #---------Methods for being able to place items and also save that position------------
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)

    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty
    
    def random_one_item(self,items):
        """Used for fertilizied soil, to spawn one random type of food"""
        spawn_new_item = random.choice(items)
        return spawn_new_item

