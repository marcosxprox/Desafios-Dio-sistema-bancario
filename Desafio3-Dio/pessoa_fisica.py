from modulo_cliente import Cliente

class PessoaFisica(Cliente):

    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf

    def __str__(self):
        return f'Nome: {self._nome}, CPF: {self._cpf}'