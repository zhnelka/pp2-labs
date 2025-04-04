import pygame

pygame.init()
screen = pygame.display.set_mode((940, 530))
pygame.display.set_caption("music player")
run = True
music = [
    "/Users/mrtva_zhanel/Downloads/Кайрат Нуртас – Алматының Түндер-Ай.mp3",
    "/Users/mrtva_zhanel/Downloads/Кайрат Нуртас – Ол Сен Емес.mp3",
    "/Users/mrtva_zhanel/Downloads/Kairat Nurtas – Seni Suiem.mp3",
    "/Users/mrtva_zhanel/Downloads/Кайрат Нуртас – Эх Қарындас.mp3"
]

pau = pygame.image.load("/Users/mrtva_zhanel/Downloads/pause.png")
nex = pygame.image.load("/Users/mrtva_zhanel/Downloads/next.png")
pre = pygame.image.load("/Users/mrtva_zhanel/Downloads/previous.png")
play = pygame.image.load("/Users/mrtva_zhanel/Downloads/play.png")  

next = False
prev = False
play_state = False  # Новый флаг, чтобы отслеживать состояние воспроизведения
pause = True
begin = True

x = 0

cat = pygame.image.load("/Users/mrtva_zhanel/Downloads/GettyImages-512291806-61d59f2.jpg")

# Размеры кнопок
button_width = 60
button_height = 60

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if begin == True:
                    pygame.mixer.music.load(music[0])
                    pygame.mixer.music.play()
                    begin = False
                    pause = False
                    play_state = True  # Музыка начала воспроизводиться
                elif pause == True:
                    pygame.mixer.music.unpause()
                    pause = False
                    play_state = True  # Музыка продолжает воспроизведение
                else:
                    pygame.mixer.music.pause()
                    pause = True
                    play_state = False  # Музыка на паузе
            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                x += 1
                if x == len(music):
                    x = 0
                pygame.mixer.music.load(music[x])
                pygame.mixer.music.play()
                play_state = True  # Музыка продолжает воспроизведение
            if event.key == pygame.K_LEFT:
                pygame.mixer.music.stop()
                x -= 1
                if x < 0:
                    x = len(music) - 1
                pygame.mixer.music.load(music[x])
                pygame.mixer.music.play()
                play_state = True  # Музыка продолжает воспроизведение

    screen.blit(cat, (0, 0))

    # Расположение кнопок по центру
    center_x = (screen.get_width() - button_width * 3) // 2  # Центр по X для 3 кнопок
    screen.blit(pre, (center_x, 130))  # Кнопка "Previous"

    # Если музыка на паузе, показываем кнопку паузы, иначе кнопку воспроизведения
    if play_state:
        screen.blit(pau, (center_x + button_width, 130))  # Кнопка "Pause"
    else:
        screen.blit(play, (center_x + button_width, 130))  # Кнопка "Play"

    screen.blit(nex, (center_x + button_width * 2, 130))  # Кнопка "Next"

    pygame.display.flip()
