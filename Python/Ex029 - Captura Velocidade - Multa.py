velocidade = float(input('Qual a velocidade do veículo ? '))
multa = float((velocidade -80)*7.00)

if velocidade > 80:
    
     print ('Você está acima da velocidade permitida de 80 km/h. \nVocê será multado em R$ {:.2f}.' .format(multa))

else:
     print ('Parabéns pela sua prudencia em garantir a sua segurança e de outrem.')
