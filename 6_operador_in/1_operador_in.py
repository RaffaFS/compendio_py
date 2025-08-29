# Nos documentos seguintes veremos o uso mais comum do operador "in", que é
# junto com "for" para a realização de laços, então recomendo que primeiro
# veja a pasta de iterações, mas depois retorne, pois o "in" tem muitas 
# outras maneiras de ser usado


##### VERIFICAÇÂO

cores = ("azul", "verde", "vermelho")
print("verde" in cores)  # True

frutas = ["maçã", "banana", "uva"]
print("banana" in frutas)  # True

texto = "Python é incrível"
print("incrível" in texto)  # True

dados = {"nome": "Ana", "idade": 25}
print("nome" in dados)   # True  → verifica se a existe
print("Ana" in dados)    # False → não verifica valores

numeros = {1, 2, 3, 4}
print(3 in numeros)  # True

##### LAÇOS

for letra in "Python":
    print(letra)

##### CONDICIONAIS

if "idade" in dados:
    print(dados["idade"])

##### COMPLEMENTO COM NOT

if "laranja" not in frutas:
    print("Não tem laranja na lista")