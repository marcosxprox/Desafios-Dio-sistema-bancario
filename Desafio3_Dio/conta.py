from historico import Historico

class Conta:

    def __init__(self, cliente, numero):
        self._cliente = cliente
        self._numero = numero
        self._saldo = 0
        self._agencia = "0001"
        self._historico = Historico()


    def sacar(self, valor):

        if self._saldo >= valor:
           self._saldo -= valor
           print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self._saldo:.2f}")
           return True

        else:
            print("Você não tem saldo suficiente para essa transação")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self._saldo:.2f}")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @property
    def agencia(self):
        return self._agencia

    def __str__(self):
        return f"Cliente: {self.cliente}"