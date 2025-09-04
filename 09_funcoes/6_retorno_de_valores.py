# Retornar um valor de uma função basicamente nos permite guardar o resultado
# de um algoritmo em uma variável, ao invés de ter que usá-lo de maneira
# Vamos entender melhor nos exemplos

# descrevendo função sem retorno
def somar(a, b):
    res = a + b
    print(res)

# Sem retorno toda a manipulação de um dado se limita ao escopo da função
# (e nem sempre queremos torná-la global pois isso pode causar problemas)
# isso quer dizer que eu farei toda a manipulação necessária e no fim tenho
# que decidir de imediato o que farei com esse dado, se mostrarei ele com
# um print ou farei um append dele para alguma lista, por exemplo

# Caso precise realizar a mesma função mais de uma vez ou várias funções
# diferentes e depois manipular os resultados sem que estejam em uma lista,
# isso só será possível com retorno

# Caso eu tente atribuir o resultado a uma variável (sem o return na função)
r1 = somar(3,4)

# O código vai literalmente atribuir a essa variável, a função com os
# parâmetros descritos, não o resultado do algoritmo.
# Isso pode ser útil para otimização, pois se eu for chamar muitas
# vezes "somar" com os parâmetros reais 3 e 4, agora só preciso chamar:
r1

# Porém não será útil para o que descrevemos nas linhas 16, 17 e 18

# descrevendo função com retorno
def somar2(a, b):
    res = a + b
    return res

res1 = somar2(3, 4)
res2 = somar2(8, 19)
print(f'Os resultados obtidos foram {res1} e {res2}. A soma dos resultados é {res1 + res2}')

# O return faz com que a função passe a valer o que é retornada, assim
# quando ela for armazanada em uma variável, não armazenará sua execução
# mas sim o dao que estiver no retorno

# OBS: esse dado pode ser de qualquer tipo, não apenas numérico