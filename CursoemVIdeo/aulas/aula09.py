frase = "Curso ciência da computação"
print(len(frase))
print(f'{frase[20:24]}')
print(frase[:7]) # da posição 0 até 7
print(frase[0::2]) # de dois em dois
print(f'quantos "C" tem? {frase.count("C")}') #case sensitive
print(f'quantos "c" tem em ciência?  {frase.count("c",6,13)}') #contagem com fatiamento
print(f'{frase.find("puta")}')# retorna inicio da palavra
print(frase.replace("Curso", "Bacharelado"))
print(frase.upper())
print(frase.lower())

frase2 = "  Aprendendo todo dia     "
print(frase2)
print(frase2.strip()) #remove espaços vazios do inicio e fim

