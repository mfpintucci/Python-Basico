c = v = d = dois = 0
	
print ('----BANCO 24H ----')
print ('Notas disponíveis para saque: 50, 20, 10 e 2')
valor = int(input('Digite o valor que deseja sacar:'))

while valor % 2  > 0:
        
    print ('Escolha um valor múltiplo de 2,00 para saque') 
    valor = int(input('Digite o valor que deseja sacar:'))
  
if valor // 50 > 0:
    c = valor // 50
    valor = valor - (c*50)
    print('Você está recebendo {} notas de R$ 50,00' .format(c))
    if valor // 20 > 0:
        v = valor // 20
        valor = valor - (v*20)
        print('Você está recebendo {} notas de R$ 20,00' .format(v))
        if valor // 10 > 0:
            d = valor // 10
            valor = valor - (d*10)
            print('Você está recebendo {} notas de R$ 10,00' .format(d))
            if valor // 2 >= 0:
                dois = valor // 2
                valor = valor - (dois*2)
                print('Você está recebendo {} notas de R$ 2,00' .format(dois))

print ('Obrigada por escolher o nosso banco! Volte sempre!')

#Exercício Python 071: Crie um programa que 
#simule o funcionamento de um caixa eletrônico
#No início, pergunte ao usuário qual será o 
#valor a ser sacado (número inteiro) e o 
#programa vai informar quantas cédulas de 
#cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50,
#R$20, R$10 e R$2.
