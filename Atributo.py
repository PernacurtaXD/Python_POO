class Pessoa:      #parâmetro ↓
    def __init__(self, v_construtor):
                                #Atributos  ↓
        self.nome =             'Luis'
        self.sobrenome =        'Santana'               # <- Valores de dentro da classe
        self.lista_nomes =      ['João', 'Maria']
        self.dicionario =       {'nome' : 'Luis', 'sobrenome': 'Santana'}
        self.aluno =            v_construtor #Atributo criado apartir do parâmetro

#Os atributos podem receber vários tipos de valores com origem de dentro ou fora da classe.

    def unir_nomes(self):
        self.nome_completo = self.nome +   self.sobrenome
        print(f"O nome completo é {self.nome_completo}")
        print(f"O nome completo é {self.lista_nomes}")
        print(f"O nome completo é {self.dicionario}")
        print(f"O nome completo é {self.aluno}")

#Valor passado para o construtor
v_construtor = 'Luisinho' #<- Valor fora da classe

pessoa = Pessoa(v_construtor)

pessoa.unir_nomes()
        