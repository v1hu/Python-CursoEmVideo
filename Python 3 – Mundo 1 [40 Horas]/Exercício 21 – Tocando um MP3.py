#mp3 modo antigo
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('des021.mp3')
pygame.mixer.music.play()
input('Pressione Enter para parar...')