import pygame
pygame.font.init()
myfont = pygame.font.SysFont("monospace", 15)

class GUIElement():
    def __init__(self, x, y, width, height, visible = True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def render(self):
        pass


class Button(GUIElement):
    def __init__(self, x, y, width, height, text, action, arguments, visible = True):
        super().__init__(x, y, width, height)
        self.text = text
        self.action = action
        self.label = myfont.render(self.text, 1, (0,0,0))
        self.arguments = arguments
        self.visible = visible
        
    def render(self, window):
        if self.visible == True:
            pygame.draw.rect(window, (255,255,255), [self.x, self.y, self.width, self.height])
            window.blit(self.label, (self.x, self.y))

    def pressed(self):
        if self.visible == True:
            self.action(self.arguments)


class Label(GUIElement):
    def __init__(self, x, y, width, height, text, update_text):
        super().__init__(x, y, width, height)
        self.text = text
        self.update_text = update_text
        self.label = myfont.render(self.text + str(self.update_text()), 1, (0,0,255))
        
    def render(self, window):
        pygame.draw.rect(window, (255,255,255), [self.x, self.y, self.width, self.height])
        self.label = myfont.render(self.text + str(self.update_text()), 1, (0,0,255))
        window.blit(self.label, (self.x, self.y))
