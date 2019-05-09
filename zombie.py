import pygame
class Zombie(object):
    def __init__(self, x, y):
        self.image = pygame.image.load('zombie.png')
        self.surimage = self.image.get_rect()
        self.x = x
        self.y = y
