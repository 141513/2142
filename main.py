import pygame
import random
import time
import sys
import Constants

from InputControllers import KeyboardController, MouseController
from SelectionController import SelectionController
from GUIController import GUIController
from World import World
from Unit import Unit

class Game():
    def __init__(self):
        self.initializePygameElements()
        self.initializeControllers()
        self.world = World(self)
        self.owned_units = set()
        self.owned_structures = set()

    def initializeControllers(self):
        self.keyboard_controller = KeyboardController(self)
        self.mouse_controller = MouseController(self)
        self.selection_controller = SelectionController(self)
        self.GUI_controller = GUIController(self)

    def initializePygameElements(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 30)
        self.window = pygame.display.set_mode(Constants.WINDOW_SIZE)

    def mainLoop(self, dt):
        self.getInput()
        self.update(dt)
        self.drawGraphics()
        self.clock.tick(60)

    def getInput(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.exitApp()
            if event.type == pygame.MOUSEMOTION:
                self.mouse_controller.mouse_position = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_controller.mouse_press(event.button, pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_controller.mouse_release(event.button, pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                self.keyboard_controller.key_pressed(event.key)
            if event.type == pygame.KEYUP:
                self.keyboard_controller.key_released(event.key)

    def update(self, dt):
        if dt > 1:
            return
        else:
            for structure in self.world.all_structures:
                structure.update(dt)
            for unit in self.world.all_units:
                unit.update(dt)
                
    def drawGraphics(self):
        self.window.fill( (0,0,0) )

        for structure in self.world.all_structures:
            structure.render(self.window)
        for unit in self.world.all_units:
            unit.render(self.window)
        #for GUI_element in self.GUI.all_elements:
        #    GUI_element.render(self.window)
        
        self.mouse_controller.render(self.window)
        
        fps = self.font.render(str(int(self.clock.get_fps())), True, (255,255,255))
        self.window.blit(fps, (50, 50))
        
        pygame.display.flip()
    
    def exitApp(self):
        IS_RUNNING = False
        pygame.quit()
        print("2142 has exited.")
        sys.exit()

game = Game()

x = Unit(game.world, 50, 50)
x.movement_queue.add_destination(500,200)

lastFrameTime = 0
IS_RUNNING = True
while IS_RUNNING:
    currentTime = time.time()
    dt = currentTime - lastFrameTime
    lastFrameTime = currentTime
    
    game.mainLoop(dt)
