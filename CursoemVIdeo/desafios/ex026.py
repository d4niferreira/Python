frase = input('Digite uma frase: ').strip().upper()
letra = input('QUal letra deseja procurar? ').strip().upper()
print(f'A letra {letra} aparece {frase.count(letra)} vezes na frase.')
print(f'A primeira letra {letra} apareceu na posição {frase.find(letra)+1}')
print(f'A última letra {letra} apareceu na posição {frase.rfind(letra)+1}')

