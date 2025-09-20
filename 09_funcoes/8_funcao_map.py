# Muito similar ao funcionamento do map em JS

# Aqui a função recebe dois parâmetros na seguinte estrutura:

# variavel = map(função, coleção)

# Para cada item dentro de uma coleção (lista, dicionário, tupla...)
# ele aplica a função passada como primeiro argumento, uma vez

# A função passada no primeiro argumento pode ser uma função comum ou lambda
# e no segundo caso, pode ser passada implicita ou explicitamente, isso é
# pode ser descrita diretamente dentro de map() ou pode ser armazenada em
# outra variável e depois ser chamada dentro de map(), vejamos um exemplo

numeros = [1,2,3]
cubo1 = map(lambda num: num ** 3, numeros)
print(list(cubo1))

# então o que fiz acima foi
# 1. Definição de uma coleção e seus elementos (nesse caso uma lista)
# 2. Definição da função map, passando explicitamente uma função lambda
#    no primeiro argumento. Volto a falar, podemos passar uma função lambda
#    ou mesmo uma função comum de maneira implicita, fazendo sua definição
#    fora do map e depois chamando-a dentro do map no primeiro argumento,
#    independente de como essa função for passada para o map, o importante
#    é que ela seja definida com um argumento pois é para ele que os itens
#    da coleção serão passados para serem utilizados corretamente
# 3. Ainda na função map, termino mencionando a coleção que desejo utilizar
# 4. Imprimo os resultados

# Vejamos um outro exemplo

emails = ['rafabieiro@gmail.com', 'brunotavar@outlook.com', 'josespindola@yahoo.com']
extrair_provedor = lambda e: e.split('@')[-1]
provedores = list(map(extrair_provedor, emails))
print(provedores)

# acima o que fizemos foi 
# 1. Definir uma outra coleção (lista de emails)
# 2. definir uma função lambda que recebe um argumento em "e" e depois
#    fatia o argumento real recebido no caractere "@" que é descartado
#    normalmente teriamos um retorno de uma lista com dois elementos,
#    as duas fatias, mas só a segunda fatia nos interessa, aquela com
#    o provedor, então colocamos a indexação [-1], que aponta que
#    queremos apenas o primeiro elemento da lista (1) de trás para 
#    frente (-), ou seja, o último elemento
# 3. Definimos a variavel provedores que recebe os resultados de um map
#    em forma de lista. Esse map recebe a função lambda descrita acima
#    como função a ser executada sobre cada item da colção e em seguida
#    recebe a coleção (lista) emails
# 4. pedimos a impressão de provedores. Detalhe, até então a operação
#    ainda não havia sido feita, apenas estava engatilhada, e é realizada
#    então apenas quando chamada

# Outro detalhe interessante sobre o map é o que diferencia ele de um
# laço for/in, por exemplo. No caso do laço as operações são feitas uma
# a uma, enquanto que aqui elas são feitas em paralelo, por isso a
# importância de definimos como vamos armazenar o resultado como fizemos
# com list em ambos os casos acima, além disso a aperação costuma ser
# finalizada com muito mais velocidade

##### Múltiplas coleções/iteráveis #####

# Existe uma outra maneira de trabalhar com map, passando vários iteráveis
# ou coleções, vejamos um exemplo

nomes = [Cleiton, Giovana, Maria]
idade = [30, 19, 25, 28]
uf = [RJ, SP, MS, SC]

formata = lambda n, i, u: '{n} tem {i} anos de idade e mora em {u}'
dados = list(formata, nomes, idade, uf)
print(dados)