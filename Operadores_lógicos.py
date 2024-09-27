print("Hello World")

#Utilizado em conjunto com os operadores de comparação

#Operador "e" = "and" para ser True, tudo tem que ser True
#Operador "ou" = "or" para ser True, apenas um tem que ser True

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque and saque <= limite)
print(saldo >= saque or saque <= limite)
print("------------------------")

#Operador Negação 

contatos_emergencia = []

not 1000 > 1500

not contatos_emergencia

not "saque 1500;"

not ""

#Operador Parênteses

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)