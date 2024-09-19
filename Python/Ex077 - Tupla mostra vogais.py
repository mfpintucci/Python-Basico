tupla = ('Você', 'é' , 'o' , 'amor', 'da', 'minha', 'vida')

for p in tupla:
    print ('\nNa palavra {} temos '.format (p.upper()),end ='')
    for letra in p:
        if letra.lower() in 'ááàaeéêiíoóôuú':
            print (letra , end = ' ')





#Crie um programa que tenha uma tupla com 
#várias palavras (não usar acentos). Depois 
#disso, você deve mostrar, para cada palavra, 
#quais são suas vogais.
