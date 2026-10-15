# Custo da Viagem - Condicao composta

D = float(input("Qual é a distância da sua viajem? "))

print(f"Você está prester a começar um viajem de {D} Km/h.")

if D <= 200:  # maior ou igual a 200

    P = D * 0.5  # se for menor ou igual a 200km usa 0.5

else:
    P = D * 0.45  # se for maior a 200km usa 0.45

print(f"E o preço da sua passagem será de R$ {P:.2f}.")
