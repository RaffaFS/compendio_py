# Um método é basicamente uma função intrínsica da linguagem utilizada
# para fazer uma manipulação mais precisa de um tipo de dado.
# Lembre, falando de Strings, maiúscula e minúscula tem diferença!

# Aqui veremos sobre métodos apenas o suficiente para nos familiarizarmos
# nos arquivos a seguir teremos listas de métodos explicados com exemplos

#############################
##### MÉTODOS DE STRING #####
#############################

endereco = "Avenida Paulista, 1811, São Paulo, São Paulo, Brasil"

##### Upper #####
# Torna maiúsculas todas as letras da string
# Útil para padronizar os dados, criando literalmente um padrão e também
# auxiliando na manipulação geral dos mesmos

print(endereco.upper())


##### Find #####
# Retorna a posição do caractere solicitado, caso exista, se não, retorna "-1"
# Se buscarmos por um conjunto específico de caracteres, uma palavra, por exemplo
# retorna o índice do primeiro caractere desse conjunto ou, da primeira letra
# dessa palavra.
# Útil para localizar conjuntos de caracteres gerais como palavras ou trechos de 
# texto dentro de grandes corpos de texto sem precisar ficar contando caracteres

print(endereco.find("futebol"))
print(endereco.find("Brasil"))

##### Replace #####
# Encontra na string o primeiro argumento passado (caractere ou conjunto dos mesmos),
# e substitui pelo segundo argumento passado. Caso o primeiro argumento passado não
# exista na string, ela apenas permanece a mesma.
# Útil para padronizar dados similares e alterar partes específicas de uma string.

print(endereco.replace("Avenida", "Av."))
print(endereco.replace("avenida", "Av."))

##### Str, Int e Float #####
# Métodos de conversão de inteiros para string e vice versa

### Str ###
# O dado abaixo é tipo inteito e vamos transformá-lo em tipo string
dado1 = 45

print(str(dado1))
print(type(str(dado1)))

### Int ###
# Para esse exemplo vamos usar a variável "endereco" que já estavamos usando acima
# mas como ela não é composta apenas de caracteres numéricos, ponto e vírgula, temos
# que primeiro captar a parte numérica da string com o "fatiamento/slice"

numero_casa = endereco[18:22]

# Agora sim utilizamos essa nova variável para transformarmos a fatia obtida em inteiro

print(int(numero_casa))
print(type(int(numero_casa)))

### Float ###
# Bem similar às características da conversão str -> int, as únicas diferenças são que
# o float nos retornará um ".0" por ser decimal e, além disso, ele reconhece "." como
# um caractere válido na string para conversão para decimal

print(int(numero_casa))
print(type(int(numero_casa)))

dado2 = "783.8290"

print(float(dado2))
print(type(float(dado2)))