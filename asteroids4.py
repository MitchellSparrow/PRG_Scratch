import pygame
import random
from globals import *
    
class Asteroid1():
    Asteroid1= pygame.image.load("Images/Asteroids/Asteroid1.png")
    Asteroid1_scaled= pygame.transform.scale(Asteroid1, ((int(Asteroid1.get_width()*Asteroid_size), int(Asteroid1.get_height() *Asteroid_size))))
    
    def __init__(self, width, height):
        self.image = self.Asteroid1_scaled
        self.width = width
        self.height = height
        self.x_pos = width
        self.y_pos = random.randrange(0, height)
    
    def Movement(self):
        self.x_pos = -difficulty
    
    def Draw(self, surface):
        surface.blit(self.image, (self.x_pos, self.y_pos))
        
    def DrawRect(self, surface):
        self.topleft = (self.x_pos, self.y_pos)
        self.rect = self.image.get_rect(topleft= (self.topleft))
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        
    def checkCollision(self, rocket):
        col = self.rect.colliderect(rocket.Rect) 
        if col == True:
            pygame.quit()     
    
class Asteroid2():
    Asteroid2= pygame.image.load("Images/Asteroids/Asteroid2.png")
    Asteroid2_scaled= pygame.transform.scale(Asteroid2, ((int(Asteroid2.get_width()*Asteroid_size), int(Asteroid2.get_height() *Asteroid_size))))
    
    def __init__(self, width, height):
        self.image = self.Asteroid2_scaled
        self.width = width
        self.height = height
        self.x_pos = width
        self.y_pos = random.randrange(0, height)
    
    def Movement(self):
        self.x_pos =  -difficulty 
    
    def Draw(self, surface):
        surface.blit(self.image, (self.x_pos, self.y_pos))
        
    def DrawRect(self, surface):
        self.topleft = (self.x_pos, self.y_pos)
        self.rect = self.image.get_rect(topleft= (self.topleft))
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        
    def checkCollision(self, rocket):
        col = self.rect.colliderect(rocket.Rect)
        if col == True:
            pygame.quit()     
  
class Asteroid3():
    Asteroid3= pygame.image.load("Images/Asteroids/Asteroid3.png")
    Asteroid3_scaled= pygame.transform.scale(Asteroid3, ((int(Asteroid3.get_width()*Asteroid_size), int(Asteroid3.get_height() *Asteroid_size))))
    
    def __init__(self, width, height):
        self.image = self.Asteroid3_scaled
        self.width = width
        self.height = height
        self.x_pos = width
        self.y_pos = random.randrange(0, height)
    
    def Movement(self):
        self.x_pos -= difficulty
    
    def Draw(self, surface):
        surface.blit(self.image, (self.x_pos, self.y_pos))
        
    def DrawRect(self, surface):
        self.topleft = (self.x_pos, self.y_pos)
        self.rect = self.image.get_rect(topleft= (self.topleft))
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        
    def checkCollision(self, rocket):
        col = self.rect.colliderect(rocket.Rect)
        if col == True:
            pygame.quit()     