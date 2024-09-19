
print ('Vou te ajudar a calcular a sua progressão aritmética!')

i = int(input('Digite o 1o termo: '))
p = int(input('Digite a razão da PA: '))
decimo = i + (10 - 1 ) * p

for c in range ( i, decimo, p):
    print (c , end ='->')
    
print ('Acabou')


#Desenvolva um programa que leia o primeiro termo
#(start) e a razão  de uma progressão aritimetica
#PA (iteração). No final mostre os 10 primeiros
#termos essa progressão 
