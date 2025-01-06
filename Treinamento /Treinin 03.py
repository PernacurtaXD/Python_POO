import os 


class Pessoa:
    def __init__(self, nome: str, idade:int, datNascimento:str):
        self.nome = nome 
        self.idade = idade
        self.datNascimento = datNascimento

    def exibir_dados(self):
        return f"Seu nome é {self.nome} e tem {self.idade} anos, e nasceu em {self.datNascimento}."


nome1 = input("Digite seu nome:")
idade1 = int(input("Digite sua idade:"))
dataNasci = input("Digite sua data de Nascimento:")

os.system("cls || clear")

pessoa1 = Pessoa(nome1, idade1, dataNasci)
print(pessoa1.exibir_dados())        