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

# Algo interessante de citar é que podemos ter listas dentro de listas então
# a chamada de seus dados tem uma estrutura um pouco diferente

pessoas = [['Ana', 29], ['Bento', 31], ['Enzo', 22]]
print(pessoas[2][1])

# O resultado do print acima será 22, pois digo para ir em pessoas, buscar o 
# índice 2 que é a terceira lista e então dentro dessa lista buscar o índice
# 1 que é o segundo valor

# Nessa mesma estrutura poderíamos, por exemplo, ter uma lista, dentro de uma
# lista, dentro de uma lista, dentro de uma lista (e assim por diante)

# A chamada de um dado único na camada mais interna seria algo como
# lista[i][i][i][i] (e assim por diante)