#codigo gpt atualizado para mp3

import pygame

# Inicializa o Pygame

pygame.init()

# Carrega a sua música MP3

pygame.mixer.music.load('des021.mp3')

# Toca a música

pygame.mixer.music.play()

# Espera você apertar Enter no terminal para encerrar a música

input('Dê Enter para parar a música...')