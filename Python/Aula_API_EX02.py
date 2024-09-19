dic = {
    'alimentos' :{},
    'linguagens': [
        {'nome':'javascript', 'criacao': 1996,
         'paradigmas' : ["eventos", "funcional"]},
        {'nome' : 'python', 'criacao' : 1991,
         'paradigma' : ['orientada a objetos', 'estruturada']},
        {'nome': 'haskell', 'criacao': 1990, 'paradigma': ['funcional']}
        ]
    }

#10 EScreva uma função "mais velha" que
#a recebe um dicionario como dic e
#b retorna (isso é diferente de imprimir) a liguagem de programação mais velha

#11 Escreva uma função que retorna uma lista (sem repetições) de paradigmas.

#Objetivo do exercício, aprender a programar funções que lêem listas e dicionários , para obter um conjunto específico de informações.

def mais_velha(dic):
    lista_linguagens = dic['linguagens']
    ling_velha = lista_linguagens[0]
    for linguagem in lista_linguagens:
        if linguagem['criacao'] < ling_velha['criacao']:
            ling_velha = linguagem
    return ling_velha

    