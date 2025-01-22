import os 

notas = []
QUANT = 3
media = 0


os.system("cls || clear")

class Boletim:
    def __init__(self, nota, nome, dataNascimento):
        self.nota = nota
        self.nome = nome
        self.datNascimento = dataNascimento
        self.soma = 0
        self.media = 0
        self.contador = 0

    def calculo_notas(self): 
        for notas_aluno in notas:
           self.soma+=notas_aluno
           self.contador = self.contador + 1     

        self.media = self.soma / self.contador

    def __str__(self):
        return f"Média: {self.media}"


nome_aluno = input("Qual o nome completo do aluno: ")
datNasc_aluno = input("Qual é a data de Nascimento do aluno: ")

for i in range(QUANT):
    nota = float(input(f"Digite sua {i+1}ª nota:"))
    notas.append(nota)

boletim = Boletim(notas, nome_aluno, datNasc_aluno, "3")

boletim.calculo_notas()
print(boletim)