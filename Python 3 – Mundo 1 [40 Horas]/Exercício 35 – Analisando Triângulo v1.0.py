# Analisando Triângulo v1.0 - Ler o comprimento de tres retas e dizer se pode fomar um triangulo
# R3 tem que ser menor que a soma de R1+R2 = R1=1 // R2=2 // R3=17 - 1+2=3
print("=-=-=-=-=" * 3)
print("Analisador de Triângulos")
print("=-=-=-=-=" * 3)

L1 = float(input("Primeiro segmento: "))
L2 = float(input("Segundo segmento: "))
L3 = float(input("Terceiro Segmento: "))

if L1 < L2 + L3 and L2 < L1 + L3 and L3 < L1 + L2:

    print("Os segmentos acimda FORMAM UM TRIÂNGULO!")

else:
    
    print("Os segmentos acima NÃO FORMAM UM TRIÂNGULO")
