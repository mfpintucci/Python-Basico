print ('Vamos calcular a sua progressão aritmética!')
print ('=-=' *15)

i = int(input('Digite o 1o termo: '))
r = int(input('Digite a razão da PA: '))
termo = i

c = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
        
    while c <= total:
        print (termo , end ='->')

        termo = termo + r
        c = c + 1
        
    print ('Pausa')
    mais = int(input('Deseja ver mais quantos termos? '))

print ('Progressão finalizada com {} termos mostrados '.format (total)) 




#melhore o exercício 61, perguntando para o usuario
#quantos termos mais ele quer ver da PA. 
#o programa só pode parar quando a resposta for zero.
 