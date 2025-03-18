import pygame


pygame.init()


WIDTH, HEIGHT = 600, 400  
BALL_RADIUS = 25  
STEP = 20  


WHITE = (255, 255, 255)
RED = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")


x, y = WIDTH // 2, HEIGHT // 2


running = True
while running:
    pygame.time.delay(50)  


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT] and x - BALL_RADIUS - STEP >= 0:
        x -= STEP
    if keys[pygame.K_RIGHT] and x + BALL_RADIUS + STEP <= WIDTH:
        x += STEP
    if keys[pygame.K_UP] and y - BALL_RADIUS - STEP >= 0:
        y -= STEP
    if keys[pygame.K_DOWN] and y + BALL_RADIUS + STEP <= HEIGHT:
        y += STEP


    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), BALL_RADIUS)
    pygame.display.update()


pygame.quit()
