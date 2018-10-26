import Constants
import pygame

class Structure(): 
    def __init__(self, world, column,row):
        self.world = world
        self.world.game.all_structures.add(self)
        self.column = column
        self.row = row

    def update(self, dt):
        pass

    def render(self, window):
        pygame.draw.rect(window, (50,250,50), [self.column * Constants.GRID_SIZE,
                                               self.row * Constants.GRID_SIZE,
                                               Constants.GRID_SIZE,
                                               Constants.GRID_SIZE])

    def select(self):
        print("Building at ", row, ".", column, " selected.")


class Radar(Structure):
    def __init__(self, world, column, row):
        super().__init__(world, column, row)
        self.range = 50

        
