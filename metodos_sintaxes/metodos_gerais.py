

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
abs()                   # valor absoluto (retorna sempre um número positivo ou zero) >>> abs(0) é 0, abs(3.2) é 3.2, abs(-4) é 4
pow()                   # alternativa a "**" >>> pow(base, expoente) ou pow(base, expoente, módulo)
divmod()                # alternativa a "//" e "%", divide e retorna quociente e resto de uma vez só >>> divmod(10, 3) é (3, 1)
bit_length()            # número de bits necessários para representar o inteiro em binário >>> (casos específicos)
to_bytes()              # conversão para bytes (casos específicos)
from_bytes()            # conversão de bytes para inteiro (usado em nível baixo)

########################
### Decimais (float) ###
########################

float()                 # conversão para float
round()                 # arredondamento, round(valor, digitos pós ponto) >>> round(4.5) é 4, round(4.6) é 5, round(3.14159, 2) é 3.14
abs()                   # valor absoluto (retorna sempre um número positivo ou zero) >>> abs(0) é 0, abs(3.2) é 3.2, abs(-4) é 4
math.floor()            # (precisa importar math no arquivo) arredonda sempre para um valor absoluto para baixo >>> math.floor(4.761) é 4
math.ceil()             # (precisa importar math no arquivo) arredonda sempre para um valor absoluto para cima >>> math.floor(6.161) é 7
math.trunc()            # similar a round, mas esse apenas ignora a parte decimal do número e retorna a parte inteira
.is_integer()           # verificar se o valor é inteiro (mesmo sendo float) >>> (2.00).is_integer() é True, (2.44).is_integer() é False
as_integer_ratio()      # mostra a fração equivalente ao dado >>> 
                        # (1.5).as_integer_ratio() é (3, 2) porque 3/2 = 1.5
                        # (2.0).as_integer_ratio() é (2, 1) porque 2/1 = 2.0
                        # (0.5).as_integer_ratio() é (1, 2) porque 1/2 = 0.5
                        # (-0.5).as_integer_ratio() é (-1, 2) porque -1/2 = -0.5
                        # (0.1).as_integer_ratio() é (3602879701896397, 36028797018963968) porque 3602879701896397/36028797018963968 = 0.1

#####################
### Strings (str) ###
#####################

len()                   # retorna a quantidade de caracteres na string >>> len(dado)
str()                   # conversão para string >>> str(dado)
.lower()                # converte todos os caracteres para minúsculas >>> dado.lower()
.upper()                # converte todos os caracteres para maiúsculas >>> dado.upper()
.strip()                # remove espaços extras das extremidades >>> dado.strip()
.split()                # separa um dado em partes e atribui os resultados em lista/array/tuple >>> 
                        # dado.split() faz uma separação a cada espaço em branco na string
                        # dado.split("/") faz separações a cada "/" na string (/ pode ser qualquer outro caractere)
                        # dado.split(" ", 2) faz separações nos dois primeiros espaços em branco encontrados, então
                        # dado = "um dois tres quatro cinco" ficaria no retorno: ['um', 'dois', 'tres quatro cinco']

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