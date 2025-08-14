# Aqui veremos os operadores lógicos matemáticos
# Para operações mais complexas é interessante saber que existe uma "ORDEM DE PRIORIDADE"
# para a resolução de equações com esses operadores

# ORDEM DE PRIORIDADE: "**", "+X e -X", "* e / e // e %", "+ e -" 

#############################
##### OPERAÇÕES BÁSICAS #####
#############################

X + Y       # Adição
X - Y       # Subtração
X * Y       # Multiplicação
X / Y       # Divisão

# As quatro acima são as operações mais básicas e fundamentais, dispensam explicações


###############################
##### OPERAÇÕES AVANÇADAS #####
###############################

X ** Y      # Potência 
            # O primeiro número (base) será elevado a potência do segundo número (expoente)

X // Y      # Divisão inteira. 
            # Além de realizar uma divisão, caso ela tenha como resultado um decimal, esse operador automaticamente 
            # arredonda o resultado para o inteiro mais próximo para baixo, tratando como int se os valores originais 
            # forem int e tratando como float se ao menos um dos valores originais for float

X % Y       # Resto de divisão
            # Esse operador realiza uma divisão inteira e, ao invés de nos retornar o resultado dessa operação
            # ele nos retorna o resto da mesma. No caso de ser uma divisão exata retorna 0


##########################
##### SINAIS UNÁRIOS #####
##########################

# Estes sinais são sinais soltos que trabalham entre si antes de afetarem diretamente uma equação

a = 2
b = -2

print(+a)       # retorna 2 pois ++2 == 2
print(-a)       # retorna -2 pois -+2 == -2
print(+b)       # retorna -2 pois +-2 == 2
print(-b)       # retorna 2 pois --2 == 2

# É a velha regrinha do "dois iguais da positivo mas um diferente da negativo"

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