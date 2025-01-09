import os 
#Criando classe para clintes da Netflix

class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome 
        self.email = email 

        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano 
        else:
            raise Exception("Plano inválido") 
       


    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        
        else: 
            print("Plano inválido")


    def ver_filme(self, filme, plano_do_filme): 

        if self.plano == plano_do_filme:
            print(f"Ver Filme {filme}")    
        elif self.plano == "premium":
            print(f"Ver Filme {filme}")
        elif self.plano == "basic" and plano_do_filme == "premium":
            print("Faça upgrade para premium para ver esse filme")
        else:
            print("Plano Inválido")


os.system("cls || clear")

cliente = Cliente("Luis", "luis@gmail.com", "basic")
print(cliente.plano)
cliente.ver_filme("Spider Man", "premium")

#no botão de upgrade 
cliente.mudar_plano('premium')
print(cliente.plano)
cliente.ver_filme("Spider Man", "premium")
