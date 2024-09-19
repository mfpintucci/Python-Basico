lista = []
opção = ''
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print ('Valor adicionado com sucesso...')
    else:
        print ('Valor duplicado, não vou adicionar...')
    opção = str(input('Quer continuar ? [ S / N ] :'))
    if opção in 'Nn':
        break
    
print ('*' *35)
print ('Você digitou os valores :', end ='')
lista.sort()
print (lista)


#if lista == lista.append():
        #print ('Número duplicado, digite outro valor')
  



