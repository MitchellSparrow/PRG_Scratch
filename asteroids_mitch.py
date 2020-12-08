import pygame
import random
from globals import *


class Asteroid():
    collision = False
    points = 0
    asteroid = pygame.image.load("Images/Asteroids/Asteroid1.png")
    asteroid_scaled = pygame.transform.scale(asteroid, ((int(
        asteroid.get_width()*Asteroid_size), int(asteroid.get_height() * Asteroid_size))))

    def __init__(self, width, height):
        self.image = self.asteroid_scaled
        self.width = width
        self.height = height
        self.x_pos = width
        self.y_pos = random.randrange(0, int(height))

    def reset(self, width, height):
        self.points = 0
        self.collision = False
        self.image = self.asteroid_scaled
        self.width = width
        self.height = height
        self.x_pos = width
        self.y_pos = random.randrange(0, int(height))

    def Movement(self):
        if self.x_pos > - self.asteroid.get_width():
            self.x_pos -= difficulty
        else:
            self.points += 1
            self.x_pos = self.width
            self.y_pos = random.randrange(0, int(self.height))

    def Draw(self, surface):
        surface.blit(self.image, (self.x_pos, self.y_pos))

    def DrawRect(self, surface):
        self.topleft = (self.x_pos, self.y_pos)
        self.rect = self.image.get_rect(topleft=(self.topleft))
        pygame.draw.rect(surface, BLACK, self.rect, 2)

    def checkCollision(self, rocket):
        col = self.rect.colliderect(rocket.Rect)
        if col == True:
            self.collision = True
