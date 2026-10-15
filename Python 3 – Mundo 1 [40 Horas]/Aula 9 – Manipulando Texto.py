# aula09 Manipulando cadeias de Textos = strings

frase = 'Curso em vídeo Python'
frase2 = '   Aprenda Python   '

#fatiamento - o ultimo valor n entra na contagem
print('FATIAMENTO')

print(frase[9]) #pegando 1 letra
print(frase[9:13]) #pega de 9a12
print(frase[9:21]) #9a20 21 n existe
print(frase[9:21:2]) #indo de 9a20 saltando de 2em2
print(frase[:5]) #quando n tem nada se considera 0, 0a4, NO INICIO
print(frase[15:]) # NO FINAL> pega do numero caso 15, e vai ate o final
print(frase[9::3]) # de 9 ate o final pulando de 3em3
print(frase[::2])

#analise de string
print('analise de string')

print(len(frase)) #comprimento da string
print(len(frase.strip()))
print(len(frase2))
print(len(frase2.strip()))
print(frase.count('o')) # quantas letras 'o' minusculo tem,diferenciando minusculo e maiusculo sempre
print(frase.count('o', 0, 13)) #0ao12 quantos 'o' minusculo tem, diferenciando minusculo e maiusculo sempre
print(frase.upper().count('O')) # vai transformar a string para maiusculo e contra quantas vezes aparece o O
print(frase.find('deo')) #diz o momento que começou a string 'deo', 11, diferenciando minusculo e maiusculo sempre
print(frase.find('android')) #string que n existe, valor -1 FIND = achar a posiçao da string
print('Curso' in frase) # IN = dizer se a palavra existe dentro da string, diferenciando minusculo e maiusculo sempre


#transformaçao de string
print('tranformaçao de string')

print(frase.replace('Python', 'Android')) # trocou a palavra python por android
print(frase.upper()) # oque era minusculo ficou maiusculo, maiusculo se mantem
print(frase.lower()) # oque era maiusculo ficou minusculo, minusculo se mantem
print(frase.capitalize()) #primeira letra da string inteira fica maiuscula
print(frase.title()) #indentifica cada palavra da string e bota a primeira letra maiuscula

print(frase2.strip()) # remove espaços sobrando
print(frase2.rstrip()) # remove os espaços da direita
print(frase2.lstrip()) # remove os espaços da esquerda

#divisao de string
print('divisao de string')

print(frase.split()) #divisao em palavras excluindos os espaços, lista todas as palavras de uma string
print(frase2.split())
print('-'.join(frase)) #
print('-'.join(frase2))
print('-'.join(frase.split()))
print('-'.join(frase2.split()))
print('-'.join(frase2.rstrip()))
print('-'.join(frase2.lstrip()))
print(frase.split()[2][3])

print("""Hello  HelloHelloHelloHelloHelloHelloHello
HelloHelloHelloHelloHelloHelloHelloHelloHelloHello
HelloHelloHelloHelloHelloHelloHelloHelloHelloHello
HelloHelloHelloHelloHelloHelloHelloHelloHelloHello
HelloHelloHelloHelloHelloHelloHelloHelloHelloHello""")

