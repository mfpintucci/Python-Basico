print ('Números Primos, são números que são divisíveis\napenas por 1 e por ele mesmo')
print ('Vamos descobrir se um numero é primo?\n')

print ('-=-' *15)
print ('\n')

n = int(input('Digite um número: '))
t = 0


for c in range (1,n+1):
    print ('{}' .format(c),end =' ')
    
    if n % c == 0:
        t = t+ 1
         
print ('\nO número {} foi divisível {} vezes.'. format(n,t))        
        
if t> 2:
    print ('O número {} não é primo'.format (n))
    
else:
    print ('O número {} é primo'.format (n))     
    
        
        
        
#Faça um programa que leia um nimero inteiro 
#e diga se ele é ou não um número primo.
