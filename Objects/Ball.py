import pygame
from pygame.locals import *
import random

class Ball:
    def __init__(self):
        self.radius     = 25
        self.x          = random.randint(self.radius, 800-self.radius)
        self.y          = random.randint(0, 300)
        self.speed_x    = 0
        self.speed_y    = 0
        self.color      = (150,0,0)
        self.max_height = 600

        self.init_y     = self.y

    def draw(self, app, surface):
        app.draw.circle(surface, self.color,(int(self.x), int(self.y)),self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if (self.y < self.max_height):
            self.max_height = self.y

