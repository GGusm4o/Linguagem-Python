# Exibe um desconto de 5% em um produto

preco = float(input('Digite o preço do produto: R$ '))
novo = preco - (preco * 5 / 100)
print('O valor do produto R${:.2f} com desconto é: R$ {:.2f}' .format(preco, novo))