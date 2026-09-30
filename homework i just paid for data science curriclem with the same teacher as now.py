import pygame
import random

pygame.init()

CAR_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
SIGNAL_CHANGE_EVENT = pygame.USEREVENT + 2


ROAD = pygame.Color('darkgray')
WHITE = pygame.Color('white')
YELLOW = pygame.Color('yellow')
BLUE = pygame.Color('blue')
ORANGE = pygame.Color('orange')
RED = pygame.Color('red')
GREEN = pygame.Color('green')

class Car(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.velocity = [3, 0]

    def update(self):
        self.rect.move_ip(self.velocity)

        sensor_triggered = False

        if self.rect.left <= 0 or self.rect.right >= 600:
            self.velocity[0] = self.velocity[0]
            sensor_triggered = True

        if sensor_triggered:
            pygame.event.post(pygame.event.Event(CAR_COLOR_CHANGE_EVENT))

            pygame.event.post(pygame.event.Event)
