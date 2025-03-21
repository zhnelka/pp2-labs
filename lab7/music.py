import pygame
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 200
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

music_file = "song.mp3"
pygame.mixer.music.load(music_file)

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
    
    screen.fill(WHITE)
    pygame.display.flip()

pygame.quit()
