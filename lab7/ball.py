import pygame

pygame.init()
screen = pygame.display.set_mode((410, 310))
pygame.display.set_caption("Red Ball")
run = True

WHITE = (255,255,255)
RED = (255,0,0)

x = 25
y = 25

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and x < 380:
                x += 20
            if event.key == pygame.K_LEFT and x > 25:
                x -= 20
            if event.key == pygame.K_UP and y > 25:
                y -= 20
            if event.key == pygame.K_DOWN and y < 280:
                y += 20
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), 25)
    pygame.display.flip()
