# break e continue são estruturas que permitem a quebra ou o avanço de um laço/loop
# não são tão utilizados mas é bom conhecer seu funcionamento

#################
##### BREAK #####
#################

for n in range(0, 10):
    if n == 3:
        break
    print(n)

print('///-///-///')

for n in range(0, 10):
    print(n)
    if n == 3:
        break

print('///-///-///')

# O que acontece acima é:
# 1. Crio um laço que retornará uma contagem de 0 a 10000000000
# 2. Crio um bloco condicional que vai disparar quando a variável temporária (n)
#    for 3, ou seja, na nona execução.
# 3. Dentro do bloco condicional passo a instrução de "break", que quebra o loop

# OBS: no segundo exemplo o número 3 ainda é renderizado pois o print(n) aparece 
#      antes do bloco que realiza o break

####################
##### CONTINUE #####
####################

for n in range(0, 10):
    if n == 3:
        continue
    print(n)

print('///-///-///')

# Esse exemplo é quase identico ao primeiro exemplo desse documento, literalmente
# apenas substituímos break por continue, e o resultado aqui já será bem diferente

# Enquanto break, para a execução do laço por inteiro, continue ignora tudo que
# está depois dele, mas apenas na volta atual do laço, e então pula para a próxima
# volta, com o próximo valor do iterável.

# Em outras palavras, nesse caso a contagem não para no 3, ela ignora o 3, mas vai até o 9

# Para vizualizarmos ainda melhor, veja esse exemplo onde ignoramos todos os pares:

for n in range(0, 10):
    if n % 2 == 0:
        continue
    print(n)

print('///-///-///')

# Vamos realizar um último exemplo onde ignoramos todas as consoantes de um texto:

total = 0
texto = 'se essa rua, se essa rua fosse minha. eu mandava, eu mandava, ladrilhar...'
print(texto)

for letra in texto:
    if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
        continue
    total += 1

print(f'O total de vogais é {total}')

# OBS: fiz questão de deixar o texto todo em minúsculo para não precisar repetir as
#      condicionais como "...and letra != 'E' and..."