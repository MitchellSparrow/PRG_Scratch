import pygame
from globals import *
import numpy as np

# Rocket object functions


class Rocket:
    # Load rocket image(s) and scale
    # Source: https://openclipart.org/detail/261323/cartoon-moon-rocket-remix-2
    Rocket_R = pygame.image.load("Images/Rockets/Rocket1.png")
    Rocket_R_scaled = pygame.transform.scale(Rocket_R, (int(Rocket_R.get_width(
    )*Rocket_size), int(Rocket_R.get_height()*Rocket_size)))
    Rocket_L = pygame.image.load("Images/Rockets/Rocket2.png")
    Rocket_L_scaled = pygame.transform.scale(Rocket_L, (int(Rocket_L.get_width(
    )*Rocket_size), int(Rocket_L.get_height()*Rocket_size)))

    def __init__(self, width, height):
        self.image = self.Rocket_R_scaled
        # Start position of Rockets
        self.width = width
        self.height = height
        self.x_pos = 0.5 * width
        self.y_pos = 0.5 * height

    def Movement(self, width, height):
        #Rocket speeds as a proportion of window width/height
        self.Rocket_y_speed = height/180
        self.Rocket_x_speed = width/120
        
        # Movement of rocket corresponding to key pressed
        # Axis movement, borders considered
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] and self.y_pos > (BORDER/2):
            self.y_pos -= self.Rocket_y_speed  # Move up by y unit

        elif key[pygame.K_DOWN] and self.y_pos < (height - (BORDER/2) - self.image.get_height()):
            self.y_pos += self.Rocket_y_speed  # Move down by y unit

        if key[pygame.K_LEFT] and self.x_pos > (BORDER/2):
            self.x_pos -= self.Rocket_x_speed  # Move left by x unit
            self.image = self.Rocket_L_scaled

        elif key[pygame.K_RIGHT] and self.x_pos < (width - (BORDER/2) - self.image.get_width()):
            self.x_pos += self.Rocket_x_speed  # Move right by x unit
            self.image = self.Rocket_R_scaled

    def Draw(self, surface):
        # Drawing sprite onto surface at current position
        surface.blit(self.image, (self.x_pos, self.y_pos))

        
    def DrawRect(self, surface):
        self.topleft = (self.x_pos, self.y_pos)
        self.Rect = self.image.get_rect(topleft=(self.topleft))
        pygame.draw.rect(surface, BLACK, self.Rect, 2)
