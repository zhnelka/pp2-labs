import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BALL_RADIUS = 25
STEP = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

ball_x, ball_y = WIDTH // 2, HEIGHT // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - STEP - BALL_RADIUS >= 0:
                ball_y -= STEP
            elif event.key == pygame.K_DOWN and ball_y + STEP + BALL_RADIUS <= HEIGHT:
                ball_y += STEP
            elif event.key == pygame.K_LEFT and ball_x - STEP - BALL_RADIUS >= 0:
                ball_x -= STEP
            elif event.key == pygame.K_RIGHT and ball_x + STEP + BALL_RADIUS <= WIDTH:
                ball_x += STEP
    
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), BALL_RADIUS)
    pygame.display.flip()

pygame.quit()
