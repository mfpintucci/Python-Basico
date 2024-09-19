from random import randint
from time import sleep

itens= ('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)

print ('Vamos brincar de Jokenpô?')
print ('x' * 30)

jogador = int(input('''Qual opção você escolhe?
	[0] Pedra
	[1] Papel
	[2] Tesoura:\n'''))

print ('\nJO')
sleep(2)
print('KEN')
sleep(2)
print('PÔ')
sleep(1)

print ('-=-' * 10)

print ('Você escolheu {} '.format(itens[jogador]))
print ('O computador escolheu {}'.format(itens[computador]))

print ('-=-' * 10)

if computador==0 and jogador==0 or computador==1 and jogador==1 or computador==2 and jogador==2:
    print ('Vocês Empataram')
    
elif computador==0 and jogador==2:
    print ('O computador venceu')
    
elif computador == 1 and jogador == 0:
    print ('O computador venceu')
    
elif computador==2 and jogador==1:
    print ('O computador venceu')

else:
    print ('PARABÉNS , VOCÊ VENCEU!!')
    






#jokenpo
