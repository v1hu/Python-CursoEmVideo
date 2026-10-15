# conversor de moedas
real = float(input('Quantos reais gostaria de converter? R$'))
print(f'Com R${real:.2f} voce pode comprar US${real / 3.27:.2f}. \n '
      f'Com R${real:.2f} voce pode comprar UND${real / 4.00:.2f}. \n'
      f'Com R$ {real:.2f} voce pode comprar Ux${real / 5.00:.2f}.')
