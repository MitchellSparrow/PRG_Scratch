
import pygame
import random
from globals import *


class Asteroid:
    collision = False
    points = 1

    # Asteroid images downloaded from:
    # 1: https://www.clipartkey.com/view/hmJJTx_asteroid-sprite-clip-art-asteroid-transparent-background/
    # 2: https://www.clipartkey.com/view/JRTbTo_asteroid-png-picture-asteroid/
    # 3: https://www.clipartkey.com/view/mmbhJw_clip-art-asteroid-picture-transparent-psyche-asteroid/
    # 4: https://www.clipartkey.com/view/hmJJih_free-asteroid-png-pic-download-vector-clipart-psd/
    # 5: https://www.clipartkey.com/view/hmJwhT_asteroids-meteoroid-clip-art-transparent-background-asteroid-png/
    # 6: https://www.clipartkey.com/view/ThhTJo_asteroid-belt-meteoroid-clip-art-transparent-background-asteroid/

    asteroid_images = [pygame.image.load("Images/Asteroids/Asteroid1.png"), pygame.image.load(
        "Images/Asteroids/Asteroid2.png"), pygame.image.load("Images/Asteroids/Asteroid3.png")]

    def __init__(self, width, height, init_val):
        rnum = random.randint(0, 2)
        self.image = self.asteroid_images[rnum]
        self.image = pygame.transform.scale(self.image, ((int(self.image.get_width(
        )*Aminsize/1000), int(self.image.get_height() * Aminsize/1000))))
        self.width = width
        self.height = height
        self.x_pos = init_val
        self.y_pos = random.randrange(0, int(height - height/20))
        self.difficulty = DIFFICULTY

    def run(self, surface, rocket,  width, height):
        ''' Main function'''
        self.Movement(width, height)
        self.Draw(surface)
        self.checkCollision(rocket)

    def reset(self, width, height, init_val):
        self.points = 1
        self.difficulty = DIFFICULTY
        self.collision = False
        rnum = random.randint(0, 2)
        self.image = self.asteroid_images[rnum]
        self.image = pygame.transform.scale(self.image, ((int(self.image.get_width(
        )*Aminsize/1000), int(self.image.get_height() * Aminsize/1000))))
        self.width = width
        self.height = height
        self.x_pos = init_val
        self.y_pos = random.randrange(0, int(height - self.image.get_height()))

    def Movement(self, width, height):
        Asteroid_speed = int(width/500) + self.difficulty
        if self.x_pos > - self.image.get_width():
            self.x_pos -= Asteroid_speed
        else:
            rnum = random.randint(0, 2)
            rnum2 = random.randrange(Aminsize, Amaxsize)/1000
            self.image = self.asteroid_images[rnum]
            self.image = pygame.transform.scale(self.image, ((
                int(self.image.get_width()*rnum2), int(self.image.get_height() * rnum2))))
            self.points += 1
            self.x_pos = width
            self.y_pos = random.randrange(
                0, int(height - self.image.get_height()))

        if self.points % 5 == 0:
            self.difficulty += 0.01

    def Draw(self, surface):
        surface.blit(self.image, (self.x_pos, self.y_pos))
        self.topleft = (self.x_pos, self.y_pos)
        self.rect = self.image.get_rect(topleft=(self.topleft))

    def checkCollision(self, rocket):
        col = self.rect.colliderect(rocket.Rect)
        if col == True:
            self.collision = True
