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
        self.i = 0

    def calculo_notas(self): 
        for i, notas_aluno in notas:
           self.soma+=notas_aluno
           self.contador = self.contador + 1     
           

        self.media = self.soma / self.contador
   

    def __str__(self):
        return (f"Aluno: {self.nome}"
                f"\nData de Nascimento: {self.datNascimento}"
                f"\nMédia: {self.media:.2f}")
                                            
         


nome_aluno = input("Qual o nome completo do aluno: ")
datNasc_aluno = input("Qual é a data de Nascimento do aluno: ")

for i in range(QUANT):
    nota = float(input(f"Digite sua {i+1}ª nota:"))
    notas.append(nota)

boletim = Boletim(notas, nome_aluno, datNasc_aluno)

boletim.calculo_notas()
print(boletim)
boletim.exibir_notas()