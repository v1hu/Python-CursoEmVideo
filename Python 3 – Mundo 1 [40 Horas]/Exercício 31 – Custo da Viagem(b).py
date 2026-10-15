# Custo da Viagem - Condicao simples

D = float(input("Qual é a distância da sua viajem? "))

print(f"Você está prester a começar um viajem de {D} Km/h.")

P = D * 0.50 if D <= 200 else D * 0.45

print(f"E o preço da sua passagem será de R$ {P:.2f}.")
