dic = {
    'alimentos' :{
        "pizzas": ['margueritta', 'mussarella', 'frango com catupiry', 'portuguesa'],
        
    "bolos": ("floresta negra", "red velvet", "de laranja", "da vó"),
    
    "calorias": {
        "leite" : 120, "fatia de pizza" : 320 , "agua" : 0, 'maçã' : 95
        }
    },
    
    
    'linguagens': [
        {'nome':'javascript', 'criacao': 1996,
         'paradigmas' : ["eventos", "funcional"]},
        {'nome' : 'python', 'criacao' : 1991,
         'paradigma' : ['orientada a objetos', 'estruturada']},
        {'nome': 'haskell', 'criacao': 1990, 'paradigma': ['funcional']}
        ]
    }

#só se aprende fazendo. Pause o vídeo e tente respponder

#se possível faça junto no seu computador.

#1. quantas chaves tem o dicionario dic
print("r1", len(dic))

#2. dic['linguagens'] é uma tupla, um dicionário ou uma lista?
print("r2", type(dic['linguagens']))

#3. Como eu faço para exibir todos os bolos ?
print("r3", (dic.get('alimentos')).get('bolos'))

print("r3b", dic['alimentos']['bolos'])

#4.Qual o tipo de lista de todos os bolos?
print("r4", type(dic['alimentos']['bolos']))

#5. O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?

#print("r5", dic['linguagens']['javascript']['criacao']) da erro de acesso
#listas de indices devem ser inteiros ouu fatias, não strings
#print("r5", (dic.get('linguagens'[0])))
#imprime NONE

print("r5", (dic["linguagens"][0]["criacao"]))


