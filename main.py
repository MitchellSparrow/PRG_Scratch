import pygame
import os
import platform
import globals
import Rocket


pygame.init()

#Insert background image and scale to resolution required
# Credit: Jeremy Perkins, URL: https://unsplash.com/photos/uhjiu8FjnsQ
bg_image = pygame.image.load("Images/Backgrounds/Space_Background.jpg")
pygame.transform.scale(bg_image, (globals.WIDTH, globals.HEIGHT))

#Set screen size and window title 
screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption("Flappy Rocket")

screen.fill(pygame.Color("blue"))
          
pygame.draw.rect(screen, pygame.Color("white"),
                  pygame.Rect(0, 0, globals.WIDTH, globals.BORDER))
pygame.draw.rect(screen, pygame.Color("white"),
                  pygame.Rect(0, globals.HEIGHT-globals.BORDER, globals.WIDTH, globals.BORDER))
pygame.draw.rect(screen, pygame.Color("white"),
                  pygame.Rect(0, 0, globals.BORDER, globals.HEIGHT))

#Adds background image to top layer of canvas
screen.blit(bg_image,(0,0))
            
pygame.display.flip()

#Game running loop
while True:
    
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

# Program termination
if platform.system() in ['Windows','Linux']:
    pygame.quit()  # for Windows or Linux users
else:
    os._exit(0)  # for Mac users.
