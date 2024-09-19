
s = 0 #acumulador
cont = 0 #contador 

for c in range (1,496,2):
    if  c% 3==0:
        s = s + c
        cont = cont + 1
print ('A soma dos {} números ímpares divisiveis por 3, no\nintervalo de 1 a 50O é {} .' .format (cont, s))
print ('Fim')


#Faça um programa que calcule a soma entre todos
#os numeros impares que sao multiplos de tres
#e que se encontram no intervalo de 1 a 500 m
#(%3 = 0)
