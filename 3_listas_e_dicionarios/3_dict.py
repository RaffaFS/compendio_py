# Tal qual listas e conjuntos, dicionários são estruturas de dados, mas diferente 
# das listas e dos conjuntos que armazenam apenas valores ou valores + índices,
# aqui armazenamos combinações de chave + valor

#############################
##### DICIONÁRIO (DICT) #####
#############################

# Em resumo, dicionários são para python o que objetos são para o JS
# E a chamada de seus valores são feitas através de suas chaves
# Abaixo temos as estruturações básicas de dicinários:

ptbr = 'Português'

brasil = {'capital': 'Brasília', 'idioma': ptbr, 'População': 210}

brasilcopy = {
    'capital': 'Brasília',
    'idioma': ptbr,
    'População': 210
}

print(brasil)
print(brasilcopy)
print(brasil['idioma'])

# O valor de um a combinação "chave+valor" de um dicionário, pode ser de qualquer tipo,
# porem a chave deve ser sempre uma string, isso se descrito como fizemos acima, mas também
# podemos criar e descrever dicts de outra maneira, veja:

carro1 = {
    'marca': 'VW',
    'modelo': 'Polo',
    'Ano': 2010,
    'Ano': 2018
}

carro2 = dict(
    marca = 'VW'
    modelo = 'Polo'
    ano = 2018
)

print(carro1)
print(carro2)

# Na primeira situação valores até podem ser repetidos, mas se uma chave se repetir o dicionário 
# descartará as duplicatas mais antigas, já na segunda ele imprimirá um erro

###############################
##### DICIONÁRIO COMPOSTO #####
###############################

# Um dicionário composto é basicamente um dicionário que armazena outros dicionários internamente
# Não há limites para quantos níveis/camadas teremos nessa estrutura porém muitas camadas podem
# prejudicar a legibilidade e até o desempenho

dados = {
    'usuario1': {
        'nome': 'Alice',
        'endereco': {
            'cidade': 'São Paulo',
            'bairro': 'Centro',
            'cep': '01000-000'
        },
        'contato': {
            'email': 'alice@email.com',
            'telefone': '11999990000',
            'rede_social': {
                'instagram': '@alice',
                'linkedin': 'alice-linkedin',
                'twitter': '@alice_tw'
            }
        }
    },
    'usuario2': {
        'nome': 'Bruno',
        'endereco': {
            'cidade': 'Rio de Janeiro',
            'bairro': 'Copacabana',
            'cep': '22000-000'
        },
        'contato': {
            'email': 'bruno@email.com',
            'telefone': '21988887777',
            'rede_social': {
                'instagram': '@bruno',
                'linkedin': 'bruno-linkedin',
                'twitter': '@bruno_tw'
            }
        }
    },
}

print(dados['usuario2']['contato']['rede_social']['twitter'])

# Acima temos um exemplo de dicionário composto das chaves principais e mais 3 níveis
# sendo o primeiro nível as chaves de nome, endereço e contato, o segundo nível, as chaves
# de email, telefone e rede social, dentro de contato e, o terceiro nível, as chaves de
# instagram, linkedin e twitter dentro da rede social

# Por fim temos um exemplo de como podemos chamar apena o valor de uma chave numa camada mais interna

###############################
##### MANIPULAÇÃO DE DICT #####
###############################

joao = dict(
    nome = 'João', 
    idade = 28
)
print(joao)

# inserção de dado no dicionário
joao['estado_civil'] = 'casado'
print(joao)

# transformação de chaves e valores do dicionário separadamente para listas para finalidades diversas
chaves = list(joao.keys())
valores = list(joao.values())
print(chaves)
print(valores)

# Apesar de não podermos fazer o caminho inverso (transformar uma lista em dicionário), por conta da
# falta de informações, podemos armazenar dicionários dentro de listas com os métodos de listas

# E assim bem na verdade até existe uma maneira muito limitada de transformar listas em dicionários
# e isso só é possível se todos os elementos da lista forem também listas com exatamente 2 elementos
# cada ou se todos os elementos da lista forem strings com exatamente 2 caracteres cada

# Onde ou quando isso será útil? Ainda não sei, mas vejamos os exemplos

lista1 = [['Nome', 'Rafael'], ['Idade', 25]]
lista2 = [['Rafa', 18], ['Babi', 19]]
lista3 = ['Ra', 'Ba', 'Lu', 'Ga']

print(dict(lista1))
print(dict(lista2))
print(dict(lista3))