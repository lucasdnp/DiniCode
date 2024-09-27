print("Hello World")

#Verifica se ele é ou não é

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

teste = curso is nome_curso
print(teste)
teste_2 = curso is not nome_curso
print(teste_2)
teste_3 = saldo is limite
print(teste_2)

print("----------------")

saldo = 1000
limite = 2000

print(saldo is limite)
print(saldo is not limite)
