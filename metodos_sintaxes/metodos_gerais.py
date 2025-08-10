##################################################
##### LISTA GERAL DE SINTAXES DE MANIPULAÇÃO #####
##################################################

# Abaixo veremos em formato de lista todas as principais sintaxes de manipulação de
# dados simples sem a utilização de funções integradas ou métodos explicitamente

##############################
### Indexação e fatiamento ###
##############################

obj[i]                      # Acessa o elemento no índice i
obj[i:j]                    # Fatia do índice i até j (exclusivo)
obj[i:j:k]             	    # Fatia com passo k
obj[::-1]              	    # Inverte sequência
obj[i] = valor      	    # Modifica posição i
obj[i:j] = valores  	    # Substitui fati
del obj[i]             	    # Remove item no índice i
del obj[i:j]           	    # Remove fatia


########################
### Desenpacotamento ###
########################

grupo = [23, 21, 54, 46, 84]

a, b, c = grupo	                                    # Atribui cada valor no grupo a uma variável
a, _, b = grupo	                                    # Ignora valor com "_"
a, b, *resto = grupo	                            # Captura o restante da sequência
primeiro, *meio, ultimo = grupo	                    # Captura início, meio e fim
primeiro, *meio, penultimo, ultimo = grupo	        # Captura início, meio e fim


##################################
##### LISTA GERAL DE MÉTODOS #####
##################################

# Abaixo veremos em formato de lista todos os atuais métodos e funções integradas
# do Python dividídos em tipos de dados para os quais usamos

# de início vamos diferenciar métodos de funções integradas. 

# Métodos são aqueles que na sintaxe correta começam com "." e são utilizados na 
# sequência do dado, como: 
# "texto.upper()"                   # Deixa toda a string em caixa alta
# "texto.find('parâmetro')"         # Encontra na string o conjunto de caracteres passado

# Funções integradas são aquelas que vem antes do dado e carregam o mesmo dentro
# de (""), como: 
#"int(longitude)"                       # Transforma a string em inteiro

#####                                                                                   #####
##### Algo interessante de se saber é que uma função integrada pode ser utilizada junto #####
##### com um método, como em:                                                           #####
#####                                                                                   #####

# tamanho = len(texto.strip())          # .strip remove os espaços no início e final do texto
                                        # e len conta e passa o número total de caracteres agora sem espaços

#####                                           #####
##### Posso também utilizar métodos encadeados: #####
#####                                           #####

# texto = "   Olá Mundo!   "
# resultado = texto.strip().upper().replace("MUNDO", "Python")

# Nesse caso o primeiro a ser resolvido é o .strip, que tira os espaços do início e do fim do texto
# depois o .upper, que deixa tudo em maiúsculo e por fim o .replace, que troca a palavra "MUNDO"
# pela palavra "Python". 

#####                                         #####
##### Posso ainda utilizar funções aninhadas: #####
#####                                         #####

# tipo = type(int(numero_casa)))         # Transformo numero_casa em inteiro com int e depois peço o tipo dele com type

# É importante observar que aqui as coisas são resolvidas de quem está mais dentro de parênteses para fora, no geral,
# são resolvidas da direita para esquerda, diferente dos métodos encadeados que são resolvidos da esquerda para a direita

######################
### Inteiros (int) ###
######################

int()                   # conversão para inteiro
abs()                   # valor absoluto
pow()                   # ou ** exponenciação
divmod()                # retorna quociente e resto
bit_length()            # número de bits necessários para representar o inteiro
to_bytes()              # conversão para bytes
from_bytes()            # (usado em nível baixo) conversão de bytes para inteiro

########################
### Decimais (float) ###
########################

float()                 # conversão para float
round()                 # arredondamento (com ou sem casas decimais)
abs()                   # valor absoluto
math.floor()            # arredondar para baixo (precisa importar math)
math.ceil()             # arredondar para cima (precisa importar math)
math.trunc()            # truncar parte decimal
is_integer()            # verificar se o valor é inteiro
as_integer_ratio()      # fração equivalente

#####################
### Strings (str) ###
#####################

len()                   # tamanho da string
str()                   # conversão para string
.lower()                # minúsculas
.upper()                # maiúsculas
.strip()                # remove espaços extras das extremidades
.split()                # separa em lista
.replace()              # substitui partes
.find()                 # / .index()                # localiza substring
.join()                 # junta elementos de lista em string
.startswith()           # verifica prefixo
.endswith()             # verifica sufixo
.capitalize()           # primeira letra maiúscula
.title()                # primeira letra de cada palavra maiúscula
.count()                # conta ocorrências
.isalpha()              # verifica apenas letras
.isdigit()              # verifica apenas números
.isalnum()              # verifica letras e números
.swapcase()             # inverte maiúsculas/minúsculas
.center()               # centraliza string
.ljust()                # alinhamento esquerdo 
.rjust()                # alinhamento direito

########################
### Booleanos (bool) ###
########################

bool()                  # conversão para booleano
Operadores and, or, not lógica booleana
any()                   # retorna True se algum elemento for verdadeiro
all()                   # retorna True se todos os elementos forem verdadeiros

Comparações (==, !=, <, >, <=, >=)
isinstance()                    # verificar tipo de dado

#####################
### Listas (list) ###
#####################

len()                   # tamanho da lista
.append()               # adicionar elemento
.extend()               # adicionar vários elementos
.insert()               # inserir em posição específica
.remove()               # remover pelo valor
.pop()                  # remover por índice
.sort()                 # ordenar (altera a lista)
sorted()                # ordenar (retorna nova lista)
.reverse()              # inverter lista
.index()                # encontrar posição de um valor
.count()                # contar ocorrências
list()                  # conversão para lista
min()                   # menor elemento 
max()                   # maior elemento
sum()                   # soma elementos numéricos

######################
### Tuplas (tuple) ###
######################

len()                   # tamanho da tupla
tuple()                 # conversão para tupla
.count()                # contar ocorrências
.index()                # encontrar posição
min()                   # menor elemento 
max()                   # maior elemento

##########################
### Dicionários (dict) ###
##########################

.get()                  # obtém valor sem erro se não existir
.keys()                 # retorna chaves
.values()               # retorna valores
.items()                # retorna pares (chave, valor)
.update()               # atualiza/adiciona elementos
.pop()                  # remove chave
.popitem()              # remove último item
.clear()                # limpa dicionário
.setdefault()           # define valor se chave não existir
dict()                  # conversão para dicionário