class Pessoa:   #Substantivo
    def __init__(self, nome, idade, cpf):
        self.nome = nome 
        self.idade = idade
        self.__cpf = cpf
        
        
#Metodo #verbos

    def correr(self):
        print('Estou Correndo')
        
    
    def __apresentar_documento(self):
        print(self.__cpf)        
        
#encapsulamento privado, o objeto não utiliza, somente a Classe.
    def beber (self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('bebendo...')

#objeto
objeto = Pessoa('Mariane', 37 ,'337285518SX')
print(objeto.nome)
print(objeto.idade)
#print(objeto.cpf) - apresenta erro depois da inserção dos __ porque foi tornado privado
#objeto.__apresentar_documento()

objeto.beber('cerveja')
objeto.beber('coca-cola')