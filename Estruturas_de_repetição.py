texto = input("informe um texto: ")
vogais = "AEIOU"

# Exemplo utilizando interável
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end=", ")
else:
    print() #Adiciona quebra de linha
    print("executa no final do laço")

print("------------------------------------------------------------")

# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")

print("------------------------------------------------------------")


opcao = -1
