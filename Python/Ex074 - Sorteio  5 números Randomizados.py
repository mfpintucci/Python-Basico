from random import randint
maior = 0
sort = ( randint(1,10),randint(1,10),randint(1,10),
		randint (1,10) , randint (1,10))
print ('Eu sorteei os números ' , end ='') 
for c in (sort):
    print (c , end=' ')
    
print ('\nO maior valor sorteado foi {}.' .format (max(sort)))
print ('O menor valor sorteado foi {}.' .format (min(sort)))
      
    
#crie um programa que gere cinco numeros 
#aleatorios e armazene dentro de uma tupla
#depois disso mostre a listagem de numeros 
#sorteados e indique o menor e maior valor.

