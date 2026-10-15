# Aluguel de carros  carro = 60r$ dia km = 0.15 por KM
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
print(f'Com {dias} dias alugados e com {km}KM rodados\nO valor total a pagar é de R${(dias * 60) + (km * 0.15):.2f}')
