import Constants

class Tile():
    def __init__(self, row, column, world):
        self.row = row
        self.column = column
        self.world = world
        self.structure = None
        
class World():
    def __init__(self, game):
        self.game = game
        self.grid = []
        self.all_units = set()
        self.all_structures = set()
        self.generate_grid()

    def generate_grid(self):
        for column in range(Constants.MAP_SIZE):
            self.grid.append([])
            for row in range(Constants.MAP_SIZE):
                self.grid[column].append(Tile(column, row, self))
