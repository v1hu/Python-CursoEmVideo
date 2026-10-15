# Procurando uma string dentro de outra IN = VAI PROCURAR A PALAVRA DENTRO DA STRING INTEIRA

nome = str(input("Digite seu nome completo: ")).strip() #tirar os espaços do começo e do final da string
print(f"Seu nome tem 'Silva'? {'SILVA' in nome.upper()}") #verifica se 'SILVA' está presente em 'nome' (transformado em maiúscula)