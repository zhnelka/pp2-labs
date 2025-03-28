import pygame


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
current_color = BLACK 


brush_size = 5
mode = "brush"  # Возможные режимы: "brush", "rectangle", "circle", "eraser"


screen.fill(WHITE)
pygame.display.update()


running = True
start_pos = None  # Начальная позиция для фигур
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_p:
                mode = "brush"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_s:
                mode = "rectangle"


        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            if mode == "brush":
                pygame.draw.circle(screen, current_color, event.pos, brush_size)
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, brush_size)
        
        elif event.type == pygame.MOUSEMOTION and event.buttons[0]:
            if mode == "brush":
                pygame.draw.circle(screen, current_color, event.pos, brush_size)
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, brush_size)
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if mode == "rectangle" and start_pos:
                end_pos = event.pos
                pygame.draw.rect(screen, current_color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
            elif mode == "circle" and start_pos:
                end_pos = event.pos
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                pygame.draw.circle(screen, current_color, start_pos, radius, 2)
        
    pygame.display.update()

pygame.quit()
