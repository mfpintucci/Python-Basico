#Tuplas
#Tuplas são estruturas de dados muito parecidas com as listas. A principal diferença é que as tuplas são imutáveis enquanto as listas são mutáveis. Podemos criar tuplas através da classe tuple, ou colocando valores separados por vírgula dentro de parenteses.

#mais restrita
#diferença sutil

frutas =("laranja", "pera", "uva",)
print(frutas)

letras = tuple("Mariane")
print(letras)

numeros = tuple([1,2,3,4])
print(numeros)

pais = ("Brasil",)
print(pais)

#para que o python entenda se é uma tupla ou uma precedência, é uma boa prática que se finalize com uma vírgula, principalmente se for uma tupla com um único elemento.

#para acessar os elementos de uma tupla, realiza-se o mesmo processo da lista, por índices.

#o uso de tuplas garante que os fatores não serão alterados, já que são imutaveis.

#count
#index
#len
