# Utilizando Módulos
# import_bebida = importa tudo
# from_bebida_import_agua = importa oque pede

# biblioteca math = matemática

# CEIL = ARREDONDAR PARA CIMA / FLOOR = ARREDONDAR PARA BAIXO
# TRUNC = TRUNCATE, VAI ELIMINAR DA VIRGULA PARA FRENTE, SEM FAZER ARREDONDAMENTO
# POW = POTENCIA  / SQRT = SQUARE ROOT = RAIZ QUADRADA / FACTORIAL = FATORIAL

from math import sqrt, floor

num = int(input('Digite um número: '))
print(f'A raiz de {num} é igual a {floor(sqrt(num))}')
