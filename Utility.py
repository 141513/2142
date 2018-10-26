import Constants
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def pixel_to_grid(x, y):
    if x > 0 and x < Constants.WINDOW_WIDTH and y > 0 and y < Constants.WINDOW_HEIGHT:
        return (int(x/Constants.GRID_SIZE), int(y/Constants.GRID_SIZE))
    else:
        raise Exception

def get_start_of_bounding_box(point1, point2):
    start = [0,0]
    end = [0,0]
    if point1[0] < point2[0]:
        start[0] = point1[0]
        end[0] = point2[0]
    else:
        start[0] = point2[0]
        end[0] = point1[0]
    if point1[1] < point2[1]:
        start[1] = point1[1]
        end[1] = point2[1]
    else:
        start[1] = point2[1]
        end[1] = point1[1]

    return start, end
    
