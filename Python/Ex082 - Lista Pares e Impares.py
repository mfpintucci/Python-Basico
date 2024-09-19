lista = []
opção = ''
pares = []
ímpares = []
n = 0
while True:
    n = int(input('Digite um número:' ))
    lista.append(n)
    opção = str(input('Quer continuar? [S/N]'))
    if opção in 'nN':
        break 
print ('*'*30)
lista.sort()
print ('Os números digitados foram:\n{}'.format(lista))

for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        ímpares.append(v)
print ('Os valores pares foram: {}'. format (pares))
print ('Os valores ímpares foram: {}'.format (ímpares))
