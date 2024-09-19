from math import floor

print ('Vai financiar uma casa ?')
print ('#'*24)
print ('Vamos avaliar os critérios')

valor = float(input('Digite o valor do imóvel que deseja financiar:\nR$ '))
salario = float(input('Digite seu salário atual : R$'))
tempo = int(input('Em quantos anos pretende financiar : '))*12

print ('Você pretende comprar um imóvel de R$ {:.2f},\nparcelado em {} vezes.'.format(valor,tempo))

compra = floor(salario*30/100)

print ('O valor investido na parcela não pode ultrapassar\nR$ {:.2f}, correspondente a 30% do seu salário '.format(compra))

parcela = floor(valor/tempo)

print ('O valor da parcela é de R$ {:.2f}.'.format(parcela))


if parcela<=compra:
    print ('Você pode financiar este imóvel')
    
else:
    print ('O financiamento deste imóvel não lhe é recomendado.')



