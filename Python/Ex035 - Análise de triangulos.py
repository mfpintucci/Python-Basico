#um de seus lados deve ser maior que o valor
#absoluto (módulo) da diferença dos outros dois
#lados e menor que a soma dos outros dois lados.

print ('~=~' *15)
print ('ANALISADOR DE TRIANGULOS')
print ('~=~' *15)

lado1 = float(input('Digite o 1o segmento: '))
lado2 = float(input('Digite o 2o segmento: '))
lado3 = float(input('Digite o 3o segmento: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
     print('Os segmentos informados podem formar um triângulo')

else:
     print ('Os segmentos informados não formam um triângulo.')