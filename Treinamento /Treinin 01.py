
class Funcionario:
    def __init__(self):
        self.__senha = 'senha'

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self , valor):
        self.__senha = valor