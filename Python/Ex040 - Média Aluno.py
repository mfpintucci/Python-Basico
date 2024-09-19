


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

print ('A media do aluno foi {:.2f}, portanto '.format(media))

if media < 5:
    print ('Aluno Reprovado')

elif media > 5 and media < 6:
    print ('Aluno em Recuperação')
    
else:
    print ('Aluno aprovado')
    
   





#escreva um programa que leia 2 notas de un aluno
#diga a media entre elas e se o aluno esta
#reprovado, em recuperacao ou aprovado. 
