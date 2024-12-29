import os 

class Pessoa:
    #Método construtor: inicializa cada nova instancia da classe Pessoa 
    def __init__(self, nome, idade):
        self.nome = nome  #Atributo para armazenar o nome 
        self.idade = idade #Atributo para armazenar a idade 

    #Método de instância: exibe uma mensagem de apresentação
    def apresentar(self):
        os.system("cls || clear")
        print(f"Olá meu nome é {self.nome} e tenho {self.idade} anos.") 


#Criação de uma instância da Classe Pessoa
pessoa1 = Pessoa('João', 25)

pessoa1.apresentar()
