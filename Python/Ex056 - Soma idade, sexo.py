

sexo = ('Masculino' 'Feminino')
somaidade = 0
mediaidade = 0
maior = 0
menor = 0
nomevelho = ''
nomenova = ''
totmulher20 = 0

for c in range (1,5):
    print ('------------{}a pessoa--------------'.format(c))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = int(input(' Digite seu sexo:\n[0] Masculino\n[1] Feminino:\nDigite aqui a opção escolhida: '))
    	
    somaidade = somaidade + idade
    mediaidade= somaidade/4
    
    if c == 1:
        menor = idade
        maior = idade
        
    if idade > maior and sexo == 0:
        maior = idade
        nomevelho = nome
    
    if idade < menor and sexo == 1:
        menor = idade
        nomenova = nome
    if idade < 20 and sexo == 1:
        totmulher20 += 1
        
    
    
    
print ('A média de idade do grupo é {:.2f}.' .format(mediaidade))
print ('A idade do homem mais velho é {} e ele se chama {}.'.format(maior,nomevelho))
print ('A idade da mulher mais nova é {} e ela se chama {}'.format(menor,nomenova))
print ('O total de mulheres menores de 20 anos é {}.'.format(totmulher20))












#desenvolva um programa que leia o nome, idade
# e sexo de 4 pessoas e no final do programa 
#mostre:

# - a media de idade do grupo
# - Qual o nome do Homem mais velho
# - Quantas mulheres tem menos de 21 anos.
