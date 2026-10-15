frase = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print(f'Seu nome em Maiusculas é {frase.upper()}')
print(f'Seu nome em Minusculas é: {frase.lower()}')
print(f'Seu nome tem {frase.lower().count("o")} vezes a letra "o"')
print(f'Seu nome tem {len(frase) - frase.count(" ")} letras')
print(f'Seu primeiro nome é {frase.split()[0]} e ele tem {len(frase.split()[0])} letras')
print('-'.join(frase.split()))