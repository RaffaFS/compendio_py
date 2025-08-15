# Já tivemos nosso primeiro contato com listas enquanto estudávamos strings
# Lá descobrimos que toda string pode ser manipulada também como uma lista
# de caracteres ordenados, cada um com um índice próprio

#########################
##### LISTAS (LIST) #####
#########################

# Uma lista é uma sequência mutável e ordenada de valores
# list está para Python como array está para Javascript
# Pode armazenar dados de tipos iguais ou diferentes

usuarios = ['Jonas', 'Sabrina', 'Henrique']
print(usuarios)

maior_de_idade = 2 > 1
usuario1 = ['Jonas', 28, maior_de_idade]
print(usuario1)

# Temos vários métodos para trabalhar com as listas, mas vejamos antes o básico

# Concatenação: juntamos todos os elementos de duas listas em uma única
print(usuarios + usuario1)

# Fatiamento: assim como nas strings, podemos fazer aqui também
print(usuarios[0:2])

# Conversão para string para utilização genérica
print(f'O primeiro da lista é: {str(usuarios[0])}')

# Conversão de string para lista
usuarioo = list(usuarios[1])
print(usuarioo)

# Alteração de valor específico
usuarios[2] = "Tiburcio"
print(usuarios)