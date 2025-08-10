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
