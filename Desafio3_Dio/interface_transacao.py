from abc import ABC, abstractmethod

class Transacao(ABC):

    @property
    @abstractmethod

    def valor(self):
        pass

    def registrar(self, conta):
        pass

