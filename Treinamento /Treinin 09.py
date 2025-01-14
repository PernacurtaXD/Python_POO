import os 
from enum import Enum

class Profissão(Enum):
    ILUSTRADOR = "Ilustrador"
    ARTISTA_FREELANCER = "Artista Freelancer"
    MOTORISTA = "Motorista"
    MEDICO = "Médico"

class Pessoa():
    def __init__(self, nome, datNascimento, email, cpf, cp: Profissão):
        self.nome = nome 
        self.datNascimento = datNascimento
        self.email = email
        self.cpf = cpf
        self.cp = cp
    
    def __str__(self):
        return f"Nome: {self.nome}\nData de Nascimento: {self.datNascimento}\nEmail: {self.email}\nCPF: {self.cpf}\nCargo: {self.cp.value}"
             
class Artista(Pessoa): 
    def __init__(self, nome, datNascimento, email, cpf, cp, portfolio, tipo_artista):
        super().__init__(nome, datNascimento, email, cpf, cp)
        self.portf = portfolio
        self.tipo_artista = tipo_artista
       
    def __str__(self):
        return f"\n{super().__str__()}\nQuantidade de artes: {self.portf}\nTipo de Artista: {self.tipo_artista}"

class Motorista(Pessoa):
    def __init__(self, nome, datNascimento, email, cpf, cp, cnh):
        super().__init__(nome, datNascimento, email, cpf, cp)
        self.cnh = cnh


    def __str__(self):
        return (f"\n{super().__str__()}\nCNH: {self.cnh}")

class Medico(Pessoa):
    def __init__(self, nome, datNascimento, email, cpf, cp, crm):
        super().__init__(nome, datNascimento, email, cpf, cp)
        self.crm = crm

    def __str__(self):
        return f"\n{super().__str__()}\nCRM: {self.crm}"


os.system("cls || clear")

artista = Artista("Luis", "04/11/2005","luis@gmail.com", "0000000-00", Profissão.ILUSTRADOR, 6, "Ilustrador")
print(artista)


artista2 = Artista("Gustavo", "15/03/2006", "black@gmail.com", "1111111-11", Profissão.ARTISTA_FREELANCER, 69, "Ilustrador RPG")
print(artista2)



motorista = Motorista("Leonardo", "20/05/2007", "leo@gmail.com", "2222222-22", Profissão.MOTORISTA,"111111111-12")
print(motorista)


motorista2 = Motorista("José", "10/02/2001", "jo@gmail.com", "1213141-20", Profissão.MOTORISTA, "22222222-23") 
print(motorista2)

medico = Medico("Marcos", "20/10/1999", "mar@gmail.com", "326532-56", Profissão.MEDICO, "111111232")
print(medico)