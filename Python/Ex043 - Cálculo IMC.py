print ('Vamos calcular seu IMC')
print ('×' *30)

peso = float(input('Insira aqui o seu peso (kg): '))
altura = float(input('Insira aqui a sua altura (m): '))

imc = peso /(altura**2)

print ('Seu IMC é de {:.2f}' .format(imc))

if imc <18.50:
    print ('Magreza')
 
elif imc >=18.50 and imc<24.90:
     print ('Normal')

elif imc >= 24.90 and imc<30:
    print ('Sobrepeso')

elif imc>30:
    print ('Obesidade')
    


#IMC
