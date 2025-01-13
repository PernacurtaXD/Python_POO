import os
import time

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
    
    def controlar_personagem(self, botao, botao2, botao3, botao4):
        if botao == "A" and botao2 == "Y":
            print("Soco bola de Fogo")
        elif botao3 == "X" and botao4 == "B":
            print("Aura suprema")
        elif botao == "A":
            print("Ataque Normal")
        elif botao2 == "Y":
            print("Carregar Xi")
        elif botao3 == "X":
            print("Bola flamejante")
        elif botao4 == "B":
            print("Escudo")

    def menu_jogo(self, menu):
        match(menu):
            case "S":
                print("Jogo pausado")
                time.sleep(6)
                os.system("cls || clear")
            case "N":
                print("Então bo de gameplay HAHAHAHA")                        
            case _:
                print("Opção desconhecida")
                
def cab():
    os.system("cls || clear")


cab()
menu = input("Você deseja pausar o jogo(S/N)?")
controle_game = ControleXbox("Preto", "6cm", "10m", "4cm")

os.system("cls || clear")
time.sleep(3)
controle_game.menu_jogo(menu)
controle_game.analogico_game("frente")
controle_game.controlar_personagem("","","X","B")

