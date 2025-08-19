# Erros acontece a todo momento na programação
# Quando um erro acontece em Python, ele sempre nos aponta onde está o erro
# um título e uma descrição do erro para que possamos corrigí-lo no código

######################
##### TRY EXCEPT #####
######################

# Sempre que um erro acontece na execução do código, a execução desse código
# é interrompida. Com os blocos "try" e "except" conseguimos tratar o erro
# 

# Basicamente colocamos todo o algoritmo que pode vir a apresentar algum tipo
# de erro, dentro de um "bloco try". Caso realmente ocorra um erro, o fluxo do
# código é desviado para o "bloco except", onde descreveremos o tratamento
# dos erros esperados.

faturamento = 1890.00
total_clientes = 0

try:
    ticket_medio = faturamento/total_clientes
    print(ticket_medio)
    print('código seguiria imprimindo isso se não houvesse erro')

except ZeroDivisionError:
    print(f'Número de clientes igual a {str(total_clientes)}. Valor inválido.')

# Acima passamos o código no bloco try, já sabendo que um erro ocorreria e
# também qual seria esse erro, o "ZeroDivisionError".

# Nesse caso, qualquer outro erro que ocorra não será tratado pelo nosso
# bloco except, apenas será exibido com sua descrição padrão. Porém o erro 
# esperado ocorre aqui e o except é disparado, fazendo com que a execução 
# siga nele e passe a ignorar o bloco try

# Podemos então criar um tratamento para cada erro esperado, mencionando
# seus respectivos nomes ou, podemos criar um tratamento genérico para
# todo e qualquer erro que possa vir a ocorrer, veja abaixo:

anos = [2019, 2020, 2021]

try:
    ano_atual = anos[3]
    print(ano_atual)
except Exception as e:
    print(f'Lista de anos é menor que o valor escolhido. Espera-se um valor entre 0 e {str(len(anos) - 1)}')
    print(f'Tipo do erro: {str(type(e))}')
    print(f'Descrição do erro: {str(e)}')

# Aqui além de criarmos um except para todo e qualquer erro que possa vir a
# acontecer, também passamos o "Exception" para o argumento "e", podendo 
# utilizar esse argumento dentro do bloco em si.

# Isso é uma boa prática apenas quando não sabemos qual erro esperar

# Outra opção ainda é criar blocos except específicos dos erros esperados
# e um except final de Exception para eventuais erros não previstos

###################
##### FINALLY #####
###################

# Blocos de finally são usados para seguir com o código depois do erro ser
# tratado pelos blocos de except.

try:
    ticket_medio = faturamento/total_clientes
    print(ticket_medio)
    print('código seguiria imprimindo isso se não houvesse erro')

except ZeroDivisionError:
    print(f'Número de clientes igual a {str(total_clientes)}. Valor inválido.')
    total_clientes = 1
    print(f'Número de clientes definido para {str(total_clientes)}.')

finally:
    print('A operação será realizada novamente.')
    ticket_medio = faturamento/total_clientes
    print(ticket_medio)