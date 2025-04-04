import pygame
import time
import random

pygame.init()  # Инициализация Pygame

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Размеры экрана
width = 800
height = 600
screen = pygame.display.set_mode((width, height))  # Устанавливаем размер экрана
pygame.display.set_caption("Snake")  # Название окна
clock = pygame.time.Clock()  # Часы для контроля FPS
snake_block = 10  # Размер блока змейки

font = pygame.font.SysFont("Verdana", 20)  # Шрифт для вывода информации

# Функция для отображения уровня
def your_level(level):
    level_str = font.render("Level:" + str(level), True, white)
    screen.blit(level_str, (700, 10))  # Отображаем уровень на экране

# Функция для отображения очков
def your_point(point):
    point_str = font.render("Points:" + str(point), True, white)
    screen.blit(point_str, (10, 10))  # Отображаем очки на экране

# Функция для рисования змейки
def our_snake(snake_block, snake_list):
   for x in snake_list:
       pygame.draw.rect(screen, white, [x[0], x[1], snake_block, snake_block])  # Рисуем каждый блок змейки

# Событие для увеличения скорости через 5 секунд
INC_SPEED1 = pygame.USEREVENT
pygame.time.set_timer(INC_SPEED1, 5000)  # Таймер для увеличения скорости через каждые 5 секунд

# Основная игровая функция
def gameLoop():
    game_over = False  # Переменная для отслеживания окончания игры

    # Начальные координаты змейки
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []  # Список для хранения сегментов змейки
    Length_of_snake = 1  # Начальная длина змейки
    snake_speed = 15  # Начальная скорость змейки

    # Начальные значения уровня и очков
    level = 0
    point = 0
    food2 = False  # Флаг для второго типа еды (дополнительные очки)

    # Первоначальные координаты еды
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    foodx2 = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody2 = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:  # Главный игровой цикл
        for event in pygame.event.get():
            if event.type == INC_SPEED1:  # Если таймер сработал
                if food2 == False:
                    food2 = True  # Включаем второй тип еды
                    pygame.time.set_timer(INC_SPEED1, 5000)  # Устанавливаем таймер на 5 секунд
                elif food2 == True:
                    food2 = False  # Выключаем второй тип еды
                    pygame.time.set_timer(INC_SPEED1, 10000)  # Устанавливаем таймер на 10 секунд
            if event.type == pygame.QUIT:  # Выход из игры
                game_over = True
            if event.type == pygame.KEYDOWN:  # Управление движением змейки
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block  # Двигаем влево
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block  # Двигаем вправо
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block  # Двигаем вверх
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block  # Двигаем вниз
                    x1_change = 0

        # Проверка на столкновение с границами экрана
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True  # Игра заканчивается, если змейка выходит за пределы экрана

        screen.fill(black)  # Заполняем экран черным цветом

        # Отображение уровня и очков
        your_level(level)
        your_point(point)

        # Обновляем позицию головы змейки
        x1 += x1_change
        y1 += y1_change

        # Рисуем вторую еду, если она активирована
        if food2 == True:
            pygame.draw.rect(screen, red, [foodx2, foody2, snake_block, snake_block])

        # Рисуем обычную еду
        pygame.draw.rect(screen, white, [foodx, foody, snake_block, snake_block])

        # Добавляем новый сегмент к змейке
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Если змейка слишком длинная, удаляем первый сегмент
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка на столкновение змейки с собой
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True

        # Рисуем змейку
        our_snake(snake_block, snake_List)
        pygame.display.update()  # Обновляем экран

        # Если змейка съела еду, обновляем координаты еды и увеличиваем длину змейки
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            point += 1
            if point % 5 == 0:  # Каждые 5 очков увеличиваем уровень и скорость
                level += 1
                snake_speed += 5

        # Если змейка съела вторую еду, обновляем координаты, увеличиваем длину и очки
        if x1 == foodx2 and y1 == foody2:
            foodx2 = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody2 = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 5
            food2 = False  # Выключаем второй тип еды
            pygame.time.set_timer(INC_SPEED1, 10000)  # Сбрасываем таймер
            point += 5
            level += 1
            snake_speed += 5  # Увеличиваем скорость змейки

        clock.tick(snake_speed)  # Ограничиваем скорость игры
    pygame.quit()  # Завершаем Pygame

gameLoop()  # Запуск игры
