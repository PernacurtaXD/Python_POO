import os 


os.system("cls || clear")

print("1- Janeiro\n2- Fevereiro\n3- Março")
print("4- Abril\n5- Maio\n6- Junho")
print("7- Julho\n8- Agosto\n9- Setembro")
print("10- Outubro\n11- Novembro\n10- Dezembro")
opcao = int(input("Escolha uma das opções?"))

match(opcao):
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:    
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Opção inválida")