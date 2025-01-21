import os 

os.system("cls || clear")

nota1 = float(input("Digite sua 1º nota:"))
nota2 = float(input("Digite sua 2º nota:"))
nota3 = float(input("Digite sua 3º nota:"))

media = (nota1 + nota2 + nota3) / 3

os.system("cls || clear")

print(f"1º Nota: {nota1}")
print(f"2º Nota: {nota2}")
print(f"3º Nota: {nota3}")
print(f"Média: {media:.2f}")