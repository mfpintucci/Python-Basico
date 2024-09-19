nome = str(input(' Digite aqui seu nome completo: ')).upper().strip()
n = nome.split()
print ('Prazer em te conhecer!')
print ('Seu primeiro nome é {}.' .format(n[0]))
print ('Seu último nome é {}.' .format(n[len(n)-1]))

#neste exercício o primeiro segredo esta em split
#pra dividir a string em conjunto de caracteres (palavras)
#depois, na logica de capturar comprimento total (len) 
#pra poder pegar  o nome completo independente do tamanho

