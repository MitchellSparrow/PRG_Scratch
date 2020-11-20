import pygame
import os
import globals


pygame.init()

screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))

screen.fill(pygame.Color("blue"))

pygame.draw.rect(screen, pygame.Color("white"),
                 pygame.Rect(0, 0, globals.WIDTH, globals.BORDER))
pygame.draw.rect(screen, pygame.Color("white"),
                 pygame.Rect(0, globals.HEIGHT-globals.BORDER, globals.WIDTH, globals.BORDER))
pygame.draw.rect(screen, pygame.Color("white"),
                 pygame.Rect(0, 0, globals.BORDER, globals.HEIGHT))

pygame.display.flip()

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

pygame.quit()  # for the rest of the people with windows or Linux
os._exit(0)  # for Mac users.
