sexo = str(input('Informe seu Sexo:[M/F] : ')).upper().strip()[0]

while sexo not in 'MF':
    sexo = str(input('Dados Incorretos. Informe seu Sexo:[M/F] : ')).upper()
    
print ('Sexo {} Registrado com sucesso'. format(sexo))

    








#Faça um programa que leia o sexo de uma pessoa
#e que só aceite M ou F. Caso ele esteja errado
#peca digitar novamente até que esteja certo 
