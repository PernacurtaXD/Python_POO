import os
import time

QUANT = 7

def cab():
    os.system("cls || clear")
    time.sleep(1)

lista = []

for i in range(QUANT):
    cab()
    nome = input("Digite seu nome:")
    sobrenome = input("Digite seu sobrenome:")

    nome_completo = nome + " " +sobrenome
    lista.append(nome_completo)


cab()
for  nomes_completos in lista:
    print(nomes_completos)



