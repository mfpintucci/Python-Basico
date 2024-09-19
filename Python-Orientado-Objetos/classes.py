class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
        self.editora = "Nome da Editora"
        
    def identidade(self):
        return (f' Sou o livro {self.nome}, e estou salvo no endereço de memória: {id(self)}')

if __name__ == '__main__':

    livro_1 = Livro("O Senhor dos Anéis" , "J.R. Tolken")
    livro_2 = Livro("Harry Potter" , "J. K. Rowling")


    print('livro 1:' , vars(livro_1))
    print(livro_1.nome)
    print(livro_1.autor)

    print('livro 2:' , vars(livro_2))

