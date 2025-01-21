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

            print("Tarefas pendentes:")
            for materia in lista:
                print(f"- {materia}")

            alterar_tarefa = input("\nQual é a matéria que foi concluída: ")

            if alterar_tarefa in lista:  
                tarefa_concluida = input("Digite o novo estado (ex: Concluída ou Pendente): ")
                
                for i, materia in enumerate(lista):
                    if materia == alterar_tarefa:
                        lista[i] = f"{alterar_tarefa} ({tarefa_concluida})"
                        print(f"Tarefa '{alterar_tarefa}' atualizada para: {tarefa_concluida}")
            else:
                print(f"Tarefa '{alterar_tarefa}' não encontrada na lista.")

            input("\nPressione Enter para continuar...")

            

        
        case 4:
            os.system("cls || clear")
            
            for materias in lista:
                print(materias)

            input("Aperte Enter para continuar...")

        case 0:
            break
            

