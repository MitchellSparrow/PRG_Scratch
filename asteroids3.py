import pygame
import random
from globals import *
    
class Asteroid():
    Asteroid1= pygame.image.load("Images/Asteroids/Asteroid1.png")
    Asteroid1_scaled= pygame.transform.scale(Asteroid1, ((int(Asteroid1.get_width()*Asteroid_size), int(Asteroid1.get_height() *Asteroid_size))))
    Asteroid2= pygame.image.load("Images/Asteroids/Asteroid2.png")
    Asteroid2_scaled= pygame.transform.scale(Asteroid2, ((int(Asteroid2.get_width()*Asteroid_size), int(Asteroid2.get_height() *Asteroid_size))))
    Asteroid3= pygame.image.load("Images/Asteroids/Asteroid3.png")
    Asteroid3_scaled= pygame.transform.scale(Asteroid3, ((int(Asteroid3.get_width()*Asteroid_size), int(Asteroid3.get_height() *Asteroid_size))))
    
    def __init__(self):
        self.image = self.Asteroid_scaled
        self.rect = self.image.get_rect(topleft = (WIDTH, random.randrange(100, HEIGHT)))
        
    def Movement(self):
        self.x -= 10                  
        
    def Draw(self, surface):
        surface.blit(self.image, (self.x_pos, self.y_pos))
        
    def DrawRect(self, surface):
        self.topleft = (self.x, self.y)
        self.rect = self.image.get_rect(topleft= (self.topleft))
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        
    def checkCollision(self, rocket):
        col = self.rect.colliderect(rocket.Rect)
        if col == True:
            pygame.quit()

class Asteroid1(Asteroid):
    def __init__(self):
        self.image = self.Asteroid1_scaled
        self.rect = self.image.get_rect(topleft = (WIDTH, random.randrange(100, HEIGHT)))
        
       
class Asteroid2(Asteroid):
    def __init__ (self):
        self.image = self.Asteroid2_scaled
        self.rect = self.image.get_rect(topleft = (WIDTH, random.randrange(100, HEIGHT)))

               
class Asteroid3(Asteroid):
    def __init__(self):
        self.image = self.Asteroid3_scaled
        self.rect = self.image.get_rect(topleft = (WIDTH, random.randrange(100, HEIGHT)))