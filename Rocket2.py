import pygame
import globals
import numpy as np

# Rocket object functions


class Rocket:
    # Load rocket image(s) and scale
    # Source: https://openclipart.org/detail/261323/cartoon-moon-rocket-remix-2
    Rocket_R = pygame.image.load("Images/Rockets/Rocket1.png")
    Rocket_R_scaled = pygame.transform.scale(Rocket_R, (int(Rocket_R.get_width(
    )*globals.Rocket_size), int(Rocket_R.get_height()*globals.Rocket_size)))
    Rocket_L = pygame.image.load("Images/Rockets/Rocket2.png")
    Rocket_L_scaled = pygame.transform.scale(Rocket_L, (int(Rocket_L.get_width(
    )*globals.Rocket_size), int(Rocket_L.get_height()*globals.Rocket_size)))

    def _init_(self):
        self.image = self.Rocket_R_scaled
        # Start position of Rocket
        self.x_pos = 0.5 * globals.WIDTH
        self.y_pos = 0.5 * globals.HEIGHT

    def Movement(self):
        # Movement of rocket corresponding to key pressed
        # Axis unit of movement is specified in globals module, borders considered
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] and self.y_pos > globals.BORDER:
            self.y_pos += globals.Rocket_y_speed  # Move up by y unit

        elif key[pygame.K_DOWN] and self.y_pos < (globals.HEIGHT - globals.BORDER - self.image.get_height()):
            self.y_pos -= globals.Rocket_y_speed  # Move down by y unit

        if key[pygame.K_LEFT] and self.x_pos > globals.BORDER:
            self.x_pos -= globals.Rocket_x_speed  # Move left by x unit
            self.image = self.Rocket_L_scaled

        elif key[pygame.K_RIGHT] and self.x_pos < (globals.WIDTH - globals.BORDER - self.image.get_width()):
            self.x_pos += globals.Rocket_x_speed  # Move right by x unit
            self.image = self.Rocket_R_scaled

    def Draw(self, surface):
        # Drawing sprite onto surface at current position
        surface.blit(self.image, (self.x_pos, self.y_pos))
