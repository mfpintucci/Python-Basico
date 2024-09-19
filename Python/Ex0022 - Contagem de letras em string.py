nome = str(input('Digite seu nome completo:')).strip()

print ('Seu nome com todas letras maiúsculas é {} .'.format(nome.upper()))
print ('Seu nome em letras minúsculas é {} .'.format (nome.lower()))

print ('O total de letras em sem nome é {} .'.format (len(nome) - nome.count(' ')))

#importante contar as letras e subtrair o contador de espaços. 
#No inicio a funcao strip ja elimina espacos indesejados no comeco
#e no final da string.

print ('O seu primeiro nome tem {} letras.'.format (nome.find(' ')))

#a função find localiza o primeiro espaço, auxiliando
#no calculo de quantas letras tem o primeiro nome.
