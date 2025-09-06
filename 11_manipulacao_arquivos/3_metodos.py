#############################
##### MÉTODOS POR MODOS #####
#############################

# Cada modo de abertura conta com métodos específicos que outros modos podem não permitir
# Vejamos as listas de métodos disponíveis para cada modo de abertura

#######################################################
##### MÉTODOS PARA MODOS COM PERMISSÃO DE LEITURA #####
#######################################################

.readable()     # Retorna True se o arquivo tiver permissão de leitura

.read()         # Retorna todo o conteúdo do arquivo
.read(17)       # Retorna os primeiros 17 caracteres/bytes do arquivo
.               # OBS: para ler de uma posição a outra primeiro usamos .seek() (veja no documento 0 dessa pasta)

.readline()     # Retorna uma linha, a partir da posição do cursor, se ele estiver no meio da linha, só lê o restante dela
.readline(11)   # Retorna os primeiros 11 caracteres de uma linha ou menos se a linha terminar antes
.readlines()    # Retorna todo o arquivo a partir da posição atual do cursor como uma lista de linhas

#######################################################
##### MÉTODOS PARA MODOS COM PERMISSÃO DE ESCRITA #####
#######################################################

.writable()     # Retorna True se o arquivo tiver permissão de escrita

.write()        # Escreve a string passada (ou bytes), no arquivo a partir da posição atual do cursor
.writelines()   # Passamos uma lista de strings pré programada e a método escreve cada índice como uma linha

##############################
##### MÉTODOS ADICIONAIS #####
##############################

.truncate()     # Reduz o arquivo para apenas aquilo que está antes da posição atual do cursor, jogando fora o restante
.truncate(94)   # Leva o cursor até a posição passada e reduz o arquivo como o descrito acima

.flush()        # Entenda que tudo que escrevemos em um arquivo a partir da sua abertura fica armazenado no buffer
                # do python, sendo de fato transferido para o arquivo apenas após seu fechamento. Esse método
                # garante que tudo que foi escrito antes com ".write()" seja passado imediatamente para o
                # arquivo e esvazia o buffer do python, sem necessitar do fechamento, agilizando processos onde
                # queremos escrever várias vezes em um arquivo mas por questões de segurança queremos que o
                # arquivo seja atualizado em tempo real e com um processo otimizado, sem a necessidade de
                # abrir e fechar o arquivo várias vezes.

.fileno()       # Retorna o "descritor do arquivo". Quando um arquivo é aberto ele ganha um número como se fosse um
                # índice, que começa a partir do 3 (pois 0, 1 e 2 são números reservados), então se eu tiver 3
                # arquivos abertos simultâneamente, seus descritores serão 3, 4 e 5 respectivamente. Utilizaremos
                # esses descritores em integrações com módulos de sistema operacional (os), por exemplo

.isatty()       # Diz se o arquivo está conectado a um terminal, retornando True ou False

.detach()       # Utiliado para separar o "buffer" do "objeto de arquivo", retornando o "objeto de arquivo bruto"
                # Isso é útil quando queremos trabalhar com os bytes de um arquivo, assumindo um controle maior
                # em operações detalhadas de baixo nível