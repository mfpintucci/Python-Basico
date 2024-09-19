#cirando sets , conjuntos

#um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iteravel.

set([1,2,3,3,1,3,4])  #{1,2,3,4}
set("abacaxi") #{"a", "i","b", "c", "x"}
set(("palio", "gol" , "celta", "palio"))  #{"gol", "celta", "palio"}

#conjuntos em python não suportam indexação e nem fatiamento. Caso queira acessar seus valores é necessário converter para lista.

#iterar conjuntos
#a forma mais comum para percorrer os dados de um set / conjunto é utilizando o comando for.

carros = {"gol" , "celta", "palio"}

for carro in carros:
    print(carro)
    
#função enumerate
#as vezes é necessário saber qual o índice do objeto dentro do laço for, para isso podemos utilizar a função enumerate.


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
    

#É possível realizar operações matemáticas de conjuntos utilizando o set.

#.union

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.union(conjunto_b))

#ai que emoção!!!
#intersection

print(conjunto_a.intersection(conjunto_b))

#difference

print(conjunto_a.difference(conjunto_b)) #1
print(conjunto_b.difference(conjunto_a)) #4 

#symmetric_difference

print(conjunto_a.symmetric_difference(conjunto_b)) #1,4

#issubset #corresponde ao pertence #esta contido

conjunto_c = { 1,2,3}
conjunto_d = {4,1,2,5,6,3}

print(conjunto_c.issubset(conjunto_d)) #true
print(conjunto_d.issubset(conjunto_c)) #false

#issuperset #não pertence #não está contido

print(conjunto_c.issuperset(conjunto_d)) #false
print(conjunto_d.issuperset(conjunto_c)) #true

#isdisjoint, #operação de conjunto disjunto, não há intersecção. Todos os elementos de um conjunto nãoo estão presentes em outro conjuto. # não há intersecção

conjunto_e = {1,2,3,4,5}
conjunto_f = {6,7,8,9}
conjunto_g = {1,0}

print(conjunto_e.isdisjoint(conjunto_f)) #true
print(conjunto_e.isdisjoint(conjunto_g)) #false


#add
#adiciona item no conjunto ,  mais ou menos como no append. a diferença é que se o item que for add já existir no conjunto set, ele será ignorado. ( em listas ele seria duplicado)

#clear limpa o set
#copy realiza a cópia
#discard descarta um valor do set. Se você passar um valor que não existe para descartar o comando será ignorado.
#Pop 