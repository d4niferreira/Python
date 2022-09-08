# Leia o salário e mostro o novo salário com 15% de aumento
salario = float(input(f'Qual é o salário do funcionário? R$'))
salario += salario * 0.15
print(f'Com aumento de 15% o novo salário do funcionário é R${salario:.2f}')