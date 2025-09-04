import time

###################################
##### MANIPULAÇÃO DE ARQUIVOS #####
###################################

# Quando falamos sobre manipulação de arquivos de texto, estaremos
# sempre utilizando "open()" que recebe dois argumentos
# open(localizacao, modo abertura)

arquivo = open('../dados1.txt', 'w')                            # anexando abertura em modo de sobreescrição à variável arquivo
arquivo.write('Rogério\n')                                      # sobrescrevendo arquivo (vazio até então)
arquivo.write('Romário')                                        # sobrescrevendo arquivo (vazio até então)
arquivo.close()                                                 # fechando arquivo

# No caso acima podemos entender melhor os argumentos em python
# o primeiro é o caminho completo desse arquivo que contém o código
# até o arquivo que contém os dados e o segundo vai de acordo com 
# o que desejamos fazer com o arquivo

# depois de abrirmos o arquivo chamamos o método desejado desdae que
# esteja disponível para aquele modo de abertura, nesse caso
# chamamos o método .write(), para escrever no nosso arquivo

# Agora vamos rodar o código e então notar 3 coisas:
# 1. Observando o arquivo "dados1.txt" veremos que as strings foram escritas no nosso arquivo de dados
# 2. Romário não substitui Rogério, foi adicionado depois dele, pois apesar de .write() funcionar na 
#    base de sobreescrição no modo de abertura 'w', isso só volta a acontecer depois que o arquivo é
#    fechado e aberto novamente
# 3. Caracteres especiais como as letras acentuadas nos nomes não são reconhecidas, vamos resolver

time.sleep(10)                   # Atrasando as próximas linhas em 10s para que você possa ver o arquivo sendo alterado "ao vivo"

################################
##### PARÂMETROS OPCIONAIS #####
################################

arquivo = open('../dados1.txt', 'w', encoding='utf-8')          # anexando abertura à variável agora com 
arquivo.write('Laís\n')
arquivo.write('André')
arquivo.close()                                                 # fechando arquivo

# Observando até os dois últimos nomes serem escritos você agora
# perceberá que eles recebem os caracteres acentudados normalmente
# graças ao encoding='utf-8'

# São vários os parâmetros opcionais de open, mas veremos isso em
# outro documento, agora quero que veja um método alternativo de
# abertura de arquivo

##### Sempre que abrimos um arquivo é importante fechar o mesmo assim
##### que realizarmos todas as operações desejadas, por isso utilizamos
##### nas duas vezes acima "arquivo.close()", porém existe uma outra
##### maneira de abertura onde o fechamento é automático, ou de outro
##### ponto de vista pode-se dizer que se cria um escopo para a
##### manipulação do arquivo

time.sleep(5)                   # Atrasando as próximas linhas em 5s para que você possa ver o arquivo sendo alterado "ao vivo"

with open('../dados1.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Se essa rua, se essa rua fosse minha...')