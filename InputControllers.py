from Unit import Unit
import pygame

class MouseController():
    def __init__(self, game):
        self.game = game
        self.mouse_position = (0,0)
        self.button_states = [None, False, False, False, False, False]
        self.last_pressed = [None, (0,0), (0,0), (0,0), (0,0), (0,0)]
        self.last_released = [None, (0,0), (0,0), (0,0), (0,0), (0,0)]
        self.selection_box_start = None
        self.selection_box_end = None
   
    def mouse_press(self, button, position):
        self.button_states[button] = True
        self.last_pressed[button] = position
        print("Mouse button ", button, " pressed at ", position)
        
        if button == 1:
            #self.check_if_unit_clicked(position)
            self.selection_box_start = position
            
        if button == 3:
            if self.game.selection_controller.selection != None:
                if self.game.keyboard_controller.key_states[304] == True:
                    self.game.selection_controller.add_destination(position)
                else:
                    self.game.selection_controller.set_destination(position)


                
                
    def mouse_release(self, button, position):
        self.button_states[button] = False
        self.last_released[button] = position
        print("Mouse button ", button, " released at ", position)

        if button == 1:
            self.selection_box_end = position
            self.game.selection_controller.set_selection_from_box(self.selection_box_start, self.selection_box_end)
            
        
    def check_if_unit_clicked(self, position):
        for unit in self.game.game.world.all_units:
            if position[0] > unit.x - unit.size and position[0] < unit.x + unit.size:
                if position[1] > unit.y - unit.size and position[1] < unit.y + unit.size:
                    if self.game.keyboard_controller.key_states[304] == True:
                        self.game.selection_controller.add_to_selection([unit])
                    else:
                        self.game.selection_controller.set_selection([unit])

    def render(self, window):
        if self.button_states[1] == True:
            pygame.draw.lines(window, (255,255,255), True, [(self.selection_box_start[0], self.selection_box_start[1]),
                                                            (self.mouse_position[0], self.selection_box_start[1]),
                                                            (self.mouse_position[0], self.mouse_position[1]),
                                                            (self.selection_box_start[0], self.mouse_position[1])
                                                             ]
                              )

    
class KeyboardController():
    def __init__(self, game):
        self.game = game
        self.key_states = {}
        for i in range(500):
            self.key_states[i] = False
    
    def key_pressed(self, key):
        self.key_states[key] = True
        print("Key ", key, " pressed.")

        if key >= 49 and key <= 57: #numbers 1 through 9
            if self.key_states[306] == True: #CTRL
                self.game.selection_controller.set_control_group(key - 48)
            else:
                self.game.selection_controller.get_control_group(key - 48)
                
        if key == 32: #space
            x = Unit(self.game.world, 50, 50)

        if key == 27:
            self.game.selection_controller.clear_selection()
        
    def key_released(self, key):
        self.key_states[key] = False
        print("Key ", key, " released.")
