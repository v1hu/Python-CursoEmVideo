import math

num = int(input('Digite um número: '))
print(f'A raiz de {num} é igual a {(math.sqrt(num))} \n'
      f'A Raiz de {num} arredondada para cima é igual a {math.ceil(math.sqrt(num))}\n'
      f'A Raiz de {num} arredondada para baixo é igual a {math.floor(math.sqrt(num))}\n'
      f'O número {num} truncada é igual a {math.trunc(math.sqrt(num))}\n'
      f'O fatorial de  {num}  é igual a {math.factorial(int(math.sqrt(num)))}\n'
      f'A potencia de {num} é igual a {math.pow(num, (math.floor(math.sqrt(num)))):.2f}\n')
