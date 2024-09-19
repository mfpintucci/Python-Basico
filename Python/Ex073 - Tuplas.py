champ = ('Atletico-MG' , 'Flamengo', 'Palmeiras',
	    'Fortaleza', 'Corinthians' ,'Bragantino' ,
	    'Fluminense' , 'America-MG' , 'Atletico-GO',
	    'Santos', 'Ceará SC' , 'Internacional',
	    'São Paulo ', 'Athletico - PR' , 'Cuiaba',
	    'Juventude', 'Gremio', 'Bahia' , 'Sport Recife',
	    'Chapecoense')
	    
print ( '-=-' *10)
print ('Lista de times {}'.format(champ)) 
print ( '-=-' *10)
print (' Os cinco primeiros colocados são:')
print(champ [0:5])
print ('-=-' * 10)
print ('Os quatro últimos colocados foram:')
print (champ [-4:])
print('-=-' * 10)
print ('Os times participantes foram:')
print (sorted(champ))
print('-=-' * 10)
print ('A Chapecoense ficou na {} posição: ' . format (champ.index("Chapecoense")+1))
	

#Exercício Python 73: Crie uma tupla preenchida 
#com os 20 primeiros colocados da Tabela do 
#Campeonato Brasileiro de Futebol, na ordem 
#de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
