import pygame
from pygame.locals import *
from Objects.Ball import Ball
from Game.GameManager import GameManager

class BouncyBalls:
    def __init__(self):
        pygame.init()

        self.app         = pygame
        self.dimensions  = 800, 600
        self.tickrate    = 100
        self.surface     = self.app.display.set_mode(self.dimensions,HWSURFACE|DOUBLEBUF|RESIZABLE)
        self.clock       = self.app.time.Clock()
        self.gamemanager = GameManager(self)

    def run(self):
        gamemanager = self.gamemanager
        app         = self.app
        surface     = self.surface
        clock       = self.clock
        tickrate    = self.tickrate

        while True:
            gamemanager.get_input(app)
            gamemanager.update(app)
            gamemanager.draw(app, surface)
            clock.tick(tickrate)



