# Sorteando uma ordem na lista
from random import shuffle

n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input('Digite o nome do segundo aluno: '))
n3 = str(input('Digite o nome do terceiro aluno: '))
n4 = str(input('Digite o nome do quarto aluno: '))

nomes = [n1, n2, n3, n4]

shuffle(nomes)


print(f' foi sorteado(a) para o grupo {nomes}')