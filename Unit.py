import math, weakref, pygame
import Utility

class MovementQueue():
    def __init__(self, unit):
        self.unit = unit
        self.has_next_move = False
        self.queue = []
        self.current_destination = (round(self.unit.x), round(self.unit.y))

    def add_destination(self, x, y):
        self.queue.append((x,y))
        
    def clear(self):
        self.queue.clear()
        self.current_destination = (round(self.unit.x), round(self.unit.y))

    def next_destination(self):
        if len(self.queue) == 0:
            self.unit.stop()
        else:
            x = self.queue[0][0]
            y = self.queue[0][1]
            self.current_destination = (x, y) 
            self.unit.direction = math.atan2(y - self.unit.y, x - self.unit.x) * 180 / math.pi
            self.unit.start_moving()
            del self.queue[0]

    def set_destination(self, x, y):
        self.queue.clear()
        self.current_destination = (x, y) 
        self.unit.direction = math.atan2(y - self.unit.y, x - self.unit.x) * 180 / math.pi
        self.unit.start_moving()

    def has_reached_destination(self):
        if Utility.distance(self.current_destination[0], self.current_destination[1], self.unit.x, self.unit.y) <= 3:
            return True
        else:
            return False

class Unit():    
    def __init__(self, world, x, y):
        self.world = world
        self.world.game.all_units.add(self)
        self.current_destination = None
        self.x = x
        self.y = y
        self.x_velocity = 0
        self.y_velocity = 0
        self.direction = 0
        self.MAX_SPEED = 50
        self.size = 20
        self.movement_queue = MovementQueue(self)
        
    def update(self, dt):
        if self.movement_queue.has_reached_destination():
            self.movement_queue.next_destination()
        self.x += self.x_velocity * dt
        self.y += self.y_velocity * dt

    def render(self, window):
        pygame.draw.polygon(window, (50,250,50), self.getTriangleCoordinates())

        pygame.draw.circle(window, (50, 50, 200), self.movement_queue.current_destination, 3)
        pygame.draw.line(window, (50, 50, 200), (self.x, self.y), self.movement_queue.current_destination)

        if len(self.movement_queue.queue) > 0:
            pygame.draw.line(window, (255,255,255), self.movement_queue.current_destination, self.movement_queue.queue[0])

        for destination in self.movement_queue.queue:
            pygame.draw.circle(window, (255,255,255), destination, 3)
        for i in range(len(self.movement_queue.queue) - 1):
            pygame.draw.line(window, (255,255,255), self.movement_queue.queue[i], self.movement_queue.queue[i + 1] )

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
        self.movement_queue.clear()

    def start_moving(self):
        self.x_velocity = self.MAX_SPEED * math.cos(math.radians(self.direction))
        self.y_velocity = self.MAX_SPEED * math.sin(math.radians(self.direction))
        
        


        
    
