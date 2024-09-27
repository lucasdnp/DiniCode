print("Hello World")

nome = "Lucas"
idade = 26
profissao = "A definir"
linguagem = "python"

dados = {"nome": "Lucas", "idade": 26, "profissao": "A definir", "linguagem": "python"}

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.".format(**dados))

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.")
      

print("-----------------------------------")

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")