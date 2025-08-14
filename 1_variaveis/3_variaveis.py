# Aqui vamos da inicio a algumas manipulações de dados básicas

#####################################
##### CONVERSÃO ENTRE NUMÉRICOS #####
#####################################

# Definindo dados
dado1 = 3.8
dado2 = 10
# Definindo dados #

print(int(dado1))
print(float(dado2))
print(complex(dado1))
print(complex(dado2))

# Rodando o código veremos que:

# 3.8 passa a ser 3 (a parte decimal é descartada e agora ele vale 3 inteiro)
# 10 passa a ser 10.0 (apesar de conter o mesmo valor geral, se tornou decimal)
# Tanto o 3.8 quanto 10, ao serem convertidos para numéricos complexos, mantém
# seu valor para o "eixo x" e obtém 0j para o "eixo y", por ser inexistente


##################################
##### MANIPULAÇÃO DE STRINGS #####
##################################

# Definindo dados #
nome = "Gean"
sobrenome = "Albuquerque"
# Definindo dados #


################
# Concatenação #
################
apresentacao = "Olá, meu nome é " + nome + " " + sobrenome + "."
print(apresentacao)

# Aqui combinamos 3 strings explícitas e duas variáveis que armazenam strings
# "texto" + var + "texto" + var + "texto"
# No fim obtemos um único texto, uma única string, armazenada em apresentacao


##############
# Formatação #
##############
apresentacao = f"Olá, meu nome é {nome} {sobrenome}"
print(apresentacao)

# Essa é outra maneira de "concatenarmos" strings, utilizando o "f" como sintaxe
# do python "colado na nossa string dinâmica" e aí temos justamente isso, uma 
# string formatada de maneira mais dinâmica


###################
# Fatiamento Fixo #
###################

# Uma coisa importante de saber em relação as strings em python é que todas elas
# são também uma lista de caracteres ordenados. Ou seja, cada caractere é atribuído
# à um índice de acordo com a sua posição na string, veja abaixo a invocação de
# determinados caracteres através de seu índice

email = "joaofeijao@gmail.com"

print(f"indice 0: {email[0]}")          # Retornará "j"
print(f"indice 10: {email[10]}")        # Retornará "@"
print(f"indice 0: {email[-1]}")         # Contado inversamente, sendo "-1" o último caractere. Retornará "m"
print(f"indice 10: {email[-3]}")        # Contado inversamente, sendo "-3" o antepenultimo caractere. Retornará "c"


############################
# Fatiamento Por Intervalo #
############################

# Funciana de maneira similar ao fatiamento fixo, a diferença é que ao invés de um
# passamos dois índices, e obteremos todos os caracteres "entre os indíces -1"
# Isso quer dizer que apesar do valor do primeiro índice ser incluído no valor final,
# o valor do último índice, não será. Veja abaixo:

print(f"indices de 0 a 10: {email[0:10]}")
print(f"indices de 0 a 10: {email[10:20]}")

# Veja só, apesar de termos visto que o valor armazenado no índice 10 é "@"
# O primeiro retorno é "joaofeijao" e não "joaofeijao@"

# Já o segundo retorno, que também usa o índice 10, mas no começo, inclui
# agora o "@", além disso, nosso último índice ocupado é o 19, mas como
# quero incluir seu valor no resultado final, utilizo para a segunda posição
# um índice acima dele.