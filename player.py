import pygame
class Player(object):
    def __init__(self, w, h):
        self.image = pygame.image.load('player.png')
        self.surimage = self.image.get_rect()
        self.x = (w/2)-(self.surimage.size[0]/2)
        self.y = (h/2)-(self.surimage.size[1]/2)
    def GetCenter(self):
        center = [int(self.x+self.surimage.size[0]/2),int(self.y+self.surimage.size[1]/2)]
        return center
