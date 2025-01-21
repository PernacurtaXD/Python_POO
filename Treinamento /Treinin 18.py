import os 


QUANT = 3
notas = []
soma = 0

class Boletim:
    def __init__(self, nota, media, nome, dataNascimento, unidade):
        self.nota = nota
        self.media = media 
        self.nome = nome
        self.datNascimento = dataNascimento
        self.unidade = unidade

    def calculo_notas(self):
        for notas_aluno in notas:
           soma+=notas_aluno


for i in range(QUANT):
    nota = float(input(f"Digite sua {i}ª nota:"))
    notas.append(nota)
