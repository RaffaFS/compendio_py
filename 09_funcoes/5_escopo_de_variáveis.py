# Um escopo "define um local". Escrevemos escopos de variáveis quando
# desejamos que uma variável só seja manipulada dentro desse local ou
# quando desejamos ter mais de uma variável com o mesmo nome e cada
# uma armazenando um valor próprio sem relações diretas com as demais
# Ou ainda, quando queremos manipular uma variável global, mas sem
# alterar seu valor global, alterando apenas seu valor "local"

def test1():
    print(f'Na função teste, n vale {n}')

#Programa principal
n = 2
test1()
print(f'No programa principal, n vale {n}')

# Nesse exemplo executo um print diretamente e depois chamo uma função
# que executa um print internamente. Em ambos os casos chamo a variável
# "n" e ambos conseguem alcança-la

def test2():
    # global y                              não mexa por enquanto, você vai entender no fim desse documento
    x = 3
    print(f'Na função teste, x vale {x}')

#Programa principal
test2()
print(f'No programa principal, x vale {x}')

# Nesse segundo exemplo vemos que a variável só é acessada e manipulada
# pelo algoritmo dentro da função, mas não no programa principal

def test3(parametro):
    # global y
    # print(f'Agora com o comando global, mesmo na função teste y vale {y}')
    y = parametro + 5
    print(f'Na função teste, y vale {y}')

#Programa principal
y = 4
test3(y)
print(f'No programa principal, y vale {y}')

# Nesse terceiro exemplo, várias coisas:
# 1. Posso declarar variáveis com o mesmo nome que, se estando em escopos diferentes não iram interferir umas nas outras
# 2. Passo y como parâmetro e o y local que = parametro + 5 vale 9, mas o y global continua valendo 4
# 3. Habilitando a palavra reservada "global", junto do nome da variável, torno o escopo da função em global, não mais
#    local, isso quer dizer que os valores atribuidos a variáveis dentro da função poderão ser utilizados globalmente
#    por isso mesmo, y, mesmo fora da função, a partir desse ponto não mantém o valor original de 4, mas passa a ser 9