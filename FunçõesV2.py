print("Hello World")

def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

print("=============================================")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)

print("=============================================")

op = somar

print(op(2,23))

print("=============================================")

salario = 2000

def salario_bonus(bonus, lista):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(4)
    print(f"lsita aux={lista_aux}")
    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista)

print(salario_com_bonus)
print(lista)
