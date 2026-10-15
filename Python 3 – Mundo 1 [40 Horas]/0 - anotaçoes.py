'''-~-~-~-~-~-~-~-~- Tipos primitivos ~-~-~-~-~-~-~-~-~-


  int()  -> Para números inteiros ----------- 17, 21, 35, 42

  float() -> Números de ponto flutuante ---2.3, 1.6, 14.9, -67.1

  bool() --> Armazena True ou False --------True, False

  str() ---> Conjunto de caracteres ------- 'narigudo', 'Pedro', 'feioso'

  type() ---> Indica o tipo primitivo da var -  x = 'Sapo Tunado'   print(type(x)) logo seu tipo primitivo é string

-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-


-~-~-~-~-~-~-~- Operadores Aritméticos ~-~-~-~-~-~-~-

  + -> Adição              ** -> Potencia
  - -> Subtração           // -> Divisão inteira
  * -> Multiplicação        % -> Resto da divisão
  / > Divisão -


           Ordem de Precedência

  1° -> ()
  2° -> **
  3° -> *  /  //  %
  4° -> +  -

-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-


~-~-~-~-~-~-~--~-~-~ Módulos -~-~-~-~-~-~-~-~-~-~-~

  Import > Importa uma biblioteca - import math

  from math import cos -> Importa somente a funçao cos da biblioteca math

  math -> Biblioteca de operadores aritméticos {

     sqrt()  -> Raiz Quadrada de um numero ------ raiz = math.sqrt(numero)
     floor() -> Arredonda o numero para baixo --- 5,23 fica 5,00
     ceil() --> Retorna um valor inteiro -------- 5,23 fica 5
     hypot() --> Retorna a hipotenusa dos catetos - math.hypot(co, ca)
     pow() ---> Potencia de um numero ----------- pow(2, 3) = 2³ = 8
     radians()-> Converte em graus radianos ------- print(math.radians(180))
     cos() ---> Retorne o cosseno em radianos --- print(math.cos(math.radians(x)))
     sin() ---> Retorne o seno em radianos ------ print(math.sin(math.radians(x)))
     tan() ---> Retorne a tangente em radianos -- print(math.tan(math.radians(x)))
  }

  random -> Gerar numeros pseudoaleatorios {

      randint() > Retorna um numero inteiro no range --------------- random.randint(1, 10)
      choice() --> Retorna um elemento aleatório da sequência - random.choice(x)
      shuffle() > Embaralha a sequência x no lugar ------------------- random.shuffle(y)
  }
-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-


-~-~-~-~-~-~-~-~- Manipulando Textos ~-~-~-~-~-~-~-~-

frase = 'ESTOU APRENDENDO A PROGRAMAR EM PYTHON'
NAO ESQUECER: em alguns casos, a frase pode conter letras "R" ou "L".

  in frase -----> Verifica se algo está dentro da frase inteira ------ retorna True ou False
  frase[9] -----> Pega o caractere da posição indicada --------------- retorna 'E'
  frase[9:13] --> Pega os caracteres das posições indicadas ----------- retorna 'ENDE'
  frase[9:18:2] --> Pega os caracteres das posições indicadas pulando 2 - retorna 'EDNOA'
  len() --------> Mostra quantos caracteres tem na frase ------------- len(frase) = 38
  count() ------> Conta quantas vezes um caractere aparece na frase -- frase.count('s')
  find() -------> Procura os caracteres escolhidos ------------------- frase.find('aprendendo')
  replace() ----> Substitui uma palavra por outra -------------------- frase.replace('PYTHON','JavaScript')
  upper() ------> Coloca todas as letras em maiúsculo ---------------- frase.upper()
  lower() ------> Coloca todas as letras em minúsculo ---------------- frase.lower()
  capitalize() -> Coloca todas as letras em minúsculo, exceto a 1ª --- frase.capitalize()
  title() ------> Cada palavra começa com letra maiúscula ------------ frase.title()
  strip() ------> Remove espaços no começo e no fim da frase --------- frase.strip() (frase.lstrip() e frase.rstrip() removem apenas no início ou fim)
  split() ------> Divide a frase em palavras com base nos espaços ---- frase.split()
  .join() ------> Junta elementos com um delimitador ----------------- ('-'.join(frase.split())) -> "Estou-aprendendo-a-programar-em-python"
  range() ------> Gera uma sequência de números ---------------------- list(range(5)) gera [0, 1, 2, 3, 4]'''

                          #outro exemplo

# Frase de exemplo
frase = 'ESTOU APRENDENDO A PROGRAMAR EM PYTHON'

# 1. Verificação e Busca
print('PYTHON' in frase)        # Verifica se "PYTHON" está na frase -> True
print(frase.find('APRENDENDO')) # Posição de "APRENDENDO" -> 6
print(frase.count('O'))         # Conta quantas vezes "O" aparece -> 3

# 2. Acesso a Letras e Partes da Frase
print(frase[9])                 # Caractere na posição 9 -> 'E'
print(frase[9:13])              # Pega caracteres da posição 9 a 12 -> 'ENDE'
print(frase[9:18:2])            # Pega caracteres da posição 9 a 17, pulando 2 -> 'EDNOA'
print(len(frase))               # Comprimento da frase -> 38

# 3. Alteração de Texto
print(frase.upper())            # Frase toda em maiúsculas
print(frase.lower())            # Frase toda em minúsculas
print(frase.capitalize())       # Apenas a primeira letra em maiúscula
print(frase.title())            # Primeira letra de cada palavra em maiúscula

# 4. Substituição e Junção
print(frase.replace('PYTHON', 'JavaScript'))  # Substitui "PYTHON" por "JavaScript"
print('-'.join(frase.split()))                # Divide por espaço e junta com hífen -> 'ESTOU-APRENDENDO-A-PROGRAMAR-EM-PYTHON'

# 5. Remoção de Espaços
print(frase.strip())            # Remove espaços no começo e no fim
print(frase.lstrip())           # Remove espaços à esquerda
print(frase.rstrip())           # Remove espaços à direita

# 6. Sequências de Números com range()
print(list(range(5)))           # Gera lista de 0 a 4 -> [0, 1, 2, 3, 4]
print(list(range(2, 10, 2)))    # Gera pares de 2 a 8 -> [2, 4, 6, 8]


'''frase = 'Curso em Vídeo'

print('-'.join(frase))

# Retorna:
C-u-r-s-o- e-m -V-í-d-e-o

# Corrigido:

print('-'.join(frase.split()))

# Retorna:
Curso-em-Vídeo'''

