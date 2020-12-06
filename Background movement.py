
import pygame
from pygame.locals import *
import sys
import os


W, H = 852, 480

    
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((W, H))

bg = pygame.image.load('Images/Backgrounds/Space_Background.jpg').convert()
bgX = 0
bgX2 = bg.get_width()


def redrawWindow():
    screen.blit(bg, (bgX, 0))
    screen.blit(bg, (bgX2, 0))


run = True

speed = 30
# Used to increase speed of background scroll and asteroids
pygame.time.set_timer(USEREVENT+1, 500)
# Every 500ms speed increases by one fps
while True:
    clock.tick(speed)
    redrawWindow()
    bgX -= 1.5
    bgX2 -= 1.5

    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()

    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()
# Background scrolls left until reach end of image(-ve)
# bgX2 enters the screen as bgX resets to the right
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == USEREVENT+1:
            speed += 1

    clock.tick(speed)
