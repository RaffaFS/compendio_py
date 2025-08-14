# Como já vimos em 1_variaveis.py, variáveis do tipo booleano armazenam valores lógicos
# True, ou False, apenas. Também é importante lembrar de sempre descrevelos com a
# primeira letra em maiúsculo.

# Aqui o que veremos são operadores de booleanos e manipulações
# Variáveis booleanas, apesar de poderem ser criadas explicitamente com True ou False
# são na maioria das vezes resultados de "comparações lógicas"

####################################
##### OPERADORES DE COMPARAÇÃO #####
####################################

# Podemos encarar os operadores de comparação sempre como uma pergunta, por exemplo no
# primeiro caso: "X é maior que Y?" se sim vai retornar True, se não, False.

X > Y           # "X é maior que Y?"
X < Y           # "X é menor que Y?"
X == Y          # "X é igual a Y?"
X >= Y          # "X é maior ou igual a Y?"
X <= Y          # "X é menor ou igual a Y?"
X != Y          # "X é diferente de Y?"

#########################################
##### OPERADORES DE LÓGICA BOOLEANA #####
#########################################

# Temos 3 operadores de lógica booleana: "or", "and" e "not"
# Enquanto aqueles que vimos acima servem para comparar dados e a partir disso gerar um valor booleano
# Estes servem para "calcular" valores booleanos gerando um novo valor do mesmo tipo

# Assim como os exemplos de comparação, podemos os primeiros dois também como uma pergunta:

X or Y or Z         # "Pelo menos um dos valores é True?"
X and Y and Z       # "Todos os valores são True?"

print(1 == 1 or 4 >= 2 or 2 != 2)
print(1 == 1 and 4 >= 2 and 2 != 2)

# Importante notar a diferença entre as perguntas. Em ambos os casos, se a resposta for positiva
# teremos um True no retorno, se for negativa, teremos um False

# not é um caso a parte, ele sempre retornará o contrário do que receber na lógica booleana

print(not True)      # Qualquer dado que já resulte um valor booleano retornará o inverso
print(not 0)         # Retorna True pois 0 é considerado False
print(not 1)         # Retorna False pois 1 é considerado True
print(not [])        # Retorna True pois uma lista vazia é considerada False
print(not "texto")   # Retorna False pois uma string não vazia é considerada True

print(not 4 >= 4 and 4 == 3 or 5 != 2)      # Retorna True

# Outra coisa interessante de saber é que existe uma ordem de precedência desses operadores também
# ORDEM DE PRECEDÊNCIA: not, and e or

# Além disso, and também pode ser substituído por "&" e or por "|", mas não é uma prática recomendável