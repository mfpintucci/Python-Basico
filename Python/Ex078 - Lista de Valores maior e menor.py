valor = []
maior = 0
menor = 0
for c in range (0, 5):
    valor.append(int(input('Digite um número para a posição {}:'.format (c+1))))
    if c == 0:
        maior = menor = valor[c]
    else:
        if valor[c] > maior:
            maior = valor[c]
        if valor[c] < menor:
            menor = valor[c]
print ('*' *30)
print ('''Foram inseridos os seguintes valores :
{}'''.format(valor))
print ('*' *30)

print ('O maior valor digitado foi : {} nas posições '.format(maior), end='')
for i, v in enumerate(valor):
    if v == maior:
        print ('{}...' .format (i+1))
print()   

print ('O menor valor digitado foi: {} nas posições ' .format (menor), end='')
for i, v in enumerate(valor):
    if v == menor:
        print ('{}...' .format (i+1))
print()   


# Faça um programa que leia 5 valores 
# numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas 
# posições na lista.
