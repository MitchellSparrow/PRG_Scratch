# -*- coding: utf-8 -*-
import pygame
from globals import *
import random

difficulty = 10

class Asteroid:
    Asteroid1= pygame.image.load("Images/Asteroids/Asteroid1.png")
    Asteroid1_scaled= pygame.transform.scale(Asteroid1, 
                                             ((int(Asteroid1.get_width()*Asteroid_size), int(Asteroid1.get_height() *Asteroid_size))))
    Asteroid2= pygame.image.load("Images/Asteroids/Asteroid2.png")
    Asteroid2_scaled= pygame.transform.scale(Asteroid2, 
                                             ((int(Asteroid2.get_width()*Asteroid_size), int(Asteroid2.get_height() *Asteroid_size))))
    Asteroid3= pygame.image.load("Images/Asteroids/Asteroid3.png")
    Asteroid3_scaled= pygame.transform.scale(Asteroid3, 
                                             ((int(Asteroid3.get_width()*Asteroid_size), int(Asteroid3.get_height() *Asteroid_size))))
       
    def __init__(self, width, height):
        self.image = self.Asteroid1_scaled
        self.x_pos = WIDTH
        self.y_pos = random.randrange(100, 900)

    def Movement(self):
        self.x_pos -= difficulty                  
            
    def Draw(self, surface):
        surface.blit(self.image, (self.x_pos, self.y_pos))

    def checkCollision(sprite1, sprite2):
        col = sprite1.rect.colliderect(sprite2.rect)
        if col == True:
            pygame.quit()
            

pygame.time.set_timer(USEREVENT+2, 1000)
pygame.time.set_timer(USEREVENT+3, 10000)
#Spawn a random asteroid every second

while run:
      
    if event.type == USEREVENT+2:
        r = random.randrange(0,3)
        if r == 0:
            asteroid.draw(asteroid1)
        elif r == 1:
            asteroid.draw(asteroid2)
        if r == 3:
            asteroid.draw(asteroid3)
    if event.type == USEREVENT+3:
        difficulty +=5
# Could be used to indicate progressing to the next level
    Asteroid.checkCollision(asteroid.image, rocket.image)