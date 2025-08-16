# Comparados a list, um conjunto ou set, é algo similar, porém seus valores
# não são ordenados, ou seja, os sets não possuem indexação, além disso,
# seus métodos são diferentes e eles também não permitem duplicatas

###########################
##### CONJUNTOS (SET) #####
###########################

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1 - set2)      # Remove do set1 os itens em comum com o set2
print(set2 - set1)      # Remove do set2 os itens em comum com o set1
print(set1 | set2)      # Concatena os sets, se os valores forem todos numéricos, retornam em ordem crescente, se não, aleatória

# Um uso muito comum de set e para limpar os itens duplicados de uma lista
# convertendo essa para set e depois convertendo o set criado para lista

lista1 = [77,88,99,99,99,11,11]
set1 = set(lista1)
lista2 = list(set1)
print(lista2)