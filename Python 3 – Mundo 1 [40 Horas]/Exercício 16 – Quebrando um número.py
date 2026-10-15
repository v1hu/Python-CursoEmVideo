from math import trunc

n = float(input('Digite um número: '))
print(f'O valor digitado foi {n} e a sua porçao inteira é {trunc(n)}')

# {trunc(n)} nesse caso poderia ser escrito {int(n)}
