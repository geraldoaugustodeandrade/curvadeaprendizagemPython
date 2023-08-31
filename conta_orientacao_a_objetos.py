#Criação de um conta financeiro que requer nome, titulo, cpf, banco e que faz transaçoes simples de deposito, saque e alteração de limites. toda projetada em orientação a objetos. 
ps:curvadeaprendizagem

class Conta:
    def __init__(self,numero, titular, saldo, limite):
        print("construindo um objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print(" O Saldo de {} pertence ao titular de nome:  {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if(valor <= (self.saldo + self.limite)):
            self.__saldo -= valor
        else:
            print( " Você não possui saldo suficiente")


    def transferir( self, valor, destino):
        self.sacar(valor)
        destino.deposita(valor)
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,limite):
        self.__limite = limite

    @staticmethod
    def banco():
        return "001"





