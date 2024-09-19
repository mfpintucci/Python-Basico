#Criar sistema de banco fictício
#desenvolver novo sistema

#1a vs depósito, saque, extrato
#operações 
#deposito, depositar valores inteiros e positivos
#todos os depositos devem ser armazenados em uma variável, e ser exibidos em um extrato. 
#saque , o sistema deve permitir 3 saques diarios de até 500 por saque . Caso o usuario não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
#extrato : Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. 
#os valores devem ser exibidos utilizando o formato R$ xxx.xx exemplo: R$ 1500.45


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
saldo = 0
limite= 500
extrato = ""
numero_saques=0
limite_saques = 3

while True:
    
    opcao = input(menu)
    if opcao == 'd':
        print('Depósito')
    
    elif opcao == 's':
        print ('Saque')
        
        
    elif opcao == 'e':
        print("Extrato")
        
        
    elif opcao == "q" :
        break
    

else:
    print("Operação inválida, por favor selecioar novamente a operação desejada.")