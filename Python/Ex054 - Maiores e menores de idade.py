from datetime import date
hoje = date.today().year

tmaior = 0
tmenor = 0
for c in range (0,7):
    d=int(input('Digite o ano de nascimento: '))
    if hoje - d < 21:
         tmenor = tmenor +1
    elif hoje - d >= 21:
         tmaior = tmaior +1
print('Fim')

print ('{} pessoas são menores de idade'.format(tmenor))

print ('{} pessoas são maiores de idade'.format(tmaior))
 
 
 
        
#Crie um programa que leia o ano de nascimento
#de 7 pessoas. No final   o programa deve mostrar.........
#quantas pessoas ja atingiram a maioridade e 
#quantas ainda nao atingiram (21 anos)
