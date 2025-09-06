############################################################
###############                              ###############
##########                 CURSOR                 ##########
###############                              ###############
############################################################

# É importante que você já tenha visto ao menos os documentos 1 e 2 dessa pasta e entendido
# sobre eles para que possa entender esse documento. Se não for o caso, veja-os e depois 
# retorne para esse documento.

# Sempre que formos trabalhar com arquivos externos temos que lembrar da posição do cursor
# Tal qual o nosso código principal, a manipulação de documentos após sua abertura open()
# segue um fluxo na manipulação, e isso é determinado pela posição do cursor que, nesse
# caso é análogo àquela barrinha preta ou branca que vemos piscando em editores de texto
# e utilizamos para identificar onde vamos escrever.

# Isso é importante de se entender pois qualquer modificação feita será feita depois da
# posição do cursor.

# Quando eu abro um arquivo, meu cursor está na posição '0'.

# Se eu peço para que meu código leia esse arquivo inteiro, meu cursor vai para a última
# posição possível, isso é, o índice referente ao último caractere do arquivo, mas se
# eu peço por exemplo arquivo.read(5), lendo apenas uma parte, depois eu não vou precisar
# pedir arquivo.read(5, 10) para que ele leia uma segunda parte, apenas arquivo.read(5) novamente
# pois o cursor já está posicionado no final da primeira parte, e começará o próximo
# comando a partir dali

# Outro exemplo é: não quero um arquivo zerado (abertura com 'w'), nem um arquivo novo
# (abertura com 'x'), então abro com 'a', assim posso escrever mais num arquivo sem
# perder o conteúdo já existente. Porém devemos observar que 'a' sempre escreve no fim
# do arquivo, como "append", ou seja, o cursor está na última posição possível para
# o arquivo. "Mas e se eu quiser escrever em uma posição específica do arquivo?"

#############################
##### MÉTODOS DE CURSOR #####
#############################

.tell()                 # Retorna a posição atual do cursor
.seek()                 # move o cursor para a posição desejada, veja os exemplos abaixo:

.seek(0)                # move o cursor para o início
.seek(10)               # move o cursor para logo a frente do décimo caractere (deixando ele "para trás"), ou do décimo byte

# Podemos passar mais um parâmetro para seek que define o ponto de partida do movimento que será feito (1 ou 2)

.seek(10, 2)            # avança o cursor em 10 a partir da posição atual
.seek(-10, 2)           # a partir do final retrocede o cursor em 10 (importante mencionar o primeiro número negativo)

.seeakable()            # indica se o arquivo permite a movimentação de cursor com o .seek()