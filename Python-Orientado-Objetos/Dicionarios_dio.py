#|Um dicionario é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por colchetes ou pelo construtor dict e contem uma lista de pares chave:valor separados por vírgula.

#As chaves devem ser compostas por valores imutaveis como tuplas e strings e a o valor pode ser qualquer objeto. 

pessoa = {"nome": "Mariane", "idade":37 }

#ou

pessoa = dict(nome="Mariane" , idade=38)

#no comando abaixo, eu insiro valor ao meu dicionario, sendo que o conteudo entre colchetes refere-se a chave imutavel do dicionário

pessoa["telefone"] = "(11) 99299-6212" 

print(pessoa)

dados = {"nome": "Mariane", "idade":37 , "telefone" : "(11) 99299-6212"}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])


#""Fazendo uma analogia com dados, isso me leva a pensar que as chaves tratam-se dos metadados, e os valores, tratam-se dos dados inseridos em cada linha. cada linha de uma tabela, é um dicionário?""""

dados["nome"] = "Mariane Ferraresi"
dados["idade"] = 38

#haverá uma substituição de valores no dicionário

print(dados)

#dicionarios podem armazenar qualquer tipo de objeto em Python com valor , desde que a chave para este valor seja imutavel.

#dicionarios aninhados

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com":{"nome" : "Giovanna" , "telefone" : "2226-2542"},
    "chappie@gmail.com" :{"nome" : "Chappie" , "telefone" : "4437-2642"}
}

print(contatos)
print(contatos["giovanna@gmail.com"]["telefone"])

#a forma mais comim de percorrer dados de um dicionario, ou iterar sobre ele, é utilizando o comando for.

for chave in contatos:
    print(chave, contatos[chave])
    
    
#ou

for chave, valor in contatos.items():
    print(chave, valor)
    

#métodos da classe dict

#clear
#utilizado para limpar o dicionario

#contatos.clear()

#COPY
#faz uma cópia do dicionário

#fromkeys
#cria chaves pra vc com valor None ou cria com valor vazio.

#Exemplo de código

#dict.fromkeys(["nome ", "telefone"])
print(dict.fromkeys(["nome ", "telefone"]))
#ou

print(dict.fromkeys(["nome ", "telefone"],"vazio"))

#get
#segunda for a de acessar valor dentro de um dicionario, quando você não tem certeza de qual o valor da chave. 

contatos["chave"] #keyerror

contatos.get("chave") #None
contatos.get("chave" , {})   #{}
contatos.get("guilherme@gmail.com", {})
#{"nome": "Guilherme", "telefone": "3333-2221"}

#pop
#remove a ultima chave ou remove a chave que você escolher

#setdefault
#insere valor dentro do seu dicionário caso ele não exista .

#update
#quando você faz um dicionario.upddate ele irá pesquisar se tem dois dicionarios com a mesma chave e atualizar, transformando em um dicionário só.

#Values
#retornar os valores. 

#in 
# #forma elegante de verificasr se uma chave existe em um dicionario

#del
#excluir valor.
#basta informar o objeto que deseja remover.

#del contatos["guilherme@gmail.com"]["telefone"]
#neste primeiro caso irá apagar o telefone de guilherme
#del contatos ["chappie@gmail.com"]
#neste segundo caso, irá apagar todo o contato de chappie, uma vez q informo a chave principal.

#se fizer somente del contatos ele ira apagar o dicionario inteiro.