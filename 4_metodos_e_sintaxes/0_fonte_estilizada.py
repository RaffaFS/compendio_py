# É importante que tenha visto a lista de caracteres especiais antes
# pois aqui usaremos uma lógica já vista de maneira mais simples lá

# O Python é uma linguagem back-end, então não constrolamos com ele
# o que é mostrado para o usuário final, mas podemos estilizar o
# que aparece no terminal, seja para chamar atenção como um alerta
# em alguma resposta do algoritmo, seja para criar alguma hierarquia
# ou padronização ou, seja para fazer graça

# Em resumo podemos estilizar toda resposta fornecida dentro de um
# print('') ou dentro de um print(f''), execute e veja

print('\033[32mOlá verde\033[m')
print('\033[42mOlá fundo verde\033[m')
print('\033[1mOlá negrito\033[m')

# O que temos acima são três exemplos, sendo o primeiro de alteração
# de cor do texto, o segundo de cor de fundo e o terceiro de estilo

# Sempre que queremos fazer uma dessas alterações incluímos os
# caracteres especiais \033[00m onde essa estilização deve iniciar
# e \033[m onde ela deve acabar, como vimos acima. No local de 
# "00" colocamos nossos números de estilização

# Veja abaixo uma lista completa das opções disponíveis:

###########################
##### ESTILO DA FONTE #####
###########################

# 0             Estilo padrão/sem estilo
# 1             Negrito
# 4             Sublinhado
# 7             Inverte as cores de texto e fundo

########################
##### COR DO TEXTO #####
########################

# 30            cinza
# 31            Vermelho
# 32            Verde
# 33            Amarelo
# 34            Azul
# 35            Roxo
# 36            Turquesa
# 37            Branco

########################
##### COR DO fUNDO #####
########################

# 40            preto
# 41            Vermelho
# 42            Verde
# 43            Amarelo
# 44            Azul
# 45            Roxo
# 46            Turquesa
# 47            Branco

# OBS1: Existem bibliotecas para melhorar isso, mas essa é a maneira
#       nativa que podemos estilizar os retornos no terminal

# OBS2: Podemos aplicar até 3 mudanças de uma vez, desde que sejam as
#       três de naturezas diferentes, veja

print("Alô alô!\033[4m\033[33m\033[41m Aqui tem estilo \033[me aqui já não tem mais")

# OBS3: Algumas opções de legibilidade ruim são impedidas e reformatadas
#       altomaticamente pelo python antes de sua renderização, veja
#       abaixo o exemplo onde tento renderizar letra roxa no fundo roxo

print("Alô alô!\033[4m\033[35m\033[45m Aqui tem estilo \033[me aqui já não tem mais")

# OBS4: Uma outra opção ainda de trabalhar com esses estilos é definir
#       variáveis no início do documento que vão armazená-los

vrm = '\033[31m'
vrd = '\033[32m'
mrl = '\033[33m'
zl = '\033[34m'
clear = '\033[m'

print(f'{vrm} Olá vermelho {clear}')
print(f'{vrd} Olá verde {clear}')
print(f'Olá {mrl}Amarelo{clear} e Olá {zl}Azul{clear}')