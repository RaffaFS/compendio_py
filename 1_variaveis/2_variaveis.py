#################
### (complex) ### tipo numérico complexo
#################
ponto = 2 + 4j
print(ponto)
print(type(ponto))
print("//////////////////////////////////////////////////")

# "Todo número complexo é um ponto em um plano cartesiano"

# Os números complexos são utilizados mais em engenharia mesmo fora da programação, mas dentro dela,
# além da engenharia, também são utilizados em gráficos de imagens, frequências e filtros de áudios,
# jogos e simulações e matemática avançada.

# Um número complexo é dividido em duas partes: "real" e "imaginária"
# Tomando o exemplo do plano cartesiano, a primeira parte representa o "eixo X" enquanto a segunda
# parte (que sempre acompanha a letra "j") representa o "eixo Y" 

###############
### (tuple) ### tipo lista
###############
coordenadas = (10, 20)
print(coordenadas)
print(type(coordenadas))
print("//////////////////////////////////////////////////")

# podemos criar uma tupla com apenas um valor, mas a virgula é obrigatório para não ser outro tipo mais comum
# podemos criar tuplas sem os parenteses na declaração de valor, mas o mais correto é usá-los
# podemos assim como em arrays, invocar um único valor da tupla utilizando seu índice

# é importante sabermos também diferenciar tuple, list e array
# os dois primeiros são nativos de python enquanto o terceiro não, mas pode ser importado

# Entre list e tuple a diferença é similar ao que vemos em JS com let e const
# Ambas são estruturas ordenadas de uma coleção de dados, ambas podem serem redefinidas por inteiro
# Porém list pode ser manipulada e ter seus valores alterados separadamente
# Enquanto tuple é fixa, não pode ter valores alterados e aceita menos métodos por isso

# Em relação a arrays poderiamos fazer um import array, mas ao invés disso é mais interessante
# trabalharmos com import numpy, mas isso veremos em outro documento na pasta bibliotecas. Em resumo, 
# esse método consome menos memória e tem uma sintaxe mais resumida que list

coordenadas = 20,
print(coordenadas)
print(type(coordenadas))
print("//////////////////////////////////////////////////")

coordenadas = 10, 40
print(coordenadas)
print(coordenadas[1])
print(type(coordenadas))
print("//////////////////////////////////////////////////")