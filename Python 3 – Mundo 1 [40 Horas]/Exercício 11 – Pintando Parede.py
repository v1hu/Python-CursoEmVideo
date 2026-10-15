# pintando parede
largura = float(input(' Largura da parede: '))
altura = float(input(' Altura da parede: '))
print(f'Sua parede tem a dimensao {largura} x {altura} e sua área é de {(largura * altura):.2f}m². \n'
      f'Para Pintar essa parade, voce precisará de {(largura * altura) / 2:.2f}l de tinta.')
