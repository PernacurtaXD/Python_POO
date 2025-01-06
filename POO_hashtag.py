class Email():
    def __init__(self, nome, email):  
        self.nome = nome
        self.email = email

    def pegar_servidor(self):
        return self.email[4:]

email1 = Email("Lira", "lira@gmail.com")
print(email1.pegar_servidor())