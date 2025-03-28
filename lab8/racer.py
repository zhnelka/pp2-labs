import pygame
import random

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гонка")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

car = pygame.image.load("car.png")  # Машина
car = pygame.transform.scale(car, (50, 100))
car_x, car_y = WIDTH // 2 - 25, HEIGHT - 120  # Начальная позиция машины
car_speed = 5  # Скорость машины

coin = pygame.image.load("coin.png")  # Монета
coin = pygame.transform.scale(coin, (30, 30))
coins = []  # Список монет

score = 0  # Очки
font = pygame.font.Font(None, 36)  # Шрифт для отображения очков

# Функция для создания монет в случайных местах
def spawn_coin():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(-600, -50)
    coins.append([x, y])

# Генерация первых монет
for _ in range(5):
    spawn_coin()

running = True
while running:
    pygame.time.delay(30)  # Задержка для плавности
    screen.fill(WHITE)  # Очистка экрана
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Управление машиной
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - 50:
        car_x += car_speed
    
    # Движение монет
    for coin_obj in coins:
        coin_obj[1] += 5  # Перемещение вниз
        if coin_obj[1] > HEIGHT:  # Если монета уходит за экран, заменяем её
            coins.remove(coin_obj)
            spawn_coin()
        
        # Проверка столкновения машины с монетой
        if car_x < coin_obj[0] < car_x + 50 and car_y < coin_obj[1] < car_y + 100:
            coins.remove(coin_obj)
            spawn_coin()
            score += 1  # счёт
    
    screen.blit(car, (car_x, car_y))  # Машина
    for coin_obj in coins:
        screen.blit(coin, (coin_obj[0], coin_obj[1]))  # Монеты
    
    # Отображение счёта
    score_text = font.render(f"Очки: {score}", True, RED)
    screen.blit(score_text, (WIDTH - 150, 20))
    
    pygame.display.update()  # Обновление экрана

pygame.quit()  # финиш
