##################################
##### LISTA GERAL DE MÉTODOS #####
##################################

# Abaixo veremos em formato de lista todos os atuais métodos e funções integradas
# do Python dividídos em tipos de dados para os quais usamos

1. Inteiros (int)
Principais métodos e funções relacionadas a manipulação de inteiros.

Mais usados → Menos usados
int()                   # conversão para inteiro
abs()                   # valor absoluto
pow()                   # ou ** exponenciação
divmod()                # retorna quociente e resto
bit_length()            # número de bits necessários para representar o inteiro
to_bytes()              # conversão para bytes
from_bytes()            # (usado em nível baixo) conversão de bytes para inteiro

2. Números de ponto flutuante (float)
Métodos/funções para manipulação de floats.

Mais usados → Menos usados
float()                 # conversão para float
round()                 # arredondamento (com ou sem casas decimais)
abs()                   # valor absoluto
math.floor()            # arredondar para baixo (precisa importar math)
math.ceil()             # arredondar para cima (precisa importar math)
math.trunc()            # truncar parte decimal
is_integer()            # verificar se o valor é inteiro
as_integer_ratio()      # fração equivalente

3. Strings (str)
Aqui estão os métodos mais utilizados na prática para manipulação de textos.

Mais usados → Menos usados
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

4. Booleanos (bool)
Métodos diretos não são comuns, mas operações e funções sim.

Mais usados → Menos usados
bool()                  # conversão para booleano
Operadores and, or, not lógica booleana
any()                   # retorna True se algum elemento for verdadeiro
all()                   # retorna True se todos os elementos forem verdadeiros

Comparações (==, !=, <, >, <=, >=)
isinstance()                    # verificar tipo de dado

5. Listas (list)
Manipulação de listas é extremamente frequente.

Mais usados → Menos usados
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
min()                   # / max()               # menor/maior elemento
sum()                   # soma elementos numéricos

6. Tuplas (tuple)
Tuplas são imutáveis, então métodos de alteração não existem.

Mais usados → Menos usados
len()                   # tamanho da tupla
tuple()                 # conversão para tupla
.count()                # contar ocorrências
.index()                # encontrar posição
min()                   # menor elemento 
max()                   # maior elemento

7. Dicionários (dict)
Estrutura chave-valor muito usada.

Mais usados → Menos usados
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