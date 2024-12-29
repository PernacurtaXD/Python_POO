import os

class Circulo:
    pi = 3.14159 #Atributo da classe 

    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return self.pi *  (self.raio ** 2)

os.system("cls || clear")

#Uso do método
circulo = Circulo(5)
print(f"A área do círculo é: {circulo.area():.2f}")


#Método estático que opera sem referência a uma instância específica 
class Matematica:
    @staticmethod
    def somar(x, y):
        return x + y
    
#Uso do método estático
resultado = Matematica.somar(10,15)
print(f"Resultado da soma: {resultado}")