import pygame
from game import Game
from settings import FPS

if __name__ == '__main__':
    # initialization
    pygame.init()
    # set the title
    pygame.display.set_caption("My TD game")
    # game run
    covid_game = Game()
    quit_game = False
    while not quit_game:
        pygame.time.Clock().tick(FPS)
        quit_game = covid_game.update()
        covid_game.draw()
    # quit game
    pygame.quit()