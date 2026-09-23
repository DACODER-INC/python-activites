import pygame
pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Wildlife Information Display')

background = pygame.transform.scale(pygame.image.load(r"C:\Users\Navraj- PC\Downloads\Iceberg-Background-PNG.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

wildlife_pic = pygame.transform.scale(pygame.image.load(r"C:\Users\Navraj- PC\Downloads\isolated-penguin-bird-on-a-transparent-background-format-png.png").convert_alpha(), (220, 220))

wildlife_rect = wildlife_pic.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))


heading_font = pygame.font.Font(None, 42)
fact_font = pygame.font.Font(None, 28)

heading_text = heading_font.render('Wildlife Spotlight: Penguin', True, pygame.Color('blue'))
heading_rect = heading_text.get_rect(center=(SCREEN_WIDTH // 2, 45))

fact_text = fact_font.render('Penguins cant fly but they can dive 500 meters deep', True, pygame.Color('blue'))

fact_rect = fact_text.get_rect(center=(SCREEN_WIDTH // 2, 420))

def game_loop():

    clock = pygame.time.Clock()

    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background, (0, 0))
        
        display_surface.blit(wildlife_pic, wildlife_rect)

        display_surface.blit(heading_text, heading_rect)

        display_surface.blit(fact_text, fact_rect)

        pygame.display.flip()

    
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()
