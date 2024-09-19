from random import randint
from time import sleep
computador = randint ( 0,5)

print( '~=~' * 15) 
print ('VAMOS BRINCAR DE ADIVINHAÇÃO')
print ('~=~' * 15)
numero = int(input('Entre 0 e 5 , em que número estou pensando : '))
print ('PROCESSANDO...')
sleep(2)

while numero!=computador:
    numero = int(input(' Tente Novamente! Entre 0 e 5 , em que número estou pensando : '))
    print ('PROCESSANDO...')
    sleep(1)
print ('PARABÉNS VOCÊ ME VENCEU')






#melhore o jogo do exercicio 28 para que o jogador
#possa arriscar palpites ate acertar qual numero o 
#computador pensou. 
