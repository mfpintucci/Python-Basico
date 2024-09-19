n = s = c = 0
print ('-'* 30)
print ('CALCULADORA PARA SOMA')
print ('-'*30)

while True:
    n = float(input('Digite um número. Para sair, digite 999 : '))
    if n == 999:
        break
    s += n
    c += 1
print ('Foram digitados {} valores e a soma entre eles é : {:.2f}' .format(c,s))
print ('Obrigada')







#Exercício Python 66: Crie um programa que 
#leia números inteiros pelo teclado. O programa
#só vai parar quando o usuário digitar o valor 
#999,que é a condição de parada. No final, 
#mostre quantos números foram digitados e qual 
#foi a soma entre elas (desconsiderando o flag).
