class Pessoa:
    def __init__(self, v_construtor):
                                #Atributos  ↓
        self.nome =             'Luis'
        self.sobrenome =        'Santana'
        self.lista_nomes =      ['João', 'Maria']
        self.dicionario =       {'nome' : 'Luis', 'sobrenome': 'Santana'}
        self.aluno =            v_construtor


    def unir_nomes(self):
        self.nome_completo = self.nome + self.sobrenome
        print(f"O nome completo é {self.nome_completo}")
        print(f"O nome completo é {self.lista_nomes}")
        print(f"O nome completo é {self.dicionario}")
        print(f"O nome completo é {self.aluno}")


v_construtor = 'Luisinho'

pessoa = Pessoa(v_construtor)

pessoa.unir_nomes()
        