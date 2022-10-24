#Leia um número real e mostre sua porcao real
#usar math >>> 6.15 tem a parte inteira 6
'''from math import trunc

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))'''

num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e sua porção inteira é {int(num)}')

