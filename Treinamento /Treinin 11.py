import os 
contador = 0
lista = []


def cab():
    os.system("cls || clear")

def lista_tarefas(tarefas):
    for i in range(quantidades_tar):
        materia = input(f"{i+1}º Digite a tarefa pendente:")
        lista.append(materia)         
        


def exibir_tarefas(materias):

    print("\nAtividades pendentes")    
    for materia in materias:
        print(materia)
        
        return materia


while True:
    cab()
    print("1- Listagem de Tarefa ")
    print("2- Remover Tarefa")
    print("3- Marcar Tarefa Concluída")
    print("4- Exibir Tarefa")
    print("0- Sair")
    opcao = int(input("Escolha uma das opções:"))
    
   

    match(opcao):
        case 1:
            cab()
            quantidades_tar = int(input("Quantas Atividades você possui nessa matéria?"))
        case 2:
            pass      

        case 3: 
            pass 

        case 4:
            exibindo = exibir_tarefas(lista )
            print(exibindo)
            break
        case 0: 
            print("Saindo...")
            break

        case _:
            print("Opção inválida, tente novamente")
    
   
