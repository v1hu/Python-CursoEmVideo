# SENO COSENO TANGENTE
from math import sin, cos, tan, radians

a = float(input('Qual o valor do angulo? '))
print(f'O angulo {a} tem o SENO {sin(radians(a)):.2f} \n'
      f'O angulo {a} tem o COSSE {cos(radians(a)):.2f} \n'
      f'O angulo {a} tem o TANGENTE {tan(radians(a)):.2f} \n'
      f'O angulo {a} tem o RAIO {radians(a):.2f} \n')