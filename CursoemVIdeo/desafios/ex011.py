# Leia a largura e altura - calcule area m²
# e a tinta necessria para pintá-la, sabendo que 1l de tinta  pinta 2m²
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print(f'DImensao de {larg} x {alt} e sua área é de {area}m²')
print(f'Para pintar essa parede, você precisará de {area/2}l de tinta')
