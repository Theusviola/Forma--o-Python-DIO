menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair ->

"""
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("Depósito")
        valor = float(input("Por favor, digite o valor que deseja depositar:"))
    
        if valor > 0:
            saldo += valor
            extrato += f"Você depositou R$ {valor} reais.\n"
        else:
            print("Valor inválido!") 


    elif opcao == 2:
        print("Saque")
        valor = float(input("Por favor, digite o valor que você gostaria de sacar:"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("Operação falhou! O valor de saque excede o limite por transação.")
        elif excedeu_saques:
            print("Número máximo de saques diário excedido.")
        else:
            saldo -= valor
            extrato += f"Você sacou R$ {valor} reais.\n"
            numero_saques += 1

    elif opcao == 3:
        print("Extrato")
        print("########## EXTRATO ##########")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Seu saldo atual é: {saldo}")
        print("#############################")


    elif opcao == 0:
        print("Muito obrigado por usar o nosso banco. Volte sempre!")
        break
    else:
        print("Opção inváida! Por favor, tente novamente e selecione uma opção válida.")

