# Iterações ocorrem quando temos uma estrutura de código conhecida por laço, ou loop
# que são estruras escritas para repetir um mesmo algoritmo várias vezes

##################
##### FOR IN #####
##################

# Em python, nossos laços são formados por for e in e, as vezes, por range
# explicitamente, nas outras, implicitamente

nomes = ['André', 'Bruno', 'Carlos', 'Jubileu']

for nome in nomes:
    print(nome)

# Um laço de repetição sempre começará com "for", em seguida passamos um argumento
# qualquer que armazenará um valor temporário dentro de si naquela execução/volta
# do laço. "in" é um apontamento que precede nosso "range", que aqui é implicito: 
# a lista nomes

# Veja outro exemplo

for hahaha in nomes:
    print(f'Oi eu sou o {hahaha}')

# Em ambos os casos bassicamente estou dizendo:
# (for) Para cada
# (nome) elemento
# (in) dentro de
# (nomes) grupo de elementos
# execute o algoritmo abaixo

#################
##### RANGE #####
#################

# Range como citado mais acima, é um terceiro parâmetro que podemos usar nos laços
# É bom lembrar que em todo algoritmo de python o índice final sempre é ignorado e
# o último a ser captado é ele -1

# Nesse caso vamos do 0 ao 5
for valor in range(6):
    print(f'{valor} do range 6')

# Nesse caso vamos do 7 ao 9
for valor in range(7, 10):
    print(f'{valor} do range 7')

# Nesse caso vamos replicar o exemplo de cima com um algoritmo diferente, o valor
# temporário será somado dentro da variável res, atribuindo a ela um novo valor,
# nos laços seguintes a operação se repete, mas "res" agora possuindo outro valor
# levando à um novo resultado final a cada execução/volta

res = 0
for valor in range(7, 10):
    res += valor
    print(res)

# Podemos ainda passar um terceiro parâmetro para range, e esse será tomado por "passo"

for valor in range(3, 10,3):
    print(valor ** valor)

# Nesse caso estou dizendo que, do "3" ao 9 ("10" -1), a cada "3" elementos o algoritmo
# seja executado, logo, nesse caso, será executado com 3, 6 e 9