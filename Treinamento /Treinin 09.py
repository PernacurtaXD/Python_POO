import os 

class Pessoa:
    def __init__(self, nome, datNascimento, email, cpf):
        self.nome = nome 
        self.datNascimento = datNascimento
        self.email = email
        self.cpf = cpf
    
    def __str__(self):
        return f"Nome: {self.nome}\nData de Nascimento: {self.datNascimento}\nEmail: {self.email}\nCPF: {self.cpf}"
             
class Artista(Pessoa): 
    def __init__(self, nome, datNascimento, email, cpf, portfolio, tipo_artista):
        super().__init__(nome, datNascimento, email, cpf)
        self.portf = portfolio
        self.tipo_artista = tipo_artista

    def __str__(self):
        return f"\n{super().__str__()}\nQuantidade de artes: {self.portf}\nTipo de Artista: {self.tipo_artista}"

os.system("cls || clear")

artista = Artista("Luis", "04/11/2005","luis@gmail.com", "0000000-00", 6, "Ilustrador")
print(artista)


artista2 = Artista("Gustavo", "15/03/2006", "black@gmail.com", "1111111-11", 69, "Ilustrador RPG")
print(artista2)
