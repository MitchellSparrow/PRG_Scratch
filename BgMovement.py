from globals import BACKGROUND_SPEED


class BgMovement():

    def __init__(self):
        self.shift = 0

    def redrawWindow(self, surface, background):
        if self.shift > background.get_width():
            self.shift = 0
        else:
            self.shift += BACKGROUND_SPEED

        surface.blit(background, (-self.shift, 0))
        surface.blit(background, (background.get_width() - self.shift, 0))
