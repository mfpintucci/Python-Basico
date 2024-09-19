#Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas 
# utilizando o construtor "list" , a função range ou colocando valores separados por vírgula dentro de 
# colchetes. Listas são objetos mutáveis, portanto podemos alterar seus valores após sua criação.


frutas = ["laranja", "maçã","uva"]
letras = list("python")
numeros = list(range(11))
carro = ["Ferrari", "F8", 42000000 , 2020, 2900 , "São Paulo", True]

print(frutas)
print(letras)
print(numeros)
print(carro)

# a lista é uma sequencia e uma forma de acessar seus
# dados é utilizando índices, onde o primeiro
# elemento encontra-se no índice zero.

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[-1])
print(frutas[-3])


#além de acessar elementos diretamente, podemos 
# extrair um conjunto de valores de uma sequencia,
# Para isso basta passa o indice inicial e/ou final
# para acessar o conjunto. Podemos ainda informar 
# quantas posições o cursos deve "pular" no acesso.

fatiamento = list("fatiamento")
print(fatiamento)

print(fatiamento[2:])
print(fatiamento[:2])
print(fatiamento[1:3])
print(fatiamento[0:3:2])
print(fatiamento[::])
print(fatiamento[::-1])

# a forma mais comum de percorrer dados em uma lista é utilizando o comando for

#Compreensão de listas
#A comprrensão de lista oferece uma sintaxe mais curta quando você deseja criar uma nova lista com base nos valores de uma lista existente, filtro, ou gerar uma nova lista aplicando uma modificação nos elementos de uma lista existente.

#possivel realizar através do laço for

#filtro versão 1

numeros = [1,30,21,2,9,65,34]
pares =[]


for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)
        

print(pares)


#filtro versão 2

numeros = [1,30,21,2,9,65,34,36]
pares = [numero for numero in numeros if numero %2 == 0 ]
print(pares)

#Modificando valores versão 1
#Elevando ao quadrado

numeros = [1,30,21,2,9,65,34,36]
quadrado = []

for numero in numeros:
    quadrado.append(numero**2)
    
print(quadrado)


#inline
numeros = [1,30,21,2,9,65,34,36]
quadrado1 = [numero**2 for numero in numeros]
print(quadrado1)

#métodos da classe list

#APPEND
lista1 = []

lista1.append(1)
lista1.append("Python")
lista1.append([40,30,20])

print(lista1)

#CLEAR

lista2 = [1,2,3]
print(lista2)
lista2.clear()
print(lista2)

#COPY

lista3 =[4,5,6]
l4 = lista3.copy()
print(lista3)

print (id(lista3))
print(id(l4))
#retorna um lista igualzinha mas com uma instancia diferente , que pode ser comprovado pelos diferentes números de ID.

#count

cores = ["vermelho", "azul", "verde", "azul"]
print(cores.count("vermelho")) #1
print(cores.count("azul")) #2
print(cores.count("verde")) #1
print(cores.count("amarelo")) #0

#Extend
#une duas listas, um merge

linguagens = ["python" , "js" , "c"]
print(linguagens) 
linguagens.extend(["java" , "csharp"])
print(linguagens)

#Index
#busca a primeira ocorrência

print(linguagens.index("java")) #3
print(linguagens.index("csharp")) #4

#pop
#o comando pop remove um elemento da sua lista. se você não determina qual o índice do item que deseja remover, ele irá sempre removendo o último.

print(linguagens) 
linguagens.pop() #csharp
print(linguagens)
linguagens.pop() #java
print(linguagens)
linguagens.pop(0) #python
print(linguagens)

#remove
#removo somente a primeira ocorrencia.
#para remover os demais você precisa saber quantas ocorrencias  tem com o acount e desenvolver uma lógica pra remover todas as ocorrências através do laço for.


linguagens1 = ["python" ,"js" , "c", "java", "csharp"]
linguagens1.remove("java")
print(linguagens1)


#reverse
#espelhamento, dá pra fazer por fatiamento também

linguagens2= ["python", "js", "c", "java", "csharp"]
print(linguagens2)
linguagens2.reverse()
print(linguagens2)

#sort
#irá oerdenar a lista
print(linguagens2)

linguagens2.sort()
print(linguagens2)

linguagens2.sort(reverse=True)
print(linguagens2)

lingua3=linguagens2.copy()
print(lingua3)

#lambda representa função anonima ; x representa os argumentos , no caso, os objetos da lista.

lingua3.sort(key=lambda x: len(x))
print(lingua3)

lingua3.sort(key=lambda x: len(x), reverse=True)
print(lingua3)

#len , função built in
#possivel verificar tamanho da string e também tamanho da lista.








