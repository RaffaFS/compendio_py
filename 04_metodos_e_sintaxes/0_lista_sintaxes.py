# Nessa pasta teremos primeiro um entendimento sobre métodos e então depois estarei
# deixando uma lista completa com todos os métodos e funções integradas nativas do Python
# mas de início é interessante conhecermos também o que podemos fazer apenas com
# sintaxes da linguagem, sem o uso de métodos ou funções

##################################################
##### LISTA GERAL DE SINTAXES DE MANIPULAÇÃO #####
##################################################

# Abaixo veremos em formato de lista todas as principais sintaxes de manipulação de
# dados simples sem a utilização de funções integradas ou métodos explicitamente

##############################
### Indexação e fatiamento ###
##############################

# Funciona em strings, listas, tuplas, arrays, bytes, etc.

obj[i]                      # Acessa o elemento no índice i
obj[i:j]                    # Fatia dos valores do índice i até j (não incluindo o j)
obj[i:j:k]             	    # Fatia com passo k
obj[::-1]              	    # Inverte sequência
obj[:]                      # cria uma cópia dos valores atuais de obj sem dependências com alterações futuras do dado original
obj[i] = valor      	    # Modifica o valor do índice i
obj[i:j] = valores  	    # Modifica os valores da fatia
del obj[i]             	    # Remove o valor no índice i
del obj[i:j]           	    # Remove os valores na fatia


########################
### Desenpacotamento ###
########################

# Pega um dado único e abstrai vários valores dele de uma única vez criando vários dados a parte

grupo = [23, 21, 54, 46, 84]

a, b, c = grupo	                                    # Atribui cada valor no grupo a uma variável descrita
a, _, b = grupo	                                    # Atribui valores como a anterior mas Ignora valor com "_"
a, b, *resto = grupo	                            # Captura o restante da sequência com *dado
primeiro, *meio, ultimo = grupo	                    # Captura valor do primeiro indice, meio e valor do último índice
primeiro, *meio, penultimo, ultimo = grupo	        # Captura valor do primeiro indice, meio, valor do penúltimo e do último índice

