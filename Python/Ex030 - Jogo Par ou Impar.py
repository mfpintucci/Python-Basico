from random import randint

computador = randint(0,10)
print ('VAMOS BRINCAR DE PAR OU ÍMPAR')

jogador = int(input('Escolha um número de 0 a 10 :' ))

j1 = str('PAR')
j2 = str('ÍMPAR')
jogo = random.sample([j1,j2],k=1)


print ('Então vamos lá .... {}'.format(jogo))
print ('O computador jogou o número {} e você jogou {}.'.format (computador,jogador))
 

resultado1 = computador % 2 == 0
resultado2 = jogador % 2 == 0
resultado3 = computador % 2 != 0
resultado4 = jogador % 2 != 0


if jogo == j1 and resultado1 and resultado2:
     print ('O computador jogou o número {} e você jogou {}. Vocês empataram'.format (computador,jogador))

elif jogo == j1 and resultado3 and resultado4:
     print ('O computador jogou o número {} e você jogou {}. Vocês perderam'.format (computador,jogador))

elif jogo == j1 and resultado1 and resultado4:
     print ('O computador jogou o número {} e você jogou {}. O computador venceu'.format (computador,jogador))

elif jogo == j1 and resultado2 and resultado3:
     print ('O computador jogou o número {} e você jogou {}. Parabéns, você venceu !!'.format (computador,jogador))

elif  jogo == j2 and resultado1 and resultado2:
     print ('O computador jogou o número {} e você jogou {}. Vocês perderam'.format (computador,jogador))

elif jogo == j2 and resultado3 and resultado4:
     print ('O computador jogou o número {} e você jogou {}. Vocês empataram'.format (computador,jogador))

elif jogo == j2 and resultado1 and resultado4:
     print ('O computador jogou o número {} e você jogou {}. Parabéns, você venceu !'.format (computador,jogador))

elif jogo == j1 and resultado2 and resultado3:
     print ('O computador jogou o número {} e você jogou {}. O computador venceu !!'.format (computador,jogador))
 

