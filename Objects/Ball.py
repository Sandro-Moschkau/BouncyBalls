import pygame
from pygame.locals import *
import random

class Ball:
    def __init__(self):
        self.radius     = 25
        self.x          = random.randint(self.radius, 800-self.radius)
        self.y          = 100 #random.randint(self.radius, 600-self.radius)
        self.speed_x    = random.randint(0, 20) - 10
        self.speed_y    = 0
        self.color      = (150,0,0)
        self.max_height  = self.y
        self.last_height = self.y

        self.project_y  = 0
        self.init_y     = self.y

    def draw(self, app, surface):
        app.draw.circle(surface, self.color,(int(self.x), int(self.y)),self.radius)

    def move (self, gravity):
        projected_x_dist = self.speed_x
        projected_y_dist = self.speed_y + gravity / 2

        self.x           += projected_x_dist
        self.y           += projected_y_dist

        self.speed_y     += gravity

        if (self.y < self.max_height):
            self.max_height = self.y

        if ((projected_y_dist < 0 and self.speed_y) > 0):
            self.last_height = self.y

