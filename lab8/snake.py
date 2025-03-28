import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20  # Размер клетки
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

snake = [(100, 100), (90, 100), (80, 100)]  # Начальное положение змейки
snake_dir = (CELL_SIZE, 0)  # Начальное движение вправо
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))  # Еда
score = 0
level = 1
speed = 10
font = pygame.font.Font(None, 36)

# Функция для генерации еды в случайной позиции
def spawn_food():
    while True:
        new_food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        if new_food not in snake:
            return new_food

running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)  # Очистка экрана
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Управление змейкой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
        snake_dir = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
        snake_dir = (CELL_SIZE, 0)
    if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
        snake_dir = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
        snake_dir = (0, CELL_SIZE)
    
    # Движение змейки
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    # Проверка на столкновение со стеной
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False
    
    # Проверка на столкновение с собой
    if new_head in snake:
        running = False
    
    # Добавляем новую голову змейки
    snake.insert(0, new_head)
    
    # Проверка на поедание еды
    if new_head == food:
        food = spawn_food()
        score += 1
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()
    
    # рисовка еды
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    
    # рисовка змейки
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
    
    # Отображение счёта и уровня
    score_text = font.render(f"Очки: {score}  Уровень: {level}", True, BLUE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(speed)  # скорость игры

pygame.quit()
