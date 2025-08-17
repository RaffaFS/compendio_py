# Condicionais são estruturas de código que só vão executar um algoritmo
# específico quando determinadas condições forem verdadeiras, além disso
# opcionalmente podemos pedir para que se as condições forem falsas,
# outro algoritmo seja executado.

##############
##### IF #####
##############

# Geralmente utilizamos if e else juntos, para criar um sistema de "acerto e erro
# ou "verdadeiro e falso", mas podemos também utilizar if sozinho, e se sua condição
# não for verdadeira, absolutamente nada será feito.

if False:
    print('É falso (não vai imprimir)')

if True:
    print('É verdadeiro')


###################
##### IF ELSE #####
###################

# Vejamos um exemplo mais real e agora já com else integrado na lógica:

senha_armazenada = 1234
senha_input = 1243

senha = senha_armazenada == senha_input

if senha:
    print('Senha correta')
else:
    print('Senha errada')

# Podemos também fazer a comparação diretamente nos blocos condicionais e,
# além disso, posso trabalhar com outras comparações:

if senha_armazenada != senha_input:
    print('Senha errada 2')
else:
    print('Senha correta 2')


################
##### ELIF #####
################

# Enquando if é um "se", e else um "se não", elif é um "se não, se"...

# O elif serve para quando queremos ter mais de duas respostas possíveis
# sendo todas mutuamente exclusivas.
# A primeira condição a ser analisada continuará sendo a condição de if
# mas se não for verdadeira, else não será mais executado instantâneamente,
# a condição de cada elif, um de cada vez de acordo com a posição que
# aparecem no código, será verificada e, apenas se todos forem falsos é
# que else será executado.

meta = 100
progresso = 42

if progresso == meta :
    print('Você bateu a meta')
elif progresso >= 4*(meta/5) :
    print('Você concluiu 80% da meta')
elif progresso >= 3*(meta/5):
    print('Você concluiu 60% da meta')
elif progresso >= 2*(meta/5):
    print('Você concluiu 40% da meta')
elif progresso >= meta/5:
    print('Você concluiu 20% da meta')
else:
    print('Você ainda não fez grande coisa')

###############################
##### CONDIÇÕES ANINHADAS #####
###############################

# Isso é, podemos fazer com que um algoritmo seja executado apenas caso
# várias condições forem verdadeiras, e podemos fazer isso de dois tipos

numero = 85

if numero >= 80 and numero <= 90 and isinstance(numero, int):
    print('Seu número está listado')
else:
    print('Seu número não está listado')

# Nesse primeiro caso acima vemos que o algoritmo do if só será executado
# se as três condições forem verdadeiras, porém no final temos ainda
# apenas dois resultados: está listado ou não está listado

# Mas e se eu quiser que o meu valor passe por várias camadas de verificações
# Só retornando o resultado final caso cumpra todas mas, diferente do exemplo
# acima, retorne uma resposta para cada caso, fazemos o seguinte:

usuario = {
    "nome": "Maria",
    "ativo": True,
    "admin": True
}

if usuario["ativo"]:
    if usuario["admin"]:
        print("Usuário ativo e administrador")
    else:
        print("Usuário ativo, mas não é administrador")
else:
    print("Usuário inativo")

# A princípio as condições aninhadas dessa maneira, em camadas, podem ter uma
# usabilidade similar a de "elif", porém a diferença é que enquanto com elif
# trabalhamos com possibilidades exclusivas, aqui, as camadas mais internas
# só serão verificadas se a camada anterior for verdadeira 