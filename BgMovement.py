import pygame


class BgMovement():
    def __init__(self, background, width):
        self.background = background
        self.bgX = 0
        self.bgX2 =  self.background.get_width()
        
    def redrawWindow(self, surface, background):
        surface.blit(self.background, (self.bgX, 0))
        surface.blit(self.background, (self.bgX2, 0))
        

    