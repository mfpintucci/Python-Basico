class Veiculo:
    
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
        
    def ligar_motor(self):
        print("Ligando o motor")


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self,cor, placa, numero_rodas, carregado):
        self.carregado = carregado
     
    
    def esta_carregado(self):
        if self.carregado == True :
            print('Estou carregado')
        else:
            print('Não estou carregado')
            
moto = Motocicleta('preta', 'acc-1234', 2)
moto.ligar_motor()

carro = Carro('branco', 'eni-6685', 4)
carro.ligar_motor()

caminhao = Caminhao('roxo', 'xbd-4065', 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()


