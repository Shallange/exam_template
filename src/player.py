class Player:
    marker = "@"#Spelarens ikon på spelplanen

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.score = 0
        self.inventory = []


    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy


    def can_move(self, x, y, grid):
        return True
        #TODO: returnera True om det inte står något i vägen


    def print_status(self, game_grid):
        """Visa spelvärlden och antal poäng."""
        print("--------------------------------------")
        print(f"You have {self.score} points.")
        print(game_grid)
