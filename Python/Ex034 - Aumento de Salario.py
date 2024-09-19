s = float(input('Qual o seu salário atual? '))

if s<=1250:
   print ('Você receberá 15% de aumento e seu salário passará a ser R$ {:.2f}' .format((s*15/100)+s))
else:
   print ('Você receberá 10% de aumento e seu salário passará a ser R$ {:.2f}'.format ((s*10/100)+s))
