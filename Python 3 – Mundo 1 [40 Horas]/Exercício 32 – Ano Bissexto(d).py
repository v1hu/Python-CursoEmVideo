# Ano Bissexto - ler um ano qualquer e dizer se ele é bissexto - simples cm variavel
# O ano A é bissexto se for divisível por 4 e não for divisível por 100, ou se for divisível por 400.

# Se você quer simplificar ainda mais, pode guardar a condição em uma variável python

A = int(input("Qual ano gostaria de analisar? "))

bissexto = (A % 4 == 0 and A % 100 != 0) or A % 400 == 0

if bissexto:
    print(f"O ano {A} é BISSEXTO!")
else:
    print(f"O ano {A} não é BISSEXTO!")


# if A % 4 == 0 = DIVISIVEL POR 4 // == (TRUE)

# A % 100 != 0 = N PODE SER DIVISIVEL POR 100 e N PODE SER DIFERENTE DE ZERO //  != (DIFERENTE DE)

# A % 4 == 0 → A é divisível por 4, sem deixar resto.

# and → E (as duas condições precisam ser verdadeiras).

# A % 100 != 0 → A não é divisível por 100 sem deixar resto.

# or → OU (basta uma das condições ser verdadeira).

# A % 400 == 0 → A é divisível por 400, sem deixar resto.
