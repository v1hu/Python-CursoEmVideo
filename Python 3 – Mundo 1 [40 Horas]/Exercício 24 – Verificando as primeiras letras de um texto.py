# Verificando as primeiras letras de um texto [:5] É PARA ACHAR SANTO DO 0 AO 5 NA STRING

cidade = str(input("Digite o nome de uma cidade: ")).strip() #tirar os espaços do começo e do final da string
print(cidade[:5].upper() == 'SANTO') #transforma em maiúscula pra facilitar a comparação, e verifica se as 5 primeiras letras são iguais a SANTO
