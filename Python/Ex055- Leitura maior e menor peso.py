
maior= 0
menor= 0
for p in range (1,6):
    peso =float(input('Insira o peso da {}a pessoa:'. format(p)))
    if p == 1:
        menor = peso
        maior = peso
        
    if peso > maior:
        maior = peso
    
    if peso < menor:
        menor = peso
        
        
print ('O menor peso digitado foi {}' .format(menor))
print ('O maior peso dogitado foi {}'.format (maior))








#Faça um programa que leia o peso de 5 pessoas e
#mostre qual foi o menor e o maior peso lido.
