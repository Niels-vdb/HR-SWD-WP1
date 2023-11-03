import pygame
from lib.button import Button
from lib.game import Game
from lib.pause import Pause

pygame.init()

# Background Music (Rhandell)
pygame.mixer.music.load("assets/sounds/bgm.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

# Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Clock
clock = pygame.time.Clock()

# Load button images (Rob)
start_img = pygame.image.load(
    'assets/img/SnorcyStartButton.png').convert_alpha()
restart_img = pygame.image.load(
    'assets/img/SnorcyRestartButton.png').convert_alpha()
exit_img = pygame.image.load('assets/img/SnorcyExitButton.png').convert_alpha()
tutorial_image = pygame.image.load(
    "assets/img/SnorcyTutorialButton.png").convert_alpha()
back_image = pygame.image.load(
    "assets/img/SnorcyBackButton.png").convert_alpha()

# Caption and icon (Rob)
pygame.display.set_caption("Snorcy: Galactic Shooter Game")
icon = pygame.image.load('assets/img/Snow1.png').convert()
pygame.display.set_icon(icon)

# Title Game (Rob)
font = pygame.font.Font('assets/font/Monocraft.otf', 64)
title_surface = font.render('', False, (219, 13, 13))
title_rect = title_surface.get_rect(midtop=(400, 110))

# Text Tutorial (Rob)
font_tutorial = pygame.font.Font('assets/font/Pixeltype.ttf', 60)
tutorial_text_surface = font_tutorial.render(
    "Welcome To Invaders Of Snorcy.", False, (252, 194, 3))
tutorial_rect = tutorial_text_surface.get_rect(center=(400, 60))
font_tutorial_explain = pygame.font.Font('assets/font/Pixeltype.ttf', 35)
arrow_text_surface = font_tutorial_explain.render(
    "To Move Around Use W.A.S.D.", False, (255, 255, 255))
arrow_rect = arrow_text_surface.get_rect(center=(400, 240))
spacebar_text_surface = font_tutorial_explain.render(
    "To Shoot Lasers Use Your Spacebar", False, (255, 255, 255))
spacebar_text_rect = spacebar_text_surface.get_rect(center=(400, 375))
tutorial1 = font_tutorial_explain.render(
    "You Have One Minute To Eliminate The Aliens.", False, (252, 194, 3))
tutorial1_rect = tutorial1.get_rect(center=(400, 100))
tutorial2 = font_tutorial_explain.render(
    "If You Survive For One Minute, You Win!", False, (252, 194, 3))
tutorial2_rect = tutorial2.get_rect(center=(400, 130))
tutorial3 = font_tutorial_explain.render(
    "You Only Have Five Lives So Be Careful!", False, (252, 194, 3))
tutorial3_rect = tutorial3.get_rect(center=(400, 160))
tutorial4 = font_tutorial_explain.render(
    "If You Get Hit By An Asteroid Or An Alien, One Life Will Be Erased.", False, (252, 194, 3))
tutorial4_rect = tutorial4.get_rect(center=(400, 190))
tutorial5 = font_tutorial_explain.render(
    "Enjoy The Game!", False, (252, 194, 3))
tutorial5_rect = tutorial5.get_rect(center=(400, 490))
tutorial6 = font_tutorial_explain.render("GOOD LUCK!", False, (252, 194, 3))
tutorial6_rect = tutorial6.get_rect(center=(400, 520))

# Images Tutorial
arrowkeys_image = pygame.image.load(
    "assets/img/SnorcyArrowButton.png").convert_alpha()
arrowkeys_rect = arrowkeys_image.get_rect(center=(400, 300))
spacebar_image = pygame.image.load(
    "assets/img/SnorcySpaceButton.png").convert_alpha()
spacebar_rect = spacebar_image.get_rect(center=(400, 420))
arrowkeys_image = pygame.image.load(
    "assets/img/SnorcyArrowButton.png").convert_alpha()

# Background image (Rhandell)
background_menu = pygame.image.load("assets/img/SnorcyMenuBG.png").convert()
tutorial_menu = pygame.image.load(
    "assets/img/SnorcyGameBackground.png").convert()
background_win = pygame.image.load("assets/img/SnorcyWinScreen.png").convert()
background_lose = pygame.image.load("assets/img/SnorcyLoseScreen.png").convert()

# pause menu (Rob)
font_pause = pygame.font.Font('assets/font/Pixeltype.ttf', 30)
pause_text_surface = font_pause.render(
    "Press Esc to pause", False, (252, 194, 3))
pause_rect = pause_text_surface.get_rect(center=(400, 20))

# Title game won (Niels)
title_win_1 = font.render('You Have Won!', False, (219, 13, 13))
title_win_1_rect = title_surface.get_rect(center=(125, 120))
title_win_2 = font.render('Congratulations!', False, (219, 13, 13))
title_win_2_rect = title_surface.get_rect(center=(75, 225))
# Title game lost (Niels)
title_lose_1 = font.render('You Have Lost!', False, (219, 13, 13))
title_lose_1_rect = title_surface.get_rect(center=(100, 130))
title_lose_2 = font.render('Try Again', False, (219, 13, 13))
title_lose_2_rect = title_surface.get_rect(center=(205, 215))

# Create button instances (Rob)
start_button = Button(100, 280, start_img, 1)
exit_button = Button(400, 280, exit_img, 1)
exit_button_2 = Button(620, 8, exit_img, 0.6)
restart_button = Button(100, 280, restart_img, 1)
restart_button_2 = Button(10, 8, restart_img, 0.6)
tutorial_button = Button(-2, 5, tutorial_image, 1)
back_button = Button(795 - 105, 595 - 62, back_image, 0.8)

running = True
game_start = False
game_won = False
game_lose = False
start_menu = True
start_menu_main = "main"

# Game Loop
game = Game()

while running:

    if start_menu:
        screen.blit(background_menu, (0, 0))
        if start_menu_main == "main":
            screen.blit(title_surface, title_rect)
            if exit_button.draw(screen):
                running = False
            if tutorial_button.draw(screen):
                start_menu_main = "tutorial"
            if start_button.draw(screen):
                start_menu = False
                game_start = True
        if start_menu_main == "tutorial":
            screen.blit(tutorial_menu, (0, 0))
            screen.blit(arrowkeys_image, arrowkeys_rect)
            screen.blit(tutorial_text_surface, tutorial_rect)
            screen.blit(arrow_text_surface, arrow_rect)
            screen.blit(spacebar_image, spacebar_rect)
            screen.blit(spacebar_text_surface, spacebar_text_rect)
            screen.blit(tutorial1, tutorial1_rect)
            screen.blit(tutorial2, tutorial2_rect)
            screen.blit(tutorial3, tutorial3_rect)
            screen.blit(tutorial4, tutorial4_rect)
            screen.blit(tutorial5, tutorial5_rect)
            screen.blit(tutorial6, tutorial6_rect)
            if back_button.draw(screen):
                start_menu_main = "main"

    if game_start:
        game.run()
        screen.blit(pause_text_surface,pause_rect)

        if game.time == 0:
            game_start = False
            game_won = True
        if game.lives == 0:
            game_start = False
            game_lose = True

    if game_won:
        screen.blit(background_win,(0,0))
        if restart_button.draw(screen):
            game_start = True
            game.time = 60
            game.lives = 5
            game.points = 0
            game_won = False
        if exit_button.draw(screen):
            running = False

    if game_lose:
        screen.blit(background_lose,(0,0))

        if restart_button_2.draw(screen):
            game_start = True
            game.time = 60
            game.lives = 5
            game.points = 0
            game_lose = False
        if exit_button_2.draw(screen):
            running = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Pause(screen,Button) 
        if event.type == pygame.QUIT:
            running = False
        #if event.type == pygame.USEREVENT+1:
            # Respawns enemies every 7.5 seconds (Niels)
            # game.draw_enemyGroup()
            
        if event.type == pygame.USEREVENT and start_menu == False:
            time_label = font.render(f"Time: {game.time}", 1, (255, 255, 255))
            game.time -= 1

    # Puts game on 60fps (Niels)
    clock.tick(60)

    # Update the screen (Niels)
    pygame.display.update()

pygame.quit()
