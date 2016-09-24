import pygame
from pygame.locals import *
from Objects.Ball import Ball

class GameManager:
    def __init__(self):
        self.ball_number = 2
        self.balls       = []
        self.gravity     = 0.5
        self.friction    = 0.00001

        for x in range(0, self.ball_number):
            self.balls.append(Ball())

    def draw(self, app, surface):
        surface.fill((25,0,0))

        for ball in self.balls:
            ball.draw(app, surface)

        self.show_debug(app, surface)
        pygame.display.flip()


    def show_debug(self, app, surface):
        counter = 1
        for ball in self.balls:
            y_pos = counter * 70
            surface.blit(app.font.Font(None, 20).render("Ball %d" % counter, 1, (250, 240, 230)), (20, y_pos + 0))
            surface.blit(app.font.Font(None, 20).render("Maximale Höhe %.2f" % ball.max_height, 1, (250, 240, 230)), (20, y_pos + 15))
            surface.blit(app.font.Font(None, 20).render("aktuelle Höhe %.2f" % ball.y, 1, (250, 240, 230)), (20, y_pos + 30))
            surface.blit(app.font.Font(None, 20).render("Start-Höhe %d" % ball.init_y, 1, (250, 240, 230)), (20, y_pos + 45))

            counter += 1

    def update(self):
        self.move_balls()
        self.detect_collisions()

    def get_input(self, app):
        keystate = app.key.get_pressed()
        for event in app.event.get():
            if event.type == QUIT or keystate[K_ESCAPE]:
                app.quit(); sys.exit()

    def move_balls(self):
        balls = self.balls

        for ball in balls:
            ball.move()

    def detect_collisions(self):
        self.detect_wall_collisions()

    def detect_wall_collisions(self):
        balls = self.balls

        for ball in balls:
            if ( ( ball.x + ball.radius >= 800 ) or ( ball.x - ball.radius <= 0 ) ):
                ball.speed_x *= -1
            else:
                ball.speed_x *= ( 1 - self.friction )

            if ( ( ball.y + ball.radius >= 600 ) ):
                trespass_distance = ball.y + ball.radius - 600
                percentage        = trespass_distance / ball.speed_y
                over_gravity      = self.gravity * percentage

                ball.speed_y -= over_gravity
                ball.speed_y *= -1
                ball.speed_y += over_gravity

                ball.y = 600 - trespass_distance - ball.radius
            else:
                ball.speed_y += self.gravity
                ball.speed_y *= ( 1 - self.friction )

