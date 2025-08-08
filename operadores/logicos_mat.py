#############################
##### OPERAÇÕES BÁSICAS #####
#############################

# Definindo variável
carrinho1 = 0

# Operador de soma
carrinho1 = 1 + 1
print(carrinho1)

# Operador de subtração
carrinho1 = 4 - 1
print(carrinho1)

# Operador de multiplicação
carrinho1 = 5 * 5
print(carrinho1)

# Operador de divisão
carrinho1 = 100 / 10
print(carrinho1)


###############################
##### OPERAÇÕES AVANÇADAS #####
###############################

# Operador de potência ou exponenciação
# Não há muito o que comentar aqui, o primeiro número (base) será elevado a potência do segundo número (expoente)
itens = 3 ** 3
print(itens)

# Operador de divisão inteira
# Além de realizar uma divisão, caso ela tenha como resultado um decimal, esse operador
# automaticamente arredonda o resultado para o inteiro mais próximo para baixo
# Nos casos abaixo o resultado seria respectivamente 1.5 e 2.347...
# Mas se tratando de "//", os resultados respectivos serão 1 e 2.0
# Observe também que, apesar de o segundo resultado ser um número inteiro matemáticamente falando,
# aqui ele retorna com .0 graças aos valores originais da operação, assim sendo tratado como "float"
itens = 3 // 2
print(itens)
itens = 5.4 // 2.3
print(itens)

# Operador de resto de divisão
# Esse operador realiza uma divisão inteira e, ao invés de nos retornar o resultado dessa operação
# ele nos retorna o resto da mesma. Por exemplo, no primeiro caso abaixo temos uma divisão exata
# sem restos (retorna 0), nos outros dois temos divisões com sobras (retornam 1 e 0.8 respectivamente)
itens = 6 % 3
print(itens)
itens = 3 % 2
print(itens)
itens = 5.4 % 2.3
print(itens)


#####################################
##### ATRIBUIÇÕES COM OPERAÇÕES #####
#####################################

# Os operadores desse grupo são: +=, -=, *=, /=, //=, **=, %=
# Basicamente todos os operadores que já vimos, aqui acompanhados do sinal "="

# Enquanto que com os operadores anteriores criávamos variáveis para armazenar o resultado de uma 
# operação com dois valores explícitos nela mesma, nas atribuições com operações armazenamos um novo 
# valor a uma variável já existente, utilizando o valor já presente nela para realizarmos a operação 

# Definindo variável
carrinho2 = 0

# Abaixo digo que carrinho2 receberá agora o valor dele mesmo (0) somado a 10
# Seu valor passará a ser 10
carrinho2 += 10
print(carrinho2)

# Nesse outro exemplo digo que carrinho2 receberá agora o valor dele mesmo (10) dividido por 5
# Seu valor passará a ser 5
carrinho2 /= 2
print(carrinho2)

# Nesse último exemplo digo que carrinho2 receberá agora o valor dele mesmo (5) elevado a potência de seu próprio valor (5) 
# Seu valor passará a ser 3125 (5*5*5*5*5)
carrinho2 **= carrinho2
print(carrinho2)