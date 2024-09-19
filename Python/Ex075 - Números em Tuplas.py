num = ( int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite o último número: ')))

print ('O número nove apareceu {} vezes'.format (num.count(9)))
if 3 in num:
    print ('O número 3 apareceu na {} posição .' . format (num.index(3)+1))
else:
    print ('O número três não foi digitado')

print ('Os números pares digitados foram ' , end='')
for n in num:
    if n% 2== 0:
        print (n , end =' ')
        
#desenvolva um programa que leia quatro valores
#pelo teclado e guarde em uma tupla. No final
#mostre
#A - quantas vezes apareceu o número 9
#B - Em que posição foi digitado o primeiro
#valor 3
#C - Quais foram ps numeros pares

