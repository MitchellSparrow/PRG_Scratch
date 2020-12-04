import pygame
import os
import platform
from globals import *


class run_scratch:
    click = False

    def __init__(self):
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background = pygame.image.load(
            "./Images/Backgrounds/Space_Background.jpg")
        pygame.display.set_caption("Flappy Rocket")
        self.rocket = pygame.image.load("./Images/Rockets/Rocket1.png")
        self.clock = pygame.time.Clock()
        # Run game
        self.run()

    def show_home_screen(self):

        self.screen.blit(self.background, (0, 0))
        rotated_rocket = pygame.transform.rotate(self.rocket, 25)
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
            self.draw_text("Playing",
                           22, WHITE, WIDTH / 2, HEIGHT / 2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    os._exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

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
        while running:
            self.screen.blit(self.background, (0, 0))
            self.draw_text("settings",
                           22, WHITE, WIDTH / 2, HEIGHT / 2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    os._exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()
            self.clock.tick(FPS)

    def music_toggle(self):
        pass

    def run(self):
        # self.show_home_screen()
        #waiting = True

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
        if platform.system() in ['Windows','Linux']:
            pygame.quit()  # for Windows or Linux users
        else:
            os._exit(0)  # for Mac users.


# Lets run the game
run_scratch()
