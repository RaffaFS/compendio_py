import time                                                                 # para uso da função sleep do módulo time mais abaixo

# Inputs são funções integradas, veremos mais sobre funções mais a frente
# Vamos começar pelos inputs por serem bastante utilizados e de fácil
# arpendizado

# É importante lembrar que a saída de um input sempre será uma string
# então se formos usar sua saída em um calculo por exemplo teremos que
# converter para int ou float

#################
##### INPUT #####
#################

# Podemos utilizar os inputs de outras maneiras, mas geralmente vamos
# usá-los armazenando-os em uma variável

nome = input('Digite seu nome: ')
comida = input('Digite sua comida preferida: ')
print(f'Olá {nome}, vamos marcar de comer {comida}?')
print('\n')                                                                 # esse comando cria um espaçamento no terminal

# O que acontece aqui é que sempre que nosso código achar um input, ele
# vai parar e esperar o retorno do usuário, só após isso é que seguirá
# com a execução.

time.sleep(2)                                                   # essa função atrasa a execução de tudo o que vem a seguir em 2s
print('Agora vamos realizar uma operação de soma?')
print('OBS: não insira letras ou símbolos, essa é a execução sem tratamento de erro ou estrutura de repetição!')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print(f'O resultado da operação é: {n1 + n2}')

# Acima decidimos trabalhar com valores numéricos nos inputs para realizarmos
# uma operação matemática, então já passei dentro das variáveis que quero o
# input convertido para float, pois funcionará tanto com inteiros quanto com
# decimais, porém se o usuário decidir colocar um caractere que não pode ser
# convertido para float, o código apresentará um erro, vamos ver como podemos
# corrigir isso:

time.sleep(2)                                                   # essa função atrasa a execução de tudo o que vem a seguir em 2s
print('Vamos realizar uma operação de multiplicação?')

while True:
    try:
        n1 = float(input('Digite o primeiro número: '))
        break
    except ValueError:
        print("Erro: Digite um caractere numérico válido")
        time.sleep(1)                                           # essa função atrasa a execução de tudo o que vem a seguir em 1s

while True:
    try:
        n2 = float(input('Digite o segundo número: '))
        break
    except ValueError:
        print("Erro: Digite um caractere numérico válido")
        time.sleep(1)                                           # essa função atrasa a execução de tudo o que vem a seguir em 1s

print(f'calculando...')
time.sleep(5)                                                   # essa função atrasa a execução de tudo o que vem a seguir em 5s
print(f'O resultado da operação é: {n1 * n2}')

# Acima então criamos um laço infinito com "while True", já que descrito
# explicitamente while será True então sempre ocorrerá.

# Dentro de while temos um bloco try que, se tudo correr bem, quebrará a
# repetição do laço com break após armazenar o input

# Se um erro for captado, caimos no bloco de except que por sua vez avisa
# o usuário do erro, cria uma pausa de 1 segundo, mas não faz uso de break
# logo, deixa que o laço execute mais uma repetição, e isso se repete até
# que o usuário passe um valor válido para a operação.

# Depois criamos um segundo while com o mesmo funcionamento, o primeiro se
# mantém resolvido, e quando o segundo também estiver