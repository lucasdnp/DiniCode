#Versão definitiva

# Definindo variáveis globais
saldo = 20000
limite_saque = 4000
extrato = []
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

# Função de depósito
def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: +R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")

# Função de saque
def sacar(valor):
    global saldo, numero_saques
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite_saque:
        print(f"O valor máximo de saque é R${limite_saque:.2f}.")
    elif numero_saques >= LIMITE_SAQUES_DIARIOS:
        print("Limite de saques diários atingido.")
    else:
        saldo -= valor
        numero_saques += 1
        extrato.append(f"Saque: -R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso!")

# Função de extrato
def exibir_extrato():
    print("\nEXTRATO BANCÁRIO")
    if extrato:
        for operacao in extrato:
            print(operacao)
    else:
        print("Nenhuma operação realizada.")
    print(f"\nSaldo atual: R${saldo:.2f}\n")

# Função principal para interagir com o sistema
def sistema_bancario():
    while True:
        print("\n--- Sistema Bancário ---")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Exibir Extrato")
        print("4 - Sair")
        opcao = input("Escolha uma operação: ")

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            depositar(valor)
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            sacar(valor)
        elif opcao == "3":
            exibir_extrato()
        elif opcao == "4":
            print("Saindo do sistema. Obrigado por usar nosso banco!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executando o sistema bancário
sistema_bancario()
