# Catetos e Hipotenusa / outra forma de escrever {hypot(c,d)} é = (c**2 + d ** 2) ** (1/2)
from math import hypot

c = float(input('Digite o valor do cateto oposto: '))
d = float(input('Digite o valor do cateto adjacente: '))
print(f'Com o cateto oposto {c} e o adjacente {d} a Hipotenusa é: {hypot(c, d):.2f} ')
