from globals import BACKGROUND_SPEED


class BgMovement():
    '''Class which displays a moving background'''

    def __init__(self):
        '''Initialize the background movement class'''
        self.shift = 0

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
