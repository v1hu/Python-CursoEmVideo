# Primeiro e último nome de uma pessoa ex - ana maria de castro rocha souza
#A ideia importante para guardar é:

# lista[-1]   # último
# lista[-2]   # penúltimo
# lista[-3]   # antepenúltimo
# Enquanto índices positivos começam do início:

# lista[0]    # primeiro
# lista[1]    # segundo
# lista[2]    # terceiro

nome = str(input("Digite seu nome completo: ")).strip() #tirar os espaços do começo e do final da string
print(f'Muito prazer em te conhecer {nome}!')
print(f"Primeiro nome: {len(nome.split()[0])}") #conta caracteres do primeiro nome
print(f"Último nome: {len(nome.split()[-1])}") #conta caracteres do último nome
print(f"Primeiro nome: {nome.split()[0]}") #divide a string em uma lista de palavras e mostra a primeira
print(f"Último nome: {nome.split()[-1]}") #divide a string em uma lista de palavras e mostra a últimaVICT