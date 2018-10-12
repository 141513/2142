from Unit import Unit

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
        if objects_to_select != None:
            for game_object in objects_to_select:
                game_object.select()

    def set_selection_from_box(self, start, end):
        objects_to_select = []
        print(start)
        print(end)
        for unit in self.game.world.all_units:
            if unit.x > start[0] and unit.x < end[0]:
                if unit.y > start[1] and unit.y < end[1]:
                    objects_to_select.append(unit)

        self.set_selection(objects_to_select)
        
                    
    def add_to_selection(self, objects_to_add):
        for game_object in objects_to_add:
            self.selection.append(game_object)
            game_object.select()
        
    def set_destination(self, position):
        for game_object in self.selection:
            if isinstance(game_object, Unit):
                game_object.set_destination(position[0], position[1])
                
    def get_control_group(self, number):
        if number >=0 and number <= 9:
            self.set_selection(self.control_groups[number])
            print("Selected conrol group ", number)

    def set_control_group(self, number):
        if number >= 0 and number <= 9:
            self.control_groups[number] = self.selection
            print("Created control group ", number)
        else:
            print("Invalid control group number.")
    
        

