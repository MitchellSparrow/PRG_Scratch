import pygame


class BgMovement():
    def __init__(self, background):
        self.bg = pygame.image.load ("./Images/Backgrounds/Space_Background_1080.jpg")
        self.bgX = 0
        self.bgX2 = self.bg.get_width()
        
    def redrawWindow(self, surface):
        surface.blit(self.bg, (self.bgX, 0))
        surface.blit(self.bg, (self.bgX2, 0))

    