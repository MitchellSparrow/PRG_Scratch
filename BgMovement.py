import pygame


class BgMovement():
    def __init__(self, background, width):
        self.background = background
        self.bgX = 0
        self.width = width
        self.bgX2 =  self.width
        
    def redrawWindow(self, surface, background):
        surface.blit(background, (self.bgX, 0))
        surface.blit(background, (self.bgX2, 0))

    