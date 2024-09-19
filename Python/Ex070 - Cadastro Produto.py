c = 0
produto = ' '
total = 0
mv =0
pv = 0
ppv = ' '

print ('-----LOJA BARATÃO DA ECONOMIA-----')

while True:
    print ('=' *30)
    print ('CADASTRE UM PRODUTO')
    print ('=' *30)
    
    produto = str(input('Produto cadastrado : ')).strip().upper()
    valor = float(input('Digite o valor do produto: R$  '))
    
    continuar = str(input('Deseja cadastrar um novo produto? [ S/N]: ')).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [ S/N]: ')).strip().upper()[0]    
    
    c +=1
    total += valor
    
    if valor >= 1000:
        mv +=1
    
    if c == 1:
        ppv = valor
        pv = produto
    else:
        if valor < ppv:
            ppv = valor
            pv = produto
    
    if continuar in 'Nn':
        break
        
print ('=' * 30)
print ('RESULTADO')
print ('=' * 30)

print ('SUBTOTAL = R$ {:.2f}'.format(total))   
print ('Foram cadastrados {} produtos'.format(c))
print ('{} produtos custaram R$1.000 ou mais.'.format(mv))
print ('O produto de menor valor foi {} que custou R$ {:.2f}'.format(pv, ppv))   

#Exercício Python 70: Crie um programa que 
#leia o nome e o preço de vários produtos. 
#O programa deverá perguntar se o usuário vai 
#continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
