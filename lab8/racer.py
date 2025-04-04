import pygame, sys  # Импортируем библиотеки pygame и sys
from pygame.locals import *  # Импортируем все константы pygame
import random, time  # Импортируем random для генерации случайных чисел и time для паузы

pygame.init()  # Инициализируем pygame

# Задаем основные параметры игры
fps = 60  # Количество кадров в секунду
width = 400  # Ширина окна
height = 600  # Высота окна
speed = 5  # Начальная скорость движения объектов
score = 0  # Количество пройденных машин-препятствий
point = 0  # Количество собранных монет

# Цвета
red = (255, 0, 0)  # Красный цвет для экрана при завершении игры
black = (0, 0, 0)  # Черный цвет для текста

# Шрифты
font = pygame.font.SysFont("Verdana", 60)  # Шрифт для надписи "Game Over"
font_small = pygame.font.SysFont("Verdana", 20)  # Шрифт для счетчика очков
game_over = font.render("Game Over", True, black)  # Создаем текст "Game Over"
 
# Загружаем фон
background = pygame.image.load("/Users/mrtva_zhanel/Downloads/street.webp")

# Создаем игровое окно
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Raser")  # Устанавливаем заголовок окна
t = pygame.time.Clock()  # Создаем объект Clock для управления FPS

# Класс противника
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  
        self.image = pygame.image.load("/Users/mrtva_zhanel/Downloads/Enemy.webp")  # Загружаем изображение врага
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)  # Устанавливаем случайное начальное положение

    def move(self):
        global score  
        self.rect.move_ip(0, speed)  # Двигаем врага вниз
        if self.rect.bottom > height + 80:  # Если враг ушел за пределы экрана
            score += 1  # Увеличиваем счетчик пройденных машин
            self.rect.top = 0  # Возвращаем врага наверх
            self.rect.center = (random.randint(40, width - 40), 0)  # Ставим в случайную позицию

# Класс монеты
class Money(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  
        self.image = pygame.image.load("/Users/mrtva_zhanel/Downloads/money.png")  # Загружаем изображение монеты
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)  # Случайное начальное положение

    def move(self):
        self.rect.move_ip(0, speed)  # Двигаем монету вниз
        if self.rect.bottom > height + 80:  # Если монета ушла за пределы экрана
            self.rect.top = 0  # Возвращаем её наверх
            self.rect.center = (random.randint(40, width - 40), 0)  # Ставим в случайное место

    def lost(self):
        self.rect.center = (1000, 1000)  # Убираем монету с экрана после сбора

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  
        self.image = pygame.image.load("/Users/mrtva_zhanel/Downloads/Player.png")  # Загружаем изображение игрока
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height - 80)  # Устанавливаем начальное положение

    def move(self):
        pressed_keys = pygame.key.get_pressed()  # Получаем нажатые клавиши

        # Двигаем игрока в зависимости от нажатых клавиш
        if self.rect.top > 0:  
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)

        if self.rect.bottom < height:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)

        if self.rect.left > 0:  
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        if self.rect.right < width:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Создаем объекты
P1 = Player()
E1 = Enemy()
M1 = Money()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

cash = pygame.sprite.Group()
cash.add(M1)

all_sprites = pygame.sprite.Group()
all_sprites.add(M1)
all_sprites.add(P1)
all_sprites.add(E1)

# Создаем пользовательское событие для увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # Каждую секунду увеличиваем скорость

# Игровой цикл
while True:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.5  # Увеличиваем скорость врагов
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Отображаем фон
    screen.blit(background, (0, 0))

    # Отображаем счетчики
    scores = font_small.render(str(score), True, black)
    screen.blit(scores, (10, 10))

    points = font_small.render(str(point), True, black)
    screen.blit(points, (380, 10))

    # Обновляем положение всех спрайтов и рисуем их на экране
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # Если игрок столкнулся с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(red)  # Заливаем экран красным
        screen.blit(game_over, (30, 250))  # Отображаем "Game Over"
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()  # Удаляем все объекты
        time.sleep(2)  # Даем время увидеть экран поражения
        pygame.quit()
        sys.exit()

    # Если игрок собрал монету
    if pygame.sprite.spritecollideany(P1, cash):
        point += 1  # Увеличиваем счетчик очков
        M1.lost()  # Убираем монету с экрана
        pygame.display.update()

    pygame.display.update()
    t.tick(fps)  # Ограничиваем FPS
