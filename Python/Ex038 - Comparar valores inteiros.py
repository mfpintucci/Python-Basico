print ('COMPARANDO VALORES INTEIROS')
print ('#' *30)

v1 = int(input('Digite um número: '))
v2 = int(input('Agora mais um: '))
	
if v1>v2:
    print ('O primeiro valor {} é maior do que o segundo valor {}.' .format (v1,v2))

elif v2>v1:
    print ('O segundo valor {} é maior do que o primeiro valor {}.'.format(v2,v1))

elif v1==v2:
    print ('Os valores são iguais!')
    
