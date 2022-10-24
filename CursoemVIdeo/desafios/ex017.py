#leia o valor de co e ca e calculea a hipotenusa

import math

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
#hipotenusa = math.sqrt(math.pow(ca,2) + math.pow(co,2))
hipotenusa = math.hypot(co,ca)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')