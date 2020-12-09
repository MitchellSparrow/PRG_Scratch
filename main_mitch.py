import pygame
import os
import platform
from globals import *
from rocket import Rocket
from Asteroids import Asteroid
import pickle


class run_scratch:

    # Default settings
    click = False
    play_music = True
    highscore = 0
    height = 600
    width = 1000
    fullscreen = False
    play_again = False
    quit = False
    count = 0

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

        # Initialise variables / Images / Clock
        self.max_width, self.max_height = pygame.display.Info(
        ).current_w, pygame.display.Info().current_h
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

        # Music initialisation
        if self.play_music:
            pygame.mixer.music.play(
                -1)

        # Run game
        self.run()

    def show_home_screen(self):

        # Background / Images on home screen
        self.screen.blit(self.background, (0, 0))
        rotated_rocket = pygame.transform.rotate(self.rocket_image, 25)
        self.screen.blit(rotated_rocket, (self.width/10, self.height/2))
        mx, my = pygame.mouse.get_pos()

        # Home screen button options
        button_1 = pygame.Rect(
            self.width/2-75, self.height*4/5 - 12.5, 150, 50)
        button_2 = pygame.Rect(
            self.width/3-75, self.height*4/5 - 12.5, 150, 50)
        button_3 = pygame.Rect(
            2*self.width/3-75, self.height*4/5 - 12.5, 150, 50)

        if button_1.collidepoint((mx, my)):
            if self.click:
                self.settings()

        if button_2.collidepoint((mx, my)):
            if self.click:
                self.tutorial()

        if button_3.collidepoint((mx, my)):
            if self.click:
                self.quit = True
                self.exit()

        pygame.draw.rect(self.screen, LIGHTBLUE, button_1, border_radius=20)
        pygame.draw.rect(self.screen, LIGHTBLUE, button_2, border_radius=20)
        pygame.draw.rect(self.screen, LIGHTBLUE, button_3, border_radius=20)

        self.draw_text("Settings", 20, WHITE,
                       self.width/2, self.height*4/5)
        self.draw_text("Tutorial", 20, WHITE,
                       self.width/3, self.height*4/5)
        self.draw_text("Quit", 20, WHITE,
                       2*self.width/3, self.height*4/5)

        # Fullscreen/Resizeable text on homescreen
        self.click = False
        self.flash_count += 10

        if self.fullscreen:
            self.draw_text_title(TITLE, 80, WHITE,
                                 self.width / 2, self.height / 6)
            self.draw_text(f"High Score: {self.highscore}",
                           30, WHITE, self.width / 2, self.height / 2.8)
            if self.flash_count % 120 == 0:
                self.draw_text("Press space to start playing!",
                               30, BLACK, self.width / 2, self.height / 1.8)
            else:
                self.draw_text("Press space to start playing!",
                               30, WHITE, self.width / 2, self.height / 1.8)
        else:
            self.draw_text_title(TITLE, 70, WHITE,
                                 self.width / 2, self.height / 6)
            self.draw_text(f"High Score: {self.highscore}",
                           22, WHITE, self.width / 2, self.height / 2.8)
            if self.flash_count % 120 == 0:
                self.draw_text("Press space to start playing!",
                               22, BLACK, self.width / 2, self.height / 1.8)
            else:
                self.draw_text("Press space to start playing!",
                               22, WHITE, self.width / 2, self.height / 1.8)

        # Initialise Rockets and Asteroids
        self.rocket = Rocket(self.width, self.height, self.fullscreen)
        self.Trocket = Rocket(self.width, self.height, self.fullscreen)

        self.asteroid = Asteroid(self.width, self.height, self.width)
        self.asteroid2 = Asteroid(self.width, self.height, self.width * 1.5)

        # Update display
        pygame.display.flip()

    def play(self):

        running = True

        # Reset rocket to original position
        self.rocket.reset(self.width / 2, self.height / 2)

        while running:
            self.screen.blit(self.background, (0, 0))
            self.draw_text(f"Score: {self.asteroid.points + self.asteroid2.points - 2}",
                           30, WHITE, 75, 10)

            # Rocket / Asteroids movements each game tick

            self.rocket.Movement(self.width, self.height)
            self.rocket.Draw(self.screen)
            self.rocket.DrawRect(self.screen)

            self.asteroid.Movement(self.width, self.height)
            self.asteroid.Draw(self.screen)
            self.asteroid.DrawRect(self.screen)
            self.asteroid.checkCollision(self.rocket)

            self.asteroid2.Movement(self.width, self.height)
            self.asteroid2.Draw(self.screen)
            self.asteroid2.DrawRect(self.screen)
            self.asteroid2.checkCollision(self.rocket)

            pygame.display.update()
            self.clock.tick(FPS)

            # Event handling - 'X' button click, ESC press, resize window
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

                # Simulate game over
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.game_over()
                        if not self.play_again:
                            running = False
                        self.rocket.reset(self.width / 2, self.height / 2)
                        self.play_again = False
                        # self.lost = True

            if self.asteroid.collision or self.asteroid2.collision:
                if self.asteroid.points > self.highscore:
                    self.highscore = self.asteroid.points + self.asteroid2.points - 2
                self.game_over()
                if not self.play_again:
                    running = False
                self.rocket.reset(self.width / 2, self.height / 2)
                self.asteroid.reset(self.width, self.height / 2, self.width)
                self.asteroid2.reset(
                    self.width, self.height / 2, self.width*1.5)
                self.play_again = False

        # After the game finishes, update the high score if needed

    def game_over(self):
        running = True

        while running:
            self.screen.blit(self.background, (0, 0))
            rotated_rocket = pygame.transform.rotate(self.rocket_image, 25)
            self.screen.blit(rotated_rocket, (self.width/10, self.height/2))
            mx, my = pygame.mouse.get_pos()

            # Text on game over screen - Fullscreen / Resizeable
            self.click = False
            self.flash_count += 10

            if self.fullscreen:
                self.draw_text_title("GAME OVER", 72, WHITE,
                                     self.width / 2, self.height / 5)
                self.draw_text(f"Score: {self.asteroid.points + self.asteroid2.points - 2}",
                               40, WHITE, self.width / 2, self.height / 3)
                self.draw_text("Press ESC to return to home",
                               30, WHITE, self.width / 2, self.height / 2.2)
                if self.flash_count % 120 == 0:
                    self.draw_text("Press space to try again!",
                                   48, BLACK, self.width / 2, self.height / 1.5)
                else:
                    self.draw_text("Press space to try again!",
                                   48, WHITE, self.width / 2, self.height / 1.5)
            else:
                self.draw_text_title("GAME OVER", 70, WHITE,
                                     self.width / 2, self.height / 6)
                self.draw_text(f"Score: {self.asteroid.points + self.asteroid2.points - 2}",
                               30, WHITE, self.width / 2, self.height / 3)
                self.draw_text("Press ESC to return to home",
                               22, WHITE, self.width / 2, self.height / 2.2)
                if self.flash_count % 120 == 0:
                    self.draw_text("Press space to try again!",
                                   22, BLACK, self.width / 2, self.height / 1.5)
                else:
                    self.draw_text("Press space to try again!",
                                   22, WHITE, self.width / 2, self.height / 1.5)

            # Update display
            pygame.display.update()
            self.clock.tick(FPS)

            # Event handling - 'X' button click, ESC press, SPACE press, resize window
            e = pygame.event.poll()
            if e.type == pygame.QUIT:
                self.exit()
                running = False
                self.quit = True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    running = False
                    self.play_again = True
            if e.type == pygame.VIDEORESIZE:
                if self.fullscreen is not True:
                    self.width = e.w
                    self.height = e.h
                    self.screen = pygame.display.set_mode(
                        (e.w, e.h), pygame.RESIZABLE)

    def tutorial(self):
        running = True
        # Reset rocket to original position
        self.Trocket.reset(self.width / 2.1, self.height / 1.5)

        while running:
            # Background
            self.screen.blit(self.background, (0, 0))

            # Tutorial rocket
            key = pygame.key.get_pressed()
            self.Trocket.Movement(self.width, self.height)
            self.Trocket.Draw(self.screen)

            # Tutorial screen text
            if self.fullscreen:
                self.draw_text_title("Tutorial",
                                     72, WHITE, self.width / 2, self.height / 7)
                self.draw_text("The Up, Down, Left, Right arrowkeys move your rocket. You can test this now!",
                               20, WHITE, self.width / 2, 2*self.height / 6)
                self.draw_text("Avoid the asteroids for as long as possible",
                               20, WHITE, self.width / 2, 3*self.height / 6)
                self.draw_text("Your score increases over time, try to beat the high score!",
                               20, WHITE, self.width / 2, 4*self.height / 6)
            else:
                self.draw_text_title("Tutorial",
                                     70, WHITE, self.width / 2, self.height / 7.5)
                self.draw_text("The Up, Down, Left, Right arrowkeys move your rocket. You can test this now!",
                               20, WHITE, self.width / 2, 2*self.height / 6)
                self.draw_text("Avoid the asteroids for as long as possible",
                               20, WHITE, self.width / 2, 3*self.height / 6)
                self.draw_text("Your score increases over time, try to beat the high score!",
                               20, WHITE, self.width / 2, 4*self.height / 6)

            # Update display
            pygame.display.update()
            self.clock.tick(FPS)

            # Event handling - 'X' button click, ESC press, resize window
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

        font = pygame.font.Font("./Fonts/GamePlayed.ttf", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_text_title(self, text, size, color, x, y):

        font = pygame.font.Font("./Fonts/Retronoid1.ttf", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def settings(self):
        running = True
        self.click = False

        while running:

            # Get mouse position
            mx, my = pygame.mouse.get_pos()

            # Draw Background and text to settings screen
            self.screen.blit(self.background, (0, 0))

            self.draw_text_title("SETTINGS", 70, WHITE,
                                 self.width / 2, self.height / 7)
            self.draw_text("Press ESC to go back",
                           22, WHITE, self.width / 2, self.height / 3)
            self.draw_text("MUSIC",
                           40, WHITE, self.width / 3, self.height / 2)
            self.draw_text("FULLSCREEN",
                           40, WHITE, self.width / 3, int(self.height / 1.5))

            # Create ON/OFF buttons
            on_off_button = pygame.Rect(
                self.width*2/3 - 30, self.height/2, 60, 40)

            on_off_button2 = pygame.Rect(
                self.width*2/3 - 30, self.height/1.5, 60, 40)

            # MUSIC option
            if self.play_music:
                pygame.draw.rect(self.screen, LIGHTBLUE,
                                 on_off_button, border_radius=20)
                self.draw_text("ON", 20, WHITE,
                               self.width*2/3, self.height/2 + 7.5)
            else:
                pygame.draw.rect(self.screen, WHITE,
                                 on_off_button, border_radius=20)
                self.draw_text("OFF", 20, LIGHTBLUE,
                               self.width*2/3, self.height/2 + 7.5)

            if on_off_button.collidepoint((mx, my)):
                if self.click:
                    if self.play_music:
                        pygame.mixer.music.pause()
                        self.play_music = False
                    else:
                        pygame.mixer.music.play(-1)
                        self.play_music = True

           # FULLSCREEN option - Cannot handle dual monitors with different resolutions
            if self.fullscreen:
                pygame.draw.rect(self.screen, LIGHTBLUE,
                                 on_off_button2, border_radius=20)
                self.draw_text("ON", 20, WHITE,
                               self.width*2/3, self.height/1.5 + 7.5)
            else:
                pygame.draw.rect(self.screen, WHITE,
                                 on_off_button2, border_radius=20)
                self.draw_text("OFF", 20, LIGHTBLUE,
                               self.width*2/3, self.height/1.5 + 7.5)

            if on_off_button2.collidepoint((mx, my)):
                if self.click:
                    self.fullscreen = not self.fullscreen
                    if self.fullscreen is True:
                        try:
                            # Load correct resolution background, update local variables and set to fullscreen mode
                            bg_path = "./Images/Backgrounds/Space_Background_" + \
                                str(self.max_height) + ".jpg"
                            self.background = pygame.image.load(bg_path)
                        except:
                            # If cant find resolution, use 1080 px height
                            bg_path = "./Images/Backgrounds/Space_Background_1080.jpg"
                            self.background = pygame.image.load(bg_path)

                        self.width = self.max_width
                        self.height = self.max_height
                        self.screen = pygame.display.set_mode(
                            (self.width, self.height), pygame.FULLSCREEN)

                    else:
                        # Load smaller background, set windo to default size
                        bg_path = "./Images/Backgrounds/Space_Background_1080.jpg"
                        self.background = pygame.image.load(bg_path)
                        self.screen = pygame.display.set_mode(
                            (1000, 600), pygame.RESIZABLE)

            # Update display
            self.click = False
            pygame.display.update()
            self.clock.tick(FPS)

            # Event handling - 'X' button click, ESC press, MOUSEBUTTON click, resize window
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

            # Show home screen
            self.show_home_screen()

            # Clock for home screen
            self.clock.tick(FPS)

            # Event handling - MOUSEBUTTON click, 'X' button click, SPACE press, resize window
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
