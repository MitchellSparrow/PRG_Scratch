from globals import BACKGROUND_SPEED, WHITE, FINISH_LINE_SPEED
import pygame


class BgMovement():
    '''Class which displays a moving background'''

    def __init__(self):
        '''Initialize the background movement class'''
        self.shift = 0
        self.start_line_shift = 0
        self.start_line = pygame.image.load(
            "./Images/Finish_line/Finish_line.png")
        pygame.init()

    def reset(self):
        self.shift = 0
        self.start_line_shift = 0

    def run(self, surface, background):
        '''Function which draws the moving background and start line'''
        self.redrawWindow(surface, background)
        self.drawStartLine(surface)

    def redrawWindow(self, surface, background):
        '''Function which redraws the background - shifted'''
        # Check if the shift is more than the width of the background
        if self.shift > background.get_width():
            self.shift = 0
        else:
            self.shift += BACKGROUND_SPEED

        # Display two backgrounds, side by side, offset by a shift value
        surface.blit(background, (-self.shift, 0))
        surface.blit(background, (background.get_width() - self.shift, 0))

    def drawStartLine(self, surface):
        '''Function which draws the start line - shifted'''
        # Check if the start line is on the screen - if so, shift it, else don't draw it at all
        if surface.get_width() / 1.3 - self.start_line_shift > - self.start_line.get_width():
            surface.blit(self.start_line, (surface.get_width() /
                                           1.3 - self.start_line_shift, 0))

            font = pygame.font.Font("./Fonts/GamePlayed.ttf", 70)
            text = font.render("START", True, WHITE)
            text = pygame.transform.rotate(text, -90)
            surface.blit(text, [surface.get_width() /
                                1.15 - self.start_line_shift, surface.get_height()/2 - text.get_height()/2])

            self.start_line_shift += FINISH_LINE_SPEED
