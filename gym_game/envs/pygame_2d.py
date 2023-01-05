import pygame
import math
screen_width = 1500
screen_height = 800
check_point = ((1200,660),(1250,120),(190,200),(1030,270),(250,475),(650,690))

class PyGame2D:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.game_speed = 60

    def action(self,action):
        if action == 0:
            self.ball += 2
        if action == 1:
            self.car.angle += 5
        elif action == 2:
            self.car.angle -= 5

        self.car.update()
        self.car.check_collision()
        self.car.check_checkpoint()

        self.car.radars.clear()
        for d in range(-90, 120, 45):
            self.car.check_radar(d)

    def evaluate(self):

    def is_done(self):

    def observe(self):

    def view(self):




