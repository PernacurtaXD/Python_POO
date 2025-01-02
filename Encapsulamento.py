import os


os.system("cls || clear")

class ContaBancaria:
    def __init__(self, titular, numero_conta):
        self.titular = titular
        self._numero_conta = numero_conta # Atributo protegido: uso indicado dentro da classe e subclasses
        self.__saldo = 0 # Atributo privado: modificação restrita dentro da classe.



    def depositar(self, valor):
        if valor > 0: 
            self.__saldo = self.__saldo +  valor 
            print(f"Depósito de R${valor:.2f} efetuado com sucesso.")
        else:
            print("Insira um valor positivo para depósito.")



    def sacar(self, valor):
        if valor > 0 and self.__saldo >=  valor:
            self.__saldo -= valor 
            print(f"Saque de R${valor:.2f} realizado com sucesso.")


    def mostrar_saldo(self):
        return self.__saldo



    def informacoes_da_conta(self):
        return f"Titular: {self.titular}, Número da Conta: {self._numero_conta}, Saldo: {self.__saldo}"

#Criando e usando a conta bancária
conta = ContaBancaria("Alice", "001122")
conta.depositar(1000)# Não seria possível acrescentar o valor diretamente no 'saldo'
conta.sacar(150)
print(conta.informacoes_da_conta())