#O que são funções?
#função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros, esses parâmetros podem ou não ter valores padrões. Usar funções torna o código mais legível e possibilita o reaproveitamento de código. Programar baseado em funções é o mesmo que dizer que estamos programando de maneira estruturada.//paradigma


def exibir_mensagem():
    print("Olá Mundo!")


    
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")
    
    
#Retornando valores
#Para retornar um valor, utilizamo a palavra reservada  return. Toda função Pythin retorna None como padrão. Diferente de outras linguagens de programação, em Python uma função pode retornar mais de um valor.

#Args e Kwargs
#podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos *args **kwargs, o método recebe os valores como tupla e dicionário respectivamente.

#Parametros especiais
#por padrão , argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome. Para melhor legibilidade e desempenho, faz sentigo restringir a maneira pelo qual argumentos possam ser passados, assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome ou por nome.



