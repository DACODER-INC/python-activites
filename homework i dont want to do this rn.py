# i used chatgpt for a boilerplate since i was really stuck Mrs. Shalini
import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.init()

background = pygame.image.load(r"C:\Users\Navraj- PC\Downloads\47183.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill('blue')
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

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
    enemy_group.add(enemy)

    score = 0
    font = pygame.font.Font(None, 100)

pygame.mixer.music.load(r"C:\Users\Navraj- PC\OneDrive\Documents\project music\MyRec_1014_1922.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player.update()

    for enemy in enemy_group:
        if player.rect.colliderect(enemy.rect):
            score += 1
            enemy.kill()
    if len(enemy_group) == 0:
        for i in range(7):
            enemy = Enemy()
            enemy_group.add(enemy)


    screen.blit(background, (0, 0))

    screen.blit(player.image, player.rect)
    enemy_group.draw(screen)


    score_text = font.render('Score: ' + str(score), True, 'white')
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()