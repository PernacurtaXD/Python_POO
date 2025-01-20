import os 

os.system("cls || clear")
lista = []



while True:
    
    print("1- Listagem de Tarefa ")
    print("2- Remover Tarefa")
    print("3- Marcar Tarefa Concluída")
    print("4- Exibir Tarefa")
    print("0- Sair")
    opcao = int(input("Escolha uma das opções:"))


    match(opcao):
        case 1:
            quantidade_tarefa = int(input("Quantas tarefas pendentes vocÊ tem:"))
            QUANT =   quantidade_tarefa

            for i in range(QUANT):
                materia = input(f"{i+1}º matéria pendente:")
                lista.append(materia)


            os.system("cls || clear")
            

            input("Aperte Enter para continuar...")
        case 2:
            os.system("cls || clear")

            for materias in lista:
                print(materias)
            
            excluir_tarefa = input("Deseja excluir qual tarefa:")

            lista.remove(excluir_tarefa)

            input("Aperte Enter para continuar...")

        case 3:
            os.system("cls || clear")
            print("Tarefas Pendentes")
            for materias in lista:
                print(materias)

            alterar_tarefa = input("Digite a tarefa que foi concluída:")

            if alterar_tarefa in lista:

                tarefa_concluida = input("Digite se há uma tarefa conclída(ex: Concluíad ou Pendente):")

                for i, alterar_tarefa in enumerate(lista):
                    if alterar_tarefa == tarefa_concluida:
                        


            
            input("Aperte Enter para continuar...")

        
        case 4:
            os.system("cls || clear")
            
            for materias in lista:
                print(materias)

            input("Aperte Enter para continuar...")

        case 0:
            break
            

