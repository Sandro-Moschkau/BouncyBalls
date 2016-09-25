import pygame
from pygame.locals import *
from Objects.Ball import Ball
import math, sys

class GameManager:
    def __init__(self):
        self.ball_number = 3
        self.balls       = []
        self.gravity     = 1
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
        counter = 0
        for ball in self.balls:
            y_pos = counter * 110 + 10
            surface.blit(app.font.Font(None, 20).render("Ball %d" % (counter + 1), 1, (250, 240, 230)), (20, y_pos + 0))
            surface.blit(app.font.Font(None, 20).render("Maximale Höhe %.2f" % ball.max_height, 1, (250, 240, 230)), (20, y_pos + 15))
            surface.blit(app.font.Font(None, 20).render("aktuelle Höhe %.2f" % ball.y, 1, (250, 240, 230)), (20, y_pos + 30))
            surface.blit(app.font.Font(None, 20).render("Start-Höhe %d" % ball.init_y, 1, (250, 240, 230)), (20, y_pos + 45))
            surface.blit(app.font.Font(None, 20).render("letzte Höhe %.2f" % ball.last_height, 1, (250, 240, 230)), (20, y_pos + 60))
            surface.blit(app.font.Font(None, 20).render("x_speed %.2f" % ball.speed_x, 1, (250, 240, 230)), (20, y_pos + 75))
            surface.blit(app.font.Font(None, 20).render("y_speed %.2f" % ball.speed_y, 1, (250, 240, 230)), (20, y_pos + 90))

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
            ball.move(self.gravity)

    def detect_collisions(self):
        self.detect_wall_collisions()

    def handle_wall_collision(self, position, speed, gravity, wall_position):
        original_speed = speed - gravity
        orig_pos       = position - ( original_speed + gravity / 2 )

        bounce_distance = 0
        final_speed     = 0

        time_to_wall   = (math.sqrt(2 * gravity * wall_position - 2 * gravity * orig_pos + abs(original_speed)**2) - abs(original_speed) ) / (gravity if gravity else 1)
        speed_at_wall  = gravity * time_to_wall + abs(original_speed)

        if original_speed < 0:
            speed_at_wall *= -1

        remaining_time = 1 - time_to_wall

        final_speed  = -gravity * remaining_time + speed_at_wall
        speed        = -final_speed

        bounce_distance = -gravity / 2 * remaining_time**2 + speed_at_wall * remaining_time

        position = wall_position - bounce_distance
        return {
            'position' : position,
            'speed'    : speed
        }

    def detect_wall_collisions(self):
        balls     = self.balls
        gravity   = self.gravity

        for ball in balls:
            if ( ball.x + ball.radius >= 800 ):
                wall = 800 - ball.radius

                after_collision = self.handle_wall_collision(ball.x, ball.speed_x, 0, wall)

                ball.x       = after_collision['position']
                ball.speed_x = after_collision['speed']

            if ( ball.x - ball.radius <= 0 ):
                wall = 0 + ball.radius

                after_collision = self.handle_wall_collision(ball.x, ball.speed_x, 0, wall)

                ball.x       = after_collision['position']
                ball.speed_x = after_collision['speed']

            if ( ball.y + ball.radius >= 600 ):
                wall = 600 - ball.radius

                after_collision = self.handle_wall_collision(ball.y, ball.speed_y, gravity, wall)

                ball.y       = after_collision['position']
                ball.speed_y = after_collision['speed']

            if ( ball.y - ball.radius <= 0 ):
                wall = 0 + ball.radius

                after_collision = self.handle_wall_collision(ball.y, ball.speed_y, gravity, wall)

                ball.y       = after_collision['position']
                ball.speed_y = after_collision['speed']

