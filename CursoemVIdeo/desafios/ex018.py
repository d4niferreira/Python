#Leia um angulo qlqr e calcule o seno, cosseno e tangente desse angulo
from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))


sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print(f'O ângulo de {angulo} tem o seno de {sen:.2f}')
print(f'O ângulo de {angulo} tem o cosseno de {cos:.2f}')
print(f'O ângulo de {angulo} tem a tangente de {tan:.2f}')

