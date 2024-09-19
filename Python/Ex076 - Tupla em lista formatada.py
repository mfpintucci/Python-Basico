prod = ('Caderno', 19, 'Caneta', 4, 'Lapis' , 2 , 
	'Borracha', 3, 'Marca-Texto' , 5, 'Postit' , 13)

print ('-' *40)
print ('{:^40}'.format('LISTA DE PREÇOS'))
print ('-'*40)

for pos in range (0, len(prod)):
    if pos % 2 == 0:
        print ('{:.<30}' .format(prod[pos]), end = '')
    else:
        print ('{:.>10.2f}' .format (prod[pos]))
               
print ('-' *40)
print ('{:^40}'.format('FIM DA LISTA DE PREÇOS'))
print ('-' *40)

#crie um programa que tenha uma tupla unica com
#nomes e preços de produtos na sequencia.
#no final mostre uma lista formatada organizando os
#dados de forma tabular.

