# Agora que já entendemos o funcionamento e a anatomia da estrutura for in
# vejamos alguns exemplos de uso mais complexos

# Se ele pode iterar sobre listas, então também pode sobre strings:
total = 0
frase = "A Alana foi no mercado comprar banana"
for letra in frase:
    if letra == 'A' or letra == 'a':
        total += 1

print(f'O total de letras "a" na frase é {total}')

# Acima então definimos uma variável total e uma frase
# No laço eu disse que para cada letra na frase (que é também uma lista de caracteres)
# Eu quero que seja verificado se o caractere é igual a "A" ou a "a" e se sim, quero
# que incremente "1" ao valor de total, assim no fim temos um algoritmo que conta quantos
# "as" temos na frase


# Além de listas também podemos iterar sobre dicionários, porém apenas com a ajuda de métodos
# Abaixo vou descrever nosso dicionário e criar um exemplo para cada método
dicio = dict(
    nome = 'Joao',
    idade = 28,
    pet = 'gato'
)

# Chaves
for chave in dicio.keys():
    print(f'A chave é {chave}')

# Valores
for valor in dicio.values():
    print(f'O valor é {valor}')

# Chaves e valores
for chave, valor in dicio.items():
    print(f'{chave} é igual a {valor}')