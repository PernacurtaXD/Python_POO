import os 
contador = 0

def cab():
    os.system("cls || clear")

def lista_tarefa(quant_tarefas):
    os.system("cls || clear")
    print("\nLista de Tarefas")
  
    for i in range(quant_tarefas):
        materias = input("Digite o nome da matéria?")
    return materias

def exibir_tarefas(quant_tarefas):
    print("\nAtividades pendentes")    
    for i in range(quant_tarefas):
        print(materias)


while True:
    cab()
    print("1- Listagem de Tarefa ")
    print("2- Remover Tarefa")
    print("3- Marcar Tarefa Concluída")
    print("4- Exibir Tarefa")
    opcao = int(input("Escolha uma das opções:"))
    
    alternativa = input("Deseja encerrar(S/N)?")
    alternativa = alternativa.upper()


    match(opcao):
        case 1:
            cab()
            quantidades_tar = int(input("Quantas Atividades você possui nessa matéria?"))

            listagem = lista_tarefa(quantidades_tar)
        
        case 4:
            exibindo = exibir_tarefas(quantidades_tar)
        case _:
            print("Opção inválida.")
    
    if alternativa == "N":
        break

