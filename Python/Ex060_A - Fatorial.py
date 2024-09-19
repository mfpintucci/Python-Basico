n = int(input('Digite um número para conhecer o seu fatorial: '))

c = n
f = 1

print ('Calculando {} ! = ' .format(n), end='')  
while c > 0:
    print('{}' .format(c), end='')
    print (' × ' if c> 1 else ' = ' , end='')
    f =  f* c
    c = c - 1
print ('{}'. format(f))
   

#Metodo tradicional para outras linguagens que não possuem o modulo fatorial
#Faça um programa que leia um número qualquer
#e calcule o seu fatorial.

#eh possivel fazer com o for
#testar
