# Aumentos múltiplos - R$ 1.250,00 = aumento de 10% - valores menores 15%

S = float(input("Qual o valor do salário ? R$ "))

if S <= 1250:

    N = S + (S * 15 / 100)

else:

    N = S + (S * 10 / 100)

print(f"Após a correção o salário {S:.2f}, com aumento passa para R${N:.2f} .")