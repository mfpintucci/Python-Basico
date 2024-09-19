ano = int(input('Que ano deseja a alisar ? '))

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print ('O ano {} é BISSEXTO' .format(ano))

else:
    print (' O ano {} não é um ano BISSEXTO'.format(ano))    