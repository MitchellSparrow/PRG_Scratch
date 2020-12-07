import pygame
import os
import platform
from globals import *
from Rocket2 import Rocket
import pickle


class run_scratch:
    click = False
    play_music = True
    highscore = 0
    height = 600
    width = 1000
    fullscreen = False
    quit = False

    def __init__(self):
        # Initialize pygame
        pygame.init()

        # try to load the settings file
        try:
            file = open("settings.txt", "rb")  # read binary
            settings = pickle.load(file)
            self.play_music = settings['play_music']
            self.highscore = settings['highscore']
            self.height = settings['height']
            self.width = settings['width']
            file.close()
        except FileNotFoundError:
            pass
        
        self.max_width, self.max_height = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.screen = pygame.display.set_mode(
            (self.width, self.height), pygame.RESIZABLE)
        self.background = pygame.image.load(
            "./Images/Backgrounds/Space_Background_1080.jpg")
        pygame.display.set_caption("Flappy Rocket")
        self.rocket_image = pygame.image.load("./Images/Rockets/Rocket1.png")
        self.clock = pygame.time.Clock()
        self.background_music = pygame.mixer.music.load(
            "./Music/background.mp3")
        self.flash_count = 0

        if self.play_music:
            pygame.mixer.music.play(
                -1)

        self.rocket = Rocket(self.width, self.height)
        self.Trocket = Rocket(self.width, self.height)

        # Run game
        self.run()

    def show_home_screen(self):
        
        self.screen.blit(self.background, (0, 0))
        rotated_rocket = pygame.transform.rotate(self.rocket_image, 25)
        self.screen.blit(rotated_rocket, (self.width/10, self.height/2))
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(
            self.width/2-75, self.height*4/5 - 12.5, 150, 50)
        
        button_2 = pygame.Rect(
            self.width/2-75, self.height*7/10 - 12.5, 150, 50)

        if button_1.collidepoint((mx, my)):
            if self.click:
                self.settings()

        if button_2.collidepoint((mx, my)):
            if self.click:
                self.tutorial()
                
        pygame.draw.rect(self.screen, LIGHTBLUE, button_1, border_radius=20)
        pygame.draw.rect(self.screen, LIGHTBLUE, button_2, border_radius=20)
        
        self.draw_text("Settings", 20, WHITE,
                       self.width/2, self.height*4/5)
        self.draw_text("Tutorial", 20, WHITE,
                       self.width/2, self.height*7/10)

        self.click = False
        self.flash_count += 10
        
        if self.fullscreen:
            self.draw_text(TITLE, 72, WHITE,
                       self.width / 2, self.height / 5)
            self.draw_text(f"High Score: {self.highscore}",
                       48, WHITE, self.width / 2, self.height / 3)
            if self.flash_count % 120 == 0:
                self.draw_text("Press space to start playing!",
                       48, BLACK, self.width / 2, self.height / 1.8)
            else:
                self.draw_text("Press space to start playing!",
                       48, WHITE, self.width / 2, self.height / 1.8)
        else:
            self.draw_text(TITLE, 48, WHITE,
                       self.width / 2, self.height / 5)
            self.draw_text(f"High Score: {self.highscore}",
                       22, WHITE, self.width / 2, self.height / 3)  
            if self.flash_count % 120 == 0:
                self.draw_text("Press space to start playing!",
                       22, BLACK, self.width / 2, self.height / 1.8)
            else:
                self.draw_text("Press space to start playing!",
                       22, WHITE, self.width / 2, self.height / 1.8)
            
        pygame.display.flip()

    def play(self):
        running = True

        while running:
            self.screen.blit(self.background, (0, 0))

            key = pygame.key.get_pressed()
            
            self.rocket.Movement(self.width, self.height) 
            self.rocket.Draw(self.screen)
            self.rocket.DrawRect(self.screen)
            
            pygame.display.update()
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                    running = False
                    self.quit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.VIDEORESIZE:
                    if self.fullscreen is not True:
                        self.width = event.w
                        self.height = event.h
                        self.screen = pygame.display.set_mode(
                            (event.w, event.h), pygame.RESIZABLE)

        # after the game finishes, update the high score if needed
        score = 0
        if score > self.highscore:
            self.highscore = score

    def tutorial(self):
        running = True

        while running:
            #Background
            self.screen.blit(self.background, (0, 0))

            #Tutorial rocket
            key = pygame.key.get_pressed()
            self.Trocket.Movement(self.width, self.height) 
            self.Trocket.Draw(self.screen)

            #Tutorial screen text
            if self.fullscreen:
                self.draw_text("Tutorial",
                               72, WHITE, self.width / 2, self.height / 7)
                self.draw_text("The Up, Down, Left, Right arrowkeys move your rocket. You can test this now!",
                               48, WHITE, self.width / 2, 2*self.height / 7 )
                self.draw_text("Avoid the asteroids for as long as possible",
                               48, WHITE, self.width / 2, 3*self.height / 7)
                self.draw_text("Your score increases over time, try to beat the high score!",
                               48, WHITE, self.width / 2, 4*self.height / 7)
            else:
                self.draw_text("Tutorial",
                               48, WHITE, self.width / 2, self.height / 7)
                self.draw_text("The Up, Down, Left, Right arrowkeys move your rocket. You can test this now!",
                               22, WHITE, self.width / 2, 2*self.height / 7 )
                self.draw_text("Avoid the asteroids for as long as possible",
                               22, WHITE, self.width / 2, 3*self.height / 7)
                self.draw_text("Your score increases over time, try to beat the high score!",
                               22, WHITE, self.width / 2, 4*self.height / 7)
            
            pygame.display.update()
            self.clock.tick(FPS)
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                    running = False
                    self.quit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.VIDEORESIZE:
                    if self.fullscreen is not True:
                        self.width = event.w
                        self.height = event.h
                        self.screen = pygame.display.set_mode(
                            (event.w, event.h), pygame.RESIZABLE)
    
    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(pygame.font.match_font(FONT_NAME), size)
        #font = pygame.font.Font("./Fonts/Pixelated_Regular.ttf", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def settings(self):
        running = True
        self.click = False

        while running:

            mx, my = pygame.mouse.get_pos()
            self.screen.blit(self.background, (0, 0))

            self.draw_text("SETTINGS", 48, WHITE,
                           self.width / 2, self.height / 7)
            self.draw_text("Press ESC to go back",
                           48, WHITE, self.width / 2, self.height / 3.5)
            self.draw_text("MUSIC",
                           48, WHITE, self.width / 3, self.height / 2)
            self.draw_text("FULLSCREEN",
                           48, WHITE, self.width / 3, int(self.height / 1.5))
            
            #Create ON/OFF buttons
            on_off_button = pygame.Rect(
                self.width*2/3 - 30, self.height/2 - 7.5, 60, 40)
            
            on_off_button2 = pygame.Rect(
                self.width*2/3 - 30, int(self.height/1.5 - 7.5), 60, 40)
            
            #MUSIC option
            if self.play_music:
                pygame.draw.rect(self.screen, LIGHTBLUE,
                                 on_off_button, border_radius=20)
                self.draw_text("ON", 20, WHITE,
                               self.width*2/3, self.height/2)
            else:
                pygame.draw.rect(self.screen, WHITE,
                                 on_off_button, border_radius=20)
                self.draw_text("OFF", 20, LIGHTBLUE,
                               self.width*2/3, self.height/2)

            if on_off_button.collidepoint((mx, my)):
                if self.click:
                    if self.play_music:
                        pygame.mixer.music.pause()
                        self.play_music = False
                    else:
                        pygame.mixer.music.play(-1)
                        self.play_music = True
            
           #FULLSCREEN option - Cannot handle dual monitors with different resolutions
            if self.fullscreen:
                pygame.draw.rect(self.screen, LIGHTBLUE,
                                 on_off_button2, border_radius=20)
                self.draw_text("ON", 20, WHITE,
                               self.width*2/3, self.height/1.5)
            else:
                pygame.draw.rect(self.screen, WHITE,
                                 on_off_button2, border_radius=20)
                self.draw_text("OFF", 20, LIGHTBLUE,
                               self.width*2/3, self.height/1.5)

            if on_off_button2.collidepoint((mx, my)):
                if self.click:                        
                    self.fullscreen = not self.fullscreen
                    if self.fullscreen is True:
                        bg_path = "./Images/Backgrounds/Space_Background_" + str(self.max_height) + ".jpg"
                        self.background = pygame.image.load(bg_path)
                        self.width = self.max_width
                        self.height = self.max_height
                        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
                    else:
                        bg_path = "./Images/Backgrounds/Space_Background_1080.jpg"
                        self.background = pygame.image.load(bg_path)
                        self.screen = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)

            
            self.click = False
            pygame.display.update()
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                    running = False
                    self.quit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                if event.type == pygame.VIDEORESIZE:
                    if self.fullscreen is not True:
                        self.width = event.w
                        self.height = event.h
                        self.screen = pygame.display.set_mode(
                            (event.w, event.h), pygame.RESIZABLE)

    def run(self):

        while not self.quit:
            self.show_home_screen()
            self.clock.tick(FPS)
            e = pygame.event.poll()
            if e.type == pygame.QUIT:
                self.exit()
                break
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    self.click = True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.play()
            if e.type == pygame.VIDEORESIZE:
                if self.fullscreen is not True:
                    self.width = e.w
                    self.height = e.h
                    self.screen = pygame.display.set_mode(
                        (e.w, e.h), pygame.RESIZABLE)

    def exit(self):
        # Program termination
        running = False
        if platform.system() in ['Windows', 'Linux']:
            pygame.quit()  # for Windows or Linux users
        else:
            os._exit(0)  # for Mac users.

        file = open("settings.txt", "wb")  # write binary
        pickle.dump({'play_music': self.play_music,
                     'highscore': self.highscore,
                     'width': self.width,
                     'height': self.height}, file)
        file.close()


# Lets run the game
run_scratch()
