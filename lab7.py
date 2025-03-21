import pygame
import math
import time

pygame.init()

WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)
WHITE = (255, 255, 255)

mickey = pygame.image.load("mickey.png")
right_hand = pygame.image.load("right_hand.png")
left_hand = pygame.image.load("left_hand.png")

right_hand = pygame.transform.scale(right_hand, (150, 10))
left_hand = pygame.transform.scale(left_hand, (120, 8))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t = time.localtime()
    minutes = t.tm_min
    seconds = t.tm_sec

    minute_angle = -(minutes * 6)
    second_angle = -(seconds * 6)

    rotated_right_hand = pygame.transform.rotate(right_hand, minute_angle)
    rotated_left_hand = pygame.transform.rotate(left_hand, second_angle)

    right_hand_rect = rotated_right_hand.get_rect(center=CENTER)
    left_hand_rect = rotated_left_hand.get_rect(center=CENTER)

    screen.fill(WHITE)
    screen.blit(mickey, (0, 0))
    screen.blit(rotated_right_hand, right_hand_rect)
    screen.blit(rotated_left_hand, left_hand_rect)
    
    pygame.display.flip()
    pygame.time.delay(1000)

pygame.quit()
