import Constants
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def pixel_to_grid(x, y):
    if x > 0 and x < Constants.WINDOW_WIDTH and y > 0 and y < Constants.WINDOW_HEIGHT:
        return (int(x/Constants.GRID_SIZE), int(y/Constants.GRID_SIZE))
    else:
        raise Exception
