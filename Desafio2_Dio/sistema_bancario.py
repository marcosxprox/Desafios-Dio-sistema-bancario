from datetime import datetime

# Validação simples do CPF
def validar_cpf(numero_cpf):
    return len(numero_cpf) == 11 and numero_cpf.isdigit()

def cadastrar_usuario(usuarios):
    cpf = {}
    nome = input("Digite o nome do usuario:")
    data_nascimento = input("Digite a data de nascimento do usuario:")
    numero_cpf = input("Digite o cpf do usuario:")

    while not validar_cpf(numero_cpf):
        print("CPF inválido. Certifique-se de que contém 11 dígitos.")
        numero_cpf = input("Digite o cpf do usuario:")

    for usuario in usuarios:
        if numero_cpf in usuario:
            print(f"Erro: O CPF {numero_cpf} já está cadastrado.")
            return  # Finaliza a função sem cadastrar um novo usuário

    endereco = input("Digite o endereço do usuario:")
    cpf[numero_cpf] = {'nome':nome, 'data_nascimento':data_nascimento, 'endereco':endereco}
    usuarios.append(cpf)


def criar_conta_corrente(usuarios, contador_contas, contas, agencia):
    cpf_usuario = input("Digite o CPF para qual se deseja criar uma conta_corrente: ")
    usuario_encontrado = None  # Inicializar variável para armazenar o usuário encontrado

    # Procurando pelo usuário
    for usuario in usuarios:
        if cpf_usuario in usuario:
            usuario_encontrado = usuario
            break

    # Caso o usuário seja encontrado
    if usuario_encontrado:
        print(f"Usuário portador do CPF: {cpf_usuario} encontrado com sucesso.")
        contador_contas += 1
        conta_corrente = f'{contador_contas} - {agencia}'

        # Identificando um índice disponível para a conta-corrente
        contador = 1
        while f'conta_corrente {contador}' in usuario_encontrado[cpf_usuario]:
            contador += 1

        # Adicionando nova conta-corrente
        usuario_encontrado[cpf_usuario][f'conta_corrente {contador}'] = conta_corrente
        contas.append(conta_corrente)
        print(f"Conta_corrente criada com sucesso: {conta_corrente}")
        return contador_contas

    else:
        print(f"Usuário portador do CPF: {cpf_usuario} não encontrado.")


def deposito(saldo, extrato_operacoes):
    date = datetime.now()
    date_br = date.strftime('%d/%m/%Y %H:%M:%S')
    valor_entrada = float(input("Digite o valor que deseja depositar R$:"))
    saldo += valor_entrada
    extrato_operacoes.append(f'Deposito - R${valor_entrada:.2f} {date_br}')
    print(f'Saldo atualizado - R${saldo:.2f}')
    return saldo

def saque(*, saldo, saida, contador, extrato_operacoes):
    date = datetime.now()
    date_br = date.strftime('%d/%m/%Y %H:%M:%S')
    if saldo < saida:
        print("Não será possível realizar o saque. Saldo insuficiente.")
    elif contador < 3:
         saldo -= saida
         extrato_operacoes.append(f"Saque - R${saida:.2f} {date_br}")
         print (f"Saldo atual - R${saldo:.2f}")
         print(f"Você ainda pode realizar {2 - contador} saque(s) hoje.")
         return saldo
    else:
        print("Limite de saques diario foi excedido.")
        return saldo

def listar_contas(usuarios, agencia):
    cpf_usuario = input("Digite o cpf do usuario:")
    usuario_encontrado = None

    for usuario in usuarios:
        if cpf_usuario in usuario:
            usuario_encontrado = usuario
            break

    print(usuario_encontrado)

    if usuario_encontrado:
        print(f"Contas do usuario com CPF {cpf_usuario}:")
        for chave, valor in usuario_encontrado[cpf_usuario].items():
            if 'conta_corrente' in chave:
                print(f'''************\n
                Agencia:{agencia}\n
                Conta:{valor[0]}\n
                Titular:{usuario_encontrado[cpf_usuario]['nome']}\n
                ************''')
    else:
        print(f"Usuário com CPF {cpf_usuario} não encontrado.")

def log_transacoes(extrato_operacoes, ultima_data):
    data_atual = datetime.now().strftime('%d/%m/%Y')
    if ultima_data != data_atual:
        extrato_operacoes.clear()
        ultima_data = data_atual
    return len(extrato_operacoes), ultima_data


def menu():
    date = datetime.now()
    date_br = date.strftime('%d/%m/%Y %H:%M:%S')
    print("******menu******\n"
          "[1] - deposito\n"
          "[2] - saque\n"
          "[3] - extrato\n"
          "[4] - cadastrar usuario\n"
          "[5] - criar conta-corrente\n"
          "[6] - listar contas\n"
          "[7] - sair\n"
          f"{date_br}\n"
          "****************")

def main():
    agencia = '0001'
    saldo = 0
    contador = 0
    contador_contas = 0
    extrato_operacoes = []
    usuarios = []
    contas = []
    ultima_data = datetime.now().strftime('%d/%m/%Y')  # Inicializa a data com o dia atual

    while True:

        menu()
        opcao = input("Escolha uma opcao:\n")

        if opcao == '1':
            limite_operacoes, ultima_data = log_transacoes(extrato_operacoes, ultima_data)
            if limite_operacoes == 10:
                print("Você excedeu o número de transações diaria. Tente novamente mais tarde")
            else:
                saldo = deposito(saldo, extrato_operacoes)


        elif opcao == '2':
            limite_operacoes, ultima_data = log_transacoes(extrato_operacoes, ultima_data)
            if limite_operacoes == 10:
                print("Você excedeu o número de transações diaria. Tente novamente mais tarde")
            else:
                saida = float(input("Digite o valor que deseja sacar:"))
                if saida > 500:
                    print("O valor do saque ultrapassa o limite de R$500.00 reais.")
                else:
                    saldo = saque(saldo=saldo, saida=saida, contador=contador, extrato_operacoes=extrato_operacoes)
                    contador += 1


        elif opcao == '3':
            if not extrato_operacoes:
                print("Nenhuma operação foi realizada até o momento.")
            else:
                print("******Extrato******")
                for extrato in extrato_operacoes:
                    print(extrato)
                print(f"Saldo - R${saldo:.2f}\n"
                     f"*******************")

        elif opcao == '4':
             cadastrar_usuario(usuarios)
             print(usuarios)

        elif opcao == '5':
         contador_contas = criar_conta_corrente(usuarios, contador_contas, contas, agencia)


        elif opcao == '6':
            listar_contas(usuarios, agencia)

        elif opcao == '7':
            print("Saindo do sistema...")
            break

        else:
            print("opção invalida tente novamente")

if __name__ == '__main__':
    main()