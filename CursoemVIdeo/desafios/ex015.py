#calcule o preco a pagar, sabendo que o carro custa R$ 60 por dia e R$0.,15 por km rodado
dias = int(input('Quantos dias alugados ? '))
km = float(input('Quantos km rodados ? '))
total = 60 * dias + 0.15 * km
print(f'O total a pagar é de R${total}')

