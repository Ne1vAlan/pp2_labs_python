import pygame

pygame.init()

# экран
WIDTH, HEIGHT = 800, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# размеры и цвета
BLOCK = 20
BLACK = (0, 0, 0)
GRAY = (240, 240, 240)
WHITE = (255, 255, 255)
SNAKE = (0, 200, 180)
BG_GRID = (50, 50, 50, 180)
MARGIN = 1
GRID_ROWS = 30
GRID_COLS = 30
BG_PADDING = 10

# координаты сетки
grid_width = GRID_COLS * BLOCK + (GRID_COLS + 1) * MARGIN
grid_height = GRID_ROWS * BLOCK + (GRID_ROWS + 1) * MARGIN
start_x = (WIDTH - grid_width) // 2
start_y = (HEIGHT - grid_height) // 2

# задний фон
bg_surface = pygame.Surface(
    (grid_width + 2 * BG_PADDING, grid_height + 2 * BG_PADDING), pygame.SRCALPHA
)
bg_surface.fill(BG_GRID)

# класс змейки
class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# начальная змейка
snake_block = [SnakeBlock(13, 13)]
dx, dy = 1, 0  # движение вправо

# таймер и скорость
clock = pygame.time.Clock()
speed = 10
move_event = pygame.USEREVENT + 1
pygame.time.set_timer(move_event, 150)

# отрисовка блока
def draw_block(color, row, column):
    x = start_x + column * BLOCK + MARGIN * (column + 1)
    y = start_y + row * BLOCK + MARGIN * (row + 1)
    pygame.draw.rect(screen, color, [x, y, BLOCK, BLOCK])

# запуск
running = True
while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # управление стрелками
            if event.key == pygame.K_LEFT and dy == 0:
                dx, dy = 0, -1
            elif event.key == pygame.K_RIGHT and dy == 0:
                dx, dy = 0, 1
            elif event.key == pygame.K_UP and dx == 0:
                dx, dy = -1, 0
            elif event.key == pygame.K_DOWN and dx == 0:
                dx, dy = 1, 0
        elif event.type == move_event:
            head = snake_block[-1]
            new_head = SnakeBlock(head.x + dx, head.y + dy)
            snake_block.append(new_head)
            snake_block.pop(0)

    screen.fill(BLACK)
    screen.blit(bg_surface, (start_x - BG_PADDING, start_y - BG_PADDING))

    # сетка
    for row in range(GRID_ROWS):
        for column in range(GRID_COLS):
            color = GRAY if (row + column) % 2 == 0 else WHITE
            draw_block(color, row, column)

    # змейка
    for block in snake_block:
        draw_block(SNAKE, block.x, block.y)

    pygame.display.flip()

pygame.quit()
