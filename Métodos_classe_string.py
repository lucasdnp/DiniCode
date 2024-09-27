print("Hello World")

curso = "pYtHon"
#Upper converte todos para maiusculo
print(curso.upper())

#Lower converte todos para minusculo
print(curso.lower())

#Title deixa a primeira letra maiuscula
print(curso.title())

print("--------------------------")

curso = "         Python   "
#remover todos os espaços
print(curso.strip() + ".")

#remover espaço da esquerda
print(curso.lstrip() + ".")

#remover espaço da direita
print(curso.rstrip() + ".")

print("--------------------------")

curso = "Python"
#adicionar e centralizar a quantidade de caracter até dar o numero de caracter que voce determinar, 
print(curso.center(10, "#"))

#juntar e adicionar o caracter que voce desejar na string
print(".".join(curso))

for letra in curso:
    print(letra, end=".")