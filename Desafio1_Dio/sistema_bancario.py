
def deposito(saldo, extrato_operacoes):
    valor_entrada = float(input("Digite o valor que deseja depositar R$:"))
    saldo += valor_entrada
    extrato_operacoes.append(f'Deposito - R${valor_entrada:.2f}')
    print(f'Saldo atualizado - R${saldo:.2f}')
    return saldo


def saque(saldo, saida, contador, extrato_operacoes):

    if saldo < saida:
        print("Não será possível realizar o saque. Saldo insuficiente.")
    elif contador < 3:
         saldo -= saida
         extrato_operacoes.append(f"Saque - R${saida:.2f}")
         print (f"Saldo atual - R${saldo:.2f}")
         print(f"Você ainda pode realizar {3 - contador} saque(s) hoje.")
         return saldo
    else:
        print("Limite de saques diario foi excedido.")
        return saldo


def menu():
   print("******menu******\n"
         "1 - deposito\n"
         "2 - saque\n"
         "3 - extrato\n"
         "4 - sair\n"
         "****************")

def main():
    saldo = 0
    contador = 0
    extrato_operacoes = []

    while True:

        menu()
        opcao = input("Escolha uma opcao:\n")

        if opcao == '1':
            saldo = deposito(saldo, extrato_operacoes)

        elif opcao == '2':
            saida = float(input("Digite o valor que deseja sacar:"))
            if saida > 500:
                print("O valor do saque ultrapassa o limite de R$500.00 reais.")
            else:
                saldo = saque(saldo, saida, contador, extrato_operacoes)
                contador +=1

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
            print("Saindo do sistema...")
            break

        else:
            print("opção invalida tente novamente")

if __name__ == '__main__':
    main()
















