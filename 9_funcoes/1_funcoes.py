# Já vimos várias funções até aqui, inclusive aglomeradas em um único
# documento na pasta 4_metodos_e_sintaxes. Aquelas (que não métodos)
# são funções integradas, isso é, já vem integradas na linguagem

# Mas a ideia de função vai além, podemos criar nossas próprias funções
# otimizando tarefas que executaremos várias vezes ao longo do código
# e/ou criando mais organização no nosso código

# O primeiro caso se dá pela economia de linhas de código, onde escreverei
# um algoritmo apenas uma vez ao invés de várias, chamando apenas seu nome
# quando ele precisar ser executado novamente

# O segundo caso se dá porque podemos criar as funções em um bloco 
# separado do fluxo do código, criando mais legibilidade no código geral
# sem que precisemos ver linhas desnecesárias, mas podendo ir até elas
# se necessário

###########################
##### CRIANDO FUNÇÕES #####
###########################

# É importante lembrar que sempre devo definir minhas funções antes do 
# meu "programa principal", isso é, antes do meu fluxo de código padrão
# e após defini-las, devo sempre pular duas linhas como regra de sintaxe

# Sempre definimos uma função da seguinte maneira: "def funcao(): algoritmo"

def linha():
    print("=-=" * 10)
    print(f'{"=-=" * 7:^30}')
    print("=-=" * 10)

linha()
print(f'{"EXEMPLO DE FUNÇÃO!":^30}')
linha()

# No caso acima, o algoritmo da minha função é apenas a impressão de algumas
# linhas, função essa que eu invoco 2 vezes para fazer a estilização de um
# título, porém uma função pode ser criada contendo qualquer algoritmo
# que será invocado ao ter o nome da função mencionado

##################################
##### FUNÇÕES COM PARÂMETROS #####
##################################

# Toda função pode receber parâmetros da seguinte maneira: "def funcao(parametro):"

def soma(a, b):
    res = a + b
    print(f'O resultado é {res}')

soma(4, 2)
soma(100, 10)
soma(12.3, 1.1)

# No caso acima criei uma função que tem "dois slots de parâmetros", para que a
# minha função possa ser executada corretamente eu devo precher esses dois slots
# sempre que fizer a invocação dessa função como fiz nos 3 exemplos

# Existe uma sintaxe para os parâmetros onde não precisso definir a quantidade
# exata de parâmetros, veja:

def soma2(*num):
    print(f'Os valores recebidos foram {num}')
    print(f'A soma dos valores é: {sum(num)}')

soma2(0,1,3,4,3,1)
soma2(3,2)

# No exemplo acima, com o uso de "*" antes do parâmetro estou dizendo que ele
# deve receber todos os valores passados como parâmetros e agrupar dentro de
# uma tupla

# No algoritmo eu imprimo os valores recebidos e logo depois a soma dos mesmos

def dobra(lista):
    indice = 0
    while indice < len(lista):
        dobrados.append(lista[indice] * 2)
        indice += 1
    print(f'Os valores passados são: {numeros}')
    print(f'Seus respectivos dobrados são {dobrados}')

numeros = [7,4,3]
dobrados = []
dobra(numeros)

# No exemplo acima temos uma função mais complexa e que faz o uso não de uma
# tupla, mas de uma lista, como parâmetro. Veremos parte a parte esse algoritmo
# mas é importante sabermos que as listas passadas após ele já foram imaginadas
# antes da sua construção

# 1. Defino a função com um parâmetro normalmente (e que receberá a lista "numeros")
# 2. Defino uma variável que armazenará 0, ela incrementará a cada laço, funcionando como índice de "numeros"
# 3. Crio um laço que diz que enquanto "indice" for menor que o comprimento total do parâmetro, ele deve rodar
# 4. Digo que quero acrescentar a "dobrados" o dobro do valor referente ao índice de "numeros" atualmente em vigor no laço
# 5. Incremento "indice" em 1 no final da volta para que na próxima volta o índice seguinte seja recebido na operação de "*"
# 6. Fora do laço, ou seja, depois que o valor de "indice" for correspondente ao comprimento de "numeros"
#    peço dois prints, um com "numeros" e outro com "dobrados"