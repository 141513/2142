import Constants
from Structure import Structure

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
        for row in range(Constants.MAP_HEIGHT):
            self.grid.append([])
            for column in range(Constants.MAP_WIDTH):
                self.grid[row].append(Tile(column, row, self))

    def get_tile_at(self, column, row):
        if column >= 0 and column < Constants.MAP_WIDTH and row >= 0 and row < Constants.MAP_HEIGHT:
            return self.grid[column][row]
        else:
            print("The tile you are trying to get does not exist.")

    def build(self, structure_to_build, grid_coordinates):
        instansiated_structure = eval(structure_to_build + "(self," + str(grid_coordinates[0]) + "," + str(grid_coordinates[1]) + ")") 
        self.get_tile_at(grid_coordinates[0], grid_coordinates[1]).structure = instansiated_structure
