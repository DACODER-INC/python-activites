import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('adding image and background image')

background_image = pygame.transform.scale(
    pygame.image.load(r"C:\Users\Navraj- PC\Downloads\background.png").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))

beluga_image = pygame.transform.scale(pygame.image.load(r'C:\Users\Navraj- PC\Downloads\beluga.jpg').convert_alpha(), (200, 200))
beluga_rect = beluga_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))

text = pygame.font.Font(None, 36).render('Just to be clear i am not a physician ', True,
    pygame.Color('black'))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))


def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(beluga_image, beluga_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    game_loop()
