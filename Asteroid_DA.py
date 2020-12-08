   
import pygame
import random
from globals import *


class Asteroid:
    collision = False
    points = 1
    
    #Asteroid images downloaded from:
    #1: https://www.clipartkey.com/view/hmJJTx_asteroid-sprite-clip-art-asteroid-transparent-background/
    #2: https://www.clipartkey.com/view/JRTbTo_asteroid-png-picture-asteroid/
    #3: https://www.clipartkey.com/view/mmbhJw_clip-art-asteroid-picture-transparent-psyche-asteroid/
    asteroid_images = [pygame.image.load("Images/Asteroids/Asteroid1.png"), pygame.image.load("Images/Asteroids/Asteroid2.png"),pygame.image.load("Images/Asteroids/Asteroid3.png")]

    
    def __init__(self, width, height):
        rnum = random.randint(0,2)
        self.image = self.asteroid_images[rnum]
        self.image = pygame.transform.scale(self.image, ((int(self.image.get_width()*Aminsize/1000), int(self.image.get_height() *Aminsize/1000))))
        self.width = width
        self.height = height
        self.x_pos = width
        self.y_pos = random.randrange(0, int(height - height/20))
        self.difficulty = 1

    def reset(self, width, height):
        self.points = 0
        self.difficulty = 1
        self.collision = False
        rnum = random.randint(0,2)
        self.image = self.asteroid_images[rnum]
        self.image = pygame.transform.scale(self.image, ((int(self.image.get_width()*Aminsize/1000), int(self.image.get_height() *Aminsize/1000))))
        self.width = width
        self.height = height
        self.x_pos = width
        self.y_pos = random.randrange(0, int(height - height/20))

    def Movement(self, width, height):
        Asteroid_speed = int(width/200)
        if self.x_pos > - self.image.get_width():
            self.x_pos -= self.difficulty * Asteroid_speed 
        else:
            rnum= random.randint(0,2)
            rnum2 = random.randrange(Aminsize, Amaxsize)/1000
            self.image = self.asteroid_images[rnum]
            self.image = pygame.transform.scale(self.image, ((int(self.image.get_width()*rnum2), int(self.image.get_height() *rnum2))))
            self.points += 1
            self.x_pos = width
            self.y_pos = random.randrange(0, int(height - height/20))
        
        if self.points % 10 == 0:
            self.difficulty += 0.01
        

    def Draw(self, surface):
        surface.blit(self.image, (self.x_pos, self.y_pos))

    def DrawRect(self, surface):
        self.topleft = (self.x_pos, self.y_pos)
        self.rect = self.image.get_rect(topleft=(self.topleft))
        pygame.draw.rect(surface, WHITE, self.rect, 2)

    def checkCollision(self, rocket):
        col = self.rect.colliderect(rocket.Rect)
        if col == True:
            self.collision = True