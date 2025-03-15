import pygame
pygame.init()

WIDTH, HEIGHT = 900, 835
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clock")


WHITE = (255, 255, 255)

left = pygame.image.load('Lab_7/Micki/left-hand.png')
right = pygame.image.load('Lab_7/Micki/right-hand.png')
background = pygame.image.load('Lab_7/Micki/main-clock.png')

bg_rect = background.get_rect(center=(WIDTH // 2, HEIGHT // 2))
left_rect = left.get_rect()
right_rect = right.get_rect()

CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2 + 50

OFFSET_Y = -40

left_rect.center = (CENTER_X, CENTER_Y + OFFSET_Y)
right_rect.center = (CENTER_X, CENTER_Y + OFFSET_Y)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False

   
    screen.fill(WHITE)

    screen.blit(background, bg_rect)

    screen.blit(left, left_rect)
    screen.blit(right, right_rect)

    pygame.display.flip()


pygame.quit()
