import pygame
class Bullet(object):
    def __init__(self, x , y,mx, my):
        self.x = x
        self.y = y
        self.speed = [0,0]

        if(mx>x):
            self.speed[0] = 1
        
        else:
            self.speed[0] = -1
        if(my>y):
            self.speed[1] = 1
        else:
            self.speed[1] = -1
    def Move(self,mx,my):
        self.x += self.speed[0]
        self.y += self.speed[1]

