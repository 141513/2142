import math, weakref, pygame
import Utility

class MovementQueue():
    def __init__(self, unit):
        self.unit = unit
        self.has_next_move = False
        self.


class Unit():    
    def __init__(self, world, x, y):
        self.world = world
        self.world.all_units.add(self)
        self.x = x
        self.y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.direction = 0
        self.MAX_SPEED = 100
        self.size = 20
        self.move_queue = []
        self.destination = (self.x, self.y)
        self.target = None
        
    def update(self, dt):
        if Utility.distance(self.destination[0], self.destination[1], self.x, self.y) <= 3:
            self.stop()
        else:
            self.x += self.x_velocity * dt
            self.y += self.y_velocity * dt

    def set_destination(self, x, y):
        self.move_queue.clear()
        self.destination = (x, y) 
        self.direction = math.atan2(y - self.y, x - self.x) * 180 / math.pi
        self.start_moving()

    def render(self, window):
        pygame.draw.polygon(window, (50,250,50), self.getTriangleCoordinates())
        pygame.draw.circle(window, (255,255,255), self.destination, 3)
        pygame.draw.circle(window, (255,0,0), (round(self.x), round(self.y)), 3)

    def getTriangleCoordinates(self):
        coordinate_list = []
        for i in [-120 + self.direction, 0 + self.direction, 120 + self.direction]:
            coordinate_list.append((
                self.x + self.size * math.cos(math.radians(i)),
                self.y + self.size * math.sin(math.radians(i))))
        return coordinate_list

    def select(self):
        print("Unit selected.")

    def stop(self):
        self.x_velocity = 0
        self.y_velocity = 0
        self.destination.clear()
        self.

    def start_moving(self):
        self.x_velocity = self.MAX_SPEED * math.cos(math.radians(self.direction))
        self.y_velocity = self.MAX_SPEED * math.sin(math.radians(self.direction))
        
        


        
    
