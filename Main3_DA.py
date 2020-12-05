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

    def __init__(self):
        # Initialize pygame
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.image.load(
            "./Images/Backgrounds/Space_Background.jpg")
        pygame.display.set_caption("Flappy Rocket")
        self.rocket_image = pygame.image.load("./Images/Rockets/Rocket1.png")
        self.clock = pygame.time.Clock()
        self.background_music = pygame.mixer.music.load(
            "./Music/background.mp3")

        # try to load the settings file
        try:
            file = open("settings.txt", "rb")  # read binary
            settings = pickle.load(file)
            self.play_music = settings['play_music']
            self.highscore = settings['highscore']
            file.close()
        except FileNotFoundError:
            pass

        if self.play_music:
            pygame.mixer.music.play(
                -1)

        self.rocket = Rocket()

        # Run game
        self.run()

    def show_home_screen(self):

        self.screen.blit(self.background, (0, 0))
        rotated_rocket = pygame.transform.rotate(self.rocket_image, 25)
        self.screen.blit(rotated_rocket, (WIDTH/10, HEIGHT/2))
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(WIDTH/2-75, HEIGHT*4/5 - 12.5, 150, 50)

        if button_1.collidepoint((mx, my)):
            if self.click:
                self.settings()

        pygame.draw.rect(self.screen, LIGHTBLUE, button_1, border_radius=20)

        self.draw_text("Settings", 20, WHITE,
                       WIDTH/2, HEIGHT*4/5)

        self.click = False

        self.draw_text(TITLE, 48, WHITE,
                       WIDTH / 2, HEIGHT / 5)
        self.draw_text("Press space to start playing!",
                       22, WHITE, WIDTH / 2, HEIGHT / 1.8)
        self.draw_text(f"High Score: {self.highscore}",
                       22, WHITE, WIDTH / 2, HEIGHT / 3)

        pygame.display.flip()

    def play(self):
        running = True

        while running:
            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.VIDEORESIZE:
                    if FULLSCREEN == False:
                        self.screen = pygame.display.set_mode(
                            (event.w, event.h), pygame.RESIZABLE)

            key = pygame.key.get_pressed()

            self.rocket.Movement()
            self.rocket.Draw(self.screen)

            pygame.display.update()
            self.clock.tick(FPS)

        # after the game finishes, update the high score if needed
        score = 0
        if score > self.highscore:
            self.highscore = score

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(pygame.font.match_font(FONT_NAME), size)
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
                           WIDTH / 2, HEIGHT / 7)

            self.draw_text("Press ESC to go back",
                           22, WHITE, WIDTH / 2, HEIGHT / 3.5)

            self.draw_text("MUSIC",
                           22, WHITE, WIDTH / 3, HEIGHT / 2)

            on_off_button = pygame.Rect(
                WIDTH*2/3 - 30, HEIGHT/2 - 7.5, 60, 40)

            if self.play_music:
                pygame.draw.rect(self.screen, LIGHTBLUE,
                                 on_off_button, border_radius=20)
                self.draw_text("ON", 20, WHITE,
                               WIDTH*2/3, HEIGHT/2)
            else:
                pygame.draw.rect(self.screen, WHITE,
                                 on_off_button, border_radius=20)
                self.draw_text("OFF", 20, LIGHTBLUE,
                               WIDTH*2/3, HEIGHT/2)

            if on_off_button.collidepoint((mx, my)):
                if self.click:
                    if self.play_music:
                        pygame.mixer.music.pause()
                        self.play_music = False
                    else:
                        pygame.mixer.music.play(-1)
                        self.play_music = True

            self.click = False

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                if event.type == pygame.VIDEORESIZE:
                    if FULLSCREEN == False:
                        self.screen = pygame.display.set_mode(
                            (event.w, event.h), pygame.RESIZABLE)

            pygame.display.update()
            self.clock.tick(FPS)

    def run(self):

        while True:
            e = pygame.event.poll()
            if e.type == pygame.QUIT:
                self.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    self.click = True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.play()
            if e.type == pygame.VIDEORESIZE:
                if FULLSCREEN == False:
                    self.screen = pygame.display.set_mode(
                        (e.w, e.h), pygame.RESIZABLE)

            self.show_home_screen()
            self.clock.tick(FPS)

    def exit(self):
        # Program termination
        if platform.system() in ['Windows', 'Linux']:
            pygame.quit()  # for Windows or Linux users
        else:
            os._exit(0)  # for Mac users.

        file = open("settings.txt", "wb")  # write binary
        pickle.dump({'play_music': self.play_music,
                     'highscore': self.highscore}, file)
        file.close()


# Lets run the game
run_scratch()
