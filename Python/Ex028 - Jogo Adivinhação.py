from random import randint
from time import sleep
computador = randint ( 0,5)

#print ('Pensei no número {} ' .format(computador))
print( '~=~' * 15) 
print ('VAMOS BRINCAR DE ADIVINHAÇÃO')
print ('~=~' * 15)
numero = int(input('Entre 0 e 5 , em que número estou pensando : '))
print ('PROCESSANDO...')
sleep(3)
if numero==computador:
     print ('PARABÉNS VOCÊ ME VENCEU')
else:
     print ('HAHA GANHEI !! PENSEI NO NUMERO {} E NÃO NO NÚMERO {} . TENTE NOVAMENTE' . format(computador, numero))
