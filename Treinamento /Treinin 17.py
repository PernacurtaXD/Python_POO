import os

os.system("cls || clear")
notas = []
soma = 0


for i in range(3):
    nota = float(input(f" Digite a {i + 1}ª nota: "))
    notas.append(nota)
    
    soma = soma + nota




for i in range(3):
    print(f"{i + 1}ª Nota: {notas[i]}")

print(soma)