

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
.split()                # separa um dado em partes e atribui os resultados em uma list >>> 
                        # dado.split() faz uma separação a cada espaço em branco na string 
                        # dado.split("/") faz separações a cada "/" na string (/ pode ser qualquer outro caractere)
                        # dado.split(" ", 2) faz separações nos dois primeiros espaços em branco encontrados, então
                        # dado = "um dois tres quatro cinco" ficaria no retorno: ['um', 'dois', 'tres quatro cinco']

.replace()              # substitui partes >>> .replace("Velho, novo")
.find()                 # localiza substring e retorna o índice da primeira letra >>> .find("mundo")
.index()                # localiza substring e retorna o índice da primeira letra >>> .index("mundo")

                        # A diferença entre .find() e .index() está no erro, o primeiro retornará -1 e o segundo um erro literal

.join()                 # junta elementos de lista (que sejam do tipo string) em uma string única >>> "separador".join(lista) 
.startswith()           # verifica se a string começa com os caracteres passados >>> .startswith("Lu") 
.endswith()             # verifica se a string termina com os caracteres passados >>> .startswith("cas") 
.capitalize()           # coloca em maiúsculo a primeira letra da string e todas as outras minúsculas
.title()                # coloca em maiúsculo a primeira letra de cada palavra na string
.count()                # conta ocorrências passadas >>> frase.count("a") vai retornar quantos "as" há na frase
.isalpha()              # verifica se todos os caracteres da string são letras do alfabeto (sem espaços, números ou símbolos)
.isdigit()              # verifica se todos os caracteres da string são números de 0 a 9 (sem letras, ponto, vírgula ou sinais)
.isalnum()              # mistura dos dois acima, verifica se todos os caracteres da string são letras ou números
.swapcase()             # inverte maiúsculas/minúsculas
.center()               # centraliza string num espaço definido >>> se texto = Python
                        # texto.center(12) retorna '   Python   '
                        # isso se dá porque Python tem 6 letras e para 12 são mais 6 que dividido entre L e R são 3 espaços pra cada
                        # então texto.center(14, "-") retorna '----Python----'

.ljust()                # Segue o mesmo padrão de .center(), mas aqui a o espaço ou caractere passado é aplicado apenas a direita
.rjust()                # Segue o mesmo padrão de .center(), mas aqui a o espaço ou caractere passado é aplicado apenas a esquerda

########################
### Booleanos (bool) ###
########################

# Aqui temos apenas um básico sobre booleanos, veremos mais em um documento separado e dedicado a eles

bool()                  # conversão para booleano, tudo que existir será true e tudo que for vazio ou de valor 0 será falso
any()                   # retorna True se algum elemento for verdadeiro >>> any(condição)
all()                   # retorna True se todos os elementos forem verdadeiros >>> all(condição)
isinstance()            # verificar se o dado é do tipo desejado >>> isinstance(dado, int)

#####################
### Listas (list) ###
#####################

len()                   # retorna a quantidade de valores na list >>> len(lista)
.append()               # adicionar elemento no final da list >>> lista.append(25) ou ("joao") ou ainda (lista2)
                        # sim, podemos incluir uma lista dentro de outra, e ficaria mais ou menos assim:
                        # lista = [25, "joao" [26, 27, 28]]

.extend()               # adicionar vários elementos há uma lista >>> lista.extend(25) ou ("joao") ou ainda (lista2)
                        # a sintaxe é a mesma de .append() mas o comportamento e retorno é diferente, teríamos aqui:
                        # lista = [25, "j", "o", "a", "o", 26, 27, 28]

.insert()               # inserir em posição específica com indice normal ou negativo >>> lista.insert(indice, valor)
.remove()               # remover pelo valor >>> lista.remove(27) vai encontrar a primeira ocorrência de 27 e removê-lo
.pop()                  # remover por índice >>> lista.remove(0) vai remover o primeiro item
.sort()                 # ordena uma lista, necessário que todos os itens sejam comparáveis entre si
                        # pode receber nenhum, um ou dois parâmetros >>>
                        # lista.sort() vai ordenar conforme o tipo do dado, string ordena pelo alfabeto, int ou float pelo valor real
                        # lista.sort(key=len) com esse parâmetro decidimos qual regra usamos para ordenar, nesse caso o comprimento
                        # lista.sort(reverse=true) com esse parâmetro dizemos que queremos ordenar de forma decrescente

sorted()                # cria uma nove lista ordenada com base em uma lista já existente que não queremos modificar
                        # sorted(lista, reverse=true, key=len)

.reverse()              # inverter a posição dos valores em uma lista
.reversed()             # se usado com "list" retorna uma nova lista invertida com base na lista usada >>> list(reversed(lista))
.index()                # encontrar posição de um valor, podendo receber dois argumentos que definem o intervalo onde será procurado
                        # ele encontrará e trará apenas a primeira ocorrência no retorno
                        # lista.index("ana", 0, 4) aqui definimos que "ana" deve ser procurada nos índices 0, 1, 2 e 3
                        # é importante perceber aqui o comportamento de fatiamento, que utiliza o primeiro índice normal e o último -1
                        # lista.index("ana", 6, len(lista)) é uma alternativa para pegarmos a lista até o fim sem correr o risco do -1

