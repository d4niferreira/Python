# Leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input('Qual o valor do produto ? R$'))
np = preco - (preco*0.05)
print(f'Com 5% de desconto o produto tem o novo valor de R${np} ')