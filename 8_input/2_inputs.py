# Assim como posso usar funções integradas diretamente nos inputs, como vimos
# no documento anterior com "float(input('...'))" também posso, diretamente
# neles, usar métodos, ou ainda usá-los como condições para if ou while:

import time

while True:
    print('--- FAÇA UMA ESCOLHA ---')
    print('1 - Virar a esquerda')
    print('2 - Virar a direita')
    print('3 - Seguir em frente')

    escolha1 = input('Escolha uma opção: ')
    
    if escolha1 == '1':
        print('Você virou a esquerda')
        break
    if escolha1 == '2':
        print('Você virou a direita')
        break
    if escolha1 == '3':
        print('Você segiu em frente')
        break
    else:
        print('Opção inválida. Tente novamente.')
        print('\n')
        time.sleep(1)

# Eu poderia também fazer esse algoritmo fora de um While, dessa maneira o uso
# de break também se faria desnecessário, porém assim não haveria laço. O algoritmo
# correspondente a escolha seria executado apenas uma vez mesmo que a escolha
# fosse inválida, sem dar uma segunda ou terceira chance ao usuário

# Uma opção não infinita, mas também não única é atribuir à while um valor X e fazer
# uma comparação de X a 3 por exemplo, e a cada ciclo incrementar 1 ao valor de X,
# quando a condição não for mais verdadeira, o loop para de acontecer, assim:

X = 0
while X < 3:
    print('--- FAÇA UMA ESCOLHA ---')
    print('1 - Virar a esquerda')
    print('2 - Virar a direita')
    print('3 - Seguir em frente')

    escolha1 = input('Escolha uma opção: ')
    
    if escolha1 == '1':
        print('Você virou a esquerda')
        break
    if escolha1 == '2':
        print('Você virou a direita')
        break
    if escolha1 == '3':
        print('Você segiu em frente')
        break
    else:
        print('Opção inválida. Tente novamente.')
        print('\n')
        time.sleep(1)
    X += 1

# Outra coisa que podemos fazer é não armazenar o input, se essa informação não
# for necessária mais a frente, passando ele diretamente como condição

X = 0
while X < 3:
    if input('Digite a senha: ') == '4321':
        print('Acesso concedido')
        break
    else:
        print('Acesso negado')
        if X == 2:
            print('Dispositivo bloqueado!')
        else:
            print('Tente novamente')
        time.sleep(1)
    X += 1

# Acima podemos ver inclusive uma outra dinâmica dentro de else que faz uso do 
# mesmo dado que usamos na verificação de while. Além disso, importante lembrar
# que uma coisa não tem ligação direta com a outra, mas nesse caso não poderemos
# utilizar esses inputs mais a frente por não termos armazenado eles