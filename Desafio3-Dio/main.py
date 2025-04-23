from pessoa_fisica import PessoaFisica
from conta_corrente import ContaCorrente
from deposito import Deposito
from saque import Saque
import random

def cadastrar_cliente(clientes):
    cpf = input("Digite o cpf do cliente:")
    while not cpf.isdigit() or len(cpf) != 11:
        cpf = input("CPF inválido. Digite um CPF válido (11 dígitos):")

    if any(cliente.cpf == cpf for cliente in clientes):
       print("CPF já cadastrado.")
       return

    nome = input("Digite o nome completo do cliente:")
    data_nascimento = input("Digite a data de nascimento:")
    cliente = PessoaFisica(nome = nome, data_nascimento = data_nascimento, cpf = cpf, endereco = cadastrar_endereco())
    clientes.append(cliente)

def cadastrar_endereco():
    endereco = input("Digite o seu endereço:")
    numero_endereco = input("Digite o número do endereço:")
    bairro = input("Digite o bairro onde você reside:")
    estado = input("Digite o estado que está localizado:")
    endereco = f"{endereco}, Nº {numero_endereco}, Bairro: {bairro}, Estado: {estado}"
    print("\nInformações completas do endereço:")
    print(endereco)
    return endereco

def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta(cliente):
    if not cliente.contas:
        print("Cliente não possui contas")
        return

    return cliente.contas[0]

def gerar_conta():
    numero_conta = random.randint(100000, 999999)
    numero_conta_str = str(numero_conta)
    soma = sum(int(digit)
            for digit in numero_conta_str)
    digito_verificador = soma % 10
    numero = numero_conta_str + "-" + str(digito_verificador)
    print(f"Numero da conta {numero} gerado com sucesso.")
    return numero

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente:\n")

    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return

    conta_cliente = recuperar_conta(cliente)

    if not conta_cliente:
        print("Cliente não possui contas.")
        return

    print("\n================ EXTRATO ================")
    transacoes = conta_cliente.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['data']}\n{transacao['tipo']}:R$ {transacao['valor']:.2f}\n"

    print(extrato)
    print(f"\nSaldo:R$ {conta_cliente.saldo:.2f}")
    print("==========================================")

def depositar(clientes):
    cpf = input("Informe o CPF do cliente:\n")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)


def menu():
    print("******menu******\n"
    "[1] - deposito\n"
    "[2] - saque\n"
    "[3] - extrato\n"
    "[4] - cadastrar usuario\n"
    "[5] - criar conta-corrente\n"
    "[6] - listar contas\n"
    "[7] - sair\n"
    "****************")


def main():
    clientes = []
    contas = []

    while True:

        menu()
        opcao = input("Escolha uma opcao:\n")

        if opcao == '1':
            depositar(clientes)

        elif opcao == '2':
            sacar(clientes)

        elif opcao == '3':
            exibir_extrato(clientes)

        elif opcao == '4':
            cadastrar_cliente(clientes)

        elif opcao == '5':
            cpf_cliente = input("Digite o CPF do cliente para criar a conta: ")
            cliente = next((c for c in clientes if c.cpf == cpf_cliente), None)

            if cliente is None:
                print("Cliente não encontrado.")
                continue

            gerar_numero = gerar_conta()
            conta = ContaCorrente(cliente, gerar_numero)
            cliente.adicionar_conta(conta)
            contas.append(conta)

        elif opcao == '6':
            print("Lista de contas\n")
            for conta in contas:
                print(f"Cliente: {conta.cliente}, Número conta-corrente: {conta.numero}, Saldo: R${conta.saldo :.2f}")

        elif opcao == '7':
            print("Saindo do sistema...")
            break

        else:
            print("opção invalida tente novamente.")

if __name__ == '__main__':
 main()