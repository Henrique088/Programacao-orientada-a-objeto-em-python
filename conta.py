class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo da conta é de {} da conta do {}".format(self.__saldo,self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self,valor):
        valor_disponivel_para_sacar = self.__saldo + self.limite
        return valor <= valor_disponivel_para_sacar

    def saca(self,valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor de {} a ser sacado ultrapassou o limte".format(valor))

    def transferir(self,conta,valor):
        if self.saca(valor)==True:
            self.saca(valor)
            conta.deposita(valor)
            print("teste")
        else:
             return print("Saldo indisponivel para transferência")
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
    def codigo_banco():
        return "001"

    @staticmethod
    def condigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}