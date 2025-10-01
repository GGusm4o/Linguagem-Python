from classes.Cliente import Cliente
from classes.Conta import Conta
from classes.ContaRemuneradaPoupanca import ContaRemuneradaPoupanca

# Testando o código
cliente1 = Cliente("123", "João", "Rua X")
cliente2 = Cliente("321", "Maria", "Rua Y")
cliente3 = Cliente("333", "Zeze", "Rua Z")

conta1 = Conta(cliente1 ,111, 2000)
conta2 = Conta(cliente1 ,222, 2000)
conta3 = ContaRemuneradaPoupanca(cliente3 ,333, 2000, 0.1)

conta2.depositar(800)

conta2.gerar_saldo()

conta3.remuneracaoConta()
conta3.gerar_saldo()


