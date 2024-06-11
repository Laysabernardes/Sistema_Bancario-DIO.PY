from datetime import datetime

menu = """
Entre com a operação desejada:

    [0] - Extrato
    [1] - Depósito
    [2] - Saque
    [3] - Sair  

"""
saldo = 0
LIMITE = 500
LIMITE_SAQUE = 3
extrato = []
contador= 0
contador_saque = 0

while True:

    opcao = int(input(menu))

    if opcao == 0:
        print("\nExtrato:")
        if len(extrato) == 0: #len() para verificar o comprimento da lista. Se o comprimento for igual a zero, significa que a lista está vazia.
            print("""
    Não foram realizadas movimentações.
                  """)
        else:
            for operacao in extrato:
                data_formatada = operacao['data'].strftime("%d/%m/%Y    %H:%M:%S")  # Formata a data e hora
                valor_formatado = "{:.2f}".format(operacao['valor'])  #     Formata o valor
                saldo_formatado = "{:.2f}".format(operacao['Saldo   Atualizao'])  # Formata o saldo atualizado
                print(f"""
    Atividade: {operacao['Atividade']} 
    Data: {data_formatada} 
    Tipo: {operacao['tipo']} 
    Valor: R$  {valor_formatado}
    Saldo Atualizado: R$ {saldo_formatado}""")

    elif opcao == 1:
        print("\nOpção selecionada - [1] Depósito")
        valor = float(input("Valor a ser depositado: "))
        if valor > 0:
            contador += 1
            saldo += valor
            operacao = {
                "Atividade": contador,
                "data": datetime.now(),
                "tipo": "Depósito",
                "valor": valor,
                "Saldo Atualizao": saldo,
            }
            extrato.append(operacao)
            print("Operação realizada com sucesso\n")
        else:
            print("Valor incorreto! Tente novamente\n")

    elif opcao == 2:
        print("Opção selecionada - [2] Saque")

        if contador_saque >= LIMITE_SAQUE:
            print("Operação não realizada pois o limite de saques permitidos foi excedido.")
            continue

        valor = float(input("Valor a ser sacado: "))
        
        if valor > LIMITE:
            print("Operação não realizada pois o valor inserido é maior que o limite permitido.")
        
        elif valor > saldo:
            print("Operação não realizada devido ao saldo insuficiente.")
        else:
            contador_saque += 1
            saldo -= valor
            operacao = {
                "Atividade": contador_saque,
                "data": datetime.now(),
                "tipo": "Saque",
                "valor": valor,
                "Saldo Atualizao": saldo,
            }
            extrato.append(operacao)
            print("Operação realizada com sucesso\n")

    elif opcao == 3:
        break

    else:
        print("Opção inválida! Tente novamente\n")

    continuar = input("Deseja realizar outra operação? (s/n): ")
    while continuar.lower() not in ['s', 'n']:
        print("Resposta inválida! Por favor, digite 's' para sim ou 'n' para não.")
        continuar = input("Deseja realizar outra operação? (s/n): ")

    if continuar.lower() == 'n':
        break
