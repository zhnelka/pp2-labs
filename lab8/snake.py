import pygame
import time
import random

pygame.init()  # Инициализируем pygame

# Определяем цвета
white = (255, 255, 255)  # Белый цвет для змейки и текста
black = (0, 0, 0)  # Черный цвет для фона

# Устанавливаем параметры окна
width = 800  # Ширина окна
height = 600  # Высота окна
screen = pygame.display.set_mode((width, height))  # Создаем игровое окно
pygame.display.set_caption("Snake")  # Устанавливаем заголовок окна

clock = pygame.time.Clock()  # Создаем объект Clock для управления FPS
snake_block = 10  # Размер одного блока змейки

# Шрифт для отображения очков и уровня
font = pygame.font.SysFont("Verdana", 20)

# Функция для отображения уровня
def your_level(level):
    level_str = font.render("Level:" + str(level), True, white)
    screen.blit(level_str, (700, 10))

# Функция для отображения очков
def your_point(point):
    point_str = font.render("Points:" + str(point), True, white)
    screen.blit(point_str, (10, 10))

# Функция для отрисовки змейки
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, white, [x[0], x[1], snake_block, snake_block])

# Основной игровой цикл
def gameLoop():
    game_over = False  # Флаг окончания игры

    # Начальная позиция змейки
    x1 = width / 2
    y1 = height / 2

    # Изменение координат (направление движения)
    x1_change = 0
    y1_change = 0

    snake_List = []  # Список координат змейки
    Length_of_snake = 1  # Начальная длина змейки
    snake_speed = 15  # Начальная скорость змейки

    level = 0  # Уровень
    point = 0  # Очки

    # Генерируем случайные координаты для еды
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:  # Пока игра не окончена
        for event in pygame.event.get():  # Обрабатываем события
            if event.type == pygame.QUIT:  # Если нажали крестик — выходим
                game_over = True
            if event.type == pygame.KEYDOWN:  # Обрабатываем нажатия клавиш
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block  # Движение влево
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block  # Движение вправо
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block  # Движение вверх
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block  # Движение вниз
                    x1_change = 0

        # Проверка выхода за границы экрана
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True  # Если вышли за границы, заканчиваем игру

        screen.fill(black)  # Заливаем фон черным цветом

        # Отображаем уровень и очки
        your_level(level)
        your_point(point)

        # Обновляем координаты змейки
        x1 += x1_change
        y1 += y1_change

        # Отрисовываем еду
        pygame.draw.rect(screen, white, [foodx, foody, snake_block, snake_block])

        # Добавляем новую голову змейки в список
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        # Ограничиваем длину змейки, удаляя старые элементы
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка на столкновение змейки с самой собой
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True  # Если змейка столкнулась с собой, заканчиваем игру

        # Отрисовываем змейку
        our_snake(snake_block, snake_List)

        pygame.display.update()  # Обновляем экран

        # Проверяем, съела ли змейка еду
        if x1 == foodx and
