print("Hello World")

conta_normal = 5000
saldo = conta_normal
cheque_especial = 10000
conta_universitaria = 3000
saldo2 = conta_universitaria
opção = -1
while opção != 0:
    opção = input("Informe uma opção:\n[1] Conta universitária \n[2] Conta normal \n[0] Sair \nSelecione a opção: ")
    saque = int(input("Digite o valor de saque: "))
    if opção == 1:
        if saldo >= saque:
            print("Saque realizado com sucesso!")
        elif saque <= (saldo + cheque_especial):
            print("Saque realizado com uso do cheque especial")
        else:
            print("Saldo insuficiente.")
    elif opção == 2:
    
        if saldo2 >= saque:
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente.")
else:
    print("Obrigado por utilizar nosso sistema")


