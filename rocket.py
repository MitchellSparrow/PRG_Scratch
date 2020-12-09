import pygame
from globals import *
import numpy as np

# Rocket object functions


class Rocket:
    # Load rocket image(s) and scale
    # Source: https://openclipart.org/detail/261323/cartoon-moon-rocket-remix-2
    Rocket_R = pygame.image.load("Images/Rockets/Rocket1.png")
    Rocket_L = pygame.image.load("Images/Rockets/Rocket2.png")

    FS_Rocket_R = pygame.transform.scale(Rocket_R, (int(Rocket_R.get_width(
    )/ROCKET_FS_SCALING), int(Rocket_R.get_height()/ROCKET_FS_SCALING)))
    FS_Rocket_L = pygame.transform.scale(Rocket_L, (int(Rocket_L.get_width(
    )/ROCKET_FS_SCALING), int(Rocket_L.get_height()/ROCKET_FS_SCALING)))

    Rocket_R = pygame.transform.scale(Rocket_R, (int(Rocket_R.get_width(
    )/ROCKET_NORMAL_SCALING), int(Rocket_R.get_height()/ROCKET_NORMAL_SCALING)))
    Rocket_L = pygame.transform.scale(Rocket_L, (int(Rocket_L.get_width(
    )/ROCKET_NORMAL_SCALING), int(Rocket_L.get_height()/ROCKET_NORMAL_SCALING)))
    
    #Load explosion images
    #Source: https://opengameart.org/content/explosions-2 credit: helpcomputer
    Explosions = [pygame.image.load("Images/Explosions/Explosion1.png"), 
                  pygame.image.load("Images/Explosions/Explosion2.png"),
                  pygame.image.load("Images/Explosions/Explosion3.png"),
                  pygame.image.load("Images/Explosions/Explosion4.png"),
                  pygame.image.load("Images/Explosions/Explosion5.png"),
                  pygame.image.load("Images/Explosions/Explosion6.png"),
                  pygame.image.load("Images/Explosions/Explosion7.png"),
                  pygame.image.load("Images/Explosions/Explosion8.png"),
                  pygame.image.load("Images/Explosions/Explosion9.png")]
    
    FS_Explosions = []
    
    for i in Explosions:
        FS_Explosions.append(pygame.transform.scale(i, (int(i.get_width(
    )*EXPLOSION_FS_SCALING), int(i.get_height()*EXPLOSION_FS_SCALING)))

    def __init__(self, width, height, fullscreen):
        self.fullscreen = fullscreen
        if self.fullscreen == True:
            self.image = self.FS_Rocket_R
        else:
            self.image = self.Rocket_R

        # Start position of Rockets
        self.width = width
        self.height = height
        self.x_pos = 0.5 * width
        self.y_pos = 0.5 * height

    def reset(self, width, height):
        if self.fullscreen == True:
            self.image = self.FS_Rocket_R
        else:
            self.image = self.Rocket_R
        # Start position of Rockets
        self.x_pos = width
        self.y_pos = height

    def Movement(self, width, height):
        # Rocket speeds as a proportion of window width/height
        self.Rocket_y_speed = height/180
        self.Rocket_x_speed = width/120

        # Movement of rocket corresponding to key pressed
        # Axis movement, borders considered
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] and self.y_pos > (BORDER/2):
            self.y_pos -= self.Rocket_y_speed  # Move up by y unit

        elif key[pygame.K_DOWN] and self.y_pos < (height - (BORDER/2) - self.image.get_height()):
            self.y_pos += self.Rocket_y_speed  # Move down by y unit

        if key[pygame.K_LEFT] and self.x_pos > (BORDER/2):
            self.x_pos -= self.Rocket_x_speed  # Move left by x unit
            if self.fullscreen == True:
                self.image = self.FS_Rocket_L
            else:
                self.image = self.Rocket_L

        elif key[pygame.K_RIGHT] and self.x_pos < (width - (BORDER/2) - self.image.get_width()):
            self.x_pos += self.Rocket_x_speed  # Move right by x unit
            if self.fullscreen == True:
                self.image = self.FS_Rocket_R
            else:
                self.image = self.Rocket_R

    def Draw(self, surface):
        # Drawing sprite onto surface at current position
        surface.blit(self.image, (self.x_pos, self.y_pos))

    def DrawRect(self, surface):
        self.topleft = (self.x_pos, self.y_pos)
        self.Rect = self.image.get_rect(topleft=(self.topleft))

    def Explosion(self, surface, clock):
        if self.fullscreen == True: 
            for pic in self.FS_Explosions:
                self.image = pic
                surface.blit(self.image, (self.x_pos, self.y_pos))
                clock.tick(0.5*FPS)
        else:
            for pic in self.Explosions:
                self.image = pic
                surface.blit(self.image, (self.x_pos, self.y_pos))
                clock.tick(0.5*FPS)
            
            
            