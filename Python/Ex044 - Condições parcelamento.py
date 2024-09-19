preço = float(input('Digite o preço do produto: '))
print ('''Escolha abaixo a condição de pagamento:
    	[1] A vista no dinheiro
    	[2] A vista no cartão 
    	[3] 2x no cartão 
    	[4] 3x ou mais no cartão ''')
    	
opção = int(input('Digite a forma de pagamento escolhida:'))
juros = preço+(preço*20/100)

if opção == 4:
    parcela = int(input('Em quantas parcelas deseja dividir?'))
    
    print ('O valor a ser parcelado com 20% de juros é: R$ {:.2f} e você pagará {} parcelas de R$ {:.2f}'.format(juros, parcela, juros/parcela))

elif opção == 1:
    print ('O valor do produto com 10% de desconto é: R$ {:.2f}'.format(preço-(preço*10/100)))

elif opção == 2:
    print ('O valor do produto com 5% de desconto é: R$ {:.2f}'.format(preço-(preço*5/100)))

elif opção == 3:
    print ('O valor a ser parcelado é: R$ {:.2f} e você pagará 2x {:.2f}'.format(preço, preço/2))
    	

#elabore um programa que calcule o valor a ser pago
#por um produto considerando seu preco normal e
#condicao de pagamento

#a vista no dinheiro: 10% de desconto
#a vista bo cartao 5% desconto 
#2x no cartao preco normal
#3x ou mais cartao 20% juros