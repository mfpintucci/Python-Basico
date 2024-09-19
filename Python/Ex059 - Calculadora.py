from time import sleep

primeiro = int(input('Digite o primeiro valor :'))
segundo = int(input('Digite o segundo valor:'))
opção  = 0
while opção != 5:
    print ('Selecione a opção desejada')
    print ('''[1] Somar
[2] Multiplicar
[3] Mostrar o maior valor
[4] Novos Valores
[5] Sair da aplicação''')
    
    opção = int(input('Digite a opção desejada: '))
    print ('='*35)
    if opção == 1:
        soma = primeiro + segundo
        print ('A soma entre os números digitados é {}.' .format(soma))
       
    elif opção  == 2:
        mult = primeiro * segundo
    
        print ('A multiplicação  entre os números digitados é {}.' .format(mult))
       
    elif opção  == 3:
        if primeiro > segundo:
            maior= primeiro
            print ('O maior número digitado é o {}.' .format(primeiro))
        
        elif primeiro == segundo:
            
            print ('Ambos os números digitados são iguais.')     
        else:   
            maior = segundo
            print ('O maior número digitado é o {}.' .format(segundo))     
    
    elif opção  == 4:
        primeiro = int(input('Digite o primeiro valor :'))
        segundo = int(input('Digite o segundo valor:'))
        
    elif opção == 5:
        print ('Finalizando....')
        sleep(2)
        print ('Obrigada por utilizar nossos serviços, volte sempre')
        
    else:
        print ('Opção incorreta')


    

#crie um programa que leia dois valores e mostre
#na tela um menu. digite 1 pra somar, digite 2 para
#multiplicar 3 para  maior, 4 para novos valores
#5 para sair do programa.

