# Primeira e última ocorrência de uma string

nome = str(input("Digite uma frase: ")).strip().upper() #tirar os espaços do começo e do final da string
print(f"Primeira ocorrência de 'A': {nome.find('A') + 1}") #encontra a primeira ocorrência de 'A' e mostra a posição (somando 1 para tornar mais legível)
print(f"Última ocorrência de 'A': {nome.rfind('A') + 1}") #encontra a última ocorrência de 'A' e mostra a posição (somando 1 para tornar mais legível)
print(f"Contagem de 'A': {nome.count('A')}") #conta quantas vezes 'A' aparece na string (já está em maiúscula)