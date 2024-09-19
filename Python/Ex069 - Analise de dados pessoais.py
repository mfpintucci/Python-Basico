
i = 0
sf = 0
sm = 0
c = 0

while True:
    print ('=' *30)
    print ('CADASTRE UMA PESSOA')
    print ('=' *30)
    
    sexo = str(input('Qual o sexo da pessoa? [M /F]: ')).strip().upper()[0]
       
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo da pessoa? [M /F]: ')).strip().upper()[0]
          
    idade = int(input('Digite a idade: '))
    
    continuar = str(input('Deseja continuar? [ S/N]: ')).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [ S/N]: ')).strip().upper()[0]    
    
    c +=1
    if sexo in 'Mm':
        sm +=1
    if sexo in 'Ff'and idade < 20:
        sf +=1
    if idade > 18:
        i += 1
    if continuar in 'Nn':
        break
        
print ('=' * 30)
print ('RESULTADO')
print ('=' * 30)

print ('{} pessoas tem mais de 18 anos'.format(i))   
print ('Foram cadastrados {} homens'.format(sm))
print ('{} mulheres tem menos de 20 anos.'.format(sf))    
print ('Foram cadastradas ao todo {} pessoas'.format(c))   

#Exercício Python 69: Crie um programa que 
#leia a idade e o sexo de várias pessoas. 
#A cada pessoa cadastrada, o programa deverá 
#perguntar se o usuário quer ou não continuar.

#No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
