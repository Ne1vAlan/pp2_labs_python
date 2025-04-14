import pygame
import random
import psycopg2

pygame.init()

food_sound = pygame.mixer.Sound('Lab_9\\Snake.2\\8labka_catch.mp3')

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

# подключение к базе данных
conn = psycopg2.connect(
    dbname="snake_game",
    user="postgres",
    password="Amfundi10", 
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Функция для добавления нового пользователя если его нет
def add_new_user(username):
    # Проверка существует ли пользователь
    cursor.execute("SELECT id FROM public.user WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user is None:
        # создание нового пользователя
        cursor.execute("INSERT INTO public.user (username) VALUES (%s) RETURNING id", (username,))
        user_id = cursor.fetchone()[0]
        print(f" A new user {username} has been created!")
    else:
        user_id = user[0]
        print(f"Welcome, {username}!")
    
    return user_id

# Запрос имени пользователя
username = input("Enter your name: ")
user_id = add_new_user(username)

# Получение уровня и скорости
cursor.execute("SELECT level, speed FROM user_score WHERE user_id = %s", (user_id,))
score_data = cursor.fetchone()

if score_data:
    level, speed = score_data
    print(f"Your level: {level}, speed: {speed}")
else:
    level, speed = 1, 15  # Начальные значения для нового пользователя
    cursor.execute("INSERT INTO user_score (user_id, score, level, speed) VALUES (%s, %s, %s, %s)",
                   (user_id, 0, level, speed))
    conn.commit()
    print("Your entry level: 1, speed: 15")

# Условия для уровней
level_settings = {
    1: {"speed": 15, "walls": []},
    2: {"speed": 20, "walls": [(5, 5), (10, 10)]},
    3: {"speed": 25, "walls": [(5, 5), (10, 10), (15, 15)]}
}

# класс блока змейки
class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# класс еды с весом и временем исчезновения
class FoodItem:
    def __init__(self, x, y, weight, ttl):
        self.x = x
        self.y = y
        self.weight = weight
        self.ttl = ttl

    def is_expired(self):
        return self.ttl <= 0

    def tick(self):
        self.ttl -= 1

# начальная змейка
snake_block = [SnakeBlock(13, 13)]
dx, dy = 1, 0  # движение вправо

# таймер и скорость
clock = pygame.time.Clock()
move_event = pygame.USEREVENT + 1
pygame.time.set_timer(move_event, 150)

# счёт
score = 0

# отрисовка блока
def draw_block(color, row, column):
    x = start_x + column * BLOCK + MARGIN * (column + 1)
    y = start_y + row * BLOCK + MARGIN * (row + 1)
    pygame.draw.rect(screen, color, [x, y, BLOCK, BLOCK])

# генерация еды не на змейке
def generate_food():
    while True:
        x = random.randint(0, GRID_ROWS - 1)
        y = random.randint(0, GRID_COLS - 1)
        occupied = any(block.x == x and block.y == y for block in snake_block)
        if not occupied:
            weight = random.choice([1, 2, 3])
            ttl = random.randint(300, 500)  # 5–8 сек
            return FoodItem(x, y, weight, ttl)

# еда
food = generate_food()

# запуск
running = True
while running:
    clock.tick(speed)

    # управление 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and dy == 0:
                dx, dy = 0, -1
            elif event.key == pygame.K_d and dy == 0:
                dx, dy = 0, 1
            elif event.key == pygame.K_w and dx == 0:
                dx, dy = -1, 0
            elif event.key == pygame.K_s and dx == 0:
                dx, dy = 1, 0
            elif event.key == pygame.K_p:  # Клавиша для паузы
                cursor.execute("UPDATE user_score SET score = %s, level = %s, speed = %s WHERE user_id = %s",
                               (score, level, speed, user_id))
                conn.commit()
                print("Your data is saved!")
        elif event.type == move_event:
            head = snake_block[-1]
            new_x = head.x + dx
            new_y = head.y + dy

            # проверка выхода за границу 
            if not (0 <= new_x < GRID_ROWS and 0 <= new_y < GRID_COLS):
                print("Game Over: out of bounds!", "Your Score is", score)
                running = False
                break

            # столкновение с теом
            if any(block.x == new_x and block.y == new_y for block in snake_block):
                print("Game Over: hit itself!", "Your Score is", score)
                running = False
                break

            new_head = SnakeBlock(new_x, new_y)
            snake_block.append(new_head)

            # сьел еду
            if new_x == food.x and new_y == food.y:
                food_sound.play()
                score += food.weight
                food = generate_food()

                # уровень 
                if score % 3 == 0:
                    level += 1
                    speed = level_settings.get(level, {"speed": 15})["speed"]  # обновляем скорость
                    # Добавляем стены для каждого уровня 
            else:
                snake_block.pop(0)

            # уменьшаем таймер еды
            food.tick()
            if food.is_expired():
                food = generate_food()

    screen.fill(BLACK)
    screen.blit(bg_surface, (start_x - BG_PADDING, start_y - BG_PADDING))

    # сетка
    for row in range(GRID_ROWS):
        for column in range(GRID_COLS):
            color = GRAY if (row + column) % 2 == 0 else WHITE
            draw_block(color, row, column)

    # еда с цветом в зависимости от веса
    if food.weight == 1:
        FOOD_COLOR = (200, 50, 50)
    elif food.weight == 2:
        FOOD_COLOR = (255, 165, 0)
    else:
        FOOD_COLOR = (255, 215, 0)
    draw_block(FOOD_COLOR, food.x, food.y)

    # змейка
    for block in snake_block:
        draw_block(SNAKE, block.x, block.y)

    # счёт и уровень
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (2, 2))

    # таймер еды 
    seconds_left = max(1, food.ttl // 40)
    timer_text = font.render(f"Food disappears in: {seconds_left}s", True, WHITE)
    screen.blit(timer_text, (WIDTH - 250, 2))

    pygame.display.flip()

# Сохраняем финальные данные при завершении игры
cursor.execute("UPDATE user_score SET score = %s, level = %s, speed = %s WHERE user_id = %s",
               (score, level, speed, user_id))
conn.commit()

# Закрытие соединения с базой данных
conn.close()

pygame.quit()
