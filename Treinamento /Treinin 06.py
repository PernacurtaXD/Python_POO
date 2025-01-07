import os 

QUANT = 5

os.system("cls || clear")

for i in range (QUANT):
    nota = float(input(f"Digite sua {i+1} nota: "))
    soma = nota + nota

print(soma)