.count()                # conta ocorrências passadas >>> lista.count(2) vai retornar o número de vezes que o número 2 aparece na lista
list()                  # cria uma lista a partir de outro elemento iterável, como fizemos acima com reversed() >>>
                        # print(list("abc")) retorna ['a', 'b', 'c']
                        # print(list(range(4))) retorna [0, 1, 2, 3]

min()                   # retorna o menor elemento
max()                   # retorna o maior elemento

                        # ambos os métodos/funções acima, trarão números por seu valor real ou strings por ordem alfabética,
                        # com exceção de casos onde usemos uma key, por exemplo "len", nesse caso trarão de acordo com o comprimento
                        # >>> min("joao", "maria", "ana"), max(3, 1, 8), min(numeros), max(palavras), min(palavras, key=len)...

sum()                   # soma elementos numéricos e apenas numéricos >>> sum(lista), ou sum(lista1 + lista2) ou sum(range(5))

######################
### Tuplas (tuple) ###
######################

len()                   # retorna a quantidade de valores na tupla >>> len(lista)
tuple()                 # conversão para tupla
.count()                # conta ocorrências passadas >>> tupla.count("azul") vai retornar o número de vezes que "azul" aparece na lista
.index()                 # encontrar posição de um valor, podendo receber dois argumentos que definem o intervalo onde será procurado
min()                   # retorna o menor elemento
max()                   # retorna o maior elemento

                        # ambos os métodos/funções acima, trarão números por seu valor real ou strings por ordem alfabética,
                        # com exceção de casos onde usemos uma key, por exemplo "len", nesse caso trarão de acordo com o comprimento
                        # >>> min("joao", "maria", "ana"), max(3, 1, 8), min(numeros), max(palavras), min(palavras, key=len)...

#######################
### Conjuntos (set) ###
#######################

# Conjuntos ou sets são estruturas similares a list, mutáveis, mas que não possuem ordem (índice) e não permitem duplicatas
# além disso, só aceitam dados não mutáveis, como strings, int, float, bool e tuple, mas não list, por exemplo

.add(elem)                                      # Adiciona um elemento ao fim da lista desde que não seja uma duplicata
.remove(elem)                                   # Remove exatamente o elemento informado. Retorna erro se ele não existir.
.discard(elem)                                  # Remove exatamente o elemento informado. Não retorna erro algum.
.pop()                                          # Remove um elemento aleatório do set e retorna ele. Erro se o set estiver vazio.
.clear()                                        # Remove todos os elementos do set, mas ele continua existindo vazio.
.update(iterável)                               # Adiciona vários elementos a partir de um iterável ao set, isso é, a partir
                                                # de outro set, lista, tupla ou string. Ignora duplicatas.

.union(iterável)                                # Retorna um novo set combinando os elementos do set original e do iterável
                                                # não contabilizando duplicatas

.intersection(iterável)                         # Retorna um novo set com os elementos em comum do set original e do iterável
.difference(iterável)                           # Retorna um novo set com os elementos presentes no set original 
                                                # e não presentes no iterável

.symmetric_difference(iterável)                 # Retorna um novo set com uma combinação dos elementos únicos de cada set
.intersection_update(iterável)                  # Modifica o set original mantendo apenas os elementos em comum entre os sets
.difference_update(outro_set)                   # Remove do set original todos os elementos que também estão no iterável
.symmetric_difference_update(outro_set)         # Modifica o set original mantendo apenas os elementos únicos de cada set
.issubset(outro_set)                            # Retorna True se todos os elementos do set original estiverem contidos no iterável
.issuperset(outro_set)                          # Retorna True se todos os elementos do iterável estiverem contidos no set original
.isdisjoint(outro_set)                          # Retorna True se o set original e o iterável não tiverem elementos em comum

##########################
### Dicionários (dict) ###
##########################

# Dicionários são estruturas similares aos objetos em JS, com uma sintaxe ligeiramente diferente

.get()                  # obtém valor solicitado, retorna "None" se não existir, também pode receber um segundo parâmentro opcional
                        # dicionario.get(nome) ou dicionario.get(nome, "Sem nome"), nesse segundo caso, se a key "nome" não existir
                        # ao invés de None, será retornado "Sem nome"

.keys()                 # retorna todas as chaves de um dicionário >>> dicionario.keys()
.values()               # retorna todos os valores de um dicionário >>> dicionario.values()
.items()                # retorna todos os pares de um dicionário (chave, valor) >> dicionario.items()
.update()               # atualiza elementos se já existirem ou adiciona novos caso não >>>
                        # dicionario.update({'idade': 31})
                        # dicionario.update(profissao='Desenvolvedor', altura=1.80)

.pop()                  # remove chave e pode receber valor padrão no caso de já não existir >>> dicionario.pop('idade', Nulo)
.popitem()              # remove último item >>> dicionario.popitem()
.clear()                # limpa o dicionário, deixando vazio >>> dicionario.clear()
.setdefault()           # procura por uma chave, se existir retorna seu valor, se não, cria a mesma e atribui o valor passado >>>
                        # dicionario.setdefault('nome', 'desconhecido')

dict()                  # conversão para dicionário