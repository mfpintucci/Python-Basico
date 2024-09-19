print ('~=~' *15)
print ('ANALISADOR DE TRIANGULOS')
print ('~=~' *15)

lado1 = float(input('Digite o 1o segmento: '))
lado2 = float(input('Digite o 2o segmento: '))
lado3 = float(input('Digite o 3o segmento: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
     print('Os segmentos informados podem formar um triângulo ', end ='')
     
     if lado1==lado2==lado3:
         print ('Equilátero')
     elif lado1!=lado2!=lado3!=lado1:
         print ('Escaleno')
     else:
         print ('Isóceles')
         
else:
     print ('Os segmentos informados não formam um triângulo.')