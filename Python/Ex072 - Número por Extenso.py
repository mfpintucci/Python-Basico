ext = ('zero', 'um', 'dois', 'tres', 'quatro',
	     'cinco', 'seis', 'sete', 'oito', 'nove', 
	     'dez' , 'onze', 'doze', 'treze', 'quatorze', 
	     'quinze' , 'dezesseis', 'dezessete', 'dezoito' , 
	     'dezenove' ,'vinte')
n = 0
cont = ' ' 

while True :
    if 0 >= n <= 20:
        n = int(input('Digite um número entre 0 e 20 :'))
        
    elif n > 20:
        n  = int(input('Número inválido. Digite um número entre 0 e 20: '))
    
    print ('Você digitou o número {} - {}'.format (n, ext[n]))
    cont = str(input('Deseja Continuar? [S/N]')).upper().strip()[0]
    if cont in 'Ss':
        n = int(input('Digite um número entre 0 e 20 :'))      
    if cont in 'Nn':
       
        print ('Obrigada por ter vindo hoje!')
        break