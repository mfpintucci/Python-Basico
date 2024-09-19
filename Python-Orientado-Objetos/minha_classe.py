class MinhaClasse:
    
    def __init__(self, att):
        self.meu_atributo = 'Olá Mundo'
        self.meu_atributo2 = att
            
            
    def meu_metodo(self):
        print ("Estou no Método!")
        
    def meu_metodo2(self, num, mult):
        return num * mult
    
    
#objeto = MinhaClasse()
#result = objeto.meu_metodo2(3,2)
#print(result)
#att = objeto.meu_metodo()
#print(objeto.meu_atributo)
#print(att)

objeto = MinhaClasse('meu atributo')
print(objeto.meu_atributo2)