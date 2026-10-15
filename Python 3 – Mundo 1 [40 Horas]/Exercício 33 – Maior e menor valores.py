# Maior e menor valores - LER 3 NUMEROS E DIZER QUAL MAIOR, MENOR - Condicional Simples

A = int(input("Primeiro valor: "))
B = int(input("Primeiro valor: "))
C = int(input("Primeiro valor: "))

# Verificando quem é menor

M = A

if B < A and B < C:
    M = B
if C < A and C < B:
    M = C
print(f"O menor valor digitado foi {M}")

# Verificando quem é o maior

M2 = A
if B > A and B > C:
    M2 = B
if C > A and C > B:
    M2 = C
print(f"O maior valor digitado foi {M2}")
