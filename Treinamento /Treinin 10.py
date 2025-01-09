import os


class ControleXbox:
    def __init__(self, valor_cor, largura, comprimento, pronfundidade):
        self.cor = valor_cor 
        self.largura = largura
        self.comprimento = comprimento 
        self.profundidade = pronfundidade


    def analogico_game(self, analogico):
        if analogico == "frente":
            print("Ir para Frente")
        elif analogico == "atrás":
            print("Ir para Atrás")
        elif analogico == "direita":
            print("Ir para Direita")        
        elif analogico == "esquerda":
            print("Ir para Esquerda")
        else: 
            pass
    
    def controlar_personagem(self, botao, botao2):
        if botao == "A":
            print("Soco bola de Fogo!!")
        elif botao == "Y":
            print("Ataque especial")
        elif botao == "X":
            print("Carregar poder")
        elif botao == "B":
            print("Defesa")
        elif  botao == "A" and botao2 == "X":
            print("Ataque Normal")
        elif botao == "X" or botao2 == "B":
            print("Upar defesa")
        elif botao2 == "":
            pass


os.system("cls || clear")


controle_game = ControleXbox("Preto", "6cm", "10m", "4cm")
controle_game.analogico_game("direita")
controle_game.controlar_personagem("X","B")