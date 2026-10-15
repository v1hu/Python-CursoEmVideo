# Adicionando cores ao Python # ANSI - escape sequence

# \033[(STYLE)(TEXT)(BACKGROUN)m] 

# \033[0;33;44m] - style 0, text black, background red

# style: 0 none(semn nada), 1 bold(negrito), 4 underline (sublinhado), 7 negative (inverte as cores, fundo vai para o texto e o texto vai para o fundo)
# text = 30 (branco), 31 (vermelho), 32 (verde), 33 (amarelo), 34 (azul), 35 (roxo), 36 (ciano), 37 (cinza) - DEZENA 30
# background = 37 (branco) 40 (preto), 41 (vermelho), 42 (verde), 43 (amarelo), 44 (azul), 45 (roxo), 46 (ciano), 47 (cinza) - DEZENA 40

print('\033[0;97;41mOlá, Mundo!\033[m')  # fundo vermelho, texto branco

print('\033[4;33;46mOlá, Mundo!\033[m') # fundo azul sublinhado , texto amarelo

print('\033[0;35;43mOlá, Mundo!\033[m') # fundo amarelo, texto roxo\

print('\033[0;97;42mOlá, Mundo!\033[m') # fundo verde, texto branco

print('\033[7;97;40mOlá, Mundo!\033[m') #INVERTIDO

print('\033[4;97;40mOlá Mundo!\033[m') #fundo preto texto branco

A = 3
B = 5
print(f'Os valores são \033[0;97;41m{A}\033[m e \033[33;46m{B}\033[m.')

cores = {'limpa':'\033[m',
         'azul': '\033[34m',
        'amarelo':'\033[33m',
        'pretoebranco': '\033[7;30m'}
         
print(f'Os valores são cores {cores["azul"]}{A}{cores["limpa"]} e {cores['pretoebranco']}{B}{cores['limpa']}.')