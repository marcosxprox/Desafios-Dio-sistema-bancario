def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    # TODO: Itere sobre cada transação na lista:
    for valor in transacoes:
        # TODO: Verifique se o valor absoluto da transação é maior que o limite:
        if abs(valor) > limite:
            # TODO: Adicione a transação à lista filtrada:
            transacoes_filtradas.append(valor)

    # Retorna a lista de transações filtradas
    return transacoes_filtradas


entrada = input("[100,-50, 300,-150],100")

entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "")
limite = float(limite.strip())  # Converte o limite para float

transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# TODO: Filtre as transações que ultrapassam o limite:
resultado = filtrar_transacoes(transacoes, limite)

print(f"\nTransações: {resultado}")