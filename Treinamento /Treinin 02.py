import os 

class Funcionario:
    def __init__(self, senha):
        self.__senha = senha

gerente = Funcionario('senha')
print(f"Senha do Gerente: {gerente.__senha}") # <- Tá funcionando rlx
