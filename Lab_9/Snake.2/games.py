import pygame
import random

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

# шрифт
font = pygame.font.SysFont("arial", 24)

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
speed = 15
move_event = pygame.USEREVENT + 1
pygame.time.set_timer(move_event, 150)

# счёт и уровень
score = 0
level = 1

# отрисовка блока
def draw_block(color, row, column):
    x = start_x + column * BLOCK + MARGIN * (column + 1)
    y = start_y + row * BLOCK + MARGIN * (row + 1)
    pygame.draw.rect(screen, color, [x, y, BLOCK, BLOCK])


# генерация новой еды не на змейке
def generate_food():
    while True:
        x = random.randint(0, GRID_ROWS - 1)
        y = random.randint(0, GRID_COLS - 1)
        occupied = any(block.x == x and block.y == y for block in snake_block)
        if not occupied:
            return SnakeBlock(x, y)

# еда
food = generate_food()

# запуск
running = True
while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # управление стрелками
            if event.key == pygame.K_a and dy == 0:
                dx, dy = 0, -1
            elif event.key == pygame.K_d and dy == 0:
                dx, dy = 0, 1
            elif event.key == pygame.K_w and dx == 0:
                dx, dy = -1, 0
            elif event.key == pygame.K_s and dx == 0:
                dx, dy = 1, 0
        elif event.type == move_event:
            head = snake_block[-1]
            new_x = head.x + dx
            new_y = head.y + dy

            # проверка выхода за границы поля
            if not (0 <= new_x < GRID_ROWS and 0 <= new_y < GRID_COLS):
                print("Game Over: out of bounds!"," Your Score is", score)
                running = False
                break

            # проверка столкновения с телом
            if any(block.x == new_x and block.y == new_y for block in snake_block):
                print("Game Over: hit itself!"," Your Score is", score)
                running = False
                break

            
            new_head = SnakeBlock(new_x, new_y)
            snake_block.append(new_head)

            # сьел еду
            if new_x == food.x and new_y == food.y:
                score += 1
                food = generate_food()


                # новый уровень
                if score % 3 == 0:
                    level += 1
                    speed += 2

            
            else:
                # обычное движение  убираем хвост
                snake_block.pop(0)

    screen.fill(BLACK)
    screen.blit(bg_surface, (start_x - BG_PADDING, start_y - BG_PADDING))

    # сетка
    for row in range(GRID_ROWS):
        for column in range(GRID_COLS):
            color = GRAY if (row + column) % 2 == 0 else WHITE
            draw_block(color, row, column)

    # еда
    FOOD = (200, 50, 50)
    draw_block(FOOD, food.x, food.y)

    # змейка
    for block in snake_block:
        draw_block(SNAKE, block.x, block.y)
    
    # счёт и уровень
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (2, 2))

    pygame.display.flip()

pygame.quit()
