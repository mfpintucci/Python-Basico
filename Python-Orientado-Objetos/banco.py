class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.__saldo = 0
        
    #metodo acessor get_saldo 
    
    property
    def ver_saldo(self):
        return self.__saldo
     
    #metodo modificador set_saldo => não utilizado em bancos
    
    def depositar(self, valor):
        if valor < 0:
            return 'Valor deve ser positivo'
        self.__saldo +=valor
        
    
    def sacar(self,valor):
        if valor < 0:
            return 'Valor deve ser positivo'
        if valor > self.__saldo:
            return 'Saldo Insuficiente'
        self.__saldo -= valor

if __name__ =='__main__':
    c1 = Conta(1, 'Rafael')