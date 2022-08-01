import pygame

pygame.mixer.init()
pygame.mixer.music.load('till i collapse.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
