import pygame
from pygame.locals import *
from Objects.Ball import Ball
from Game.GameManager import GameManager

class BouncyBalls:
    def __init__(self):
        pygame.init()

        self.gamemanager = GameManager()
        self.app         = pygame
        self.dimensions  = 800, 600
        self.tickrate    = 100
        self.surface     = self.app.display.set_mode(self.dimensions)
        self.clock       = self.app.time.Clock()

    def run(self):
        gamemanager = self.gamemanager
        app         = self.app
        surface     = self.surface
        clock       = self.clock
        tickrate    = self.tickrate

        while True:
            gamemanager.get_input(app)
            gamemanager.update()
            gamemanager.draw(app, surface)
            clock.tick(tickrate)



