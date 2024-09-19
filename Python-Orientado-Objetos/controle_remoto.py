class ControleRemoto:
    
    #características / atributos
    def __init__(self, televisao , comodo):
        self.televisao = televisao
        self.comodo = comodo
        
    #ações / métodos
    def avancar_canal(self):
        print('Canal Avancado')
        
        
    def voltar_canal(self):
        print ('Voltar o Canal')
        
        
    def escolher_canal(self, canal):
        print ('alterado para o canal :{} '.format(canal))
        

#objeto        
controle_sala = ControleRemoto ('samsung', 'sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolher_canal(12)

#objeto
controle_quarto =ControleRemoto('LG' , 'quarto')
print(controle_quarto.comodo)
print(controle_quarto.televisao)