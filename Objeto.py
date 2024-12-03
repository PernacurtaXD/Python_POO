import os 

os.system("cls || clear")

class Pessoa:
# Inicializador que recebe o valor do objeto vindo de fora da classe
    def __init__(self, nome, sobrenome):
         # Objeto ↓           Atributo ↓
        self.nome =             nome
        self.sobrenome =        sobrenome

    def unir_nomes(self):
        #O parâmetro 'self' que permite o acesso dos atributos em outra função apenas dentro da classe
        self.nome_completo  = self.nome + ' ' + self.sobrenome
        print(f"O nome completo é {self.nome_completo}")

#Criar uma instância
nome = input(str("Digite seu nome:"))
sobrenome = input(str("Digite seu sobrenome:"))
pessoa = Pessoa(nome, sobrenome)


pessoa.unir_nomes()