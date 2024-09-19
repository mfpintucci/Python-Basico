print ('Vamos calcular o valor da sua viagem')
print ('#' * 30)

distancia = int(input('Qual a distância da sua Viagem em Km? '))

if distancia >= 200:
     print( 'O valor da sua passagem será de R$ {:.2f}' .format(distancia * 0.45))
else:
      print( 'O valor da sua passagem será de R$ {:.2f}' .format(distancia * 0.50))
