#############################
##### MODOS DE ABERTURA #####
#############################

# 'r' abre o arquivo apenas para leitura e apresenta erro se o arquivo não existir
# 'w' abre o arquivo e zera seu conteúdo ou cria um novo se o arquivo não existir ou não for encontrado, permite escrita mas não leitura
# 'x' cria um arquivo único e gera erro se já existir um com o mesmo nome, permite escrita mas não leitura
# 'a' abre o arquivo para escrever no final dele (append), mas não permite leitura

##### Em Resumo, utilizo 'r' quando quero captar dados, 'w' quando quero criar um novo arquivo e escrever nele ou sobreescrever
##### um arquivo existente, 'x' com o mesmo primeiro objetivo de w mas com a segurança de que estarei criando um arquivo 
##### novo e não sobreescrevendo um que já existe e 'a' para manter tudo o que já existe no arquivo mas escrever no final

##### Também poderia fazer uma abertura com 'r' para captar os dados e outra com 'w' para sobrescrever o arquivo depois que
##### guardei suas informações, podendo devolvê-las ao arquivo em outra formatação ou apenas partes junto do incremento

##### Porém, também a outros modos para leitura e escrita que veremos abaixo

####################
##### CONJUTOS #####
####################

# Os caracteres abaixo são usados com um dos de cima para criar outros modos

# '+' >>> 'r+', 'w+' ou 'a+ >>> Basicamente permite leitura e escrita com o comportamento padrão "da letra"

# 't' >>> 'rt' ou 'wt' >>> Usa o modo de texto padrão, seja para leitura ou escrita, isso é, formatação de código
#                          interpretando quebras de linha no texto do arquivo como '\n', por exemplo

# 'b' >>> 'rb' ou 'wb' >>> Usa o modo binário, mais comumente usado para arquivos como imagens, vídeos, áudios,
#                          PDFs... Trabalha com bytes ao invés de strings e não intetpreta codificação e quebras