# Toca musica

import pygame
pygame.mixer.init()
pygame.mixer.music.load('RockThatBody.mp3')
pygame.mixer.music.play()
pygame.event.wait()

print('\nMusica: RockThatBody.mp3')