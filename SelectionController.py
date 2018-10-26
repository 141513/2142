from Unit import Unit
import Utility

class SelectionController():
    def __init__(self, game):
        self.game = game
        self.selection = set()
        self.control_groups = {}
        for i in range(10):
            self.control_groups[i] = None

    def clear_selection(self):
        self.selection = set()
        print("Selection cleared.")

    def set_selection(self, objects_to_select):
        self.selection = objects_to_select

    def set_selection_from_box(self, point1, point2):
        objects_to_select = []
        start, end = Utility.get_start_of_bounding_box(point1, point2)
        for unit in self.game.all_units:
            if unit.x > start[0] and unit.x < end[0]:
                if unit.y > start[1] and unit.y < end[1]:
                    objects_to_select.append(unit)    
        self.set_selection(objects_to_select)
        
    def add_to_selection(self, objects_to_add):
        self.selection.append(objects_to_add)
        
    def set_destination(self, position):
        for game_object in self.selection:
            if isinstance(game_object, Unit):
                game_object.movement_queue.set_destination(position[0], position[1])

    def add_destination(self, position):
        for game_object in self.selection:
            if isinstance(game_object, Unit):
                game_object.movement_queue.add_destination(position[0], position[1])
                
    def get_control_group(self, number):
        if number >=0 and number <= 9:
            self.set_selection(self.control_groups[number])

    def set_control_group(self, number):
        if number >= 0 and number <= 9:
            self.control_groups[number] = self.selection

    def stop(self):
        for unit in self.selection:
            unit.stop()
    
        

