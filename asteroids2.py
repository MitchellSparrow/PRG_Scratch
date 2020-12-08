import pygame
import random

    
class Asteroid():
    Asteroid1= pygame.image.load("Images/Asteroids/Asteroid1.png")
    Asteroid1_scaled= pygame.transform.scale(Asteroid1, 
                                             ((int(Asteroid1.get_width()*Asteroid_size), int(Asteroid1.get_height() *Asteroid_size))))
    Asteroid2= pygame.image.load("Images/Asteroids/Asteroid2.png")
    Asteroid2_scaled= pygame.transform.scale(Asteroid2, 
                                             ((int(Asteroid2.get_width()*Asteroid_size), int(Asteroid2.get_height() *Asteroid_size))))
    Asteroid3= pygame.image.load("Images/Asteroids/Asteroid3.png")
    Asteroid3_scaled= pygame.transform.scale(Asteroid3, 
                                             ((int(Asteroid3.get_width()*Asteroid_size), int(Asteroid3.get_height() *Asteroid_size))))
    def __init__(self, x, y, width, height):
        self.image = self.Asteroid_scaled
        self.rect = self.image.get_rect()
        Asteroid_rect.x = WIDTH
        Asteroid_rect.y = random.randrange(100,WIDTH)
        
    def Movement(self):
        self.x_pos -= difficulty                  
        
    def Draw(self, surface):
        surface.blit(self.image, (self.x_pos, self.y_pos))
        
    def DrawRect(self, surface):
        self.topleft = (self.x_pos, self.y_pos)
        self.rect = self.image.get_rect(topleft= (self.topleft))
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        
    def checkCollision(sprite1, sprite2):
        col = Asteroid.rect.colliderect(rocket.Rect)
        if col == True:
            pygame.quit()

class Asteroid1(Asteroid):
    def __init__(self, x, y, width, height):
        self.image = Asteroid1_scaled
        self.rect = self.image.get_rect()
        Asteroid1_rect.x = WIDTH
        Asteroid1_rect.y = random.randrange(100,HEIGHT)
        
    def checkCollision(sprite1, sprite2):
        col = Asteroid1.rect.colliderect(rocket.Rect)
        if col == True:
            pygame.quit()
       
class Asteroid2(Asteroid):
    def __init__ (self, x, y, width, height):
        self.image = Asteroid2_scaled
        self.rect = self.image.get_rect()
        asteroid2_rect.x = WIDTH
        asteroid2_rect.y = random.randrange(100,HEIGHT)
        
    def checkCollision(sprite1, sprite2):
        col = Asteroid2.rect.colliderect(rocket.Rect)
        if col == True:
            pygame.quit()
               
class Asteroid3(Asteroid):
    def __init__(self, x, y, width, height):
        self.image = Asteroid3_scaled
        self.rect = self.image.get_rect()
        asteroid3_rect.x = WIDTH
        asteroid3_rect.y = random.randrange(100,HEIGHT)
        
    def checkCollision(sprite1, sprite2):
        col = Asteroid3.rect.colliderect(rocket.Rect)
        if col == True:
            pygame.quit()
              
    
pygame.time.set_timer(USEREVENT+2, 1000)
pygame.time.set_timer(USEREVENT+3, 10000)
#Spawn a random asteroid every second

while run:
      
    if event.type == USEREVENT+2:
        r = random.randrange(0,3)
        if r == 0:
            Asteroid.draw(Asteroid1)
        elif r == 1:
            Asteroid.draw(Asteroid2)
        elif r == 3:
            Asteroid.draw(Asteroid3)
    if event.type == USEREVENT+3:
        difficulty +=5
# Could be used to indicate progressing to the next level
    Asteroid1.checkCollision(Asteroid1.rect, rocket.Rect)
    Asteroid2.checkCollision(Asteroid2.rect, rocket.Rect)
    Asteroid3.checkCollision(Asteroid3.rect, rocket.Rect)