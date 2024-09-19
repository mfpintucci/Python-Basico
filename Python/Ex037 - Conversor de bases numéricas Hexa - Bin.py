num = int(input('Digite um número: '))
print (''' Escolha uma das bases para CONVERSÃO:
[1] Converter para BINARIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')

opção = int(input('Sua opção: '))

if opção == 1:
    print ('O número {} convertido para BINÁRIO é {}'.format(num, bin(num)))
elif opção == 2:
    print ('O número  {} convertido para OCTAL é {}.'.format(num, oct(num)))
    
elif opção == 3:
   print('O número  {} convertido para HEXADECIMAL é {}.'.format(num, hex(num)))








#conversor bases numericas
#deixar por ultimo

#tem um modulo de 4 videos
#no curso em video sobre essr assunto 