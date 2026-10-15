# Sorteando um item na lista
from random import choice

n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))
n5 = str(input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4, n5]
print(f'O aluno sorteado foi o {choice(lista)} ')