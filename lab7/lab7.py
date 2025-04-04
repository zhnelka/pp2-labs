import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((829, 836))
run = True
pygame.display.set_caption("Mickey Clock")

mickey = pygame.image.load("/Users/mrtva_zhanel/Downloads/main-clock.png")
left = pygame.image.load("/Users/mrtva_zhanel/Downloads/left-hand.png")
right = pygame.image.load("/Users/mrtva_zhanel/Downloads/right-hand.png")

while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
        screen.blit(mickey, (0, 0))
        time = datetime.datetime.now()
        rot1 = pygame.transform.rotate(left, -time.second * 6)
        rot1_rect = rot1.get_rect(center = (829/2, 836/2))
        screen.blit(rot1, rot1_rect)
        rot2 = pygame.transform.rotate(right, -time.minute * 6)
        rot2_rect = rot2.get_rect(center = (829/2, 836/2))
        screen.blit(rot2, rot2_rect)

        pygame.display.flip()
