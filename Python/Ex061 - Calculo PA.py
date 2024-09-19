print ('Vamos calcular a sua progressão aritmética!')
print ('=-=' *15)

i = int(input('Digite o 1o termo: '))
r = int(input('Digite a razão da PA: '))
t = int(input('Quantos termos deseja ver na sua PA? '))
termo = i + (t - 1 ) * r

c = 0
p = 0

while c < termo:
    c = c + r
    



#for c in range ( i, termo, r):
    print (c , end ='->')
    
print ('Acabou')


#Desenvolva um programa que leia o primeiro termo
#(start) e a razão  de uma progressão aritimetica
#PA (iteração). No final mostre os 10 primeiros
#termos essa progressão 

#refazer exercicio 51 usando o while.
