#Separando digitos de um número
num = int(input("Digite um número: "))

print(f'Analisando o número {str(num)}...')
print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')