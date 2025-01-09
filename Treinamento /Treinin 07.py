import os 

class ControleRemoto:
    def __init__(self, valor_da_cor, altura, profundidade, largura):
        self.cor = valor_da_cor
        self.altura = altura 
        self.profundidade = profundidade
        self.largura = largura 

    def passar_canal(self, botao):
        if botao == '+':
            print("Aumentar o canal")
        elif botao == '-':
            print("Diminuir o canal")

os.system("clear")

controle_remoto = ControleRemoto('preto', '10cm', '2cm', '2cm')
print(controle_remoto.altura)
controle_remoto.passar_canal("+")

controle_remoto2 = ControleRemoto("\ncinza", "10cm", "2cm", "2cm")
print(controle_remoto2.cor)
controle_remoto.passar_canal("-")

controle_remoto3 = ControleRemoto("\nbranca", "12cm", "3cm", "2cm")
print(controle_remoto3.cor)
controle_remoto.passar_canal("+")