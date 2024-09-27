print("Hello World!")
#Utilizando apenas IF
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")

print("------------------------------")
#Utilizando IF e ELSE
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

else:
    print("Saldo insuficiente!")

print("------------------------------")
#Utilizando ELIF
opção = int(input("Informe uma opção:\n[1] sacar \n[2] Extrato: "))

if opção == 1:
    valor = float(input("Informe a quantia para o saque: "))
    # ...
elif opção == 2:
    print("Exibindo o extrato ...")

else:
    sys.exit("Opção inválida")

print("------------------------------")

