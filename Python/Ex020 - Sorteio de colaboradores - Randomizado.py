import random
print('Vamos sortear a ordem dos auxiliares que ficarão\nresponsáveis pelas contagens das Curvas em Outubro')

print('Abaixo, digite os nomes dos participantes: ')


n1=str(input('Digite 1o nome '))
n2=str(input('Digite 2o nome '))
n3=str(input('Digite 3o nome '))
n4=str(input('Digite 4o nome '))
n5=str(input('Digite 5o nome '))
n6=str(input('Digite 6o nome '))
n7=str(input('Digite 7o nome '))
n8=str(input('Digite 8o nome '))
n9=str(input('Digite 9o nome '))
n10=str(input('Digite 10o nome '))
n11=str(input('Digite 11o nome '))
n12=str(input('Digite 12o nome '))


#na reaolucao do exercicio o Gustavo
#Guanabara cria lista explicita para a 
#randomizacáo, entretanto a vs python
#utilizada nao reconhece a lista 
#lista=[n1,n2,n3,n4,n5]

k=int(input('Digite o número de colaboradores a serem\nsorteados de acordo com o número de atividades\nque precisam ser executadas: '))

escolhido=random.sample([n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12],k=k)


print('Os auxiliares escolhidos foram {}'.format(escolhido))
