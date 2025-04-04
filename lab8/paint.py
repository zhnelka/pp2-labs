import pygame
    
def main():
    pygame.init()

    width = 800
    height = 600
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    color = black

    screen = pygame.display.set_mode((width, height))
    layer = pygame.Surface((width, height))
    clock = pygame.time.Clock()
    
    X, Y, x, y = -1, -1, -1, -1
    radius = 10

    screen.fill(white)
    layer.fill(white)
    
    isMouseDown = False
    drawLine = True
    drawRect = False
    drawCircle = False
    eraser = False

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    color = black
                    
                if event.key == pygame.K_2:
                    color = red
                    
                if event.key == pygame.K_3:
                    color = blue
                    
                if event.key == pygame.K_4:
                    color = yellow
                    
                if event.key == pygame.K_5:
                    color = green

                if event.key == pygame.K_UP:
                    if not radius == 50:
                        radius += 3
                
                if event.key == pygame.K_DOWN:
                    if not radius == 1:
                        radius -= 3
                    
                if event.key == pygame.K_q:
                    drawRect = True
                    drawCircle = False
                    eraser = False
                    drawLine = False
                    
                if event.key == pygame.K_w:
                    drawRect = False
                    drawCircle = True
                    eraser = False
                    drawLine = False
                    
                if event.key == pygame.K_e:
                    drawRect = False
                    drawCircle = False
                    eraser = True
                    drawLine = False

                if event.key == pygame.K_r:   
                    drawRect = False
                    drawCircle = False
                    eraser = False
                    drawLine = True
            
            if event.type == pygame.MOUSEBUTTONDOWN:    
                if event.button == 1:
                    isMouseDown = True
                    x =  event.pos[0]
                    y = event.pos[1]
                    X =  event.pos[0]
                    Y =  event.pos[1]
                
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                layer.blit(screen, (0, 0))
      
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    x =  event.pos[0]
                    y =  event.pos[1]

        if drawLine and pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(screen, color, mouse, radius)

        if isMouseDown and X != -1 and Y != -1 and x != -1 and y != -1 and drawRect:
            screen.blit(layer, (0, 0))
            r = calculateRect(X, Y, x, y)
            pygame.draw.rect(screen, color, pygame.Rect(r), radius)
        
        if isMouseDown and X != -1 and Y != -1 and x != -1 and y != -1 and drawCircle:
            screen.blit(layer, (0, 0))
            r = calculateRect(X, Y, x, y)
            pygame.draw.ellipse(screen, color, r, radius)
        mouse = pygame.mouse.get_pos()
        
        if eraser and pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(screen, white, mouse, radius)
            
        pygame.display.flip()
        clock.tick(100000000000000)

def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
    
main()
