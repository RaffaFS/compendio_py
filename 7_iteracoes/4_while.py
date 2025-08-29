import time                                                                 # para uso da função sleep do módulo time mais abaixo

# while é também uma estrutura de repetição ou de iteração
# enquanto com for in diziamos que queriamos que o laço
# fosse executado uma quantidade de vezes pré-definida de
# acordo com o range explícito ou implícito, aqui dizemos
# algo tipo

# Enquanto "isso", continue executando o laço
# vamos vizualizar isso de maneira mais completa e literal
# para podermos entender melhor:

x = 1
while x <= 10:
    print(x)
    x += 1
    time.sleep(.5)                                               # essa função atrasa a execução de tudo o que vem a seguir em 0.5s
print('x se tornou 11, logo não é mais menor ou igual a 10, então o laço foi interrompido.')

# Acima temos um exemplo do uso de while. Enquanto a condição
# for verdadeira ele continuará executando o laço.
# Abaixo vamos ver mais dois exemplos, que nos deixarão
# entender melhor as possibilidades que temos com while

print('Em 3 segundos um laço infinito iniciará')
time.sleep(3)                                                    # essa função atrasa a execução de tudo o que vem a seguir em 3s

# veremos mais sobre inputs nos documentos seguintes, mas aqui
# basta saber que pediremos um valor não declarado previamente,
# para o usuário, e por isso não poderiamos usar for in
y = ''
while y != 'S' or y != 's':
    y = input('Deseja sair? [S/N]')

# Nos documentos de inputs veremos mais usos de while dentro
# de exemplos com laços infinitos e uso do break