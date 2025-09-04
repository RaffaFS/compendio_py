# Parâmetros opcionais são parâmetros formais já com valores reais padrão
# passados em sua criação

def somar(a, b, c):
    res = a + b + c
    print(f'A soma vale {res}')

# Nesse primeiro caso esperasse que eu passe três valores, e no caso de
# passar apenas dois, por exemplo, o código apresentará um erro

def somar(a, b, c=0):
    res = a + b + c
    print(f'A soma vale {res}')

# Já nesse segundo caso, eu defino um valo padrão para "c" já em sua criação
# isso significa que "a" e "b" são obrigatórios por ainda não terem valor
# algum atribuído, mas "c" é opcional, por conta de que caso não passemos
# um novo valor para ele, o algoritmo assumirá por "0" o valor de "c" e 
# rodará normalmente

# Poderíamos ainda fazer uma função com os três valores opcionais, isso é
# caso quiséssemos que ela rodasse mesmo sem receber dado algum, caso
# quiséssemos saber explicitamente que ela foi chamada com os valores
# padrão, sem atribuição de novos valores aos parâmetros

def somar(a=0, b=0, c=0):
    res = a + b + c
    print(f'A soma vale {res}')