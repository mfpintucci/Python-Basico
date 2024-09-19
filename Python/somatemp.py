def somatemp():
    soma = 0
    cont=1
    while cont <=30:
        temp = float(input('temperatura'))
        soma = soma +temp
        cont+=1

    return soma



#inicio
s=somatemp()
print('A soma das temperaturas é' , s)
#fim