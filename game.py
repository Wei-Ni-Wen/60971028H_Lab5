import pygame
import os
from enemy import EnemyGroup
from tower import TowerGroup
from settings import WIN_width, WIN_height
from color_settings import *

# load images
image_BG = pygame.image.load(os.path.join("images", "Map.png"))
image_hp = pygame.image.load(os.path.join("images", "hp.png"))
image_hpgray = pygame.image.load(os.path.join("images", "hp_gray.png"))
image_pause = pygame.image.load(os.path.join("images", "pause.png"))
image_continue = pygame.image.load(os.path.join("images", "continue.png"))
image_sound = pygame.image.load(os.path.join("images", "sound.png"))
image_muse = pygame.image.load(os.path.join("images", "muse.png"))

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((WIN_width,  WIN_height))
        self.image_BG = pygame.transform.scale(image_BG, (WIN_width,  WIN_height))
        self.hp_images = [pygame.transform.scale(image_hp, (40, 40)),
                          pygame.transform.scale(image_hpgray, (40, 40))]
        self.hp = 10
        self.max_hp = 10
        self.money = 100
        self.enemies = EnemyGroup()
        self.towers = TowerGroup()

    def draw(self):
        """
        Draw everything in this method.
        :return: None
        """
        # draw background and menu
        self.window.blit(self.image_BG, (0, 0))
        pygame.draw.rect(self.window, black, [0, 0, WIN_width, 80])
        self.window.blit(image_muse, (700, 0))
        self.window.blit(image_sound, (780, 0))
        self.window.blit(image_continue, (860, 0))
        self.window.blit(image_pause, (940, 0))
        # draw enemies
        self.enemies.draw(self.window)
        # draw towers
        self.towers.draw(self.window)
        pygame.display.update()

    def update(self):
        game_quit = False
        # event loop
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
                return game_quit
            # player press action
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n and self.enemies.is_empty():
                    self.enemies.add(10)  # generate 10 enemy for the next wave
            # player click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.towers.get_click(mouse_x, mouse_y)

        # update tower action
        self.towers.update(self.enemies)
        # update enemy action
        self.enemies.update()
        return game_quit
