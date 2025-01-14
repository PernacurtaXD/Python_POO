import os 


def lista_tarefa(quant_tarefas, tarefa):
    print("\nLista de Tarefas")
    for i in range(quant_tarefas):
        print(f"{tarefa}")
    return tarefa


while True:
    print("1- Listagem de Tarefa ")
    print("2- Remover Tarefa")
    print("3- Marcar Tarefa Concluída")
    print("4- Exibir Tarefa")
    opcao = int(input("Escolha uma das opções:"))
    alternativa = input("Deseja encerrar(S/N)?")

    match(opcao):
        case 1:
            tarefas_aula = input("Qual é a matéria?")
            quantidades_tar = int(input("Quantas Atividades você possui nessa matéria?"))

            listagem = lista_tarefa(quantidades_tar, tarefas_aula)
            