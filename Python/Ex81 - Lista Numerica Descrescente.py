lista = []
opção = ''
while True:
    n = int(input('Digite um número:' ))
    lista.append(n)
    opção = str(input('Quer continuar? [S/N]'))
    if opção in 'nN':
        break 
    
print ('*'*30)
print ('Foram adicionados {} elementos à lista' .format (len(lista)))
lista.sort(reverse=True)
print ('Os números digitados de forma decrescente foram:\n{}'.format(lista))
if 5 in lista:
    print ('O valor 5 foi encontrado na lista')
else:
    print ('O valor 5 não foi localizado') 