while True:
    n = int(input('Digite um número para ver sua Tabuada [ -n: sair]'))
    print ('-'*30)
    c = 1
    if n < 0:
        break
    while c <= 10: 
        print ('{:2} × {:2} = {:2} '. format (n, c, n*c))   
        c += 1
    print ('-'*30)
print ('Fim do programa Tabuada')


#Exercício Python 67: Faça um programa que 
#mostre a tabuada de vários números, um de cada
#vez, para cada valor digitado pelo usuário. 
#O programa será interrompido quando o número 
#solicitado for negativo.
