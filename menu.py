import pygame
import os

# initialization
pygame.init()
# import images
image_menu = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
image_btnSell = pygame.image.load(os.path.join("images", "sell.png"))
image_btnUpgrade = pygame.image.load(os.path.join("images", "upgrade.png"))

class UpgradeMenu:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(image_menu, (180, 180))  # set image_menu's size
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.image_btnSell = pygame.transform.scale(image_btnSell, (35, 35))  # set image_btnSell's size
        self.image_btnUpgrade = pygame.transform.scale(image_btnUpgrade, (60, 35))  # # set image_btnUpgrade's size
        self.__buttons = [Button(image_btnUpgrade, "upgrade", x-30, y-85),
                                Button(image_btnSell, "sell", x-20, y+55)]  # save button's list

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.image, self.rect)
        # draw button
        x, y = self.rect.center
        win.blit(self.image_btnSell, (x - 18, y + 50))
        win.blit(self.image_btnUpgrade, (x - 32, y - 80))

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons   # return button's list

class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        # create buttun_rect
        self.btnSell_rect = pygame.Rect(x, y, 60, 40)
        self.btnUpgrade_rect = pygame.Rect(x, y, 40, 40)

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        # return buttun_rect's range
        return self.btnSell_rect.collidepoint(x, y) and self.btnUpgrade_rect.collidepoint(x, y)

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name  # return button's name






