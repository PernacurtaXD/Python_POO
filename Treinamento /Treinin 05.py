import os 

os.system("clear")
num1 = int(input("Digite um número:"))
num2 = int(input("Digite mais um número:"))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

os.system("clear")

print(f"Soma = {soma}")
print(f"Subtração = {sub}")
print(f"Multiplicação = {mult}")
print(f"Divisão = {div}")