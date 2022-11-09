nome = str(input("Qual seu nome completo? ")).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem um total de {len(nome)- nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")}')


