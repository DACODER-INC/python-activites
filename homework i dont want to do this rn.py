# i used chatgpt for a boilerplate since i was really stuck Mrs. Shalini
import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.init()

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill('blue')
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)
    def update(self):
        keys = pygame.keys.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y += 5
        if keys[pygame.K_DOWN]:
            self.rect.y -= 5

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((40, 30))
        self.image.fill('red')
        self.rect = self.image.get_rect()

        
        self.rect.x = random.randint(0, SCREEN_WIDTH - 40)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - 30)


player = Player()

enemy_group = pygame.sprite.Group()

for i in range(7):
    enemy = Enemy()

    score = 0
    pygame.font.Font('VT323', 'blue', 100)
