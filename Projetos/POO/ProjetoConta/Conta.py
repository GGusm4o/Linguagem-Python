# Código da Classe

class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False    # Não tem saldo suficiente
        else:
            self.saldo -= valor
            return True     # Saque realizado com sucesso

    def gerar_extrato(self):
        print(f"Número: {self.numero}\nCPF: {self.cpf}\nNome: {self.nomeTitular}\nSaldo: R${self.saldo}")

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ("Transferencia Realizada")

# Código do exemplo
'''
c1 = Conta(1, 12344321, "Gusmão", 9000)
c1.depositar(500)

valor_saque = 300
resultado_saque = c1.sacar(valor_saque)

if resultado_saque:
    print(f"Saque de R${valor_saque} realizada com sucesso!")
else:
    print(f"Saldo insuficiente para realizar o saquue!")

c1.gerar_extrato()
'''
conta1 = Conta(123, 88888888, "Maria", 0)
conta2 = Conta(124, 99999999, "Pedro", 500)

print(conta2.transfereValor(conta1, 300))

conta1.gerar_extrato()
conta2.gerar_extrato()
