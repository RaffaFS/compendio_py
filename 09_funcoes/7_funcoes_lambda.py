# Essa é uma maneira alternativa de declarar uma função, onde a criamos
# sem nem mesmo a necessidade de nomeá-la. Utilizamos elas normalmente
# para escrever expressões muito pequenas, mas que ainda compensam ser
# armazenadas em uma função para o melhor desempenho do nosso código
# por conta da possível grande quantidade de vezes que utilizaremos
# aquela expressão.

# Se comparado ao JS seria como se o que geralmente fazemos aqui em python
# fosse uma "declaração de função" e a função lambda seria uma "expressão
# de função"

# Basicamente guardamos uma expressão curta dentro de uma variável, com
# a sintaxe correta, e quando precisamos fazer uso dela chamamos a variável

# variável = lambda parametro: expressão
# variável = lambda parametro1, parametro2, ... : expressão

# Então para coisas simples ao invés de
def soma1(a, b):
    res = a + b
    return res

print(f'O resultado é {soma1(2,3)}')

# Eu poderia fazer
soma2 = lambda a, b: a + b
print(f'O resultado é {soma2(4,5)}')

# Vejamos outro exemplo e mais uma dica de otimização de código simples

numero_par = lambda num: True if num % 2 == 0 else False

numeros = [2,18,1,3,2,9]
for numero_atual in numeros:
    if numero_par(numero_atual) == True:
        print(f'O número {numero_atual} par')
    else:
        print(f'O número {numero_atual} impar')

# O que fiz acima foi definir uma função lambda que recebe um número como
# argumento e depois pede uma comparação da divisão desse número por dois
# dentro de um bloco de if/else simplificado, no caso:

# Verdadeiro se resto da divisão de numero por 2 for 0 se não falso

# Isso porque todo inteiro par, se dividido por dois não terá restos

# depois defino uma lista de números, e crio um laço for/in com essa lista
# dentro do laço crio uma condição, na condição passo a função com o
# numero_atual, isso é, o número que está sendo usado na repetição atual do
# laço, como argumento da função, e digo que se o retorno for True, ou seja
# se a função definir que a divisão daquele número por dois não gerar restos,
# executamos o bloco if, dizendo que o número é par, se não, executamos o else

#################################
##### FUNÇÕES DE ALTA ORDEM #####
#################################

# Até então nossos parâmetros sempre eram variáveis numéricas, strings,
# booleanos ou listas, por exemplo, mas agora conseguimos passar
# funções lambda como parâmetros de outras funções e também passar 
# uma função lambda no retorno de outra função para executar um
# determinado algoritmo com os dados daquele escopo, retornando o
# resultados de sua operação

# E uma função tendo ao menos um desses dois casos, é o que caracteriza-a
# como uma função de alta ordem

# Bem, já vimos algo similar ao primeiro caso, um pouco mais acima,
# onde utilizamos uma lambda como argumento para um laço for/in
# mas vejamos abaixo um exemplo completo com os dois casos

# definindo função de alta ordem
def aplicar_operacao(operacao):
    return lambda x: operacao(x)

# Passando uma função lambda
dobro = aplicar_operacao(lambda n: n * 2)

# Usando a função retornada
print(dobro(5))

# primeiro definimos uma função padrão que deverá receber outra como argumento
# nela trazemos apenas o retorno, e nele, uma função lambda

# na definição de "dobro", defino que essa será uma função lambda baseada em 
# "aplicar_operacao", ou seja, sempre que eu chamar "dobro", estarei na verdade
# chamando "aplicar_operacao" e, agora sim, com outra lambda como argumento

# Isso é um cas simples, mas vejamos o que acontece quando chamo "dobro(5)"
# a chamada de "dobro" implica na chamada de "aplicar_operacao" com o
# argumento pré-definido (lambda n: n * 2), o cinco não é passado aqui
# já que de certa forma, "dobro" é a própira "aplicar_operacao" mas com
# argumento fixo, ou seja, "5" é um argumento pertencente a lambda que está
# dentro de dobro, ele tomará o lugar de "x" e só depois o de "n", mais ou 
# menos nesse caminho:

# 1. dobro(5)
# 2. dobro = aplicar_operacao(lambda n: n * 2)(5)
# 3. return lambda 5: (lambda n: n * 2)(5)              # operando no nível de x
# 4. return lambda 5: 5 * 2                             # o valor de x passa para n, operando no nível de n
# 5. return 10 