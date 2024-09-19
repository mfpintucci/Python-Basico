print ('Olá,  colaborador! Hoje iremos calcular seu novo salário com 15% de aumento!')

s=float(input('Digite seu salário atual :R$ '))
novo=s+(s*15/100)

print ('Com o aumento de 15% o seu salário passará de R${} para R$ {}.'.format (s,novo))
