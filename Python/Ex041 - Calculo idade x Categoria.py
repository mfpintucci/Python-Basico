from datetime import date
hoje = date.today().year

nascimento = int(input('Em que ano você nasceu? '))
	
idade = hoje-nascimento

if idade < 9:
    print ('Você tem {} anos e sua categoria é MIRIM.'.format(idade))
    
elif idade >= 9 and idade <14:
    print ('Você tem {} anos e sua categoria é INFANTIL.'.format(idade))

elif idade >=14 and idade =<19:
    print ('Você tem {} anos e sua categoria é JUNIOR.'.format(idade))
    
elif idade >19 and idade <=25:
    print ('Você tem {} anos e sua categoria é SENIOR.'.format(idade))
    
else:
    print ('Você tem {} anos e sua categoria é MASTER.'.format(idade))

#confederacao nacional de natacao precisa de um
#programa que leia a data de nascimento do nadador
#e informe em que categoria de natacao ele se encontra 

#ate 9 anos: mirim
#ate 14 anos: infantil
#ate 19 anos: junior
#ate 25 anos: senior
#acima 25 anos: master
