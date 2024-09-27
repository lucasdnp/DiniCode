print("Hello World")

#def sacar(self, valor: float) #inicio do bloco do metodo
    #if self.saldo >= valor: #inicio do bloco if
        #self.saldo -= valor
        #fim do bloco do if
#fim do bloco do método

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Sucesso ao realizar o saque!")
        print("Retire o seu dinheiro na boca do caixa.")

    if saldo <= valor:
        print("Saldo insuficiente para o saque.")
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

sacar(600)



