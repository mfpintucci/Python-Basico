#Desafio
#Daenerys é a khaleesi dos Dothraki. Juntamente com Drogon, eles vão atrás do Tyrion, para tentar dominar Westeros. Ela possui, além do seu dragãozinho, um rastreador que mede o nível de energia de qualquer ser vivo. Todos os seres com o nível menor ou igual a 8000, ela considera como se fosse um inseto. Quando passa deste valor, que foi o caso do Drogon, ela se espanta e grita “Mais de 8000”. Baseado nisso, utilize a mesma tecnologia e analise o nível de energia dos seres vivos.

#Entrada
#A primeira linha contém um número inteiro C relativo ao número de casos de teste. Em seguida, haverá C linhas, com um número inteiro N (100 <= N <= 100000) relativo ao nível de energia de um ser vivo.

#Saída
#Para cada valor lido, imprima o texto correspondente.

#''' 
#IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
# - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
#   casos, é necessário converter/tratar os dados de entrada; 
# - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
#   impressão dos dados de saída. 
#'''
#    ''' 
#    TODO Leia as as entradas e crie as condições necessárias para verificar se é maior ou
#    menor do que 8000 e imprima "Inseto!" ou "Maior que 8000!" para cada caso.
#    '''


C = int(input()) 

for i in range (C):
  
  N = int(input())
  teste = []
  teste.append(N)
  
  for n in teste:
    if N > 8000:
      print("Mais de 8000!")
    
    else:
      print("Inseto!")

    
