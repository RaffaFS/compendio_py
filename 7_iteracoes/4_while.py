import time                                                                 # para uso da função sleep do módulo time mais abaixo

# while é também uma estrutura de repetição ou de iteração
# enquanto com for in diziamos que queriamos que o laço
# fosse executado uma quantidade de vezes pré-definida de
# acordo com o range explícito ou implícito, aqui dizemos
# algo tipo

# Enquanto "isso", continue executando o laço
# vamos vizualizar isso de maneira mais completa e literal
# para podermos entender melhor:

x = 0
while x < 10:
    print(x)
    x += 1
    time.sleep(1)                                               # essa função atrasa a execução de tudo o que vem a seguir em 1s