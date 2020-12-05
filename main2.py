import pygame
import os
import platform
from globals import *
from Rocket2 import Rocket


class run_scratch:
    click = False

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
                       WIDTH / 2, HEIGHT / 4)
        self.draw_text("Press space to start playing!",
                       22, WHITE, WIDTH / 2, HEIGHT / 2)
        pygame.display.flip()

    def play(self):
        running = True

        while running:
            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if platform.system() in ['Windows', 'Linux']:
                        pygame.quit()
                    else:
                        os._exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            key = pygame.key.get_pressed()

            self.rocket.Movement()
            self.rocket.Draw(self.screen)

            pygame.display.update()
            self.clock.tick(FPS)

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
            self.screen.blit(self.background, (0, 0))

            mx, my = pygame.mouse.get_pos()

            mute_button = pygame.Rect(WIDTH*2/3-75, HEIGHT*4/5 - 12.5, 150, 50)
            unmute_button = pygame.Rect(WIDTH/3-75, HEIGHT*4/5 - 12.5, 150, 50)

            pygame.draw.rect(self.screen, LIGHTBLUE,
                             mute_button, border_radius=20)

            self.draw_text("Mute Music", 20, WHITE,
                           WIDTH*2/3, HEIGHT*4/5)

            pygame.draw.rect(self.screen, WHITE,
                             unmute_button, border_radius=20)

            self.draw_text("Unmute Music", 20, LIGHTBLUE,
                           WIDTH/3, HEIGHT*4/5)

            if mute_button.collidepoint((mx, my)):
                if self.click:
                    pygame.mixer.music.pause()

            if unmute_button.collidepoint((mx, my)):
                if self.click:
                    pygame.mixer.music.play(-1)

            self.click = False

            self.draw_text("Press ESC to go back",
                           22, WHITE, WIDTH / 2, HEIGHT / 2)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if platform.system() in ['Windows', 'Linux']:
                        pygame.quit()
                    else:
                        os._exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            pygame.display.update()
            self.clock.tick(FPS)

    def music_toggle(self):
        pass

    def run(self):
        # self.show_home_screen()
        # waiting = True

        while True:
            e = pygame.event.poll()
            if e.type == pygame.QUIT:
                break
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    self.click = True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    self.play()

            self.show_home_screen()
            self.clock.tick(FPS)

        # Program termination
        if platform.system() in ['Windows', 'Linux']:
            pygame.quit()  # for Windows or Linux users
        else:
            os._exit(0)  # for Mac users.


# Lets run the game
run_scratch()
