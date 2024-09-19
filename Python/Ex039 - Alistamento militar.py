from datetime import date
hoje = date.today().year

ano= int(input('Digite o ano do seu nascimento: '))


idade = hoje-ano
falta=18-idade
passou=idade-18

print ('Voce tem {} anos.'.format (idade))


if idade<18:
    print ('Ainda falta {} anos para seu alistamento'.format(falta))
    
elif idade==18:
    print ('Está na hora de você se alistar')
    
else:
    print ('Já se passaram {} anos da época do alistamento'.format(passou))
    
    
    
    
#aula 8 modulo 1 , assistir novamente.
#escreva um programa que leia o ano de nascimento
#do usuario e diga:

#se ele ainda vai se alistar
#se esta no ano de alistamento
#ou se passou do prazo do alistamento militar.

#precisa capturar data do sistema para calcular
#a idade 

#o programa deve mostrar quanto tempo falta 
#ou quanto tempo passou do prazo
